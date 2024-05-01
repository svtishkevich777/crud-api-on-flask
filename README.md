# crud-api-on-flask-using-mongodb
# setup

clone the repository
```sh
$ git clone git@github.com:svtishkevich777/crud-api-on-flask.git
$ cd crud-api-on-flask
```
Create a virtual environment to install dependencies in and activate it:
```sh
1. First update the PIP
$ python3 -m pip install --upgrade pip
```
```sh
2. Next we indicate the python version with which we want to work
   and the name of the virtual environment.
$ virtualenv -p python3.8 .venv
```
```sh
3. And then activate the created virtual environment
$ source .venv/bin/activate
```
```sh
4. Then you need to set the dependencies:
(.venv)$ pip install -r requirements.txt
```
```sh
5. Now you can run the development server in the terminal.
$ python run.py
```
# Setup Docker

For start Docker, you need to run command:

```sh
$ docker-compose up --build
```
Available endpoints:
```sh
    Home-page    -> http://0.0.0.0:8080
    get-all-users -> http://0.0.0.0:8080/api/v1/users
    create-users  -> http://0.0.0.0:8080/api/v1/users
    get-users     -> http://0.0.0.0:8080/api/v1/users/<add-id>
    put-users     -> http://0.0.0.0:8080/api/v1/users/<add-id>
    delete-users  -> http://0.0.0.0:8080/api/v1/users/<add-id>
    
```
example of data
```sh
{
  "name": "User_name",
  "age": 30
}
```

# Description of the task
```sh
Создать docker-compose.yml разворачивающий приложение на python с простой реализацией REST API. 
Решение должно состоять из двух контейнеров:

а) Любая NoSQL DB.

б) Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.

в) Создаем значение ключ=значение, изменяем ключ=новое_значение, читаем значение ключа.

г) Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.
```
