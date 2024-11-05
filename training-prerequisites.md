# Training Prerequisites
   
Have the images in a registry available for attendees
   
```bash

$ git clone https://github.com/infralovers/training-flask-app
$ cd training-flask-app/
$ echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

$ docker build -t ghcr.io/infralovers/training-flask-app:v1 .
$ docker push ghcr.io/infralovers/training-flask-app:v1

$ git switch v2
$ docker build -t ghcr.io/infralovers/training-flask-app:v2 .
$ docker push ghcr.io/infralovers/training-flask-app:v2

$ git switch v3
$ docker build -t ghcr.io/infralovers/training-flask-app:v3 .
$ docker push ghcr.io/infralovers/training-flask-app:v3
```
