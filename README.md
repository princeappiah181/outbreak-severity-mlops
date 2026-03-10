# Public Health Outbreak Severity Prediction (MLOps Project)

## API Demo

![API Demo](images/api_demo.jpg)

## Live API

The deployed API is available here:

https://outbreak-severity-api.onrender.com/docs

## Overview
This project builds an end-to-end machine learning system that analyzes disease outbreak reports and predicts whether an outbreak is high 
severity or low severity.<br>
The goal is to demonstrate how machine learning can support early warning systems for public health by automatically analyzing outbreak
reports and identifying events that may require urgent attention.The system processes outbreak text, extracts epidemiological indicators such 
as reported cases and deaths, and combines them with natural language features to generate a severity prediction.<br>
This repository also demonstrates the full machine learning lifecycle, including data processing, model training, explainability, and 
deployment as a production API.

## Motivation
Disease outbreak reports contain valuable information for public health monitoring, but manual analysis does not scale when reports are 
collected from multiple sources.
This project explores how machine learning can assist with:<br>
identifying severe outbreaks quickly<br>
prioritizing public health response<br>
supporting decision-makers with interpretable predictions<br>
The system is intended as a decision support tool, not a replacement for epidemiological expertise.

## Dataset
The dataset consists of World Health Organization Disease Outbreak News (DON) reports.
The reports were collected through web scraping and contain information about:<br>
outbreak description<br>
case counts<br>
death counts<br>
geographic regions<br>
public health response

Each report is labeled as high severity or low severity based on epidemiological indicators such as reported deaths, case counts, and 
risk language.

## Feature Engineering
The model combines textual information and structured epidemiological signals.

### Text Features
Natural language processing is applied using TF-IDF vectorization to capture important words and phrases related to disease outbreaks.
Examples include:<br>
outbreak<br>
deaths<br>
confirmed cases<br>
Ebola<br>
yellow fever<br>

### Structured Features
Additional features are extracted from the report text:<br>
number of reported deaths<br>
number of reported cases<br>
presence of high-risk emergency phrases<br>
Log transformations are applied to numeric variables to reduce skew.

## Model
The final model is a hybrid classification system combining:<br>
TF-IDF text features<br>
structured outbreak indicators<br>
A logistic regression classifier is trained on the combined feature space.

Performance
Final hybrid model results:<br>
Accuracy: ~95%<br>
ROC-AUC: ~0.99<br>
False negatives: very low after threshold tuning<br>
The model prioritizes recall for severe outbreaks, which is important in early warning systems.

Model Explainability
To ensure interpretability, the project includes SHAP analysis to understand feature contributions.<br>
The most influential features include:<br>
reported deaths<br>
emergency risk phrases<br>
reported case counts<br>
This allows users to see why the model flagged an outbreak as severe.

## Deployment
The trained model is deployed as a FastAPI web service.<br>
The API:<br>
receives outbreak text<br>
extracts structured features<br>
applies TF-IDF vectorization<br>
generates a severity prediction<br>
returns the result as JSON<br>
Example API response:<br>
{<br>
  "severity_prediction": 1,<br>
  "probability_severe": 0.96<br>
}<br>
The service is deployed on Render.<br>
API Endpoints<br>
Health Check<br>
GET /health<br>
Confirms that the service is running.<br>

Prediction Endpoint<br>
POST /predict<br>
Example request:<br>
{<br>
  "report": "Ebola outbreak reported with 350 deaths and rapid spread across multiple regions."<br>
}<br>

## Project Structure
outbreak-severity-mlops<br>
│<br>
├── app.py<br>
├── feature_pipeline.py<br>
├── requirements.txt<br>
├── severity_model.pkl<br>
├── tfidf_vectorizer.pkl<br>
├── notebooks<br>
│   └── modeling_and_analysis.ipynb<br>
└── README.md

## Technologies Used
Python<br>
Scikit-learn<br>
FastAPI<br>
Pandas<br>
NumPy<br>
SHAP<br>
Uvicorn<br>
Render (deployment)<br>

Example Use Cases<br>
Potential applications include:<br>
automated monitoring of outbreak reports<br>
prioritizing global health alerts<br>
assisting epidemiological surveillance systems<br>

Ethical Considerations<br>
This system should be used only as a support tool for analysts and public health professionals.<br>
Machine learning predictions should always be interpreted alongside expert judgment.

Future Improvements<br>
Possible extensions include:<br>
incorporating additional data sources<br>
adding geographic outbreak modeling<br>
training transformer-based NLP models<br>
building a real-time dashboard for outbreak monitoring<br>

## Run Locally

Clone the repository

git clone https://github.com/princeappiah181/outbreak-severity-mlops.git

cd outbreak-severity-mlops

Install dependencies

pip install -r requirements.txt

Start the API

uvicorn app:app --reload

Open the API docs

http://127.0.0.1:8000/docs

## Author
Prince Appiah, Ph.D <br>
Data Science

This project was developed as part of a practical exploration of machine learning in production and public health analytics.
