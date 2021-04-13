# Petition-Server

`GSM-Space`는 `광주소프트웨어마이스터고등학교 3기 학생회`의 공약으로 선생님과 학생간의 소통을 원활히 하기 위하여 제작하였습니다.

## 기술스택
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

## 실행방법

1. `Repository`를 `clone` 합니다.
```sh
git clone https://github.com/GSM-Space/Petition-Server.git
```

2. `requirement.txt`를 이용하여 필요한 `package`를 다운받습니다.
```sh
pip install -r requirements.txt
```

3. [환경변수를 입력해줍니다.](#환경-변수)

4. 다음 명령어를 통해 프로그램을 실행시킵니다.
```sh
python src/run_server.py -R -P 5225
# -R은 저장시 자동 실행 옵션이며, -P는 프로그램을 동작시킬 포트 번호이다. 공백시에 환경변수에 입력된 값으로 실행됩니다.
```

5. 다음으로 요청을 보내, 서버가 잘 작동하는지 확인을 한다.

> POST /api/test

## 환경 변수

### /config.ini
```ini
[default]
DB_URL = "mysql://{account name}:{account password}@localhost:{using port number}/{DB name}?charset=utf8"
PORT = "you will write youn want port number"
```
