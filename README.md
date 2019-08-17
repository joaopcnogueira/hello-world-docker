# Docker Hello World

### Instructions

Clone the repository:
```console
foo@bar:~$ git clone https://github.com/joaopcnogueira/hello-world-docker.git
```

Go to hello-world-docker folder:
```console
foo@bar:~$ cd hello-world-docker
```

Build the docker: 
```console
foo@bar:~$ docker build -t hello-world-app .
```
Run the app with either the first command below or the second:
```console
foo@bar:~$ docker run -it --rm -v "$HOME"/Downloads:/usr/src/app/output --name my-running-app hello-world-app
```


When the script finish running, we should have a file small_titanic.csv inside you "Downloads" folder.


References: 
* https://towardsdatascience.com/why-you-should-care-about-docker-9622725a5cb8
* https://towardsdatascience.com/docker-for-python-development-83ae714468ac
* https://hub.docker.com/_/python

