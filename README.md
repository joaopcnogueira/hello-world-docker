# Docker Hello World

### Instructions

Clone the repository:
```console
foo@bar:~$ git clone https://github.com/joaopcnogueira/hello-world-docker.git
foo
```

Go to hello-world-docker folder:
```console
foo@bar:~$ cd hello-world-docker
foo
```

Build the docker: 
```console
foo@bar:~$ docker build -t hello-world-app .
foo
```
Run the app with either the first command below or the second:
```console
foo@bar:~$ docker run -it --rm --name my-running-app hello-world-app
foo
```
```console
foo@bar:~$ docker run hello-world-app
foo
```
