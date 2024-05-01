# Sentiment-Analysis-with-Movie-Reviews
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ml3o3YLw)

## Table of Contents
- [Reproducibility](reproducibility)
- [Fiction Background](#fictional-background)
- [Task](#task)
- [MLOps](#mlops)
- [Containerized Deployment](#containerized-deployment)
- [LocalHost Server](#localhost-server)
- [See More](#see-more)

## Reproducibility
- The requirements.txt contains the required libraries + more
- Git clone my repository and run all the cells in the ipynb file - '/workspace/workspace.ipynb'

## Fictional Background
Marvin works at the last Blockbusta Videoz (a fictional video rental shop) where his task is to classify movie and TV show reviews to help curate a special section of the store.

One day while perusing his favorite website, Marvin came upon a post about someone who secretly automated their job and then quietly took off on a long (paid) vacation. Inspired, Marvin set aside a portion of his salary to hire a developer to write a few scripts to scrape movie reviews from various sources. It's a bit noisy, but aggregating many reviews has cut the time he previously spent on his job by half.

Now, after reading an article about AI, Marvin wants to take things a step further: he is searching for a program that can determine a) whether or not a piece of text is a movie/TV show review and b) whether or not each review is positive (the movie/TV show is recommended) or negative (the movie/TV show should be avoided).

Marvin has put together a competition and advertised it on Fraggle (a fictional platform for competitive data science).

## Task
![ticket-2974645_1280](https://github.com/uazhlt-ms-program/grad-level-term-project-kaggle-competition-weezymatt/assets/85853890/004101cf-4822-412e-abc1-8f4a69ce5575)

See https://uazhlt-ms-program.github.io/ling-539-course-blog/assignments/class-competition

Competition: https://www.kaggle.com/competitions/ling-539-sp-2024-class-competition

Invitation URL: https://www.kaggle.com/t/33320feca02e42bd924c3473e3a8c2fd

<a name="mlops"></a>
## MLOps — *Where does my model go from here?*
This Sentiment Analyisis was a part of a class competition to predict whether or not a piece of text is a movie/TV show review and b) whether or not each review is positive or negative. The project was also an exercise to deploy the final model by using FastAPI, Docker and cloud provider Render to host the site (the free version of Render ran out of memory (used over 512MB) while running my code). We will instead recommend using Docker to pull the image to run the move in your local server.

## Containerized Deployment
Below are a fews commands to pull the image from DockerHub and test the model in your machine. The FastAPI Documentation details the available endpoints, JSON request and response formats, and information specified in my ```mlapi.py``` file. You can access this documentation by adding the /docs to the server (http://localhost:8000/docs). Additionally, you can simply clone my repository to reproduce the results.

1. Pull the Image.
```bash
docker pull weezygeezer/reviews-api:latest     
```
2. Run a Container.
```bash
docker run -d -p 8080:80 weezygeezer/reviews-api:latest
```
3. Visit the LocalHost server.
(http://localhost:8000/docs)

## LocalHost Server
The FastAPI documentation sends a JSON request to the model. Below is an example of how the API will look on your machine:

<img width="1376" alt="SA-rev" src="https://github.com/uazhlt-ms-program/grad-level-term-project-kaggle-competition-weezymatt/assets/85853890/15189fe7-01c7-419b-bab5-499f31f65e23">
<img width="1342" alt="SA-example" src="https://github.com/uazhlt-ms-program/grad-level-term-project-kaggle-competition-weezymatt/assets/85853890/05af8189-b3bb-4f9e-8736-8e99c4a1d860">

## See more
I lied. There's nothing more to see but thanks for reading!
