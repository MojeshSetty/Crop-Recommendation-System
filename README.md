# 🌾 Crop Price Prediction System using Machine Learning

<img src="https://img.shields.io/badge/Flask-App-green" alt="Flask Badge"/> 
<img src="https://img.shields.io/badge/MachineLearning-RandomForest-blue" alt="ML Badge"/> 
<img src="https://img.shields.io/badge/Python-3.8+-yellow" alt="Python Badge"/>  
<br>

A web-based application that predicts crop prices based on inputs like commodity, location, market, season, and day using a trained machine learning model. Built with Flask and deployed with a simple UI.

---

## 📸 Demo Preview

![App Preview](https://drive.google.com/uc?export=view&id=1JcdY7YL7CqrI3g8qZp4pC5mfsfZhqMQM)

---

## 🚀 Features

✅ Predict crop prices for any selected combination of  
  🔸 Commodity  
  🔸 State, District, Market  
  🔸 Month, Day, Season  

✅ Built using a trained ML model (`regr.pkl`)  
✅ User-friendly Web UI using **Flask + HTML Templates**  
✅ Easy to deploy locally  

---

## 🧠 Technologies Used

- Python 3.8+
- Flask
- NumPy
- Pickle
- HTML/CSS (Jinja2 templating)
- Machine Learning Model (e.g., Random Forest)

---

## 📁 Project Structure

```bash
├── app.py               # Main Flask application
├── regr.pkl             # Trained machine learning model
├── templates/
│   ├── index.html       # Input form
│   └── result.html      # Result display
├── static/              # CSS/JS or images (if any)
├── assets/              # Screenshots for README
└── README.md            # You're here!
