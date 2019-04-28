# Smile
---
#### Install

> [Docker](https://docs.docker.com/install/)

> [Docker compose](https://docs.docker.com/compose/install/)

---

### Clone and run
To get project
> `git clone git@github.com:BakitD/Smile.git`

> `cd Smile/`

Run command
> `docker-compose up -d`


### Using Postman collection

Import collection `Chaining API.postman_collection.json` from postman directory.


Open `ChainingGet` and press `Send` button. You can check in environments tab, that
token was set to the value which we obtained from POST request to /api/auth/login in
pre-request script.


`or you can send requests separately`


Open `POST_auth_login` request and press `Send`, than check token environmnet variable.
It must equals to token that you will see in respone body. Then open `GET_hello_world` and press `Send`.
Reponse body should equals to:
```json
{
    "hello": "world"
}
