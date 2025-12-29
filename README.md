# Project Demeter: Machine Learning Based Crop Prediction

Project Demeter is a personalized agricultural guidance system developed by Team Troubleshooters for Junior Makeathon 2021. It utilizes machine learning to help farmers choose the most suitable and profitable crops based on their specific land conditions, bridging the gap between traditional experience and scientific knowledge.

## Problem Statement
Choosing the right crop and seed for a specific piece of land is a complex challenge due to numerous variables like soil health, weather, and market conditions. Existing solutions often provide only generic information or focus solely on crop health rather than yield and profit optimization.


## Our Solution
Demeter provides a web-based application (with plans for mobile integration) that offers personalized yield predictions. By analyzing specific environmental and soil data, the app generates Cultivation Plans that include:



- Major and Subordinate Crop Choices.


- Estimated Investment and Profit.


- Fertilizer Requirements based on NPK levels.

- A Detailed Timeline from land preparation to harvest.

## Technical Features
### Data Inputs
The system processes a wide variety of factors to ensure accurate predictions:


Environmental: Rainfall, Temperature, and Humidity.



Soil Parameters: pH value and NPK (Nitrogen, Phosphorus, Potassium) levels.



Land Characteristics: Total area and soil type.


### Machine Learning Model

Algorithm: The prototype utilizes a Machine Learning algorithm (initially modeled using dummy/simulated data) to output predicted yield.




Training: The model was trained using Normal Distribution Data generated via SciKit as public data was unavailable.


Framework: Built using a Python-Flask backend to manage CRUD operations and serve the ML model responses.


## Prototype Development
Backend: Python-Flask framework.


Machine Learning: Scikit-Learn for model training and parameter tuning, using Decision Trees algorithm. 



Frontend: Web Application (HTML/CSS) for the prototype.



Data Strategy: * Synthetic Data: Utilized Normal Distribution data generation as public datasets were unavailable at time of development.



Model Mapping: Mapped agricultural inputs to structural formats inspired by the Boston Housing Sample for robust initial prototyping
