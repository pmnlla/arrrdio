# Arrrdio
The piracy-fueled, open music queue!

## Objective

The objective of the project is to create an open-queue radio system with an announcer, free to everyone. This is unfeasible for a series of reasons, notably copyright and IP laws. Thus, there is no known publicly hosted instance.

However, there are a series of use cases for this system regardless, my favorite being a platform agnostic alternative to Spotify's jams.

## The Stack

The following dependencies are required:

- A running mongodb instance; can be done through Atlas as well.
- RabbitMQ
- ffplay (packaged with ffmpeg).
- Python >=3.12 w/ pip & venv
- bun

## Setup: Frontend

The frontend is located in the `arrrdio-webui` folder, as a nuxt.js project. Simply run `bun i; bun run dev` after configuring `nuxt.config.ts` to point to your backend instance.

## Setup: Backend

1. Configure `arrrdio-backend/radio/interface/.env` to point to your mongo instance, following the provided `.env.example` file.
2. Install python requirements into a venv - they are listed in the root of this repository under `requirements`
3. With a rabbitmq instance runnimg, cd into the `arrrdio-backend` folder on 2 TTYs.
 a. On your first TTY, cd into `radio/interface` and run `$ dramatiq tasks`.
 b. On your second TTY, cd into `radio/` and run `$ python3 manage.py runserver`. This should start up a development WSGI server for the backend.

