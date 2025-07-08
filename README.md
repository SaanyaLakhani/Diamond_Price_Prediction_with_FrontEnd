
DIAMOND PRICE PREDICTION PROJECT
================================

PROJECT OVERVIEW:
------------------
This project predicts the price of a diamond based on its characteristics using a Machine Learning regression model. It includes a complete end-to-end pipeline from data analysis to web deployment using Streamlit. The goal is to provide a user-friendly interface for estimating diamond prices based on user input parameters.

The model is trained using the 'diamonds.csv' dataset and deployed through a web app with an intuitive UI that allows users to input values like carat, cut, color, and clarity to get real-time price predictions.

FILES INCLUDED:
---------------
1. diamonds.csv – Dataset containing diamond features and prices
2. Diamond_Price_Prediction_Project.ipynb – Jupyter Notebook with complete data analysis, model training, and evaluation
3. app.py – Streamlit web application code for deployment
4. download.jpg – Background image used in the UI
5. RandomForest_diamond_price_model.pkl – Pre-trained Random Forest model (must be placed in the same folder)
6. README.txt – This file

DATASET DETAILS:
----------------
Source: Kaggle or similar open-source dataset repository
File: diamonds.csv

Key Features Used:
- Carat: Weight of the diamond
- Cut: Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- Color: Diamond color from D (best) to J (worst)
- Clarity: Ranges from I1 (lowest) to IF (internally flawless)
- Depth: Total depth percentage
- Table: Width of the top of the diamond
- x, y, z: Dimensions used to compute Volume (x × y × z)

Target Variable:
- Price: Diamond price in US Dollars

MODEL INFORMATION:
------------------
Algorithm: Random Forest Regressor
Steps involved:
- Data Cleaning and Preprocessing
- Categorical Encoding (Label encoding for cut, color, clarity)
- Feature Engineering (including volume calculation)
- Model Training and Evaluation
- Model Export using joblib

Evaluation Metrics:
- R-squared score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

WEB APPLICATION FEATURES:
--------------------------
Developed using Streamlit
Title: Diamond Price Predictor
User Inputs:
- Carat (slider)
- Cut (dropdown)
- Color (dropdown)
- Clarity (dropdown)
- Depth (slider)
- Table (slider)
- Volume (slider)

Output:
- Predicted Diamond Price in USD
- Tips section on the left with background image
- Custom styled UI using HTML and CSS inside Streamlit

SETUP INSTRUCTIONS:
-------------------
1. Install required Python libraries:
   - streamlit
   - numpy
   - pandas
   - joblib
   - scikit-learn

   You can install them using pip:
   pip install streamlit numpy pandas joblib scikit-learn

2. Make sure the following files are in the same directory:
   - app.py
   - RandomForest_diamond_price_model.pkl
   - download.jpg

3. Run the Streamlit app:
   streamlit run app.py

4. The app will open in your default browser.
   Use the sliders and dropdowns to input diamond attributes and click the predict button to get the estimated price.

PROJECT OUTPUT:
---------------
- Real-time prediction of diamond prices
- A clear and modern UI with interactive inputs
- Helpful visual tips for users on choosing diamonds
- Accurate and interpretable predictions using Random Forest

CONCLUSION:
-----------
This project demonstrates a practical use-case of machine learning in the gem and jewelry industry. It helps users estimate the value of diamonds based on physical and visual features. The project integrates data science, machine learning, and UI/UX through Streamlit to offer a deployable, real-world application.

Developed as part of a Machine Learning portfolio project by Saanya Lakhani. Feel free to reachout in case of any doubts.
