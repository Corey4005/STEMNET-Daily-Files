# How to build the docker files locally 
1. First, build the base image `Dockerfile-parent` using the following command: 
```
docker build -t base -f Dockerfile-parent .
```
2. Second, build the child image `Dockerfile-child` using the following command:
```
docker build -t debian-stemnet -f Dockerfile-child .
```
3. Run the container locally 
```
docker run -it -d -v ./data_out/home/user/data_out -e LOCAL_USER_ID=`id -u $USER` --name stemnet debian-stemnet
```
4. Interact with the container as `root` using the following command:
```
docker exec -it stemnet bash
```
5. Or, interact with the container as `user` using the following command: 
```
docker exec -it -u user stemnet bash
```
6. Inspect local images that were built using the following command: 
```
docker image ls
```
7. Inspect running containers on the local host:
```
docker ps
```
8. How to kill and remove the container:
```
docker kill stemnet
docker container rm stemnet
```
9. How to remove the images from your host machine:
```
docker rmi -f base
docker rmi -f debian-stemnet
```
