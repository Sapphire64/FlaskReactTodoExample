var React = require('react');
var TodoActions = require('../actions/TodoActions');

var TodoFooter = React.createClass({
    handleClick: function (event) {
        var markAsDone = confirm("Do you really want to mark everything as done?");
        if (markAsDone) {
            TodoActions.markAllAsDone();
        }
    },
    render: function () {
        return (
            <div className="footer">
                <div className="row">
                    <div className="all-cnt col-md-6">
                        {this.props.undoneTodos.length} items left
                    </div>
                    <div className="mark-all col-md-6">
                        <button type="button"
                                onClick={this.handleClick}
                                className="btn btn-link">Mark all as complete</button>
                    </div>
                </div>
            </div>
            )
    }
});

module.exports = TodoFooter;