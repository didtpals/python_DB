import keyboard # 키 입력을 하기 위한 라이브러리

import ConnectDB
import DBaction

p = print

conn = ConnectDB.Connect_DB()
DBaction.PrintNotice()


while True: 
    key = keyboard.read_key() # 누른 키를 읽고 지정키를 누르면 커스텀 함수에 있는 결과값 출력, read_key()는 문자를 반환함.

    if  key == "s": # Select 함수 실행
        DBaction.Select(conn)

    if key == "i": # Insert 함수 실행
        DBaction.Insert(conn)
    
    if key == "u": # Update 함수 실행
        DBaction.Update(conn)

    if key == "d": # Delete 함수 실행
        DBaction.Delete(conn)

    if key == "D": # All_Delete 함수 실행
        DBaction.All_Delete(conn)

    if key == "a": # Add_Column 함수 실행
        DBaction.Add_Column(conn)

    if key == "c": # Drop_Column 함수 실행
        DBaction.Drop_Column(conn)

    if key == "C": # Create_Table 함수 실행
        DBaction.Create_Table(conn)

    if key == "e":
        break

    else:
        if key == "shift" or key == "enter":
            continue
        p("존재하지 않는 KEY 입니다.") # 지정 키 이외의 키를 누르면 출력
        continue