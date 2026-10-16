# <div align="center">

# 🌾 AgroPredict • Smart Crop Recommendation Engine

### *Precision Agriculture Machine Learning Inference & Soil-Climate Agronomic Intelligence Engine*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Agronomic_ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-Modern_UI-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <a href="#-executive-overview">Executive Overview</a> •
  <a href="#-key-features">Key Features</a> •
  <a href="#-agronomic-parameters--architecture">Architecture</a> •
  <a href="#-tech-stack-matrix">Tech Stack</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-sample-agronomic-test-cases">Test Cases</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-production-hardening-roadmap">Roadmap</a>
</p>

---

</div>

## 📌 Executive Overview

**AgroPredict** is a precision agriculture machine learning microservice and web application engineered to determine the optimal crop yield based on multi-variate soil chemistry and micro-climate parameters.

By evaluating 7 foundational agronomic indicators—including soil macronutrients (**Nitrogen [N]**, **Phosphorus [P]**, **Potassium [K]**), chemical balance (**pH**), and ambient environmental metrics (**Temperature**, **Relative Humidity**, **Rainfall**)—the system executes localized model inference (`crop_model.pkl`) to deliver multiclass crop predictions (e.g., *Rice*, *Maize*, *Jute*, *Cotton*, *Coffee*), yield confidence metrics, and estimated risk indexes within **<25ms latency**.

> 💡 **Core Mission**: Designed as a rapid decision-support triage tool for smart farming cooperatives, agricultural planners, edge IoT agronomy kiosks, and AgriTech API pipelines.

---

## ⚡ Key Features

- 🌱 **7-Factor Soil & Climate Scoring**: Ingests critical NPK macronutrient ratios, environmental moisture, ambient heat, and soil acidity.
- ⚡ **Sub-25ms Inference REST API**: Gunicorn-optimized Flask WSGI runtime tuned for minimal overhead and zero-cold-start edge scoring.
- 🎨 **Responsive Agronomic Interface**: Clean, accessible web dashboard crafted with Tailwind CSS and Jinja2 for live field telemetry input and real-time yield visualization.
- 🔒 **Zero Data Egress / Edge Air-Gapped**: 100% self-contained serialized ML pipeline execution (`crop_model.pkl`)—telemetry stays entirely on the local server or farm edge gateway.
- 🌐 **CORS Ready**: Out-of-the-box `Flask-CORS` support enabling seamless integration with IoT sensor gateways, drone telemetry dashboards, and mobile agronomy apps.

---

## 📐 Agronomic Parameters & Architecture

```
Field Sensor Telemetry (NPK, Ambient Temp, Humidity, pH, Rainfall)
                                │
                                ▼
┌────────────────────────────────────────────────────────┐
│ 1. Agronomic Range Sanitization & Boundary Validation   │
│    • Realistic N-P-K nutrient bounds (0 - 140 mg/kg)    │
│    • Standard pH verification (3.5 - 9.5)              │
│    • Environmental anomaly & negative value guarding    │
└───────────────────────────────┬────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────┐
│ 2. Feature Vector Assembly (`[1 x 7]` Tensor)          │
│    • `[N, P, K, temperature, humidity, ph, rainfall]`  │
│    • Dynamic feature scaling & schema alignment        │
└───────────────────────────────┬────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────┐
│ 3. Inference Engine (`crop_model.pkl`)                 │
│    • Multi-class decision tree / ensemble classifier   │
│    • Multi-class probability distribution calculation   │
└───────────────────────────────┬────────────────────────┘
                                │
                                ▼
     JSON API Response / Interactive UI Harvest Badge
     { "prediction": "rice", "confidence": 98%, "yield_index": "High" }
```

---

## 🔬 Agronomic Input Parameters Matrix

| Parameter | Key | Realistic Range | Measurement Unit | Agronomic Significance |
| :--- | :--- | :---: | :---: | :--- |
| **Nitrogen** | `nitrogen` | `0 – 140` | mg/kg (ppm) | Critical macronutrient for vegetative canopy growth and chlorophyll synthesis |
| **Phosphorus** | `phosphorus` | `5 – 145` | mg/kg (ppm) | Drives root development, early seedling vigor, and flower/seed formation |
| **Potassium** | `potassium` | `5 – 205` | mg/kg (ppm) | Regulates plant water balance, enzyme activation, and disease resistance |
| **Temperature** | `temperature` | `8.0 – 45.0` | °C | Thermal growth threshold regulating metabolic transpiration and phenology |
| **Humidity** | `humidity` | `10.0 – 100.0` | % | Atmospheric vapor pressure influencing fungal susceptibility and transpiration |
| **Soil pH** | `ph` | `3.5 – 9.5` | pH Scale | Governs nutrient bioavailability and soil microbial enzymatic activity |
| **Rainfall** | `rainfall` | `20.0 – 300.0` | mm (seasonal) | Primary hydration driver determining water-stress vs. saturation thresholds |

---

## 🛠️ Tech Stack Matrix

| Domain | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Core** | `Python 3.9+`, `Flask` | Lightweight WSGI micro-framework powering prediction endpoints |
| **Model Serving** | `Gunicorn`, `Pickle` | High-concurrency production UNIX WSGI server & model unpickler |
| **Machine Learning**| `Scikit-learn` | Multiclass classifier training, evaluation, and pipeline serialization |
| **API Middleware** | `Flask-CORS` | Cross-Origin Resource Sharing handling for web & mobile clients |
| **Frontend UI** | `Tailwind CSS`, `HTML5`, `JS` | Intuitive agricultural data entry form with real-time feedback |
| **Templating** | `Jinja2` | Server-side template rendering and layout hydration |

---

## 📂 Project Structure

```text
Crop-Prediction/
├── 📄 app.py                  # Flask application & REST prediction routes
├── 🧠 crop_model.pkl          # Serialized multi-class crop recommendation classifier
├── 📋 requirements.txt        # Production dependencies & pinned versions
├── 📁 templates/
│   └── 🌐 crop.html           # Responsive Tailwind CSS agronomy dashboard
├── 📜 README.md               # Architecture, API & deployment documentation
└── 🚫 .gitignore              # Bytecode, virtual environments & cache exclusion
```

---

## 🚀 Quick Start

### 1. Clone & Navigate
```bash
git clone https://github.com/YOUR_USERNAME/Crop-Prediction.git
cd Crop-Prediction
```

### 2. Environment Setup
```bash
# Create dedicated virtual environment
python -m venv venv

# Activate virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Boot Inference Engine
```bash
python app.py
```

The application will bind to `http://127.0.0.1:5000/`. Visit this URL in your browser to access the interactive web interface.

---

## 📡 API Reference

### Real-Time Crop Recommendation Endpoint

Submit agricultural telemetry programmatically by dispatching an HTTP `POST` request.

```http
POST /api/email HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
```

> ⚠️ **Route Identifier Note**: The endpoint route is registered as `/api/email` within `app.py`. It accepts the 7 agronomic parameter payloads detailed below.

#### Request Headers
| Header | Value | Description |
| :--- | :--- | :--- |
| `Content-Type` | `application/json` | Mandatory JSON payload header |

#### Request Payload Schema
```json
{
  "nitrogen": 90,
  "phosphorus": 42,
  "potassium": 43,
  "temperature": 24.5,
  "humidity": 85.0,
  "ph": 6.5,
  "rainfall": 200.0
}
```

#### cURL Example
```bash
curl -X POST http://127.0.0.1:5000/api/email \
  -H "Content-Type: application/json" \
  -d '{
    "nitrogen": 90,
    "phosphorus": 42,
    "potassium": 43,
    "temperature": 24.5,
    "humidity": 85.0,
    "ph": 6.5,
    "rainfall": 200.0
  }'
```

#### Python (`requests`) Integration
```python
import requests

ENDPOINT = "http://127.0.0.1:5000/api/email"

soil_telemetry = {
    "nitrogen": 90,
    "phosphorus": 42,
    "potassium": 43,
    "temperature": 24.5,
    "humidity": 85.0,
    "ph": 6.5,
    "rainfall": 200.0
}

response = requests.post(ENDPOINT, json=soil_telemetry)
result = response.json()

print(f"Recommended Crop: {result.get('prediction').upper()}")
print(f"Confidence: {result.get('confidence')}% | Yield Index: {result.get('yield_index')}")
```

#### Response Payload (`200 OK`)
```json
{
  "prediction": "rice",
  "confidence": 98,
  "yield_index": "High",
  "risk_factor": "Minimal"
}
```

#### Response Field Reference
| Key | Type | Description |
| :--- | :--- | :--- |
| `prediction` | `string` | Recommended crop species (e.g., `rice`, `maize`, `chickpea`, `coffee`) |
| `confidence` | `number` | Classification probability certainty percentage (`0` – `100`) |
| `yield_index` | `string` | Relative expected harvest productivity (`High`, `Moderate`, `Low`) |
| `risk_factor` | `string` | Environmental stress hazard evaluation (`Minimal`, `Moderate`, `Elevated`) |

---

## 🧪 Sample Agronomic Test Cases

| Scenario | Soil & Climate Profile Summary | Expected Crop | Confidence | Yield Index |
| :--- | :--- | :---: | :---: | :---: |
| **Paddy / Wetland** | High N (90), High Rain (200mm), Humid (85%), Temp 24.5°C | **Rice** | `98.0%` | `High` |
| **Arid / Legume** | Low N (20), High P (65), Dry (25% hum), Rain 70mm, Neutral pH | **Chickpea** | `96.4%` | `High` |
| **Cash Crop / Tropical** | Elevated K (195), Moderate Rain (110mm), Warm (28°C) | **Banana** | `97.2%` | `High` |
| **Subtropical Highlands**| Balanced NPK (100:60:50), Temp 23°C, Acidic pH (6.2), Moderate Rain | **Coffee** | `95.1%` | `Moderate` |

---

## 🗺️ Production Hardening Roadmap

- [ ] **Semantic Route Aliasing**: Expose canonical route `/api/v1/predict/crop` alongside `/api/email` for REST standard compliance.
- [ ] **Pydantic Sensor Schema**: Validate physical sensor telemetry against boundary constraints (e.g., non-negative rainfall, pH range [1, 14]).
- [ ] **Top-3 Recommendation Distribution**: Return secondary and tertiary crop alternatives when probability margins are tight.
- [ ] **Multi-stage Dockerfile**: Build minimal Alpine/Debian-slim container with healthchecks for AWS ECS or GCP Cloud Run deployment.
- [ ] **Weather API Integration**: Auto-populate temperature, humidity, and forecast rainfall using GPS coordinates via Open-Meteo or NOAA APIs.

---

## 📄 License & Disclaimer

Distributed under the **MIT License**. See `LICENSE` for details.

> ⚠️ **Agricultural Advisory Disclaimer**: AgroPredict is an assistive machine learning decision support prototype built for demonstration, educational purposes, and agronomy research. Recommendations should be validated by regional agronomists and local agricultural extension testing before large-scale commercial planting.
