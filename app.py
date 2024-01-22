from flask import Flask, render_template, request
import os 
import numpy as np
from BostonHousePrediction.pipeline.prediction import PredictionPipeline
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CRIM =float(request.form['crim'])
            ZN =float(request.form['zn'])
            INDUS =float(request.form['indus'])
            CHAS =float(request.form['chas'])
            NOX =float(request.form['nox'])
            RM =float(request.form['rm'])
            AGE =float(request.form['age'])
            DIS =float(request.form['dis'])
            RAD =float(request.form['rad'])
            TAX =float(request.form['tax'])
            PTRATIO =float(request.form['ptratio'])
            B =float(request.form['black'])
            LSTAT =float(request.form['stat'])

            data = [CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]
            data = np.array(data).reshape(1, 13)

            # Make prediction
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('result.html', prediction=str(predict))

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
