var TodoActions = require('../actions/TodoActions');
var AppDispatcher = require('../dispatcher/AppDispatcher');
var TodoConstants = require('../constants/TodoConstants');

var TodoApi = {
    getTodoData: function () {
//    var data = JSON.parse(localStorage.getItem('product'));
        var data = [
            {'id': 'lol', 'data': 'asdasdads', 'is_active': false},
            {'id': 'lol2', 'data': 'asdasdfsfsdads', 'is_active': false},
            {'id': 'lol3', 'data': 'sdfsdffsasdasdads', 'is_active': true}
        ];
        TodoActions.receiveTodos(data);
    },
    updateTodoItem: function (todo) {
        var id = todo.id;
        var body = {'data': todo.data, 'is_active': todo.is_active};
        // Submit
        console.log(id);
        console.log(body);
    },
    createTodoItem: function (todo) {
        // Send to server
        console.log("Creating...");
        console.log(todo);
        todo.id = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
        // Return resulting item
        return todo;
    }
};

module.exports = TodoApi;