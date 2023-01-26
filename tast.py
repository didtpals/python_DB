import sqlalchemy # SQL 데이터베이스에 연동
import pandas as pd # 데이터 프레임을 사용하기 위한 라이브러리
import keyboard # 키 입력을 하기 위한 라이브러리
import time # time.sleep을 사용하기 위한 라이브러리

conn = sqlalchemy.create_engine("postgresql://postgres:didtpals1010@localhost:5432/join_db")

def Alter_Table():
    try:
        query = "alter table admin add name varchar"
        conn.execute(query)
        print("ALTER_TABLE")
    except Exception as e:
        print(e)

def didtpals():
    chat = input("추가할 컬럼 이름 : ")


while True: 
    key = keyboard.read_key() # 누른 키를 읽고 지정키를 누르면 커스텀 함수에 있는 결과값 출력, read_key()는 문자를 반환함.
    time.sleep(0.5)
    if key == "a":
        Alter_Table()