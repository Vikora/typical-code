# Docker

## Basic commands

    docker build -t <tag> .

Build an image from local Dockerfile


    docker run -it <image> bash

Run a container from the image, enter into it via bash.

`-t`     : Allocate a pseudo-tty

`-i`     : Keep STDIN open even if not attached

`-d `    : In the background in a "detached" mode

`--name` : Give the container a name

`--rm`   : Automatically clean up the container


    docker ps

List active images

`-a`     : All images with any status


    docker system prune

Remove all

## Dockerfile

