# cs_416_project_2
A multi container web-app.


# Prerequisites
node
python
docker engine

# Production configuration

<strong>EVERYONE</strong>

Everyone must ensure their changes work properly on the dev build.

To run the production config, run
```docker compose -f compose.prod.yaml up --build```
The -v flag removes the database volume. This only exposes port 80 to the localhost, for the frontend. 

The API requests are routed according to the ```nginx.conf``` file, and routed through the docker network "app_net".

To shut down, run
```docker compose -f compose.prod.yaml down -v```

# Developer configuration

NOTE: You may omit the ```-v``` flag if you wish to have your data persist. It is optional, but good to test that it works every once in a while.

<strong>FRONTEND</strong>

To run the developer config, run
 ```docker compose -f compose.dev.yaml up --build```
 
Then, cd into frontend, and run 

```
npm i
npm run serve
```

This will spin up a local dev server, where the local frontend will post its API requests to port 8000, where the backend is listening


<strong>BACKEND</strong>

The backend is also being served hot, so any changes you make to the backend will re-compile instantly! Hit the backend directly with
```localhost:8000/<path>```
Where ```<path>``` is one of the FastAPI endpoints. This will make a simple GET request to the ```<path>``` endpoint.

POST Requests need to be tested throught the frontend.

To shut down, ctrl+c then run
```docker compose -f compose.dev.yaml down -v```
