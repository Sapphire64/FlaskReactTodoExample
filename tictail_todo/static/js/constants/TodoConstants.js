var keyMirror = require('react/lib/keyMirror');
var _ = require('underscore');

var actions = keyMirror({
    RECEIVE_DATA: null,
    UPDATE_TODO: null,
    CREATE_TODO: null,
    TODO_CREATED: null,
    MARK_ALL_AS_DONE: null
});

var apiConstants = {
    'apiUrl': '/todos/'
};


module.exports = _.extend(actions, apiConstants);