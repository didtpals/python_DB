import sqlalchemy # SQL 데이터베이스에 연동
import pandas as pd # 데이터 프레임을 사용하기 위한 라이브러리
import keyboard # 키 입력을 하기 위한 라이브러리
import time # time.sleep을 사용하기 위한 라이브러리

# conn_string="dbname='join_db' host='localhost' user='postgres' password='didtpals1010'" # postgresql 연동을 위한 정보를 작성해준다 (데이터베이스명, 호스트, 사용자명, 패스워드)
# conn = db.connect(conn_string) # conn_string으로 작성헤준 정보를 사용해 연결을 위한 변수


# create_engine 함수를 사용하여 DB를 호출한다. ("postgresql://username:password@host:port/dbname")
print("--------------------")
db_name = input("DB_NAME : ") # DB_NAME 입력 
print("--------------------")
# create_engine 함수를 사용하여 DB를 호출한다. ("postgresql://username:password@host:port/dbname")
conn = sqlalchemy.create_engine(f"postgresql://postgres:didtpals1010@localhost:5432/{db_name}")

print("DB access")

def Create_Table():
    try: # Try 문을 사용하여 예외처리
        name = input("CREATE_TABLE NAME : ") # input 함수를 사용하여 생성할 TABLE NAME 입력
        column = input("COLUMN : ") # input 함수를 사용하여 생성할 테이블의 COLUM 입력
        query = f"create table {name} ({column})" # 연결된 DB에 있는 테이블을 생성 해주는 query를 문자열로 변수에 저장 
        conn.execute(query) # conn.execute( )함수를 사용해서 쿼리를 전송하고 실행.
        print("--------------------")
        print("CREATE TABLE") # TABLE이 성공적으로 생성 되면 CREATE TABLE 출력
        print("--------------------")
    except Exception as e: # 예외 문구를 설정
        print(e) # 예외 문구를 띄움
def Select():
    try:
        chat = input("SELECT RANGE : ") # SELECT RANGE 입력
        table = input("SELECT_TABLE NAME : ") # SELECT_TABLE NAME 입력
        query = f"select {chat} from {table}" # 연결된 DB에 있는 테이블을 호출 해주는 query를 문자열로 변수에 저장
        db = pd.read_sql(query, conn) # 연결된 DB에서 쿼리에 맞는 결과값을 DB 변수에 저장        
        print("--------------------------------------------------------------")
        print(db) # 호출된 결과값 출력
        print("--------------------------------------------------------------")
    except :
        print("--------------------")
        print("error")
        print("--------------------")

def Update():
    try:
        table = input("UPDATE_TABLE NAME : ") # UPDATE_TABLE NAME 입력
        column = input("WHAT COLUMN : ") # WHAT COLUMN 입력
        value = input("UPDATE VALUE : ") # UPDATE VALUE 입력
        id = input("WHERE ID : ") # WHERE ID 입력
        query = f"update {table} set {column} = {value} where id = {id}"
        conn.execute(query) 
        print("--------------------")
        print("UPDATE") # 호출된 결과값 출력
        print("--------------------")
    except Exception as e :
        print(e)

def Insert():
    try:
        table = input("TABLE NAME : ")
        query = f"select * from {table}"
        db = pd.read_sql(query, conn)  
        table_length = len(db) + 1 # 행의 길이에 +1

        table = input("INSERT_TABLE NAME : ")
        chat = input("VALUES (VALUE1, VALUE2 ...) : ")
        query = f"insert into {table} values ({table_length},{chat})"
        conn.execute(query)
        print("--------------------")
        print("INSERT") # 호출된 결과값 출력
        print("--------------------")
    except Exception as e :
        print(e)

def Delete():
    try:
        table = input("DELETE_TABLE NAME : ")
        chat = input("WHERE ID : ")
        query = f"delete from {table} where id = {chat}"
        conn.execute(query)
        print("--------------------")
        print("DELETE")
        print("--------------------")
    except Exception as e:
        print(e)

def All_Delete():
    try:
        table = input("ALL DELETE_TABLE NAME : ")
        query = f"delete from {table}"
        conn.execute(query)
        print("--------------------")
        print("ALL DELETE")
        print("--------------------")
    except Exception as e:
        print(e)

def Add_Column():
    try:
        table = input("ADD COLUMN_TABLE NAME : ")
        chat = input("ADD COLUMN : ")
        query = f"alter table {table} add {chat} varchar"
        conn.execute(query)
        print("--------------------")
        print("ADD COLUMN")
        print("--------------------")
    except Exception as e:
        print(e)

def Drop_Column():
    try:
        table = input("DROP_COLUMN_TABLE NAME : ")
        chat = input("DROP COLUMN : ")
        query = f"alter table {table} drop column {chat}"
        conn.execute(query)
        print("--------------------")
        print("DROP COLUMN")
        print("--------------------")
    except Exception as e:
        print(e)

while True: 
    key = keyboard.read_key() # 누른 키를 읽고 지정키를 누르면 커스텀 함수에 있는 결과값 출력, read_key()는 문자를 반환함.
    time.sleep(0.3)
    if  key == "s": # Select 함수 실행
        Select()

    if key == "u": # Update 함수 실행
        Update()

    if key == "i": # Insert 함수 실행
        Insert()
    
    if key == "d": # Delete 함수 실행
        Delete()

    if key == "D": # All_Delete 함수 실행
        All_Delete()

    if key == "a": # Add_Column 함수 실행
        Add_Column()

    if key == "c": # Drop_Column 함수 실행
        Drop_Column()

    if key == "C": # Create_Table 함수 실행
        Create_Table()

    if key == "e":
        break