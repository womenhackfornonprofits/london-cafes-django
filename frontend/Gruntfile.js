module.exports = function(grunt) {
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');


    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        //------- CSS Minify -------//
        cssmin: {
          combine: {
            files: {
              '../london_cafes/static/styles/styles.css': ['css/styles.css']
            }
          }
        },

        //------- SASS -------//
        sass: {
          dist: {
            files: {
              'css/styles.css': 'sass/styles.scss'
            }
          }
        },
        //------- Watch SASS -> CSS -------//
        watch: {
            sass: {
                files: 'sass/**/*.scss',
                tasks: ['sass']
            }
        },
        uglify: {
            options: {
                compress: true,
                mangle: true,
                sourceMap: true
            },
            target: {
                src: 'scripts/**.js',
                dest: '../london_cafes/static/scripts/londoncafes.min.js'
            }
        },
        copy: {
            img: {
                files: [
                    // includes files within path
                    {
                        expand: true,
                        src: ['img/*'],
                        dest: '../london_cafes/static/',
                        filter: 'isFile'
                    },
                ],
            },
        },
    });


    grunt.registerTask('default', ['sass', 'cssmin', 'uglify', 'copy:img', 'watch']);
}