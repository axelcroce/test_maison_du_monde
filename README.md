# test_maison_du_monde
Technical test for Maison du Monde.
This is a simple Python/Flask app to check how many times some query strings occur in a list of strings. For the sake of the test, the list of strings is an environment variable set by the Dockerfile and the query strings is passed as an argument in the URL.
It returns a dictionary with the query strings as keys and the number of time it occurs in the list of strings as value.

Examples :
- input :    
    - strings = "ab,ab,abc"
    - queries = "ab,abc,bc"
- output :
{
  "ab": 2, 
  "abc": 1, 
  "bc": 0
}




## How to use the App

### Installation
- Clone the repository
    - git clone git@github.com:axelcroce/test_maison_du_monde.git
- Move to the directory
    - cd test_maison_du_monde

### Docker commands

1. Build the image : 
    - sudo docker build -t test_maison_du_monde:1.0 .

2. Run docker image :
    - sudo docker run -d -p 8000:8000 test_maison_du_monde:1.0

3. Stop and remove docker container :
    1. Get the id of the container :
    - sudo docker ps
    2. Stop and remove it :
    - sudo docker stop <id> && sudo docker rm <id>

OR

2. Running docker image using docker-compose to debug:
    - sudo docker-compose up

3. Delete stop and remove docker container using docker-compose:
    - sudo docker-compose down

### Using the Flask app

Currently there's no swagger implemented.
Once you run the Docker image, you can interact with the application.
To interact with the application :
- Connect to http://localhost:8000/
- Pass the argument queries to the url
- examples :
    - for the queries abc,ab,ac : http://localhost:8000/?queries=abc,ab,ac
    - for the queries fesrl,erb,abc : http://localhost:8000/?queries=fesrl,erl,abc

