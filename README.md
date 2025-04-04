# Class Manager!

A multi container web-app, with a production and development configuation.


# Prerequisites
node
python
docker engine

# Production configuration

<strong>EVERYONE</strong> must ensure their changes work properly on the dev build.

To run the production config, run
```docker compose -f compose.prod.yaml up --build```
The -v flag removes the database volume. This only exposes port 80 to the localhost, for the frontend.

The API requests are routed according to the "nginx.conf" file, and routed through the docker network "app_net".

To shut down, run
```docker compose -f compose.prod.yaml down -v```

# Developer configuration

NOTE: You may omit the ```-v``` flag if you wish to have your data persist. It is optional, but good to test that it works every once in a while.

## FRONTEND

All editing should be localized to the "App.vue" file in /frontend/src. Static assets go in the /assets folder.

To run the developer config, run
```docker compose -f compose.dev.yaml up --build```

Then, cd into frontend, and run

```
npm i
npm run serve
```

This will spin up a local dev server at ```http://localhost:8080```, where the local frontend will post its API requests to port 8000, where the backend is listening


## BACKEND

The backend uses [Pydantic models](https://docs.pydantic.dev/latest/) to recieve and validate JSON objecets from the frontend.

There are two data models, pydantic (recieveing from frontend) and SQLAlchemy(Querying database). They are identical.
All you have to know is you recieve the pydantic model as a function parameter, and convert it to a SQLAlchemy model when
you want to query the database. You can see their definitions in the "/backend/Functions" folder.

To interact with your API endpoints, visit ```http://localhost:8000/docs``` for the FastAPI interactive documentation. The pydantic model is also defined there under "Schemas"

The backend is also being served hot, so any changes you make to the backend will re-compile instantly! Hit the backend directly with the interactive docs. All endpoints need to be tested either through the frontend or the interactive docs.

<strong>To shut down</strong>, ctrl+c then run ```docker compose -f compose.dev.yaml down -v```
