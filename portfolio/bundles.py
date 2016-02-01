from flask.ext.assets import Bundle
from flask.ext.assets import Environment


assets = Environment()

js = Bundle(
    'bower_components/jquery/dist/jquery.js',
    'bower_components/bootstrap/js/alert.js',
    'bower_components/bootstrap/js/modal.js',
    'bower_components/bootstrap/js/dropdown.js',
    'bower_components/bootstrap/js/collapse.js',
    'bower_components/bootstrap/js/affix.js',

    output='gen/lib.js',
    filters='rjsmin'
)

css = Bundle(
    'css/styles.less',

    output='gen/styles.css',
    filters='less,cssmin'
)
