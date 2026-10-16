# Crop Prediction

A smart agricultural web application that predicts the most suitable crop type based on soil and environmental conditions. This project combines a Flask backend with a trained machine learning model to assess key farming parameters such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.

## Overview

The application helps farmers and agricultural planners choose appropriate crops based on field conditions. By inputting soil and climate values, the model predicts the best crop category and returns the result through a simple web interface.

## Features

- Crop recommendation based on soil and weather inputs
- Real-time prediction using a trained ML model
- User-friendly web form for agriculture data
- REST API for model inference
- Fast, lightweight deployment using Flask

## Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn
- Pickle (for loading the trained model)

### Frontend
- HTML5
- Tailwind CSS
- JavaScript
- Jinja2 templates

### Machine Learning
- Pre-trained crop recommendation model stored as `crop_model.pkl`
- Model inference using agronomic parameters:
  - nitrogen
  - phosphorus
  - potassium
  - temperature
  - humidity
  - pH
  - rainfall

## Project Structure

```text
Crop-Prediction/
├── app.py                  # Flask app and prediction API
├── crop_model.pkl         # Trained crop recommendation model
├── requirements.txt        # Python dependencies
├── templates/
│   └── crop.html           # Frontend UI
├── readme.md               # Project documentation
└── .gitignore              # Optional git ignore settings
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Crop-Prediction
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask app:

```bash
python app.py
```

Then open the browser at:

```text
http://127.0.0.1:5000/
```

## API Endpoint

The project exposes a prediction endpoint:

```http
POST /api/email
```

Example JSON payload:

```json
{
  "nitrogen": 90,
  "phosphorus": 42,
  "potassium": 43,
  "temperature": 24.5,
  "humidity": 85,
  "ph": 6.5,
  "rainfall": 200
}
```

Example response:

```json
{
  "prediction": "rice",
  "confidence": 98,
  "yield_index": "High",
  "risk_factor": "Minimal"
}
```

## Notes

- The app loads the trained crop model from `crop_model.pkl` at runtime.
- This project is designed for demonstration and learning purposes.
- In real-world deployments, additional validation, farmer-specific recommendations, and robust data checks should be added.

## License

This project is intended for educational and demonstration purposes. Add a license if you plan to distribute or deploy it publicly.
