import sqlalchemy # SQL 데이터베이스에 연동
import pandas as pd # 데이터 프레임을 사용하기 위한 라이브러리
import keyboard # 키 입력을 하기 위한 라이브러리
import time # time.sleep을 사용하기 위한 라이브러리

# conn_string="dbname='join_db' host='localhost' user='postgres' password='didtpals1010'" # postgresql 연동을 위한 정보를 작성해준다 (데이터베이스명, 호스트, 사용자명, 패스워드)
# conn = db.connect(conn_string) # conn_string으로 작성헤준 정보를 사용해 연결을 위한 변수


# create_engine 함수를 사용하여 DB를 호출한다. ("postgresql://username:password@host:port/dbname")
conn = sqlalchemy.create_engine("postgresql://postgres:didtpals1010@localhost:5432/join_db")

def Create_Table():
    try:
        name = input("CREATE_TABLE NAME : ")
        column = input("COLUMN : ")
        query = f"create table {name} ({column})"
        conn.execute(query)
        print("CREATE TABLE")
    except Exception as e:
        print(e)
def Select():
    try:
        chat = input("SELECT RANGE : ")
        table = input("SELECT_TABLE NAME : ")
        query = f"select {chat} from {table}" # 연결된 DB에 있는 테이블을 호출 해주는 query를 문자열로 변수에 저장
        db = pd.read_sql(query, conn) # 연결된 DB에서 쿼리에 맞는 결과값을 DB 변수에 저장        
        print(db) # 호출된 결과값 출력
    except :
        print("error")

def Update():
    try:
        table = input("UPDATE_TABLE NAME : ")
        column = input("WHAT COLUMN : ")
        value = input("UPDATE VALUE : ")
        id = input("WHERE ID : ")
        query = f"update {table} set {column} = {value} where id = {id}" # 연결된 DB 테이블에 있는 UPDATE를 문자열로 변수에 저장
        conn.execute(query) # 연결된 테이브렝 있는 UPDATE 수행
        print("UPDATE") # 호출된 결과값 출력
    except Exception as e :
        print(e)

def Insert():
    try:
        table = input("TABLE NAME : ")
        query = f"select * from {table}" # 연결된 DB에 있는 테이블을 호출 해주는 query를 문자열로 변수에 저장
        db = pd.read_sql(query, conn) # 연결된 DB에서 쿼리에 맞는 결과값을 DB 변수에 저장  
        table_length = len(db) + 1

        table = input("INSERT_TABLE NAME : ")
        chat = input("VALUES (VALUE1, VALUE2 ...) : ")
        query = f"insert into {table} values ({table_length},{chat})" # 연결된 DB 테이블에 있는 UPDATE를 문자열로 변수에 저장
        conn.execute(query) # 연결된 테이브렝 있는 UPDATE 수행
        print("INSERT") # 호출된 결과값 출력
    except Exception as e :
        print(e)

def Delete():
    try:
        table = input("DELETE_TABLE NAME : ")
        chat = input("WHERE ID : ")
        query = f"delete from {table} where id = {chat}"
        conn.execute(query)
        print("DELETE")
    except Exception as e:
        print(e)

def All_Delete():
    try:
        table = input("ALL DELETE_TABLE NAME : ")
        query = f"delete from {table}"
        conn.execute(query)
        print("ALL DELETE")
    except Exception as e:
        print(e)

def Add_Column():
    try:
        table = input("ADD COLUMN_TABLE NAME : ")
        chat = input("ADD COLUMN : ")
        query = f"alter table {table} add {chat} varchar"
        conn.execute(query)
        print("ADD COLUMN")
    except Exception as e:
        print(e)

def Drop_Column():
    try:
        table = input("DROP_COLUMN_TABLE NAME : ")
        chat = input("DROP COLUMN : ")
        query = f"alter table {table} drop column {chat}"
        conn.execute(query)
        print("DROP COLUMN")
    except Exception as e:
        print(e)

while True: 
    key = keyboard.read_key() # 누른 키를 읽고 지정키를 누르면 커스텀 함수에 있는 결과값 출력, read_key()는 문자를 반환함.
    time.sleep(0.3)
    if  key == "s":
        Select()

    if key == "u":
        Update()

    if key == "i":
        Insert()
    
    if key == "d":
        Delete()

    if key == "D":
        All_Delete()

    if key == "a":
        Add_Column()

    if key == "c":
        Drop_Column()

    if key == "C":
        Create_Table()

    if key == "e":
        break