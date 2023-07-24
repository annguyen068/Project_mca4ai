import streamlit as st
import pandas as pd
from data_cleaning import clean_data
from student_list import student_list
from analyze import analyze_student_ratio
from analyze import analyze_student_distribution
from kmeans import classify
from phanloai import phanloai

input_file = "py4ai-score.csv"
df = clean_data(input_file)

st.set_page_config(layout="wide")

st.title('Phân tích và xem điểm Python4AI')


tabs_titles = ('Danh sách',
               'Phân tích thống kê',
               'Phân nhóm',
               'Phân loại')
tabs = st.tabs(tabs_titles)
with tabs[0]:
    student_list()

with tabs[1]:
    tabs1_titles = ('Tỷ lệ học sinh',
                    'Điểm')
    tabs1 = st.tabs(tabs1_titles)
    with tabs1[0]:
        analyze_student_ratio(df)
    with tabs1[1]:
        analyze_student_distribution(df)

with tabs[2]:
    number = int(st.slider('Number input',min_value=1,max_value=10, step = 1))
    if st.button('OK'):
        classify(df, number)
    

with tabs[3]:
    phanloai(df)
    



