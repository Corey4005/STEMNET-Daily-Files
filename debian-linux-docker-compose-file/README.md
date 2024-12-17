# How to run the docker-complose.yml file

The STEMNET docker container runs as a root user when creating daily and climatology files. The container will 
direct the files created by root to a `data_out` volume directory on the local machine. To make sure the host machine 
has the correct permissions for that directory, the user must run the environment script `envsetup.sh`. This 
will set an environment variable that is used by the [startup script](https://github.com/Corey4005/STEMNET-Daily-Files/blob/main/debian-linux-build/entrypoint.sh) 
called by the container on startup. The effect of the script is that the user and group id on the `data_out` folder on the host machine
will match with the shared folder it is mapped to in the container. 

1. Set the `LOCAL_USER_ID` environment variable using the `envsetup.sh` script:
```
./envsetup.sh
```
2. Run docker compose file to pull the image from docker hub and start a stemnet container
```
docker compose up -d 
```
3. Attach to the newly created stemnet container as `root`
```
docker exec -it stemnet bash
```
4. Or, attach to the stemnet container as `user`:
```
docker exec -it -u user bash
```

You can exit the bash shell by typing `exit` and hitting `enter` on your keyboard. 
Output files created by the container will be dumped in the `./data_out` directory on the host machine.  
