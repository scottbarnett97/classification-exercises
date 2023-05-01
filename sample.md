# Classification Project Summary

## Project Objectives
> - Document the code, the process, the findings, and the key takeaways in a Jupyter Notebook Final Report
> - Create modules that make the process repeatable and the report easier to read and follow
> - Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers
> - Refine work with a Report, in the form of a jupyter notebook, that will be walked through in a 5 minute presentation to a group of collegues and managers about the work did, why, goals, what was found, methodologies, and conclusions.
> - Answer panel questions about the code, process, findings and takeaways, and model.

## Business Goals
> - Find drivers for customer churn at Telco.  Why are customers churning?
> - Construct a ML classification model that accurately predicts customer churn.
> - Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

## Deliverables
> - Readme (.md)
> - Final Report (.ipynb)
> - Acquire and Prepare Modules (.py)
> - Predictions (.csv)
> - A non_final Notebook (.ipynb)


## Data Dictionary

|Target|Datatype|Definition
|:-------|:-------|:----------|
|churn|7043 non-null: int64| 1: customer has churned, 0: customer hasn't churned|

|Feature|Datatype|Definition|
|:-------|:-------|:----------|
|customer_id                        |7043 non-null: object | identifier for each individual customer's account|
|senior_citizen                     |7043 non-null: int64  | 1: is senior citizen, 0: ins't senior citizen|
|tenure                             |7043 non-null: int64  | how long a customer has been utilizing telco services|
|monthly_charges                    |7043 non-null: float64| how much a customer pays per month|
|total_charges                      |7043 non-null: float64| how much a customer has paid since beginning their services with telco|
|is_female                          |7043 non-null: int64  | 1: is a female, 0: is a male|
|has_partner                        |7043 non-null: int64  | 1: has a significant other, 0: is single|
|has_dependents                     |7043 non-null: int64  | 1: has children, 0: doesn't have children|
|has_phone_service                  |7043 non-null: int64  | 1: has phone service with telco, 0: doesn't have phone service through telco|
|multiple_lines_Yes                 |7043 non-null: uint8  | 1: has multiple phone lines, 0: doesn't have multiple phone lines|
|online_security_Yes                |7043 non-null: uint8  | 1: utilizes online security services, 0: doesn't use online security|
|online_backup_Yes                  |7043 non-null: uint8  | 1: has online backup services via telco, 0: doesn't use online backup services|
|device_protection_Yes              |7043 non-null: uint8  | 1: has device protection via telco, 0: doesn't have device protection|
|tech_support_Yes                   |7043 non-null: uint8  | 1: has technical support services with telco, 0: doesn't have technical support services|
|streaming_tv_Yes                   |7043 non-null: uint8  | 1: has tv streaming capabilities with their account, 0: doesn't have tv streaming|
|streaming_movies_Yes               |7043 non-null: uint8  | 1: has movie streaming capabilities with their account, 0: doesn't have movie streaming|
|contract_type_One year             |7043 non-null: uint8  | 1: must renew their contract every year, 0: doesn't renew their contract each year|
|contract_type_Two year             |7043 non-null: uint8  | 1: must renew their contract every two years, 0: doesn't renew their contract every two years|
|internet_service_type_Fiber optic  |7043 non-null: uint8  | 1: has fiber optic internet, 0: doesn't have fiber optic internet|
|internet_service_type_None         |7043 non-null: uint8  | 1: doesn't have internet service via telco, 0: does have internet service with telco|
|payment_type_Credit car (automatic)|7043 non-null: uint8  | 1: makes payments via automatic credit card transfer, 0: doesn't use automatic credit card transfer|
|payment_type_Electronic check      |7043 non-null: uint8  | 1: makes payments via electronic checks, 0: doesn't use electronic checks to make payments|
|payment_type_Mailed check          |7043 non-null: uint8  | 1: makes payments via mailed in checks, 0: doesn't use mailed checks to make payments|

## Initial Hypotheses
> I believe that monthly charges and total charges will play a large part in whether a customer will churn or not.  The questions I need answered are how the other features may influence how much a customer may pay at any given time and if specific demographics affect the price threshold for customers (such as age or gender).

## Executive Summary - Key Findings and Recommendations
> 1. Utilizing the following features outlined in X_train, X_validate, and X_test I was able to narrow down my best model for predicting churn at Telco using a random forest model with a max depth of 5 and an 80% accuracy rate.

> 2. Many features help to predict churn with some of the bigger predictors being age (senior_citizen), how much a customer is paying (monthly_charges, total_charges, contract_type, payment_type) and what's affecting how much they pay (internet_service_type), and finally whether customers have adequate support with their plan (tech_support)

> 3. My recommendations are that customers are encouraged to sign up with a one or two year contract by maybe offering technical support included.  We should also focus on a younger crowd who has an established family because they tend to churn at a lesser rate.

## Project Plan

### Planning Phase

> - Created a README.md file
> - Imported all of my tools and files needed to properly conduct the project

### Acquire Phase

> - Utilized my acquire file to pull telco data from a Codeup database

### Prepare Phase

> - Utilized my prepare file to clean up my telco dataset
> - Split the overall dataset into my train, validate, and test datasets
> - Utilized my explore file to create a list of numerical datatype features and a list of categorical datatype features for future exploration

### Explore Phase

> - Created a for loop that used my explore file to create a visualization for every categorical feature.  The explore file also allowed for hypothesis testing each feature to ensure a relationship between the feature and the target (churn).
> - Asked further questions about that data such as how monthly charges effects churn rate and the relationship between other features and monthly charges.  Also explored how age played a part in churn rate and if any other feature could assist in predicting churn for older customers.

### Model Phase

> - Set up the baseline accuracy for future models to base their success on
> - Trained multiple models for each type of classification technique (Decision Tree, Logistic Regression, Random Forest, KNN)
> - Validated all models to narrow down my selection to the best performing model.
> - Chose the MVP of all created models and used the test data set to ensure the best model worke entirely to expectations

### Deliver Phase

> - Prepped my final notebook with a clean presentation to best present my findings and process to other Data Scientists and stakeholders alike.
> - Ensured that a prediction csv was generated for future proof of my working model

## How To Reproduce My Project

> 1. Read this README.md
> 2. Download the acquire.py, prepare.py, explore.py and final_report.ipynb files into your directory along with your own env file that contains your user, password, and host variables
> 3. Run my final_report.ipynb notebook
> 4. Congratulations! You can predict future churn at Telco!