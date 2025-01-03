# 펫시터 매칭 서비스

## 1. 주제 선정 배경
"해피투개더"는 1인 가구의 반려견을 고령의 펫시터에게 맡기는 맞춤형 매칭 서비스이다. 고령 인구가 900만 명을 돌파하고 초저임금 근로자 중 60세 이상 비율이 45.5%에 달하는 현실을 반영하여 기획되었다. 글로벌 펫케어 시장은 연평균 8.4%의 성장률을 기록하고 있으며, 1인 가구의 반려견 양육 또한 꾸준히 증가하고 있는 추세이다. 추천 알고리즘은 콘텐츠 기반 필터링(Content-Based Filtering) 방식을 기반으로 하여 사용자의 선호도와 펫시터의 특성을 매칭하고, 유사도 점수가 가장 높은 상위 10명의 펫시터를 추천한다.

## 2. Django 시작하기
- - -
### Python Version
- Python 3.12.1  [Python 공식 웹사이트](https://www.python.org/downloads/)

### 가상 환경 생성
```
python -m venv venv
```

### 가상 환경 생성(Git Bash)
```
source venv/Scripts/activate
```
_커맨드라인 앞에 (venv)라는 텍스트가 표시되면 가상 환경 활성화 상태_

### 필요한 라이브러리 설치
```
pip install django
pip install numpy
pip install Pillow
```

### Django 설치 확인
```
python -m django --version
```

### Django 서버 실행
```
python manage.py runserver
```
_서버가 실행되면 http://127.0.0.1:8000/ 또는 http://localhost:8000/ 로 접속 가능_

### 가상 환경 비활성화
```
deactivate
```

### 가상 환경 삭제
```
rm -rf venv
```

## 3. 상세 보기
[![Naver Blog Badge](https://img.shields.io/badge/Naver%20Blog-03C75A?style=flat&logo=Naver&logoColor=white)](https://blog.naver.com/genie290/223214425548)
