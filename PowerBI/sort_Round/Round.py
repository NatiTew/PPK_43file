# import pandas as pd
#
# # อ่านไฟล์ Excel
# df = pd.read_excel('Data/data_Round.xlsx')
#
# # แปลงคอลัมน์ `date` เป็น datetime
# df['date'] = pd.to_datetime(df['date'], errors='coerce')
#
# # อ่านไฟล์ Excel ที่มีวันหยุดเพิ่มเติม
# holidays = pd.read_excel('Data/Holiday.xlsx')
# holidays['date'] = pd.to_datetime(holidays['date'], errors='coerce').dt.date
# # print(holidays)
#
# # ลบข้อมูลที่ซ้ำกันโดยยึดตามรายการแรกที่ลงมาก่อน
# df.sort_values(by='date', inplace=True)  # จัดเรียงตามวันที่ก่อน
# df.drop_duplicates(subset=['date', 'customer_id'], keep='first', inplace=True)
#
# # สร้าง DataFrame ใหม่สำหรับบันทึกข้อมูลที่เติมเข้ามา
# new_entries = []
#
# # สร้าง DataFrame ที่มีข้อมูลทุกวันที่ต้องการ (ในกรณีนี้ใช้ช่วงเวลาในข้อมูลที่มีอยู่)
# all_dates = pd.date_range(start=df['date'].min().date(), end=df['date'].max().date(), freq='D')
#
#
# # รายชื่อ unique
# unique_customers = df[['customer_id', 'customer_name']].drop_duplicates(subset='customer_id', keep='first')
# # name = unique_customers.values.tolist()
# # print(unique_customers)
#
# data = df[['date', 'customer_id', 'customer_name', 'order', 'urlP']].drop_duplicates()
# data['date'] = pd.to_datetime(data['date'], errors='coerce').dt.date
# # real = data.values.tolist()
#  # print(data['date'])
#
# for single_date in all_dates:
#     # print(single_date.date())
#     # ข้ามวันเสาร์และอาทิตย์
#     if single_date.weekday() >= 5:
#         continue
#
#     # ข้ามวันหยุดเพิ่มเติม
#     if single_date.date() in holidays['date'].values:
#         print(single_date)
#         continue
#
#     for index_name, row_name in unique_customers.iterrows():
#         # print(row_name['customer_id'])
#         check1 = False
#         for index, row in data.iterrows():
#             if single_date.date() == row['date'] and row_name['customer_id'] == row['customer_id']:
#                 check1 = True
#                 break
#         if check1 == False:
#             # print(str(single_date) + row_name['customer_id'])
#             new_entries.append({
#                 'date': pd.Timestamp(f'{single_date} 07:00'),
#                 'customer_id': row_name['customer_id'],
#                 'customer_name': row_name['customer_name'],
#                 'order': 'ไม่พบข้อมูล',
#                 'urlP': 'NoPic'
#             })
#
# # เพิ่มข้อมูลใหม่เข้าไปใน DataFrame เดิม
# df_new_entries = pd.DataFrame(new_entries)
# df = pd.concat([df, df_new_entries])
#
# # จัดเรียงข้อมูลตามวันที่และเวลา
# df.sort_values(by='date', inplace=True)
#
# # จัดเก็บข้อมูลลงในไฟล์ Excel ใหม่
# df.to_excel('Data/new_file.xlsx', index=False)
#
# print("การจัดการข้อมูลเสร็จสมบูรณ์และบันทึกลงในไฟล์ Excel ใหม่เรียบร้อยแล้ว")
#
#

import pandas as pd

# อ่านไฟล์ Excel
df = pd.read_excel('Data/data_Round.xlsx')

# แปลงคอลัมน์ `date` เป็น datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# อ่านไฟล์ Excel ที่มีวันหยุดเพิ่มเติม
holidays = pd.read_excel('Data/Holiday.xlsx')
holidays['date'] = pd.to_datetime(holidays['date'], errors='coerce').dt.date

# ลบข้อมูลที่ซ้ำกันโดยยึดตามรายการแรกที่ลงมาก่อน
df.sort_values(by='date', inplace=True)  # จัดเรียงตามวันที่ก่อน
df.drop_duplicates(subset=['date', 'customer_id'], keep='first', inplace=True)

# สร้าง DataFrame ใหม่สำหรับบันทึกข้อมูลที่เติมเข้ามา
new_entries = []

# สร้าง DataFrame ที่มีข้อมูลทุกวันที่ต้องการ (ในกรณีนี้ใช้ช่วงเวลาในข้อมูลที่มีอยู่)
all_dates = pd.date_range(start=df['date'].min().date(), end=df['date'].max().date(), freq='D')

# รายชื่อ unique
unique_customers = df[['customer_id', 'customer_name']].drop_duplicates(subset='customer_id', keep='first')

# ตรวจสอบแต่ละวันในช่วงวันที่ทั้งหมด
for single_date in all_dates:
    # ข้ามวันเสาร์และอาทิตย์
    if single_date.weekday() >= 5:
        continue

    # ข้ามวันหยุดเพิ่มเติม
    if single_date.date() in holidays['date'].values:
        continue

    # รายชื่อที่ลงชื่อในวันนั้นๆ
    signed_in_today = df[df['date'].dt.date == single_date.date()]['customer_id'].unique()

    # ตรวจสอบแต่ละคนในรายชื่อทั้งหมด
    for index_name, row_name in unique_customers.iterrows():
        if row_name['customer_id'] not in signed_in_today:
            new_entries.append({
                'date': pd.Timestamp(f'{single_date} 07:00'),
                'customer_id': row_name['customer_id'],
                'customer_name': row_name['customer_name'],
                'order': 'ไม่พบข้อมูล',
                'urlP': 'NoPic'
            })

# เพิ่มข้อมูลใหม่เข้าไปใน DataFrame เดิม
df_new_entries = pd.DataFrame(new_entries)
df = pd.concat([df, df_new_entries], ignore_index=True)

# จัดเรียงข้อมูลตามวันที่และเวลา
df.sort_values(by='date', inplace=True)

# จัดเก็บข้อมูลลงในไฟล์ Excel ใหม่
df.to_excel('Data/new_file.xlsx', index=False)

print("การจัดการข้อมูลเสร็จสมบูรณ์และบันทึกลงในไฟล์ Excel ใหม่เรียบร้อยแล้ว")





