

```markdown
# 🏠 Real Estate Price Prediction Web App

This is a Python-based web application built using [Dash](https://dash.plotly.com/) that predicts the **house price per unit area** based on:

- Distance to the nearest MRT station
- Number of convenience stores nearby
- Latitude
- Longitude

The prediction model is trained using **Linear Regression** from `scikit-learn`.

---

## 🔮 Features

- Real-time price prediction based on user input
- Clean and responsive Dash UI
- Trained using real housing data
- Easily extendable (add map input, more features, ML models)

---



## 📂 File Structure

```

real-estate-price-app/
├── app.py                 # Dash application
├── model\_training.py      # Optional: model training script
├── real\_estate\_model.pkl  # Saved regression model
├── requirements.txt       # Required Python packages
└── README.md              # This file

````

---

## 📦 Installation (Local Setup)

```bash
# Clone the repo
git clone https://github.com/your-username/real-estate-price-app.git
cd real-estate-price-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
````

---

## 📈 Sample Data Used

The dataset used includes information about housing prices in relation to MRT station distance, convenience stores, and location coordinates.

---

## ✨ Future Enhancements

* Add map input for selecting location
* Include total area or number of rooms
* Support for multiple ML models (Random Forest, XGBoost, etc.)
* Deploy to Heroku or AWS Lambda

---

## 🧑‍💻 Author

Made with ❤️ by [Your Name](https://github.com/sanyagupta31)

```

---


