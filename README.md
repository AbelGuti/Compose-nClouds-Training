# Docker Compose Training
This is a Docker compose exercise made for nClouds Training.

## Project structure
### Database Directory
A MySQL database consisting of one table with a list of nClouds' case studies (see database/database.sql).

### Webapp Directory
The webapp retrieves the case studies from the database and shows them in a HTML page. This webapp is build using Flask.

## Exercise
* Fork this repository from your GitHub personal account.
* Create a compose.yml file to run the webapp and the database.

Once your created the compose.yml file, run:
```
docker compose build
docker compose up
```

Access localhost and if everything looks good, commit your changes into your repository.

## Tips
* Take a look at the database configuration defined on the webapp/server.py file. Use the same credentials for your MySQL container.
* Learn about how MySQL docker image works in: https://hub.docker.com/_/mysql
