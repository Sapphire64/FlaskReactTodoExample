var keyMirror = require('react/lib/keyMirror');

// Define action constants
module.exports = keyMirror({
    RECEIVE_DATA: null,
    UPDATE_TODO: null,
    CREATE_TODO: null,
    TODO_CREATED: null,
    MARK_ALL_AS_DONE: null
});