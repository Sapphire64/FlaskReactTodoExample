module.exports = function (grunt) {
    grunt.initConfig({
        sass: {                              // Task
            dist: {                            // Target
                options: {                       // Target options
                    style: 'expanded'
                },
                files: {                         // Dictionary of files
                    'tictail_todo/static/css/main.css': 'tictail_todo/static/scss/main.scss'       // 'destination': 'source'
                }
            }
        },
        watch: {
            css: {
                files: 'static/scss/*.scss',
                tasks: ['sass']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['sass']);
    grunt.registerTask('build', ['sass']);
};