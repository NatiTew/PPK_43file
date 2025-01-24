import pandas as pd

# โหลดข้อมูลจากไฟล์
df = pd.read_csv('Lastcase\\input.csv', encoding='utf-8')  # หรือใช้ pd.read_excel('your_file.xlsx')

# แปลงคอลัมน์ 'startdatetime' และ 'operdate' เป็นรูปแบบ datetime
df['startdatetime'] = pd.to_datetime(df['startdatetime'])
df['operdate'] = pd.to_datetime(df['operdate']).dt.date

# กรองข้อมูลที่ startdatetime ไม่เกิน 16:00:00 และ flag_emergency เป็น 'N'
filtered_df = df[(df['startdatetime'].dt.time <= pd.to_datetime('16:00:00').time())]
# filtered_df = df[(df['startdatetime'].dt.time <= pd.to_datetime('16:00:00').time()) &
#                  (df['flag_emergency'] == 'N')]

# หาตำแหน่งของเคสสุดท้ายของแต่ละห้องในแต่ละวัน
last_cases = filtered_df.loc[filtered_df.groupby(['oper_room', 'operdate'])['startdatetime'].idxmax()]

# สร้างคอลัมน์ใหม่ 'status' และระบุว่าเป็น 'Lastcase' สำหรับเคสสุดท้ายที่พบ
df['status'] = 'Not Lastcase'
df.loc[last_cases.index, 'status'] = 'Lastcase'

# ตรวจสอบผลลัพธ์
print(df)

# บันทึกผลลัพธ์ลงไฟล์
df.to_csv('Lastcase\\updated_file.csv', index=False, encoding='utf-8')  # หรือใช้ df.to_excel('updated_file.xlsx', index=False)



