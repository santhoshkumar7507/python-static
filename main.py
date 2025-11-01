from flask import Flask, render_template
from main2 import main2
app = Flask(__name__)
app.register_blueprint(main2, url_prefix='/admin')

@app.route('/')
def test():
    return "<h1>Test Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)