# FastAPI with Docker

[Link to DockerHub](https://hub.docker.com/repository/docker/pekkamattinen/devops-fast)

To run this FastAPI application you'll need to execute following commands in a terminal:

```terminal
docker build . -t fast 
docker run -p 127.0.0.1:8080:8080 fast
```
