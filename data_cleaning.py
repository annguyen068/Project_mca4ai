import pandas as pd
import re 

def clean_data(input_file):
    # Đọc dữ liệu từ tập tin py4ai-score.csv
    df = pd.read_csv(input_file)

    df.isna().sum()
    df['REG-MC4AI'].fillna(value='N', inplace=True)
    df['BONUS'].fillna(value=0, inplace=True)
    for i in range(1, 11):
        df[f'S{i}'].fillna(value=0, inplace=True)

    def group_filter(row):
        if re.search('CV', row['CLASS']):
            return 'Chuyên Văn'
        if re.search('CTIN', row['CLASS']):
            return 'Chuyên Tin'
        if re.search('CTRN', row['CLASS']):
            return 'Trung Nhật'
        if re.search('CT', row['CLASS']):
            return 'Chuyên Toán'
        if re.search('CL', row['CLASS']):
            return 'Chuyên Lý'
        if re.search('CH', row['CLASS']):
            return 'Chuyên Hoá'
        if re.search('CA', row['CLASS']):
            return 'Chuyên Anh'
        if re.search('CSD', row['CLASS']):
            return 'Sử Địa'
        if re.search('(TH|SN)', row['CLASS']):
            return 'TH/SN'
        return 'Khác'

    df['CLASS-GROUP'] = df.apply(group_filter, axis=1)

    def room_filter(row):
        if re.search('114', row['PYTHON-CLASS']):
            return '114'
        # if re.search('114-S', row['PYTHON-CLASS']):
        #     return '114'
        if re.search('115', row['PYTHON-CLASS']):
            return '115'
        # if re.search('115-C', row['PYTHON-CLASS']):
        #     return '115'
    
    df['ROOMS'] = df.apply(room_filter, axis=1)

    def grade_filter(row):
        if re.search('10', row['CLASS']):
            return '10'
        if re.search('11|12', row['CLASS']):
            return '11+12'
    
    df['GRADES'] = df.apply(grade_filter, axis=1)   
    
    df['S-AVG'] = (df['S1'] + df['S2'] + df['S3'] + df['S4'] + df['S5'] + df['S7'] + df['S8'] + df['S9']) / 8
    
    return df
