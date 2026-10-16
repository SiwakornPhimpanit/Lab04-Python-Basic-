import streamlit as st
import pandas as pd

# 1. เตรียมข้อมูล
scores = [[55, 63, 77, 81], 
          [65, 61, 67, 72], 
          [97, 95, 92, 88]]
names = ["Sarayut", "Nattapong", "Pongsakorn"]
subjects = ["Math", "Science", "English", "History"]

# 2. นำข้อมูลใส่ Pandas DataFrame เพื่อการจัดการที่ง่ายขึ้น
df = pd.DataFrame(scores, columns=subjects, index=names)

# 3. ตั้งค่าหน้าเว็บ Streamlit
st.set_page_config(page_title="Student Scores", layout="centered")

# 4. แสดงผลบนเว็บ
st.title("📊 ตารางคะแนนนักเรียน")
st.write("แสดงผลตารางแบบ Interactive (คลิกที่หัวคอลัมน์เพื่อเรียงลำดับได้)")

# ใช้ st.dataframe สำหรับตารางที่เลื่อนและเรียงข้อมูลได้ หรือ st.table สำหรับตารางแบบคงที่
st.dataframe(df, width='stretch')