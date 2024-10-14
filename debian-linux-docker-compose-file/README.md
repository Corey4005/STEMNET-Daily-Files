# How to run the docker-complose.yml file

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
