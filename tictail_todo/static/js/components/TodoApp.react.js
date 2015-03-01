var React = require('react');
var TodoStore = require('../stores/TodoStore');
var TodoInput = require('../components/TodoInput.react');
var TodoList = require('../components/TodoList.react');
var TodoFooter = require('../components/TodoFooter.react');

var getTodos = function () {
    return {
        'todos': TodoStore.getTodos(),
        'undoneTodos': TodoStore.getUndoneTodos()
    }
};

var TodoApp = React.createClass({

    getInitialState: function () {
        return getTodos();
    },

    componentDidMount: function () {
        TodoStore.addChangeListener(this._onChange);
    },


    componentWillUnmount: function () {
        TodoStore.removeChangeListener(this._onChange);
    },

    render: function () {
        return (
            <div className="todo-container">
                <div className="header">
                    <h1>Todos</h1>
                </div>
                <TodoInput />
                <TodoList todos={this.state.todos} />
                <TodoFooter undoneTodos={this.state.undoneTodos} />
            </div>
            );
    },

    _onChange: function () {
        this.setState(getTodos());
    }

});

module.exports = TodoApp;