from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle



app = Flask(__name__)
@app.route('/',methods=['GET'])
@cross_origin()
def home_page():
    return render_template("Index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            TAX = float(request.form['TAX'])
            ZN = float(request.form['ZN'])
            CRIM = float(request.form['CRIM'])
            B = float(request.form['B'])
            AGE = float(request.form['AGE'])
            RAD = float(request.form['RAD'])
            LSTAT = float(request.form['LSTAT'])
            INDUS = float(request.form['INDUS'])

            filename = 'randomforest_model.pickle'
            model = pickle.load(open(filename, 'rb'))
            prediction = model.predict([[TAX,ZN,CRIM,B,AGE,RAD,LSTAT,INDUS]])
            print('prediction value is ', prediction)
            # showing the prediction results in a UI
            return render_template('predict.html', prediction=round(prediction[0],3))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('Index.html')

if __name__ == "__main__":
    app.run(debug=True)



