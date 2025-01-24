import pandas as pd

# อ่านข้อมูลจากไฟล์ Excel
input_file = 'CT/input_3260.xlsx'  # ไฟล์ต้นฉบับ
output_file = 'CT/output_3260.xlsx'  # ไฟล์ผลลัพธ์

# อ่านข้อมูลเข้า DataFrame
df = pd.read_excel(input_file)

# แยก servicename เป็นลิสต์และจัดเรียง
df['servicename_list'] = df['servicename'].apply(lambda x: sorted(x.split(',')))

# แปลงรายการ servicename เป็นข้อความเพื่อจัดกลุ่ม
df['sorted_services'] = df['servicename_list'].apply(lambda x: ','.join(x))

# นับจำนวนความถี่ของกลุ่มบริการ
frequency = df['sorted_services'].value_counts().reset_index()
frequency.columns = ['sorted_services', 'frequency']

# รวมผลลัพธ์กลับไปยัง DataFrame เดิม
df = df.merge(frequency, on='sorted_services', how='left')

# บันทึกไฟล์ Excel
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Processed Data')
    frequency.to_excel(writer, index=False, sheet_name='Frequency Analysis')

print(f"ไฟล์ผลลัพธ์ถูกบันทึกที่ {output_file}")
