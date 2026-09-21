🌱 Crop Recommendation Engine

A weather-aware, soil-aware crop intelligence engine that transforms farm conditions into actionable crop recommendations.

<p align="center">
  <img src="static/background.jpg" alt="Crop Recommendation Engine" width="900"/>
</p>
<p align="center">
  <strong>From raw farm conditions → agricultural intelligence → ranked crop recommendations.</strong>
</p>

⸻

🚀 What Is This?

Choosing the right crop is not simply a matter of knowing the season.

A crop’s suitability depends on a combination of soil, temperature, humidity, rainfall, growing season, and local environmental conditions.

This project implements a standalone crop recommendation system that combines:

* 🌱 Machine Learning
* 🌦️ Real-time weather intelligence
* 🌍 Location-aware environmental data
* 🧪 Soil compatibility analysis
* 📊 Rule-based agronomic scoring
* 🌾 Crop suitability ranking
* 💧 Fertilizer recommendations
* 🔄 Graceful fallback logic

Instead of relying entirely on a trained model, the engine combines data-driven prediction with deterministic agricultural rules, making the recommendation pipeline more interpretable and resilient.

⸻

✨ Core Capabilities

🌾 Intelligent Crop Recommendation

The engine evaluates available crops against the farm’s environmental conditions and produces suitability scores rather than simply returning an arbitrary crop label.

🌦️ Weather-Aware Analysis

Weather information can be obtained dynamically using the selected location.

The system considers environmental factors such as:

* Temperature
* Humidity
* Rainfall
* Historical weather information

This allows recommendations to react to actual environmental conditions.

🧪 Soil Compatibility

Different crops thrive in different soil conditions.

The engine evaluates the supplied soil type against the known agronomic requirements of each crop.

📅 Season Intelligence

Crop recommendations are filtered according to growing-season compatibility.

A crop that is environmentally suitable but seasonally incompatible can therefore be excluded from the candidate set.

🤖 Hybrid Intelligence

The system is designed around two complementary approaches:

                  FARM INPUT
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Machine Learning        Rule-Based Engine
          │                       │
          │                       │
          └───────────┬───────────┘
                      ▼
             Suitability Analysis
                      │
                      ▼
              Ranked Recommendations

The ML pipeline provides learned predictions, while the rule-based engine provides deterministic environmental reasoning.

💧 Fertilizer Intelligence

The system can additionally determine fertilizer-related recommendations based on the selected crop and agricultural knowledge stored by the application.

🛡️ Graceful Missing-Data Handling

Environmental information is not always available.

Instead of blindly penalizing a crop when a weather variable is missing, the scoring engine can evaluate the available evidence and normalize the result accordingly.

⸻

🧠 How It Works

The recommendation pipeline follows a multi-stage process.

┌─────────────────────┐
│     User Inputs     │
│                     │
│ Location            │
│ Soil Type           │
│ Growing Season      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Weather Intelligence│
│                     │
│ Temperature         │
│ Humidity            │
│ Rainfall            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Candidate Generation│
│                     │
│ Available Crop Data │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Season Filtering  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Rule-Based Scoring  │
│                     │
│ Temperature         │
│ Humidity            │
│ Rainfall            │
│ Soil                │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Machine Learning    │
│ Prediction Pipeline │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Recommendation +    │
│ Explanation         │
└─────────────────────┘

⸻

📊 Suitability Scoring

The rule-based engine evaluates environmental compatibility for every candidate crop.

Temperature

A crop receives maximum compatibility when the supplied temperature falls inside its preferred temperature range.

Outside the range, the score decreases according to the distance from the acceptable range.

Humidity

Humidity compatibility is evaluated against the crop’s preferred humidity range.

Rainfall

Rainfall compatibility is calculated against the crop’s expected rainfall range.

Soil

Soil compatibility is determined by comparing the supplied soil type with the crop’s preferred soil types.

Normalization

The final score is normalized to:

0.0 ───────────────────────────── 1.0
 │                                  │
Poor suitability            Excellent suitability

Only available environmental inputs contribute to the denominator, preventing missing weather information from unfairly reducing a crop’s score.

⸻

🤖 Machine Learning Pipeline

The project also contains a trained machine-learning pipeline based on Random Forest classification.

The ML engine:

1. Loads the trained model lazily.
2. Encodes categorical agricultural attributes.
3. Generates probability predictions.
4. Evaluates candidate crops.
5. Produces crop-level suitability probabilities.

Core model artifacts include:

model.pkl
crop_encoder.pkl
soil_encoder.pkl
season_encoder.pkl

The trained model is intentionally kept separate from the rule-based scoring logic.

This makes it possible to evolve either component independently.

⸻

🧩 Architecture

                    ┌──────────────────────┐
                    │      Flask App       │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       Weather Service     ML Engine       Scoring Engine
              │                │                │
              ▼                ▼                ▼
       Weather Data       Random Forest    Rule Evaluation
                               │                │
                               └───────┬────────┘
                                       ▼
                              Crop Recommendation
                                       │
                          ┌────────────┴────────────┐
                          ▼                         ▼
                   Recommendation             Fertilizer
                                                Guidance

⸻

🛠️ Technology Stack

Technology	Purpose
🐍 Python	Core application logic
🌐 Flask	Web application & API layer
🧠 Scikit-learn	Machine learning
📊 Pandas	Dataset processing
🔢 NumPy	Numerical computation
🌦️ Requests	External weather API communication
🐘 PostgreSQL	Agricultural knowledge/data storage
🎨 HTML/CSS/JavaScript	Frontend interface
🚀 Gunicorn-compatible deployment	Production deployment

⸻

📁 Project Structure

Crop-Recommendation-Engine/
│
├── app.py
│
├── crop_engine.py
├── ml_engine.py
├── scoring_engine.py
├── weather_service.py
├── database.py
│
├── train_model.py
├── test_engine.py
│
├── model.pkl
├── crop_encoder.pkl
├── soil_encoder.pkl
├── season_encoder.pkl
│
├── data/
│   └── crop_dataset.csv
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── welcome.html
│
├── static/
│   ├── background.jpg
│   ├── script.js
│   └── style.css
│
├── Procfile
├── requirements.txt
└── .gitignore

⸻

⚙️ Getting Started

1. Clone the repository

git clone https://github.com/shaheeq27/Crop-Recommendation-Engine.git
cd Crop-Recommendation-Engine

2. Create a virtual environment

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

Windows

python -m venv .venv
.venv\Scripts\activate

⸻

3. Install dependencies

pip install -r requirements.txt

⸻

4. Configure the database

The application reads database configuration from environment variables.

export DB_NAME="crop_recommendation"
export DB_USER="postgres"
export DB_PASSWORD="your_password"
export DB_HOST="localhost"
export DB_PORT="5432"

Never commit real credentials to the repository.

⸻

5. Run the application

python app.py

The Flask server runs on:

http://localhost:10000

Open the address in your browser.

⸻

🧪 Testing

Run the included engine tests with:

python test_engine.py

The test suite covers core recommendation behavior and validates the interaction between the recommendation components.

⸻

🌦️ Weather Data

The weather subsystem retrieves environmental information using external weather services.

The system can use location information to obtain relevant climate data such as:

Temperature
Humidity
Rainfall
Historical weather

This information is then passed into the recommendation pipeline.

⸻

🧠 Design Philosophy

This project intentionally avoids treating machine learning as a black box.

A pure ML system can answer:

“What crop did the model predict?”

A hybrid agricultural intelligence system can additionally answer:

“Why does this crop fit the current environmental conditions?”

That distinction is important.

The engine therefore separates:

Prediction
    +
Agronomic Rules
    +
Environmental Context
    +
Season Compatibility
    ↓
Recommendation

This architecture also provides a practical fallback when complete environmental information or ML inference is unavailable.

⸻

🔬 Engineering Principles

Modularity

Weather retrieval, machine learning, scoring, database access, and application routing are separated into independent modules.

Explainability

Rule-based scoring provides a deterministic mechanism for understanding crop suitability.

Fault Tolerance

Missing environmental values do not automatically invalidate the recommendation process.

Extensibility

New crops, scoring rules, weather providers, or ML models can be introduced without redesigning the entire application.

Deployment Ready

The repository includes a Procfile and production-oriented dependency configuration for web deployment.

⸻

🔮 Future Improvements

Potential directions for extending the engine include:

* 📈 Larger real-world agricultural datasets
* 🛰️ Satellite-derived environmental features
* 🌍 Regional soil databases
* 🌧️ Long-term climate trend analysis
* 💰 Market-price-aware recommendations
* 💧 Irrigation optimization
* 🦠 Disease-risk prediction
* 📊 Confidence-aware recommendations
* 🧠 Ensemble ML models
* 🔍 Explainable AI with feature-level reasoning
* 📱 Mobile-first agricultural interfaces
* 🌾 Region-specific crop calendars

⸻

⚠️ Disclaimer

This project is intended for research, experimentation, and educational purposes.

Crop suitability depends on many factors that may not be fully represented by the available data. Recommendations should therefore be treated as decision-support information rather than a substitute for professional agronomic advice.

⸻

🌱 The Bigger Idea

Agricultural recommendation should not be:

Input → Black Box → Crop

It should be:

Farm Conditions
      ↓
Environmental Intelligence
      ↓
Agronomic Compatibility
      ↓
Machine Learning
      ↓
Rule-Based Reasoning
      ↓
Suitability Ranking
      ↓
Actionable Recommendation

The goal is not merely to predict a crop.

The goal is to understand why a crop fits the land. 🌾

⸻

👨‍💻 Author

Shaik Shaheeq

Computer Science Engineering
India

⸻

<p align="center">
  <strong>🌱 Data. Weather. Soil. Intelligence.</strong>
  <br/>
  <sub>Turning agricultural conditions into explainable crop recommendations.</sub>
</p>
