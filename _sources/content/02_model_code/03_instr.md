# Steps to reproduce results

## Launching a notebook on Google Colaboratory 

The [model code](./04_model.ipynb) can be executed without having to install anything on a local machine using Google's online notebook infrastructure.  

> At the time of writing this is the recommended option due to a temporary shortage of capacity on mybinder.org

1. Open the model code page of this book
2. In the top right hand corner you will see that a rocket ship icon is added to the tool bar.  Move the cursor over this rocket ship and select **Colab** from the drop down list
3. The model notebook will now launch on Google Colaboratory.  This is similar to a remote instance of Jupyter. You will be presented with a notebook containing the model code.
4. From the `Runtime` menu select `Run All`. This will run all cells and reproduce the results of the study.

```{admonition} Google account
In order to run notebooks in Google Colaboratory you are required to sign into a Google account
```

## Launching Jupyter Lab on BinderHub

The [model code](./04_model.ipynb) can be executed without having to install anything on a local machine.  

1. Open the model code page of this book
2. In the top right hand corner you will see that a rocket ship icon is added to the tool bar.  Move the cursor over this rocket ship and select Binder from the drop down list
3. Jupyter lab will now launch on BinderHub.  This is a remote instance of Jupyter. You will be presented with a notebook containing the model code.
4. From the `Run` menu select `Run All`. This will run all cells and reproduce the results of the study.


```{admonition} Launching a remote instance of Jupyter
Note that BinderHub will build a Docker image containing the required software and model code. If the instance has not been used for several days this will take several minutes to complete.  The launch will speed up after an initial build.  None of this is affected by the speed of your local machine.   

```

## Executing code in the book

The [model code](./04_model.ipynb) can also be excuted directly from the pages of this book.  To do this repeat steps 1-2 above, but select `live code` from the drop down menu.  Blocks of code will now be converted to interactive and executable **cells**.  

> Note live code uses mybinder.org.  This is experiencing a temporary shortage of capacity.


## Executing the code on a local machine using Docker

The model and software environment used to create it are available as a `docker` image.  

You will need `docker` installed on your local machine from https://www.docker.com/products/docker-desktop

* linux users can install: `sudo apt-get install docker.io`
* Mac OS users can install docker desktop: https://docs.docker.com/docker-for-mac/install/
* Windows user can install docker desktop via WSL2: https://docs.docker.com/docker-for-windows/install/ 

## Downloading the image

```
# pull the image containing the model from dockerhub 
docker pull tommonks01/treat_sim
```

## Running the container and model.

Open a terminal or cmd line

```
# run the docker image and map local port 8181 to port 80 on the container
docker run -p 8181:80 tommonks01/treat_sim
```

Launch a browser and navigate to:
```
localhost:8181
```

This launches Jupyter-Lab.  The model can be found in the model.ipynb notebook.  