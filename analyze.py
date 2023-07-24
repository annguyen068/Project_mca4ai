import pandas as pd
import streamlit as st
import plotly.express as px
# from student_list import student_list
from data_cleaning import clean_data

# input_file = "cleaned_data.csv"
# df = clean_data(input_file)

# Hàm vẽ biểu đồ tỷ lệ học sinh
def draw_student_ratio_chart(data, column_name, titles):
    fig = px.pie(data, names=column_name, title=titles)
    st.plotly_chart(fig)

def analyze_student_ratio(data):
    # Tạo selectbox để chọn loại biểu đồ
    chart_type = st.selectbox('Chọn loại biểu đồ', ['Giới tính', 'Phòng học', 'Lớp chuyên', 'Khối'])

    # Dựa vào lựa chọn của người dùng, lọc dữ liệu và vẽ biểu đồ phù hợp
    if chart_type == 'Giới tính':
        draw_student_ratio_chart(data, 'GENDER', 'Tỉ lệ học sinh theo ' + chart_type)
        st.write('Nam hứng thú với AI hơn')
    elif chart_type == 'Phòng học':
        draw_student_ratio_chart(data, 'ROOMS', 'Tỉ lệ học sinh theo ' + chart_type)
    elif chart_type == 'Lớp chuyên':
        draw_student_ratio_chart(data, 'CLASS-GROUP', 'Tỉ lệ học sinh theo ' + chart_type)
    elif chart_type == 'Khối':
        draw_student_ratio_chart(data, 'GRADES', 'Tỉ lệ học sinh theo ' + chart_type)


def draw_student_distribution_chart(data, session, column_name):
    st.plotly_chart(px.histogram(data, x = session, range_x=(0,10), color = column_name), theme = None)

def analyze_student_distribution(data):
    # Tạo các checkbox cho việc chọn S1, S2, ..., S10 và GPA
    col1, col2, col3, col4,col5 = st.columns(5)
    # selected_sessions = []
    with col2:
        selected_sessions = st.selectbox('Chọn các Session', [f'S{i}' for i in range(1, 11)] )
        # Tạo radio button list cho việc chọn loại biểu đồ
    with col4:
        chart_type = st.radio('Phân loại', ['Giới tính', 'Phòng học', 'Lớp chuyên', 'Khối'])

    
    col_chart1, col_chart2, col_chart3, col_chart4 = st.columns(4)
    with col_chart1:            
        # Dựa vào lựa chọn của người dùng, lọc dữ liệu và vẽ biểu đồ phù hợp
        if chart_type == 'Giới tính':
            draw_student_distribution_chart(data, selected_sessions, 'GENDER')
        elif chart_type == 'Phòng học':
            draw_student_distribution_chart(data, selected_sessions, 'ROOMS')
        elif chart_type == 'Lớp chuyên':
            draw_student_distribution_chart(data, selected_sessions, 'CLASS-GROUP')
        elif chart_type == 'Khối':
            draw_student_distribution_chart(data, selected_sessions, 'GRADES')
    
    with col_chart3:
        # st.plotly_chart(px.pie(data[data['GPA'] >= 6],'CLASS-GROUP',title='Tỉ lệ đậu lớp MC'))
        draw_student_ratio_chart(data[data['GPA'] >= 6],'CLASS-GROUP', 'Tỉ lệ đậu lớp MC theo GPA')
    
    st.write('''

    Kết luận:\n
        - Phân bố điểm giữa các session không đồng đều.\n
        - Đa số đạt điểm tối đa.\n
        - Điểm số của S10 được rải đều, và là Session có nhiều dưới trung bình nhất.\n
        - Tỉ lệ đậu lớp MC thuộc vào lớp chuyên Toán nhiều nhất.\n
        --> Session 10 (Final exam) có độ khó cao nhất.\n
        --> Các Session khác điểm cao có thể không nhờ vào năng lực thực.\n

    ''')