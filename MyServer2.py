from flask import Flask
app = Flask(__name__)

# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
#     return 'Hello World 2!'

@app.route('/hello/name')
def hello_name(name):
    return 'Hello %s!' % name

# This the main driver fxn
if __name__ == '__main__':
    # run() method of Flask class runs the app on local dev server
    app.run()