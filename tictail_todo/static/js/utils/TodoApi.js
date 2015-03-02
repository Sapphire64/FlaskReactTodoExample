var request = require('superagent');
var TodoActions = require('../actions/TodoActions');
var AppDispatcher = require('../dispatcher/AppDispatcher');
var TodoConstants = require('../constants/TodoConstants');



var TodoApi = {
    getTodoData: function () {
        request.get(TodoConstants.apiUrl).end(function (res) {
            TodoActions.receiveTodos(res.body);
        });
    },
    updateTodoItem: function (todo) {
        var id = todo.id;
        var body = {'data': todo.data, 'is_active': todo.is_active};
        // Submit
        request.put(TodoConstants.apiUrl + id).send(body).end();
    },
    createTodoItem: function (todo) {
        // Send to server
        return request.post(TodoConstants.apiUrl).send(todo);
    }
};

module.exports = TodoApi;