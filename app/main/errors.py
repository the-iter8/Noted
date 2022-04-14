from flask import render_template

from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    # TODO: make template named 404.html and uncomment line below and remove last line of function
    # return render_template('404.html'), 404
    return "<h1>Page Not Found !</h1>"

@main.app_errorhandler(500)
def internal_server_error(e):
    # TODO: make template named 500.html and uncomment line below and remove last line of function
    # return render_template('500.html'), 500
    return "<h1>Internal Server Error !</h1>"
