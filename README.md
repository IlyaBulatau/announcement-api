# Стек
![](https://img.shields.io/badge/Python-3.10-blue?style=socila&logo=Python&labelColor=gray)
![](https://img.shields.io/badge/FastAPI-0.104.1-blue?style=socila&logo=Python&labelColor=gray)
![](https://img.shields.io/badge/SQLAlchemy-2.0.23-blue?style=socila&logo=Python&labelColor=gray)
![](https://img.shields.io/badge/Docker-24.0.2-blue?style=socila&logo=Python&labelColor=gray)
![](https://img.shields.io/badge/PostgreSQL-14.10-blue?style=socila&logo=Python&labelColor=gray)

<br>

# Схема базы данных

![Untitled (3)](https://lh3.googleusercontent.com/pw/ADCreHee98a-4pR3Mhoq3ohfqV6rCnggi63RgrPIBNnfPoasq6fMd2qx5soo6DXrlLnc_0ihg5MRNgJaD5fhmbV4Eizai-B9tAYv7ji8rJJs5nkms0zczhwR3BkL7205DKrWuFE9lRKixIXZMHY0OCFvkibRtzg_vpIPLR2RNgrWULPtWVXtidb2RdI58tl7TTFBUVr5VOAw51Dk-heod0UHSlm3dxg2klfOHNP9CXxyctz3YdAiKbvle3XjNs7bqjlFjZNo0C41ggpjIA9ZHKmmP1L9w0zhdBSLWfUre8KerolQZVOZFBi6OCLEnqq2vV8QQz0wyNQLmp3iXuD8RSjDISWl-KL_lVrNbpPZ5zRYsv_C_E5oGmsWjGiNHFHn2p1BcTy7r24_CwcWWN3EtDsSCvc0Wx0Y0iTfmJRgnxRIqA76YtDE6awi569WZg2TmkdBc4HLWZra0_gJ-dqaiY7qaxWPjQn-vjb3_QYJ1uiGq45h7xzoiAgX_0Gbl6_d-IIsKRE7f0RUJ9tgW3uA0REunLG2lVsd1C9JYMGGiAomBA-kMCOEYkauB2ElzUx7_yx5msRQz9U0WCEFanDmVzMdOpysasENFf-aUo5rBzG3rwA2xPAksYHGpIbQ-de7Kxyahv_hYX6I1ahQxLvs7hUX0ZEN3lJtEgi43Be13uK9-746DJgpuAWtALEktslrIWg9R5M8xodMAmGGVg0S49TF9UZq3j5U58TcPMLCJhPVAHOSMZWJE3F4E5I7J_uKA1YnbfvzXwc_J8kQ5SYf0pxADgtzXDWxsUROsjZWvtzHvzCc_7IO3lplAOSdJ2xPZ_2Ow4nv7HUXg8fadAKSEFVdUJW-CPKssjZsES4cGLU3nfWKkN_F_UkjyrZDI63luLGJ=w891-h640-s-no?authuser=0)

<br>

# Структура кода

**src** - папка с кодом, внутри содержит: 
- **apps**:
    папка с приложениями в каждом приложении есть файлы с ендпоинтами, менеджерами работы с БД, схемами и прочими файлами связанными с этим приложением
- **database**:
    содержит файл подключения к базе данных, обьект базового менеджера и папку с моделями
- **endpoints**:
    папка с общеми ендпоинтами не относящимися к какому либо приложению, содержит файл 1 ендпоинтом для проверки работоспособности сервера
- **exceptions**:
    содержит файл для кастомных ошибок, и файл с обработчиками ошибок для приложения
- **migrations**
    папка с миграциями 
- **settings.py**
    файл для считывания переменных окружения и настройки проекта
- **main.py**
    файл с приложением и подключеним роутеров 

<br>

# Запуск
1. Клонировать репозиторий
```
git clone https://github.com/IlyaBulatau/announcement-api.git
```
2. Установить зависимости 
```
poetry install
```
3. Активируйте виртуальное окружение
```
poetry shell
```
4. В папке `env` есть файл `.env.exaplme`, переименуйте его в `.env`, это файл с переменными окружения, для запуска проекта их можно не менять, а можно и вписать свои - по желанию
```
mv env/.env.example env/.env
```
5. Создайте и примените миграции к базе данных
```
make migrations
```
затем
```
make migrate
```
6. Запустите контенеры
```
docker compose --env-file ./env/.env up -d
``` 
или
```
make run
```
## После этих шагов сервер поднимется, документация будет доступена по адресу [localhost:8000/api/v1/docs ](localhost:8000/api/v1/docs)

<br>

# Ендпоинты
## Для проверки работоспособности конечных точек можно воспользоватся `Postman`, `curl` либо `swagger` по ссылки на документацию проекта.
## Все ендпоинты кроме `api/v1/auth/login` и `api/v1/auth/register` защищенны проверкой jwt токена, поэтому что бы проверить работу остальных конечных точек,
## нужно пройти регистрацию и получить `Bearer` токен, и затем этот токен вставлять в заголовок `Authorization`, кроме этого есть ендпоинты которые
## доступны только супер юзерам. После регистрации пользователи не становяться супер-юзером, что бы сделать юзера супер-юзером
## нужно зайти в базу данных и вручную поставить галочку в поле `is_superuser`, для этого есть контейнер `pgadmin`.

____

## **non-auth** - ендпоинт не трубющий аутендификации
## **auth** - требуется токен авторизации
## **admin** - требуется токен от супер-юзера
___

1.
- **/api/v1/healthcheck/**
- `GET`
- Проверка сервера
- `non-auth`
```
curl --location 'http://localhost:8000/api/v1/healthcheck'
```
Возвращает `200`, `{"Status":"OK"}` 

<br>

2. 
- **/api/v1/auth/register**
- `POST`
- Регистрация
- `non-auth`
```
curl --location 'http://localhost:8000/api/v1/auth/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "cool-admin",
    "email": "cool_admin@gmail.com",
    "password": "hack_me_plz"
}'
```
Возвращает `201`, `{
    "id": "ea146ac2-6caf-425e-ad64-2b7b7e21a6fb",
    "email": "cool_admin@gmail.com",
    "is_active": true,
    "is_superuser": false,
    "is_verified": false,
    "username": "cool-admin",
    "created_on": "2023-12-10T09:45:48.044526",
    "update_on": "2023-12-10T09:45:48.044526"
}`

<br>

3. 
- **/api/v1/auth/login**
- `POST`
- Аутентификация, [ссылка](https://fastapi-users.github.io/fastapi-users/12.1/usage/flow/#request_1) на документацию этого энтпоинта от библиотеки `fastapi-users`
- `non-auth`
```
curl --location 'http://localhost:8000/api/v1/auth/login' \
--form 'username="cool_admin@gmail.com"' \
--form 'password="hack_me_plz"'
```
Возвращает `200`, `{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo",
    "token_type": "bearer"
}`

<br>

4. 
- **/api/v1/auth/logout**
- `POST`
- [fastapi-users logout](https://fastapi-users.github.io/fastapi-users/10.0/usage/routes/#post-logout)
- `auth`
```
curl --location --request POST 'http://localhost:8000/api/v1/auth/logout' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo'
```
Возвращает `204`

<br>

> [!IMPORTANT]
> **Время жизни токена можно задать параметром `JWT_TTL_SEC` в файле `src/apps/auth/config.py`**

<br>

5. 
- **/api/v1/users/set_permission**
- `PATCH`
- Назначает пользователя администратором
- `admin`
```
curl --location --request PATCH 'http://localhost:8000/api/v1/users/set_permission' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo' \
--data '{
    "username": "existed-user-from-database"
}'
```
Возвращает `200`, `{
    "id": "1d989138-4f96-4eb3-b51b-14ca7381e3ac",
    "email": "existed_user_from_database@gmail.com",
    "is_active": true,
    "is_superuser": true,
    "is_verified": false,
    "username": "existed-user-from-database",
    "created_on": "2023-12-10T09:46:17.688530",
    "update_on": "2023-12-10T10:05:09.643149"
}` 

<br>

6. 
 - **/api/v1/categories/comments/delete/{comment_id}**
 - `DELETE`
 - Удаление комментариев в любой группе объявлений, если комментарий не найден в базе данных вернет `404` 
 - `admin`
 ```
 curl --location --request DELETE 'http://localhost:8000/api/v1/categories/comments/delete/1d989138-4f96-4eb3-b51b-14ca7381e3ac' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo'
 ```
Возвращает `200`, `{"Status": "Successful"}` 

7. 
- **/api/v1/announcement/**
- `POST`
- Создает новое обьявление в базе данных
- `auth`
```
curl --location 'http://localhost:8000/api/v1/announcement/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo' \
--data '{
    "title": "my new announcement",
    "content": "Loren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren Input",
    "category": "sale"
}'
```
Возвращает `201`, `{
    "title": "my new announcement",
    "content": "Loren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren Input",
    "category": "sale",
    "id": "564dc3dc-59db-4bc7-be25-3682a69dd8c4",
    "user_id": "45e8ff95-cede-4605-ae2d-129af6b56beb",
    "created_on": "2023-12-10T10:29:43.340521"
}`

<br>

> [!IMPORTANT]
> **При создании обьявления можно указывать только определенные категории, которые записаны в классе `EnumCategory` в файле `src/database/modelcategory.py`**
> **если захотите изменить категории не забудьте выполнить миграцию в базу данных `make migrations` затем `make migrate`**

<br>

8. 
- **/api/v1/announcement/**
- `GET`
- Берет все обьявления из базы данных
- `auth`
```
curl --location --request GET 'http://localhost:8000/api/v1/announcement/?limit=3&offset=1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo'
```
Возвращает `200`, `[
    {
        "id": "93e7d52d-2de7-409f-a29a-69f04466aeff",
        "title": "First"
    },
    {
        "id": "912e0ff3-5422-4529-b6c8-9c8ce1a367a3",
        "title": "Second"
    },
    {
        "id": "a4a39640-010e-4426-ab1e-3e9493f3a136",
        "title": "Third"
    }
]`

<br>

9. 
- **api/v1/announcement/{announcement_id}**
- `GET`
- Берет из базы данных обьявление по ID 
- `auth`
```
curl --location 'http://localhost:8000/api/v1/announcement/564dc3dc-59db-4bc7-be25-3682a69dd8c4' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo'
```
Возвращает 200, `{
    "title": "my new announcement",
    "content": "Loren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren InputLoren Input",
    "category": "sale",
    "id": "564dc3dc-59db-4bc7-be25-3682a69dd8c4",
    "user_id": "45e8ff95-cede-4605-ae2d-129af6b56beb",
    "created_on": "2023-12-10T10:29:43.340521"
}`

<br>

10. 
- **/api/v1/announcement/delete/{announcement_id}**
- `DELETE`
- Удаляет обьявление пользователя по ID(можно удалить только свое)
- `auth`
```
curl --location --request DELETE 'http://localhost:8000/api/v1/announcement/delete/564dc3dc-59db-4bc7-be25-3682a69dd8c4' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYTE0NmFjMi02Y2FmLTQyNWUtYWQ2NC0yYjdiN2UyMWE2ZmIiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwMjIwMzczMX0.loO_iZ5CIaFRFY0lUyRbGojYKW4L6LLAPkR87FuoVbo'
```
Возвращает `200`, `{"Status": "Successful"}` 