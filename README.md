# Production Data Science with Cauldron Workshop

These are the resources for the Cauldron introductory workshop. The focus of 
this workshop is to familiarize you with an un-notebook-based workflow using
Cauldron and the additional production tooling that the workflow supports.

## Prerequisite Setup

In preparation for this workshop, you will need to complete the following
setup instructions:

### 1. GitHub

If you do not have one already, please create an account at
[GitHub](https://github.com). If you are not comfortable with using git on the
command line and do not have a preferred git client, you should also download 
and install [GitHub Desktop](https://desktop.github.com/).

### 2. PyCharm

You are certainly welcome to use whatever IDE or Text Editor you prefer for
authoring your Python code. However, this workshop will rely heavily on 
features available within the free and open-source PyCharm Community Edition.
If you wish to use an alternative editor, you should be familiar with all of 
the commonly used git commands including branch management.

Download the [PyCharm: Community Edition](https://www.jetbrains.com/pycharm/download/)
and install it. If you already have PyCharm installed, please make sure that 
you have the latest version.

### 3. Docker

You will need to have a functioning Docker community edition environment 
running on your computer. Download link and installation instructions are 
available at:

- **MacOS**: [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac)
- **Windows 10 Professional**: [Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)
- **Windows 10 Home**: [Docker Toolbox](https://www.docker.com/products/docker-toolbox)

Make sure that after you download and install Docker that you run the Docker
application to start it. If Docker is successfully installed and running, you
will be able to run the following command in a Windows or Mac terminal:

```bash
$ docker --version
```

and you should see the command return version information about your docker
installation. If for some reason the command does not work, make sure you have
started the Docker application after installing it and have given it enough
time to fully start the background docker service.

**Docker Toolbox Users**
*You will need to open the Docker Toolbox shell instead of the standard 
windows shell to access docker.*


### 3. Docker Images

Once docker is installed and working, you will need to install a few docker 
images that we use throughout the workshop. These images can take a while
to download, so please make sure you install them before the workshop starts:

- [Cauldron](https://hub.docker.com/r/swernst/cauldron/): This image contains 
  the Cauldron Python kernel. Install it by running the following docker 
  command:
  
  ```bash
  $ docker pull swernst/cauldron:latest-miniconda
  ```
  
- [Coala](https://hub.docker.com/r/coala/base/): This image contains automated 
  code review and linting for Python. Install it by running the following 
  docker command:
  
  ```bash
  $ docker pull coala/base:latest
  ```
