### **Запуск проекта в docker**

`git clone https://github.com/mesherinovivan/emphasoft.git`

`cd emphasoft`

`docker-compose build`


`docker-compose up`

### **Запуск миграций**

`docker exec -it emphasoft_web_1 ./manage.py migrate`

### **Запуск создание суперпользователя**

`docker exec -it emphasoft_web_1 ./manage.py createsuperuser`

### **Запуск тестов**


`docker-compose run  web  python -m pytest --ds=api.settings -vv` 

# API

##### Авторизация

`curl  -X POST   -H "Content-Type: application/json"   -d '{"username": "admin", "password": "admin"}'  http://localhost:8000/api-token-auth/`

##### POST
`curl -X POST "http://localhost:8000/api/v1/users/<USER_ID!!!!>/"  -H "Content-Type: application/json" \
 -H "Authorization:Bearer <TOKEN!!!!!>" \
 -d "{ \"username\": \"iamescherinov\", \"first_name\": \"test\", \"last_name\": \"test\", \"password\": \"testtest\", \"is_active\": false}"`

##### GET
`curl -X ПУЕ "http://localhost:8000/api/v1/users/"  -H "Content-Type: application/json" \
 -H "Authorization:Bearer <TOKEN!!!!!>" `

##### PUT
`curl -X PUT "http://localhost:8000/api/v1/users/<USER_ID!!!!>/"  -H "Content-Type: application/json" \
 -H "Authorization:Bearer <TOKEN!!!!!>" \
 -d "{ \"username\": \"iamescherinov\", \"first_name\": \"test\", \"last_name\": \"test\", \"password\": \"testtest\", \"is_active\": false}"`
 
##### DELETE
`curl -X DELETE "http://localhost:8000/api/v1/users/<USER_ID!!!!>/"  -H "Content-Type: application/json" \
 -H "Authorization:Bearer <TOKEN!!!!!>" \
 -d "{ \"username\": \"iamescherinov\", \"first_name\": \"test\", \"last_name\": \"test\", \"password\": \"testtest\", \"is_active\": false}"`
