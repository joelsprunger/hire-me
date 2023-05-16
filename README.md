# Welcome to hire-me an AI powered virtual interview
In this web-app I use an LLM to answer questions about my personal and professional background. The answers provide links to my resume, projects, and hobbies. If you like this app feel free to use my code to make one for yourself.

## Design
### Frontend
Flask templates extended from base.html with [bootstrap](https://getbootstrap.com/) calls for styling and animation

### Backend
Python Flask for rendering html from templates, and managing forms, and a simple python dictionary to store/review prior QA pairs. 
These are stored in flask session objects so that each user will see only their own prior questions.

#### AI question and answering
Open AI api and Lang Chain are used for answering questions. TODO: link to LangChain article.

## Getting started
### Code Setup
1) Python 3.9 (I used a virtual environment with 3.9.5) 
2) Fork this repo and clone it.
3) pip install requirements.txt
4) Change out my resume for yours.
5) In /ai_service/ai_answers.py you can change the list of sources to point to your resume and other documents. Edit the biographical.txt
file to be your own information. Feel free to add more sources this should scale up to work with many
sources and long sources.
6) ENVIRONMENT VARIABLES 
   * SECRET_KEY is used by flask to secure the form data. This can
   be set to anything. 
   * OPENAI_API_KEY is used by Lang Chain to access GPT API you will need to sign up for an OPENAI developer account. You can get $5 of free
   credits to get started and get a key. You can also look at using a free open source model. I was able to do this, but it requires a GPU to be 
   at all effective and I deployed this to google Cloud Run, which doesn't have GPUs

### Running 
To run and debug locally run app.py this will produce an ip address/link to the app running locally

### Deployment
I deployed this using GCP Cloud Run. 
1) First I followed the quickstart to deploy to cloud using cloud cli and building a docker image.
   1) You will need to set the environment variables on GCP for your project
2) Next I followed the getting started guide to continuously deploy except that I selected use docker image rather than google build packs.
This provides more flexibility if I were to switch hosting services, and allows me to build the docker image and test it out locally if 
there are any issues with the image that need to be debugged.


