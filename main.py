
from flask import Flask, render_template
from flask import Flask, request,Response,render_template
from flask_cors import CORS, cross_origin




app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)







