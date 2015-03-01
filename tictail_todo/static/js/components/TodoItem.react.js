var React = require('react');
var TodoActions = require('../actions/TodoActions');

var TodoItem = React.createClass({
    todoChanged: function (event) {
        var isChecked = event.target.checked;
        this.props.todo.is_active = !isChecked;
        TodoActions.updateTodoState(this.props.todo);
    },
    render: function () {
        var todo = this.props.todo;
        return (
            <li key={todo.id} className={'todo' + (todo.is_active ? '' : ' checked')}>
                <label>
                    <input type="checkbox"
                    onChange={this.todoChanged}
                    checked={!todo.is_active}/>
                                {todo.data}
                </label>
            </li>
            )
    }
});

module.exports = TodoItem;