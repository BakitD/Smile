# Smile
---
#### Install

> [Docker](https://docs.docker.com/install/)

> [Docker compose](https://docs.docker.com/compose/install/)

---

### Clone and run
To get project
> `git clone git@github.com:BakitD/Smile.git`

Run command
> `docker-compose up -d`


### Using Postman collection

Import collection `Chaining API.postman_collection.json` from postman directory.

Then open `POST_auth_login` request and press `Send`, than check token environmnet variable.
It must equals to token that ypu will receive in respone body. Then open `GET_hello_world`.
Reponse body should equals to:
```json
{
    "hello": "world"
}
