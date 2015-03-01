var React = require('react');
var TodoActions = require('../actions/TodoActions');


var TodoInput = React.createClass({
    getInitialState: function () {
        return {value: ''};
    },
    handleChange: function (event) {
        this.setState({value: event.target.value});
    },
    handleClick: function (event) {
        // TODO: disable input
        var value = this.state.value;

        if (value.length < 1) {
            return
        }

        TodoActions.createTodoItem(value);

        this.setState({value: ''});
    },
    render: function () {
        var value = this.state.value;
        return (
            <div className="input-form">
                <form className="form-inline">
                    <div className="row">
                        <div className="col-md-8 todoinput-group">
                            <div className="form-group">
                                <input type="text" className="form-control"
                                    value={value} onChange={this.handleChange}
                                    placeholder="What needs to be done?" />
                            </div>
                        </div>
                        <div className="col-md-4 addbtn-group">
                            <button type="button"
                                onClick={this.handleClick}
                                className="btn btn-submit">Add Todo
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            )
    }
});

module.exports = TodoInput;