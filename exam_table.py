def print_table(table):
    num_cols = len(table[0])
    col_widths = [max(len(str(row[i])) for row in table) for i in range(num_cols)]
    
    line_length = sum(col_widths) + (num_cols * 3)
    
    print("=" * line_length)
    for row in table:
        for i, item in enumerate(row):
            # ใช้ f-string กำหนดความกว้าง (< คือจัดชิดซ้าย)
            print(f"{str(item):<{col_widths[i]}}", end=' | ')
        print()  # ขึ้นบรรทัดใหม่เมื่อจบแถว
        print("-" * line_length)
    # เปลี่ยนเส้นสุดท้ายให้เป็นเครื่องหมาย = เพื่อปิดกรอบให้สวยงาม (ถ้าต้องการ)
    print("=" * line_length)


scores = [[55, 63, 77, 81], 
          [65, 61, 67, 72], 
          [97, 95, 92, 88]]

names = ["Sarayut", "Nattapong", "Pongsakorn"]
subjects = ["Math", "Science", "English", "History"]

table_show = scores.copy()
subject_show = subjects.copy()
subject_show.insert(0, "Name")  # เพิ่มหัวตาราง
table_show.insert(0, subject_show)  # เพิ่มแถวหัวตาราง
for i in range(len(names)):
    table_show[i + 1].insert(0, names[i])  # เพิ่มชื่อผู้เรียนในแต่ละแถว

print(table_show)

print("Scores:")
print_table(table_show)


