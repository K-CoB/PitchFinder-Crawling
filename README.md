# Pitch Finder 
부를 노래 추천을 위한 음역대 측정 기반 노래 필터링 서비스

> ‘들을’ 노래가 아닌 ‘부를’ 노래를 찾기 위해 <br/>
> 개인 음역대를 측정하고 측정된 음역대를 기반으로 <br/>
> 노래를 필터링하는 서비스, 피치파인더

<br/>

## 🧑‍🤝‍🧑 Team
|<img src="https://avatars.githubusercontent.com/u/79985974?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/75469131?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/89910703?v=4" width="150" height="150"/>|
|:-:|:-:|:-:|
|[@chaeri93](https://github.com/chaeri93)|[@seondal](https://github.com/seondal)|[@CSE-pebble](https://github.com/CSE-pebble)|
|데이터 수집 & 백엔드 개발|프론트엔드 개발|팀장 & 프론트엔드 개발|

<br/>


##  🛠️ How to install
- 본 레포 clone `git clone https://github.com/K-CoB/music-data-crawling`
- 클론한 프로젝트 폴더를 연다
- env.example을 참고하여 .env 파일을 만든다
  ```bash
  MYSQL_HOST=
  MYSQL_USERNAME=
  MYSQL_PASSWORD=
  MYSQL_DB=
  YOUTUBE_API_KEY=

  ```
- 프로젝트 내에 있는 Dockerfile로 도커를 빌드하여 프로그램을 실행한다.
  ```
  docker build .
  docker run
  ```

  
<br/>

## 📚 Stack
| **Section**       | Tech        |
| ---------------- | ---------------------------- |
| **인프라**       | AWS Lambda, API Gateway, CloudWatch      |
| **언어**         | Python                       |
| **데이터베이스** | MySQL, AWS RDS               |
| **데이터** | BeautifulSoup, Youtube API        |

<br/>

## 🔐 System Architecture
<img width="816" alt="image" src="https://github.com/K-CoB/pitch-finder-lambda/assets/79985974/c119c65a-5870-445e-8410-5032825995df">

<br/>

## 🗂️ Folder Structure
```python
music-data-crawling
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── lib
│   ├── database
│   │   ├── __init__.py # 음악 데이터와 데이터베이스 연결
│   │   └── mysql
│   │       └── mysql.py # 데이터베이스 연결 및 CRUD 함수
│   ├── formulate.py # 음계를 MidiNote로 변환
│   ├── music.py # 나무위키에서 음악 크롤링
│   ├── settings.py # 데이터베이스 연결 설정
│   └── youtube.py # 유튜브 api 사용하여 url 크롤링
├── main.py # 크롤링 실행 함수
├── requirementx.txt # 프로젝트 실행하는데 필요한 라이브러리
├── table.sql # 데이터베이스 테이블 생성
└── utils
    ├── constant
    │   └── __init__.py # 음악 클래스 
    ├── utils.py # 로깅 설정
    └── validate.py # 데이터 전처리
```
