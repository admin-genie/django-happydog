# Django 웹 개발 #
- - -
### Python Version
- Python 3.12.1 [Python 공식 웹사이트](https://www.python.org/downloads/)
#### Project Folder
```
cd myproject
```

#### 가상 환경 생성
```
python -m venv venv
```

#### 가상 환경 생성(Git Bash)
```
source venv/Scripts/activate
```
_커맨드라인 앞에 (venv)라는 텍스트가 표시되면 가상 환경 활성화 상태_

#### 필요한 라이브러리 설치
```
pip install django
pip install numpy
pip install Pillow
```

#### Django 설치 확인
```
python -m django --version
```

#### Django 서버 실행
```
python manage.py runserver
```
_서버가 실행되면 http://127.0.0.1:8000/ 또는 http://localhost:8000/로 접속 가능_

#### 가상 환경 비활성화(작업 이후)
```
deactivate
```

#### 가상 환경 삭제
```
rm -rf venv
```
