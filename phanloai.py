import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def phanloai(data):
    col1,col2 =st.columns(2)
    with col1:
        # Chọn features và target
        X = data[['S-AVG', 'S6']]
        y = data['S10']

        # Cho phép người dùng nhập số lượng test thông qua widget number_input
        test_size1 = st.number_input('Số lượng test (phần trăm)', min_value=0.1, max_value=0.9, step=0.1, value=0.1,key="linear")
        
        # Chia dữ liệu thành tập train và test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size1)

        # Xây dựng mô hình Linear Regression
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Dự đoán điểm S10 trên tập test
        y_pred = model.predict(X_test)

        st.write(f'Độ chính xác: {round(model.score(X_test, y_test),1)}')
        
        df_test = pd.DataFrame({'NAME': data.loc[y_test.index, 'NAME'],'S-AVG': data.loc[y_test.index, 'S-AVG'], 'S6': data.loc[y_test.index, 'S6'], 'S10_actual': y_test, 'S10_predicted': y_pred})
        st.dataframe(df_test, width = 800)
        

       
        st.write('Độ chính xác của khi dự đoán điểm thi cuối kì dựa vào Điểm thi giữa kì và Điểm bài tập không cao')

    with col2:
        X = data[['S6', 'S10']]
        y = data['GPA']

        # Cho phép người dùng nhập số lượng test thông qua widget number_input
        test_size2 = st.number_input('Số lượng test (phần trăm)', min_value=0.1, max_value=0.9, step=0.1, value=0.1, key="logistic")

        # Chia dữ liệu thành tập train và test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size2)
        
        # Xây dựng mô hình Linear Regression
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Dự đoán điểm GPA trên tập test
        y_pred = model.predict(X_test)

        st.write(f'Độ chính xác (linear): {round(model.score(X_test, y_test), 3)}')

        df_test = pd.DataFrame({'NAME': data.loc[y_test.index, 'NAME'], 'S6': data.loc[y_test.index, 'S6'],'S10': data.loc[y_test.index, 'S10'],'GPA_ACTUAL': y_test, 'GPA_predicted': y_pred})
        st.dataframe(df_test, width = 800)
        st.write('Độ chính xác của khi dự đoán điểm GPA dựa vào Điểm thi giữa kì và Điểm cuối kì rất cao, hơn 80%')

        


