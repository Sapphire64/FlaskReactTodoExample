module.exports = function (grunt) {
    grunt.initConfig({
        browserify: {
            client: {
                src: 'tictail_todo/static/js/app.js',
                dest: 'tictail_todo/static/js/build.js',
                options: {
                    transform: [ require('grunt-react').browserify ]
                }
            }
        },
        sass: {
            dist: {
                options: {
                    style: 'expanded'
                },
                files: {
                    'tictail_todo/static/css/main.css': 'tictail_todo/static/scss/main.scss'
                }
            }
        },
        watch: {
            css: {
                files: 'tictail_todo/static/scss/*.scss',
                tasks: ['sass']
            },
            js: {
                files: ['tictail_todo/static/js/**/*.js', '!tictail_todo/static/js/build.js'],
                tasks: ['browserify']
            }
        }
    });

    grunt.loadNpmTasks('grunt-browserify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['sass']);
    grunt.registerTask('build', ['sass', 'browserify']);
};