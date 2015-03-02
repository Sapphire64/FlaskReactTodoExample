var AppDispatcher = require('../dispatcher/AppDispatcher');
var EventEmitter = require('events').EventEmitter;
var TodoConstants = require('../constants/TodoConstants');
var TodoApi = require('../utils/TodoApi');
var _ = require('underscore');

var _todos = [];

var resortTodos = function () {
    /* TODO: remove sorting when drag-and-drop will be implemented */
    _todos = _.sortBy(_todos, function (todo) {
        return [!todo.is_active, todo.data]
    });
};

var loadTodoData = function (data) {
    _todos = data;
    resortTodos();
};

var update = function (todo) {
    var selectedTodo = _.findWhere(_todos, {'id': todo.id});
    selectedTodo.is_active = todo.is_active;
    
    resortTodos();
};

var insertTodo = function (todo) {
    _todos.push(todo);
    resortTodos();
};

var getUndoneTodos = function () {
    return _.filter(_todos, function (td) {return Boolean(td.is_active) });
};

var markAllAsDone = function (todos) {
    for (var i=0; i<todos.length; i++) {
        todos[i].is_active = false;
    }
    resortTodos();
};

// Extend TodoStore with EventEmitter to add eventing capabilities
var TodoStore = _.extend({}, EventEmitter.prototype, {
    insertTodo: function (todo) {
        insertTodo(todo);
        this.emit('change');
    },
    // Return Todo data
    getTodos: function () {
        return _todos;
    },
    getUndoneTodos: function () {
        return getUndoneTodos();
    },

    // Emit Change event
    emitChange: function () {
        this.emit('change');
    },

    // Add change listener
    addChangeListener: function (callback) {
        this.on('change', callback);
    },

    // Remove change listener
    removeChangeListener: function (callback) {
        this.removeListener('change', callback);
    }

});

// Register callback with AppDispatcher
AppDispatcher.register(function (payload) {
    var action = payload.action;

    switch (action.actionType) {

        // Respond to RECEIVE_DATA action
        case TodoConstants.RECEIVE_DATA:
            loadTodoData(action.data);
            break;
        case TodoConstants.UPDATE_TODO:
            TodoApi.updateTodoItem(action.data);
            update(action.data);
            break;
        case TodoConstants.CREATE_TODO:
            TodoApi.createTodoItem(action.data).end(
                function (res) {
                    TodoStore.insertTodo(res.body);
                }
            );
            break;
        case TodoConstants.MARK_ALL_AS_DONE:
            var undoneTodos = getUndoneTodos();

            _.each(undoneTodos, function (todo) {
                todo.is_active = false;
                TodoApi.updateTodoItem(todo);
            });
            markAllAsDone(undoneTodos);
            break;
        default:
            return true;
    }

    // If action was responded to, emit change event
    TodoStore.emitChange();

    return true;

});

module.exports = TodoStore;