from flask import Flask # import Flask class
app = Flask(__name__) # Create an instance of Flask class (this is the WSGI application)



# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.

# route() fxn is a decorator of Flask class -- it specifies URL endpoint fxn will be handling
    # specifically, it is root URL with variable called 'name' that will be passed onto URL
@app.route('/<name>')
# Defining the hello_name function with optional parameter
def hello_name(name='Alex'):
    return '<p>Hello %s!</p>' % name

# This prints basic hello world when URL pasted into browser:
# @app.route('/')
# def hello_world():
#    return 'Hello world!'

# This the main driver fxn
if __name__ == '__main__':
    # run() method of Flask class runs the app on local dev server
    app.run()

# Either approach here should work:
    # python MyServer2.py

    # set FLASK_APP=MyServer2.py
    #  flask run