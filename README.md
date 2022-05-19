# VASC Teacher Portal
The services powering the VASC Sea Turtle Simulation. 

## Development
The project utilizes Django, The Django Rest Framework, and TailwindCSS for styling.
All of this is packaged up in convenient docker containers for local development and
deployment. Ensure that you have both Docker and docker-compose installed on your local
machine. To spin up the development environment, from the root of the directory
run the command:

```zsh
docker-compose up -d --build
```

This will build the project locally on your machine and then expose it at [localhost:8009/](http://localhost:8009/).
You will also need to create a local superuser within the service, which can be done by issuing the following 
command and then following the instructions provided in the terminal:

```zsh
docker-compose exec -it vasc_teacher_portal python manage.py createsuperuser
```

## Production
The service is currently deployed at [vr.uncw.edu/VASC/](https://vr.uncw.edu/VASC/), hosted on our
production server. Deployment looks very similar to development, with the key difference being the 
incantation. A number of environment variables must be set, which are defined within .ci/prod.docker-compose.yaml.
As of current, all of these variables can be found on the server at ```/etc/environment```. If the service
is moved to a new hosting location, ensure these environment variables are set once again.
To deploy the service, from the root of the project directory, run the following command:
```zsh
sudo sh .ci/build.sh
```