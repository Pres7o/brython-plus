const gulp = require("gulp");
const concat = require("gulp-concat");
const terser = require("gulp-terser");
const ver = '3.14.0'


gulp.task("brython", function () {
  return gulp
    .src([
      'brython.js',
      'brython_stdlib.js',
    ])
    .pipe(concat('brython.min.js')) // merged + minified file
    .pipe(terser()) // minify modern JS
    .pipe(gulp.dest('./'))
});
