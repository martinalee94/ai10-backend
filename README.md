# [π§](https://emojipedia.org/yoga/) WellAI(μ°λΌμ΄)
  *μΈμ  μ΄λμλ λΉμ μ κ±΄κ°μ μ±μμ§λ AI ννΈ μλΉμ€, μ°λΌμ΄*


## 1. νλ‘μ νΈ μκ° β
### [Wellai](https://github.com/martinalee94/wellai) (λ©μΈ λ ν¬μ§ν λ¦¬ λ§ν¬)<br>
β μ°λΌμ΄ λ©μΈ λ ν¬μ§ν λ¦¬μ μμΈν λ΄μ©μ΄ μ²¨λΆ λμ΄ μμΌλ νμΈν΄ μ£ΌμΈμ!

<br>

- **κ΄λ ¨ λ¬Έμ**
  - [μμ΄μ΄νλ μ](https://www.figma.com/file/0FC6VjrVkBBflLS2iMMo8U/νμ λ³Έ)
  - [μκ΅¬ λͺμΈμ](https://unruly-space-e0e.notion.site/a1fd4e5741974262860677ff806af234)


## 2. μ¬μ©ν κΈ°μ  β
| ννΈ | κΈ°μ  |
| ------ | ------ |
| λ°±μλ  | <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"></a> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=PostgreSQL&logoColor=white"/></a> <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/></a> <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=Nginx&logoColor=white"/></a> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/></a> |

<br>


## 3. μ€ν λ°©λ² β
#### .env.prod & .env.prod.db 
- 'example_' λ‘ μμνλ λΆλΆλ€ κ° μ€ν νκ²½μ λ§κ² λ°κΏμ νμΌ μμ±

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

#### docker μ€ν
```
docker-compose up
```


## 4. νλ‘μ νΈ νμ μκ° β
| μ΄λ¦ | ν¬μ§μ | λ΄λΉ μλ¬΄ |
| ------ | ------ | ------ |
| **μ΄μμ** | νμ₯ / λ°±μλ / λμμΈ | 1. μ μ  DB μ€κ³ λ° API κ°λ°<br> 2. Docker λ° NGINX λ°°ν¬ κ΄λ¦¬<br> 3. git submodule λ ν¬μ§ν λ¦¬ κ΄λ¦¬<br> 4. μ μ²΄ μλΉμ€ νμ΄μ§ λμμΈ <br>  |
| **μ΅μν** | λ°±μλ | 1. μ½μ€ DB μ€κ³ λ° API κ°λ° <br> 2. Docker λ° Gunicorn λ°°ν¬ κ΄λ¦¬<br> 3. DB λ°μ΄ν° μ½μ λ° μμ±|
| **κΉνμμ¬** | μΈκ³΅μ§λ₯ | 1. μΈκ³΅μ§λ₯ μλΉμ€ μ΄κΈ° κΈ°ν,μ‘°μ¬<br> 2.λ°μ΄ν° μμ§, μ μ²λ¦¬, λͺ¨λΈλ‘ μ μ²λ¦¬, λͺ¨λΈλ§, λͺ¨λΈ νκ° λ° μ ν<br> 3. ν΄λΌμ΄μΈνΈ μ¬μ΄λ λͺ¨λΈλ‘ λ³ν λ° κ²½λν<br> 4. λ©μΈ μλΉμ€ νμ€νΈ λ° λ©μΈ μλΉμ€ νμ€νΈ μ½λ μμ±|
| **κ°κ²½μ±** | νλ‘ νΈμλ | 1. λ§μ΄νμ΄μ§ κ΅¬ν <br> 2. μ€μκ° μμ μ²λ¦¬ μλΉμ€ κ΅¬ν <br> 3. ν ν° νλ‘μ°(access/refresh) κ΅¬ν |
| **νμ€ν** | νλ‘ νΈμλ | 1.νμκ°μ νμ΄μ§ / μ½μ€ νμ΄μ§ κ΅¬ν<br> 2. νμκ°μ / μ½μ€ / λ§μ΄νμ΄μ§ API μ°λ |


<br>

## 5. μμ€ν μν€νμ³ β
![image](https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team10/wellai/uploads/2d30cd91d59ff6dffa39c34a146e69e3/archi.001.png)


## 6. Database κ΅¬μ‘° β
![image](https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team10/backend/uploads/89991d2660dc6a4c3f2139df470570a3/image.png)
