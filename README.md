# Arrrdio
The piracy-fueled, open music queue!

[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTQuNDg0Mzg2NDQ0MDkxOCIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDE1NC40ODQzODY0NDQwOTE4IDM1Ij48cmVjdCB3aWR0aD0iNTkuNzUwMDAzODE0Njk3MjY2IiBoZWlnaHQ9IjM1IiBmaWxsPSIjNGE0YTRhIi8+PHJlY3QgeD0iNTkuNzUwMDAzODE0Njk3MjY2IiB3aWR0aD0iOTQuNzM0MzgyNjI5Mzk0NTMiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDAwMDAiLz48dGV4dCB4PSIyOS44NzUwMDE5MDczNDg2MzMiIHk9IjIxLjUiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtZmFtaWx5PSInUm9ib3RvJywgc2Fucy1zZXJpZiIgZmlsbD0iI0ZGRkZGRiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9IjIiPkhFSURJPC90ZXh0Pjx0ZXh0IHg9IjEwNy4xMTcxOTUxMjkzOTQ1MyIgeT0iMjEuNSIgZm9udC1zaXplPSIxMiIgZm9udC1mYW1pbHk9IidNb250c2VycmF0Jywgc2Fucy1zZXJpZiIgZmlsbD0iI0ZGRkZGRiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjkwMCIgbGV0dGVyLXNwYWNpbmc9IjIiPkZBTkNMVUI8L3RleHQ+PC9zdmc+)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-h9rbs.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/contains-17-coffee-cups.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/it-works-why.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/featured/featured-made-with-crayons.svg)](https://forthebadge.com)

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

