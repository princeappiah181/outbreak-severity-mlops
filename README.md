# Public Health Outbreak Severity Prediction - End-to-End ML System

## Live Demo 
Streamlit App

![UI Demo](images/ui_demo1.jpg)
![UI Demo](images/ui_demo2.jpg)

The deployed UI is available here:
https://outbreak-severity-mlops-8g9tnu3artsgreihxidvub.streamlit.app/


## API Documentation

The deployed API is available here:

https://outbreak-severity-api.onrender.com/docs


## Overview
This project builds an end-to-end machine learning system that analyzes disease outbreak reports and predicts whether an outbreak is high severity or low severity.<br>
The goal is to demonstrate how machine learning can support early warning systems for public health by automatically analyzing outbreak reports and identifying events that may require urgent attention.<br>
The system processes outbreak text, extracts epidemiological indicators such as reported cases and deaths, and combines them with natural language features to generate a severity prediction.<br>
This repository demonstrates the complete machine learning lifecycle, including:<br>
data processing<br>
feature engineering<br>
model training<br>
explainability<br>
API deployment<br>
browser-based inference interface<br>

## System Architecture
User Interface (Streamlit)<br>
        ↓<br>
FastAPI REST API<br>
        ↓<br>
Feature Engineering<br>
        ↓<br>
TF-IDF Vectorization<br>
        ↓<br>
Logistic Regression Model<br>
        ↓<br>
Severity Prediction<br>

The architecture separates the user interface, API layer, and machine learning model, reflecting a common production ML system design.

## Motivation
Disease outbreak reports contain valuable information for public health monitoring, but manual analysis becomes difficult as the volume of reports increases.<br>
This project explores how machine learning can assist with:<br>
identifying severe outbreaks quickly<br>
prioritizing public health responses<br>
supporting decision-makers with interpretable predictions<br>
The system is intended as a decision support tool, not a replacement for epidemiological expertise.<br>

## Dataset
The dataset consists of World Health Organization Disease Outbreak News (DON) reports.<br>
Reports were collected through web scraping and contain information about:<br>
outbreak descriptions<br>
reported cases<br>
reported deaths<br>
geographic regions<br>
public health responses<br>
Each report is labeled as high severity or low severity based on epidemiological indicators such as reported deaths, case counts, and risk language.<br>

## Feature Engineering
The model combines textual features with structured epidemiological signals.<br>

Text Features <br>

Natural language processing is applied using TF-IDF vectorization to capture important outbreak-related words and phrases.<br>
Examples include:<br>
outbreak<br>
deaths<br>
confirmed cases<br>
Ebola<br>
yellow fever<br>

Structured Features<br>

Additional signals are extracted from the report text:<br>
number of reported deaths<br>
number of reported cases<br>
presence of high-risk emergency phrases<br>
Log transformations are applied to numeric variables to reduce skew.<br>

Model<br>
The final model is a hybrid classification system combining:<br>
TF-IDF text features<br>
structured outbreak indicators<br>
logistic regression classifier<br>

Performance<br>

Final hybrid model results:<br>
Accuracy: ~95%<br>
ROC-AUC: ~0.99<br>
False negatives: minimized after threshold tuning<br>
The model prioritizes recall for severe outbreaks, which is critical for early warning systems.<br>

Model Explainability<br>
To improve interpretability, the project includes SHAP analysis to understand feature contributions.<br>
The most influential predictors include:<br>
reported deaths<br>
emergency risk phrases<br>
reported case counts<br>
This allows analysts to understand why the model flagged an outbreak as severe.<br>

## Deployment
The trained model is deployed as a FastAPI web service and exposed through a REST API.<br>
The API:<br>
receives outbreak text<br>
extracts structured features<br>
applies TF-IDF vectorization<br>
generates a severity prediction<br>
returns the result as JSON<br>

Example response:<br>
{<br>
  "severity_prediction": 1,<br>
  "probability_severe": 0.96<br>
}<br>

The backend API is deployed on Render, while the user interface is deployed on Streamlit Community Cloud.<br>

## API Endpoints

Health Check<br>
GET /health<br>
Confirms that the API service is running.<br>

Prediction Endpoint<br>
POST /predict<br>
Example request:<br>
{<br>
  "report": "Ebola outbreak reported with 350 deaths and rapid spread across multiple regions."<br>
}<br>

## Project Structure
outbreak-severity-mlops
│
├── app.py
├── streamlit_app.py
├── feature_pipeline.py
├── requirements.txt
├── severity_model.pkl
├── tfidf_vectorizer.pkl
│
├── images/
│   └── api_demo.jpg
│   └── ui_demo.jpg
│
├── notebooks/
│   └── scoping_data_modeling_deployment_updated.ipynb
│
└── README.md


## Technologies Used
Python<br>
Scikit-learn<br>
FastAPI<br>
Streamlit<br>
Pandas<br>
NumPy<br>
SHAP<br>
Uvicorn<br>
Render (API deployment)<br>
Streamlit Community Cloud (UI deployment)<br>

## Example Use Cases
Potential applications include:<br>
automated monitoring of outbreak reports<br>
prioritizing global health alerts<br>
assisting epidemiological surveillance systems<br>
supporting public health decision-making<br>

## Ethical Considerations
This system should be used only as a support tool for analysts and public health professionals.<br>
Machine learning predictions should always be interpreted alongside expert judgment.

## Future Improvements
Possible extensions include:<br>
incorporating additional outbreak data sources<br>
adding geographic outbreak modeling<br>
training transformer-based NLP models<br>
building a real-time outbreak monitoring dashboard<br>

## Run Locally
Clone the repository:<br>
git clone https://github.com/princeappiah181/outbreak-severity-mlops.git<br>

Navigate to the project:<br>
cd outbreak-severity-mlops<br>

Install dependencies:<br>
pip install -r requirements.txt<br>

Start the API:<br>
uvicorn app:app --reload<br>

Open the API documentation:<br>
http://127.0.0.1:8000/docs<br>

Run the Streamlit interface:<br>
streamlit run streamlit_app.py<br>

## Author
Prince Appiah, Ph.D<br>
Data Science<br>

This project was developed as a practical exploration of machine learning in production and public health analytics.





