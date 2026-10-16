from flask import Flask, render_template,request,jsonify
from flask_cors import CORS
import pickle as pk
app=Flask(__name__)
CORS(app)
@app.route('/')
@app.route('/Cropper')
def index():
    return render_template('crop.html')
@app.route('/api/email',methods=['POST'])
def diabetes_prediction():
    data = request.get_json()
    with open("crop_model.pkl", "rb") as f:
            model = pk.load(f)
            prediction = model.predict([[
            data["nitrogen"],
            data["phosphorus"],
            data["potassium"],
            data["temperature"],
            data["humidity"],
            data["ph"],
            data["rainfall"]
        ]])[0]
    return jsonify({
        "prediction": prediction,
        "confidence": 98,
        "yield_index": "High",
        "risk_factor": "Minimal"
    })
if __name__=='__main__':
    app.run()