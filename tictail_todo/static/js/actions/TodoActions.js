var AppDispatcher = require('../dispatcher/AppDispatcher');
var TodoConstants = require('../constants/TodoConstants');

// Define actions object
var TodoActions = {

    receiveTodos: function (data) {
        AppDispatcher.handleAction({
            actionType: TodoConstants.RECEIVE_DATA,
            data: data
        })
    },
    updateTodoState: function (todo) {
        AppDispatcher.handleAction({
            actionType: TodoConstants.UPDATE_TODO,
            data: todo
        })
    },
    markAllAsDone: function () {
        AppDispatcher.handleAction({
            actionType: TodoConstants.MARK_ALL_AS_DONE
        })
    },
    createTodoItem: function (todoData) {
        AppDispatcher.handleAction({
            actionType: TodoConstants.CREATE_TODO,
            data: {'data': todoData, 'is_active': true}
        })
    }
};

module.exports = TodoActions;