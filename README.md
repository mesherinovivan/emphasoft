### **Запуск проекта в docker**

`git clone https://github.com/mesherinovivan/emphasoft.git`

`cd emphasoft`

`docker-compose build`

`docker-compose up`

### **Запуск тестов**


`docker-compose run -e BASE_URL="http://web:8000/" -e TEST_PASSWORD="admin" -e TEST_USER="admin" web  python -m pytest` 

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
