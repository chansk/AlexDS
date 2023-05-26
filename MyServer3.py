from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'John Doe'
    return render_template('/index.html', name=name)

# When using render_template, Flask automatically looks into folder named "templates"

if __name__ == '__main__':
    app.run()
