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

### 2. Docker

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
$ docker pull swernst/cauldron:latest-miniconda
```

You should see in response to this command that the cauldron container image 
is downloaded onto your system for use.