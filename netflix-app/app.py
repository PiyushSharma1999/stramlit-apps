import streamlit as st
import streamlit.components.v1 as stc
import joblib
import pandas as pd
import os
import altair as alt


# DB management
import sqlite3
conn = sqlite3.connect('data/netflix_titles.csv')
c = conn.cursor()

# Search function

def fetch_movie(title):
    c.execute("SELECT * FROM netflix_titles WHERE title LIKE '%{}%'".format(title))
    data = c.fetchall()
    return data

# Load models

def load_model(model_file):
    model = joblib.load(open(os.path.join(model_file),"rb"))
    return model

# Models
PIPE_TITLE_vs_TYPE_PREDICTOR =load_model('models/pipe_lr_cv_title_type_prediction_sept_27_2021_model.pkl')
PIPE_DESC_vs_TYPE_PREDICTOR =load_model('models/pipe_lr_cv_type_desc_prediction_sept_27_2021_model.pkl')
PIPE_DESC_vs_RATING_PREDICTOR =load_model('models/pipe_nb_desc_rating_sept_27_2021_model.pkl')