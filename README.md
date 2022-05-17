# [🧘](https://emojipedia.org/yoga/) WellAI(웰라이)
  *언제 어디서나 당신의 건강을 책임지는 AI 홈트 서비스, 웰라이*


## 1. 프로젝트 소개 ✅
### [Wellai](https://github.com/martinalee94/wellai) (메인 레포지토리 링크)<br>
↑ 웰라이 메인 레포지토리에 자세한 내용이 첨부 되어 있으니 확인해 주세요!

<br>

- **관련 문서**
  - [와이어프레임](https://www.figma.com/file/0FC6VjrVkBBflLS2iMMo8U/확정본)
  - [요구 명세서](https://unruly-space-e0e.notion.site/a1fd4e5741974262860677ff806af234)


## 2. 사용한 기술 ✅
| 파트 | 기술 |
| ------ | ------ |
| 백엔드  | <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"></a> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=PostgreSQL&logoColor=white"/></a> <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/></a> <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=Nginx&logoColor=white"/></a> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/></a> |

<br>


## 3. 실행 방법 ✅
#### .env.prod & .env.prod.db 
- 'example_' 로 시작하는 부분들 각 실행 환경에 맞게 바꿔서 파일 생성

```
# .env.prod
SECRET_KEY = example_secretkey
DJANGO_SETTINGS_MODULE = config.settings.local
DJANGO_ALLOWED_HOSTS = 127.0.0.1 localhost
POSTGRESQL_DATABASE = example_database
POSTGRESQL_USER = example_user
POSTGRESQL_PASSWORD = example_password
POSTGRESQL_HOST = db
POSTGRESQL_PORT = 5432
TEST_DATABASE = example_testdatabase


# .env.prod.db 
POSTGRES_DB = example_database
POSTGRES_USER = example_user 
POSTGRES_PASSWORD = example_password
```

#### docker 실행
```
docker-compose up
```


## 4. 프로젝트 팀원 소개 ✅
| 이름 | 포지션 | 담당 업무 |
| ------ | ------ | ------ |
| **이영숙** | 팀장 / 백엔드 / 디자인 | 1. 유저 DB 설계 및 API 개발<br> 2. Docker 및 NGINX 배포 관리<br> 3. git submodule 레포지토리 관리<br> 4. 전체 서비스 페이지 디자인 <br>  |
| **최영훈** | 백엔드 | 1. 코스 DB 설계 및 API 개발 <br> 2. Docker 및 Gunicorn 배포 관리<br> 3. DB 데이터 삽입 및 생성|
| **김한예슬** | 인공지능 | 1. 인공지능 서비스 초기 기획,조사<br> 2.데이터 수집, 전처리, 모델로 전처리, 모델링, 모델 평가 및 선택<br> 3. 클라이언트 사이드 모델로 변환 및 경량화<br> 4. 메인 서비스 테스트 및 메인 서비스 테스트 코드 작성|
| **강경욱** | 프론트엔드 | 1. 마이페이지 구현 <br> 2. 실시간 영상 처리 서비스 구현 <br> 3. 토큰 플로우(access/refresh) 구현 |
| **홍준형** | 프론트엔드 | 1.회원가입 페이지 / 코스 페이지 구현<br> 2. 회원가입 / 코스 / 마이페이지 API 연동 |


<br>

## 5. 시스템 아키텍쳐 ✅
![image](https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team10/wellai/uploads/2d30cd91d59ff6dffa39c34a146e69e3/archi.001.png)


## 6. Database 구조 ✅
![image](https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team10/backend/uploads/89991d2660dc6a4c3f2139df470570a3/image.png)
