

**Real Estate Price Prediction App**

A Python web app built using Dash that predicts **house price per unit area** based on:

* Distance to the nearest MRT station
* Number of convenience stores nearby
* Latitude and Longitude

---



**App Overview**

This app:

* Uses a trained **Linear Regression** model (from scikit-learn)
* Loads the model from a `.pkl` file
* Accepts user input via interactive fields
* Predicts the house price instantly

---

**Project Folder Structure**

```
real-estate-price-app/
│
├── app.py                 --> Dash app frontend + backend
├── model_training.py      --> Script to train the ML model (optional)
├── real_estate_model.pkl  --> Pre-trained model (via joblib)
├── requirements.txt       --> Python dependencies
└── README.md              --> Project description (this file)
```

---

**How to Run Locally**

1. Clone the repository
   `git clone https://github.com/your-username/real-estate-price-app.git`

2. Navigate into the folder
   `cd real-estate-price-app`

3. Create and activate virtual environment (optional but recommended)
   `python -m venv venv`
   `source venv/bin/activate` (on Windows: `venv\Scripts\activate`)

4. Install dependencies
   `pip install -r requirements.txt`

5. Run the app
   `python app.py`

6. Open your browser and visit
   `http://127.0.0.1:8050`

---

**Requirements**

* dash
* pandas
* scikit-learn
* joblib
* gunicorn (for deployment)

These are listed in `requirements.txt`.

---

**Future Enhancements**

* Add interactive map input
* Upgrade to Random Forest or XGBoost models
* Display neighborhood analytics or trends
* Add historical price charts

---

**Made with ❤️ by sanya**


