row1 = []
row1.append("Sarayut")
row1.append(" - ")
row1.append(" - ")
row1.append(" - ")
#print(row1)  # Output: ['Sarayut', ' - ', ' - ', ' - ']

row2 = []
row2.append("Tanyarat")
row2.append("Chatkarwee")
row2.append("Kitibodee")
row2.append("Siwakorn")
#print(row2)  # Output: ['Tanyarat', 'Chatkarwee', 'Kitibodee', 'Siwakorn']

row3 = []
row3.append("Nattapong")
row3.append("Piyapong")
row3.append("Rattppom")
row3.append("Pichaya") 

table = []
table.append(row1)
table.append(row2)
table.append(row3)

def print_table(table):
    # 1. หาจำนวนคอลัมน์
    num_cols = len(table[0])
    
    # 2. หาความกว้างสูงสุดของข้อมูลในแต่ละคอลัมน์
    col_widths = [max(len(str(row[i])) for row in table) for i in range(num_cols)]
    
    # 3. คำนวณความยาวของเส้นขอบ (ความกว้างตัวอักษรทั้งหมด + ความกว้างของ ' | ' ในแต่ละคอลัมน์)
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

print("Table:")
print_table(table)