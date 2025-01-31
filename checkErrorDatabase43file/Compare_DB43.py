import os
import difflib

# กำหนดโฟลเดอร์ที่เก็บไฟล์จากทั้งสองฐาน
db1_path = "db1/"
db2_path = "db2/"

# ดึงรายชื่อไฟล์จากทั้งสองฐานข้อมูล
db1_files = set(os.listdir(db1_path))
db2_files = set(os.listdir(db2_path))

# ตรวจสอบไฟล์ที่มีชื่อเหมือนกันในทั้งสองฐาน
common_files = db1_files.intersection(db2_files)

# ถ้าไม่มีไฟล์ที่ชื่อเหมือนกัน ให้แจ้งเตือน
if not common_files:
    print("ไม่พบไฟล์ที่ชื่อเหมือนกันในทั้งสองฐานข้อมูล")
    exit()

# วนลูปเปรียบเทียบแต่ละไฟล์ที่ชื่อเหมือนกัน
for filename in common_files:
    file1 = os.path.join(db1_path, filename)
    file2 = os.path.join(db2_path, filename)

    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # เปรียบเทียบจำนวนบรรทัด
    diff_line_count = abs(len(lines1) - len(lines2))
    print(f"\n🔍 เปรียบเทียบไฟล์: {filename}")
    print(f"📌 จำนวนบรรทัดต่างกัน: {diff_line_count}")

    # ค้นหาบรรทัดที่ต่างกัน
    diff_lines = list(difflib.ndiff(lines1, lines2))
    diff_results = [line for line in diff_lines if line.startswith("- ") or line.startswith("+ ")]

    # แสดงบรรทัดที่แตกต่างกัน
    if diff_results:
        print("⚠️ พบแถวที่แตกต่างกัน:")
        for line in diff_results:
            print(line.strip())
    else:
        print("✅ ไฟล์นี้เหมือนกัน 100%")
