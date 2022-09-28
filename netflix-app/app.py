import streamlit as st
import streamlit.components.v1 as stc
import joblib
import pandas as pd
import os
import altair as alt


# DB management
import sqlite3
conn = sqlite3.connect('streamlit/netfilx-app/data/netflix_titles.sqlite')
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

def plot_prediction_proba(pred_proba_df):
    c = alt.Chart(pred_proba_df).mark_bar().encode(
        x='Classes',
        y='Probabilities',
        color = 'Classes'
    )
    st.altair_chart(c)

#  User interface
custom_title = """
<div style="font-size:40px;font-weight:bolder;background-color:#fff;padding:10px;
border-radius:10px;border:5px solid #464e5f;text-align:center;">
		<span style='color:blue'>N</span>
		<span style='color:black'>E</span>
		<span style='color:black'>T</span>
		<span style='color:black'>F</span>
		<span style='color:green'>L</span>
		<span style='color:blue'>I</span>
		<span style='color:black'>X</span>
		<span style='color:blue'> - </span>
		<span style='color:blue'>M</span>
		<span style='color:#464e5f'>o</span>
		<span style='color:red'>v</span>
		<span style='color:green'>i</span>
		<span style='color:red'>e</span>
		<span style='color:black'>D</span>
		<span style='color:blue'>B</span>
		
</div>
"""

def main():
    stc.html(custom_title)

    menu = ["Home","Predict","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

        with st.form(key = 'searchForm'):
            search_movie = st.text_input("Search Movie")
            submit_button = st.form_submit_button(label="Search")

        if submit_button:
            # Layout
            col1 , col2 = st.columns([1,3])

            with col1:
                st.info("Showing Results For:{}".format(search_movie))

            with col2:
                st.info("Results")
                results = fetch_movie(search_movie.title())

                for i in results:
                    movie_type = i[1]
                    movie_title = i[2]
                    movie_yeaar = i[6]
                    movie_desccription = i[11]
                    with st.expander("{},{}".format(movie_title,movie_type)):
                        st.write(movie_desccription)
    
    elif choice == "Predict":
        st.subheader("Netflix Prediction")

        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='titleForms'):
                search_title = st.text_input("Enter Title Here")
                submit_title_button = st.form_submit_button("Predict")
            
            if submit_title_button:
                prediction = PIPE_TITLE_vs_TYPE_PREDICTOR.predict([search_title])
                predicion_proba = PIPE_TITLE_vs_TYPE_PREDICTOR.predict_proba([search_title])[0]
                st.info(prediction[0])
                pred_proba_df = pd.DataFrame({'Probabilities':predicion_proba,'Classes':PIPE_TITLE_vs_TYPE_PREDICTOR.classes})
                st.dataframe(pred_proba_df)
                plot_prediction_proba(pred_proba_df)
        
        with col2:
            with st.form(key='descFormms'):
                search_desc = st.text_area("Enter Description Here")
                submit_desc_button = st.form_submit_button("Predict")

            if submit_desc_button:
                st.write(search_desc)
                result = PIPE_DESC_vs_TYPE_PREDICTOR.predict([search_desc])
                rating = PIPE_DESC_vs_RATING_PREDICTOR.predict([search_desc])
                st.success(result[0])
                st.info(rating[0])

                pred_proba_df_type = pd.DataFrame({'Probabilities':PIPE_DESC_vs_TYPE_PREDICTOR.predict_proba([search_desc])[0],
                                                    'Classes':PIPE_DESC_vs_TYPE_PREDICTOR.classes_})
                
                pred_proba_df_rating = pd.DataFrame({'Probabilities':PIPE_DESC_vs_RATING_PREDICTOR.predict_proba([search_desc])[0],
                                                    'Classes':PIPE_DESC_vs_RATING_PREDICTOR.classes_})

                with st.expander("Probability:Type"):
                    st.write(pred_proba_df_type)
                    plot_prediction_proba(pred_proba_df_type)
                
                with st.expander("Probability:Rating"):
                    st.write(pred_proba_df_rating)
                    plot_prediction_proba(pred_proba_df_rating)

    else:
        st.subheader("About")

if __name__=='__main__':
    main()