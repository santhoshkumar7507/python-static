from flask import Blueprint, render_template

main2 = Blueprint('main2', __name__, static_folder='static', template_folder='Templates')

@main2.route("/home")
@main2.route("/")
def home():
    return render_template('home.html')

@main2.route('/test')
def test():
    return "<h1>test</h1>"