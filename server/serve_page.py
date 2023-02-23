
import psycopg2
import json 
import pandas as pd
import pandas.io.sql as sqlio
import streamlit as st

db_name = 'properties'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'postgres'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
conn = psycopg2.connect(db_string)


def path_to_image_html(path):
    return '<img src="' + path + '" width="240" >'

@st.cache_data
def convert_df(input_df):
     input_df.rename(columns={"prop_name": "listing name", "img_src": "image"}, inplace=True)
     return input_df.to_html(escape=False, formatters=dict(image=path_to_image_html))


if __name__ == "__main__":
    sql = "select prop_name, img_src from props;"
    df = sqlio.read_sql_query(sql, conn)
    conn.close()
    
    st.title(f'Sreality - {len(df)} items:')

    html = convert_df(df)

    st.markdown(
        html,
        unsafe_allow_html=True
    )