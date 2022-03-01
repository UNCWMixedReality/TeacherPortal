# Set working directory
# First attemps to cd into .ci, if that fails try from one level up
cd .ci || cd /home/docker/TeacherPortal/.ci

# build and deploy
docker-compose --file prod.docker-compose.yaml build --build-arg S3_KEY=${S3_KEY} --build-arg S3_SECRET_KEY=${S3_SECRET_KEY};
docker-compose --file prod.docker-compose.yaml up -d;