'use strict';

const gulp = require('gulp');
const autoprefixer = require('gulp-autoprefixer');
const sass = require('gulp-sass');

/*
##### ----- #####
##### PATHS #####
##### ----- #####
*/

const paths = {
    styles: {
        sass:  ['./themes/martian/static/css/sass/**/*.scss', './themes/martian/static/css/sass/**/*.sass'],
        dest: './themes/martian/static/css'
    }
};

/*
##### ----- #####
##### TASKS #####
##### ----- #####
*/

function compileSass() {
  return gulp.src(paths.styles.sass)
    .pipe(sass().on('error',sass.logError))
    .pipe(gulp.dest(paths.styles.dest));
}

function autoprefixCss() {
  return gulp.src(paths.styles.dest)
    .pipe(autoprefixer())
    .pipe(gulp.dest(paths.styles.dest))
}

/*
##### -------- #####
##### WATCHERS #####
##### -------- #####
*/

/*
##### ------- #####
##### EXPORTS #####
##### ------- #####
*/
exports.compileSass = compileSass;
exports.autoprefixCss = autoprefixCss;
exports.buildCss = gulp.series(compileSass, autoprefixCss);
