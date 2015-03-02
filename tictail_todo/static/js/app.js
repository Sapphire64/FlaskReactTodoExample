var React = require('react');
var TodoApp = require('./components/TodoApp.react');
var TodoApi = require('./utils/TodoApi');

TodoApi.getTodoData();

React.render(
    <TodoApp />,
    document.getElementById('todoapp')
);