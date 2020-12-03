# Petition-Server

### 모듈 설치
pip install -r requirements.txt

### 서버 실행
1. 파일을 클론이나 다운 후 파일에다가 넣어놓는다.
2. 해당 경로로 찾아가 src/config.ini를 만들어준다.
    - MySQL DB_URL을 넣어주면 된다.
    ```ini
        [default]
        DB_URL = "your MYSQL DB URL"
        PORT = "you will write youn want port number"
    ```
3. 실행을 해준다.
    - python src/run_server.py -R(Reload option) -P (Port number)
        - 이때 -R이나 -P는 옵션이니 안넣어줘도 된다.


    
