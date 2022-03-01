# Set working directory
# First attemps to cd into .ci, if that fails try from one level up
cd .ci || cd /home/docker/TeacherPortal/.ci

# build and deploy
docker-compose build --build-arg S3_KEY=${S3_KEY} --build-arg S3_SECRET_KEY=${S3_SECRET_KEY};
docker-compose up -d;