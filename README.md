# test_mdm
Technical test for Maison du Monde

## Docker commands

- Build the image : 
    - docker build -t test_mdm:1.0 .

- Run docker image :
    - docker run -d -p 8000:8000 test_mdm:1.0

- Using docker-compose to debug:
    - docker-compose up

- Delete docker-compose:
    - docker-compose down

## Flask app

Currently there's no swagger implemented

To interact with the application :
- Connect to http://localhost:8000/
- Pass the argument queries to the url
- example http://localhost:8000/?queries=abc,ab,ac
