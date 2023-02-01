from flask import Flask
import Pred2 # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    # return my_function(3)
#     return Pred2.print_date("hello") # my module again with fxn and probably input if necessary
    return Pred2.stock_pred()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)