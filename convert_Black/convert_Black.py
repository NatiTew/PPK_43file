import pandas as pd

while(True):
    input_k = input("Enter your choice OPD = 1, IPD = 2 : ")
    if input_k == "1":
        file_search_O = pd.read_excel('data_F43/DIAGNOSIS_OPD.xlsx', dtype=str)
        file_data_O = pd.read_csv('data_F43/diagnosis_opd.txt', sep='|', dtype=str, encoding='utf-8')
        file_search_O['status'] = ""
        # วนลูปตามเงื่อนไขของข้อมูลในไฟล์ค้นหา
        for index, row in file_search_O.iterrows():
            if pd.notna(row['black']):
                # ค้นหาแถวที่ตรงกันในไฟล์ข้อมูล
                matching_rows = file_data_O[
                    (file_data_O['SEQ'] == row['seq']) &
                    (file_data_O['DATE_SERV'] == row['date_serv']) &
                    (file_data_O['DIAGTYPE'] == row['diagtype']) &
                    (file_data_O['DIAGCODE'] == row['diagcode'])
                    ]

                if not matching_rows.empty:
                    file_data_O.loc[matching_rows.index, 'DIAGCODE'] = row['black']
                    file_search_O.at[index, 'status'] = "done"
                else:
                    file_search_O.at[index, 'status'] = "not done"
            else:
                # เงื่อนไขเพิ่มเติมเมื่อ row['black'] เป็นค่าว่าง
                if row['diagcode'] in ['I480', 'I481', 'I482', 'I489', 'I483', 'I484']:
                    file_data_O.loc[file_data_O['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'I48'
                    file_search_O.at[index, 'black'] = "I48"
                    file_search_O.at[index, 'status'] = "Done_I48&J96x"
                elif row['diagcode'] in ['J9600', 'J9601', 'J9609']:
                    file_data_O.loc[file_data_O['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'J960'
                    file_search_O.at[index, 'black'] = "J960"
                    file_search_O.at[index, 'status'] = "Done_I48&J96x"
                elif row['diagcode'] in ['J9610', 'J9611', 'J9619']:
                    file_data_O.loc[file_data_O['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'J961'
                    file_search_O.at[index, 'black'] = "J961"
                    file_search_O.at[index, 'status'] = "Done_I48&J96x"
                elif row['diagcode'] in ['J9690', 'J9691', 'J9699']:
                    file_data_O.loc[file_data_O['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'J969'
                    file_search_O.at[index, 'black'] = "J969"
                    file_search_O.at[index, 'status'] = "Done_I48&J96x"

        # บันทึกไฟล์ข้อมูลที่ถูกแก้ไขเป็น .txt โดยคั่นด้วยเครื่องหมาย | และแปลงเป็น UTF-8
        file_data_O.to_csv('data_F43/updated_diagnosis_opd.TXT', sep='|', index=False, encoding='utf-8')

        # บันทึกไฟล์ค้นหาที่มีการอัปเดตสถานะเป็นไฟล์ Excel
        file_search_O.to_excel('data_F43/updated_DIAGNOSIS_OPD.xlsx', index=False)
        print("Update OPD done")

    elif input_k == "2":
        file_search_I = pd.read_excel('data_F43/DIAGNOSIS_IPD.xlsx', dtype=str)
        file_data_I = pd.read_csv('data_F43/diagnosis_ipd.txt', sep='|', dtype=str, encoding='utf-8')
        file_search_I['status'] = ""
        # วนลูปตามเงื่อนไขของข้อมูลในไฟล์ค้นหา
        for index, row in file_search_I.iterrows():
            if pd.notna(row['black']):
                # ค้นหาแถวที่ตรงกันในไฟล์ข้อมูล
                matching_rows = file_data_I[
                    (file_data_I['AN'] == row['an']) &
                    (file_data_I['DATETIME_ADMIT'] == row['datetime_admit']) &
                    (file_data_I['WARDDIAG'] == row['warddiag']) &
                    (file_data_I['DIAGTYPE'] == row['diagtype']) &
                    (file_data_I['DIAGCODE'] == row['diagcode'])
                    ]

                if not matching_rows.empty:
                    file_data_I.loc[matching_rows.index, 'DIAGCODE'] = row['black']
                    file_search_I.at[index, 'status'] = "done"
                else:
                    file_search_I.at[index, 'status'] = "not done"

            else:
                # เงื่อนไขเพิ่มเติมเมื่อ row['black'] เป็นค่าว่าง
                if row['diagcode'] in ['I480', 'I481', 'I482', 'I489', 'I483', 'I484']:
                    file_data_I.loc[file_data_I['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'I48'
                    file_search_I.at[index, 'black'] = "I48"
                    file_search_I.at[index, 'status'] = "Done_I48&J96x"
                elif row['diagcode'] in ['J9600', 'J9601', 'J9609']:
                    file_data_I.loc[file_data_I['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'J960'
                    file_search_I.at[index, 'black'] = "J960"
                    file_search_I.at[index, 'status'] = "Done_I48&J96x"
                elif row['diagcode'] in ['J9610', 'J9611', 'J9619']:
                    file_data_I.loc[file_data_I['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'J961'
                    file_search_I.at[index, 'black'] = "J961"
                    file_search_I.at[index, 'status'] = "Done_I48&J96x"
                elif row['diagcode'] in ['J9690', 'J9691', 'J9699']:
                    file_data_I.loc[file_data_I['DIAGCODE'] == row['diagcode'], 'DIAGCODE'] = 'J969'
                    file_search_I.at[index, 'black'] = "J969"
                    file_search_I.at[index, 'status'] = "Done_I48&J96x"

        # บันทึกไฟล์ข้อมูลที่ถูกแก้ไขเป็น .txt โดยคั่นด้วยเครื่องหมาย | และแปลงเป็น UTF-8
        file_data_I.to_csv('data_F43/updated_diagnosis_ipd.TXT', sep='|', index=False, encoding='utf-8')

        # บันทึกไฟล์ค้นหาที่มีการอัปเดตสถานะเป็นไฟล์ Excel
        file_search_I.to_excel('data_F43/updated_DIAGNOSIS_IPD.xlsx', index=False)
        print("Update IPD done")
    elif input_k == "999":
        print("End Program")
        break



    #
    # # โหลดข้อมูลจากไฟล์ โดยกำหนด dtype เป็น str เพื่อให้ทุกคอลัมน์เป็นชนิดข้อความตั้งแต่ตอนอ่านไฟล์เข้ามา
    # file_data = pd.read_csv('data_F43/data_file.txt', sep='|', dtype=str, encoding='utf-8')
    # file_search = pd.read_excel('data_F43/search_file.xlsx', dtype=str)
    #
    # # สร้างคอลัมน์ F_status ในไฟล์ค้นหา เพื่อบันทึกสถานะ (ชนิดข้อความ)
    # file_search['F_status'] = ""
    #
    # # วนลูปตามเงื่อนไขของข้อมูลในไฟล์ค้นหา
    # for index, row in file_search.iterrows():
    #     # เงื่อนไขแรก: ตรวจสอบ F_del เพื่อทำการลบแถว
    #     if pd.notna(row['F_del']) and row['F_del'] == "del":
    #         matching_rows = file_data[
    #             (file_data['SEQ'] == row['F_seq']) &
    #             (file_data['DATE_SERV'] == row['F_date_serv']) &
    #             (file_data['DIAGTYPE'] == row['F_diagtype']) &
    #             (file_data['DIAGCODE'] == row['F_diagcode'])
    #             ]
    #
    #         if not matching_rows.empty:
    #             file_data.drop(matching_rows.index, inplace=True)
    #             file_search.at[index, 'F_status'] = "done"
    #         else:
    #             file_search.at[index, 'F_status'] = "not done"
    #
    #     # เงื่อนไขที่สอง: ตรวจสอบ F_blue2 เพื่อทำการแก้ไขและเพิ่มแถวใหม่
    #     elif pd.notna(row['F_blue2']):
    #         matching_rows = file_data[
    #             (file_data['SEQ'] == row['F_seq']) &
    #             (file_data['DATE_SERV'] == row['F_date_serv']) &
    #             (file_data['DIAGTYPE'] == row['F_diagtype']) &
    #             (file_data['DIAGCODE'] == row['F_diagcode'])
    #             ]
    #
    #         if not matching_rows.empty:
    #             # แก้ไข DIAGCODE เป็น F_blue1
    #             file_data.loc[matching_rows.index, 'DIAGCODE'] = row['F_blue1']
    #
    #             # สร้างแถวใหม่โดย copy ข้อมูลจากแถวที่ตรงกันแล้วเปลี่ยน DIAGCODE เป็น F_blue2 และ DIAGTYPE เป็น 2
    #             new_row = matching_rows.copy()
    #             new_row['DIAGCODE'] = row['F_blue2']
    #             new_row['DIAGTYPE'] = "2"
    #             file_data = pd.concat([file_data, new_row], ignore_index=True)
    #
    #             # อัปเดตสถานะใน F_status เป็น "done"
    #             file_search.at[index, 'F_status'] = "done"
    #         else:
    #             # ถ้าไม่พบแถวที่ตรงกัน อัปเดต F_status เป็น "not done"
    #             file_search.at[index, 'F_status'] = "not done"
    #
    #     # เงื่อนไขที่สาม: ถ้า F_blue2 เป็นค่าว่างและ F_blue1 ไม่เป็นค่าว่าง
    #     elif pd.isna(row['F_blue2']) and pd.notna(row['F_blue1']):
    #         # ค้นหาแถวที่ตรงกันในไฟล์ข้อมูล
    #         matching_rows = file_data[
    #             (file_data['SEQ'] == row['F_seq']) &
    #             (file_data['DATE_SERV'] == row['F_date_serv']) &
    #             (file_data['DIAGTYPE'] == row['F_diagtype']) &
    #             (file_data['DIAGCODE'] == row['F_diagcode'])
    #             ]
    #
    #         if not matching_rows.empty:
    #             # แก้ไข DIAGCODE เป็น F_blue1
    #             file_data.loc[matching_rows.index, 'DIAGCODE'] = row['F_blue1']
    #
    #             # อัปเดตสถานะใน F_status เป็น "done"
    #             file_search.at[index, 'F_status'] = "done"
    #         else:
    #             # ถ้าไม่พบแถวที่ตรงกัน อัปเดต F_status เป็น "not done"
    #             file_search.at[index, 'F_status'] = "not done"
    #
    # # บันทึกไฟล์ข้อมูลที่ถูกแก้ไขเป็น .txt โดยคั่นด้วยเครื่องหมาย | และแปลงเป็น UTF-8
    # file_data.to_csv('data_F43/updated_data_file_Blue.txt', sep='|', index=False, encoding='utf-8')
    #
    # # บันทึกไฟล์ค้นหาที่มีการอัปเดตสถานะเป็นไฟล์ Excel
    # file_search.to_excel('data_F43/updated_search_file_Blue.xlsx', index=False)
