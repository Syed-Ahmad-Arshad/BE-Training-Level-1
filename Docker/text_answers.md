## Q1: Compare different kinds of docker image families. Alpine, Slim, Stretch, Buster, Jessie, Bullseye. What does this mean? How are they different? What advantage do they provide over the others?
Stretch, Buster, Jessie
```
Images with tags of buster, stretch and jessie are codenames of different debian releases. Buster is codename of all version 10 releases, Stretch was codename for all version 9 releases and similarly Jessie was for version 8.
```
Bullseye
```
Bullseye and Bookworm are codenames for future releases. 
```
Slim
```
The slim image is a paired down version of the full image. This image generally only installs the minimal packages needed to run your particular tool.
```
Alpine
```
Alpine images are based on linux.
```
## Q2: Difference between Entrypoint and CMD directive in a Dockerfile?
Both CMD and Entrypoint sepcify the programs that need to be executed when the container starts running. However, there are some differences. CMD directives will be ignored when RUN has tha parameters but Entrypoint will not be ignored. Ideally there should only be 1 CMD command but if there are multiple, only the last one won't be ignored. Both CMD and Entrypoint can be used together in certain situations. 

## Q3: Explain this command written inside a Dockerfile:RUN mkdir /app/django/helloworld
It makes a directory named helloworld at the path current_dir/app/django.

## Q4: Explain the concept of layering in Docker images/containers?
There are certain commands like RUN, COPY and ADD that will make a new layer on top of other layers. There can be multiple layers in a docker image and each layer will correspond to certain commands. A layer contains the differences between the preceding layer and current layer. All the layers are read only except the top most one. There is a writable layer on top that is called container layer.