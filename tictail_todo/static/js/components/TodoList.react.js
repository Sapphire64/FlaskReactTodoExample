var React = require('react');
var TodoItem = require('../components/TodoItem.react.js');

var TodoList = React.createClass({

    render: function () {
        return (
            <div className="body">

                <ul className="todos">
                    {this.props.todos.map(function (todo, index) {
                        return (
                            <TodoItem key={todo.id} todo={todo} />
                        )
                    })}
                </ul>
            </div>
            )
    }
});

module.exports = TodoList;