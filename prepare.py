import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import numpy as np
import env
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def prep_iris(df):
    '''
    This function will drop any duplicate observations, 
    drop ['species_id', 'measurement_id'],Rename the species_name column to just species
    and create dummy variables of the species name and concatenate onto the iris dataframe. 
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['species_id', 'measurement_id'])
    df.rename(columns ={'species_name' : 'species'}, inplace=True)
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)
    return df


def prep_titanic(df):
    '''
    This function will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'], fill missing embark_town with 'Southampton'
    and create dummy vars from sex and embark_town. 
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['deck', 'embarked', 'class', 'age'])
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df



def prep_telco(df):
    '''
    This function will drop any duplicate observations, 
    drop [payment_type_id', 'internet_service_type_id','contract_type_id']
    and create dummy vars from 'gender','partner','dependents','tech_support','streaming_tv','streaming_movies'
                                ,'paperless_billing','churn','contract_type','internet_service_type','payment_type'. 
    '''
    df = df.drop_duplicates()
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id','contract_type_id'])    
    dummy_df = pd.get_dummies(df[['gender','partner','dependents','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','contract_type','internet_service_type','payment_type']], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def split_data(df,strat):
    '''
    Be sure to code it as train, validate, test = split_data(df,'column you want to stratify')
    take in a DataFrame and return train, validate, and test DataFrames; stratify on survived.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[{strat}])
    train, validate = train_test_split(train_validate, 
                                       test_size=.25, 
                                       random_state=123, 
                                       stratify=train_validate[{strat}])
    # Validate my split.
    print(f'train -> {train.shape}, {round(train.shape[0]*100 / df.shape[0],2)}%')
    print(f'validate -> {validate.shape},{round(validate.shape[0]*100 / df.shape[0],2)}%')
    print(f'test -> {test.shape}, {round(test.shape[0]*100 / df.shape[0],2)}%')
    return train, validate, test

