# Vector Database (and AI prompt?)
by Henriques Amaral Guilherme Filipe, Schneider Bastien, Salamin Alexandre


## Description of the project

This project focuses on developing a high-performance vector database, leveraging Qdrant for efficient indexing and retrieval of vector data.

For our project, we decided to do a recommendation of games based on the steam collection until 2019. With Qdrant, it will provide a solution for our project thanks to his rapid and accurate processing.

We will mainly focus on the explanation of how vector database work and compare it to other solution.

## Step-by-step installation
You can find the extended version in the [qdrant website](https://qdrant.tech/).

## Requirement

 - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - [Python](https://www.python.org/downloads/)
 - Python client (Like [VS code](https://code.visualstudio.com/download), [Intellij](https://www.jetbrains.com/idea/download/?section=windows),...)

##  Starting the Qdrant docker

1. Have all the requirement installed
2. Install the Qdrant docker (via the command prompt for example)
```docker pull qdrant/qdrant```
3. Run the docker
``docker run -p 6333:6333 qdrant/qdrant``
4. You can access to the website UI of the [docker](http://localhost:6333/dashboard)
![Image01.png](Images%2FImage01.png)
5. Now you can access everytime to the UI pannel. Don't forget to always run the docker before going to the website.

## Access with Python client

1. Install the needed packages via ```pip install``` :
 - qdrant-client
 - pandas
 - numpy
 - fastapi
 - sentence-transformer
2. 
