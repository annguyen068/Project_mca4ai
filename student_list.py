import streamlit as st
from data_cleaning import clean_data


input_file = "py4ai-score.csv"
df = clean_data(input_file)



def student_list():
    with st.container():
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.write('Giới tính')
            nam = st.checkbox('Nam',True)
            nu = st.checkbox('Nữ',True)
            gender = []
            if nam:
                gender.append('M')
                
            if nu:
                gender.append('F')

        with col2:
            grades = []
            grade_names = ('Tất cả','Lớp 10','Lớp 11','Lớp 12')
            grade = st.radio('Khối lớp',grade_names)
            if grade == 'Tất cả':
                grades = df['CLASS'].values
            if grade == 'Lớp 10':
                gr10 = df[df['CLASS'].str.startswith('10')]['CLASS'].values
                for i in gr10:
                    grades.append(i)
            if grade == 'Lớp 11':
                gr11 = df[df['CLASS'].str.startswith('11')]['CLASS'].values
                for i in gr11:
                    grades.append(i)
            if grade == 'Lớp 12':
                gr12 = df[df['CLASS'].str.startswith('12')]['CLASS'].values
                for i in gr12:
                    grades.append(i)
            
        with col3:
            room_names = ('Tất cả',
                    'A114',
                    'A115')
            room = st.selectbox('Phòng',options=room_names)
            rooms = []
            if room == 'Tất cả':
                rooms = df['PYTHON-CLASS'].values
            elif room == 'A114':
                rooms.append('114-S')
                rooms.append('114-C')

            else:
                rooms.append('115-S')
                rooms.append('115-C')
                
            
        with col4:
            buoi_names = ['Sáng-Chiều', 'Sáng', 'Chiều']
            session = []

            buoi = st.selectbox('Buổi', buoi_names) 

            if buoi == 'Sáng-Chiều':
                session = df['PYTHON-CLASS'].values
            elif buoi == 'Sáng':
                session.append('114-S')
                session.append('115-S')
            else:
                session.append('114-C')
                session.append('115-C')
        
    st.write('Lớp chuyên')
    with st.container():
        col1b, col2b, col3b,col4b,col5b = st.columns(5)
        classes = []
        with col1b:
            
            van_cl = st.checkbox('Văn',True)
            toan_cl = st.checkbox('Toán',True)

            if van_cl :
                classes.append('10CV1')
                classes.append('10CV2')
            if toan_cl:
                toan = df[(df['CLASS'].str.contains('CT1')) | 
                          (df['CLASS'].str.contains('CT2')) | 
                          (df['CLASS'].str.contains('CT3'))]['CLASS'].values
                for i in toan:
                    classes.append(i)
        with col2b:
            ly_cl = st.checkbox('Lý',True)
            hoa_cl = st.checkbox('Hóa',True)

            if ly_cl:
                classes.append('10CL1')
                classes.append('10CL2')
            if hoa_cl:
                classes.append('10CH2')
                classes.append('12CH1')

        with col3b:

            anh_cl = st.checkbox('Anh',True)
            tin_cl = st.checkbox('Tin',True)
            if anh_cl:
                anh = df[df['CLASS'].str.contains('CA')]['CLASS'].values
                for i in anh:
                    classes.append(i)
            if tin_cl:
                classes.append('10CTIN')
     
        with col4b:

            su_dia_cl = st.checkbox('Sử Địa',True)
            trn_cl = st.checkbox('Trung Nhật',True)

            if su_dia_cl:
                classes.append('10CSD')
                classes.append('11CSD')
            if trn_cl:
                classes.append('10CTRN')
        with col5b:
            th_sn_cl = st.checkbox('TH/SN',True)
            khac_cl = st.checkbox('Khác',True)

            if th_sn_cl:
                th_sn = df[(df['CLASS'].str.contains('TH')) | (df['CLASS'].str.contains('SN'))]['CLASS'].values
                for i in th_sn:
                    classes.append(i)
            if khac_cl:
                khac = df[(df['CLASS'].str.contains('10A')) | 
                          (df['CLASS'].str.contains('11A')) | 
                          (df['CLASS'].str.contains('B')) ]['CLASS'].values
    df_filter = df[(df['GENDER'].isin(gender)) & 
                    (df['CLASS'].isin(grades)) &
                    (df['CLASS'].isin(classes)) &
                    (df['PYTHON-CLASS'].isin(rooms)) & 
                    (df['PYTHON-CLASS'].isin(session))]
    st.write('Số HS',df_filter.shape[0])
    st.write('GPA cao nhất',df_filter['GPA'].max(),'thấp nhất',df_filter['GPA'].min(),'trung bình',round(df_filter['GPA'].mean(),1))
    
    st.dataframe(df_filter)
    