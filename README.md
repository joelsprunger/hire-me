# Welcome to hire-me: an AI powered virtual interview
In this web-app I use an LLM to answer questions about my personal and professional background. The answers provide links to my resume, projects, and hobbies. If you like this app feel free to use my code to make one for yourself.

<img width="1131" alt="Screen Shot 2023-05-15 at 9 26 17 PM" src="https://github.com/joelsprunger/hire-me/assets/43421397/3c47ad5d-6160-471e-b42e-2b520ac5f3ad">


[LIVE DEMO](https://hire-joel.com)

## Design
### Frontend
Flask templates extended from base.html with [bootstrap](https://getbootstrap.com/) calls for styling and animation

### Backend
Python Flask for rendering html from templates, and managing forms, and a simple python dictionary to store/review prior QA pairs. 
These are stored in flask session objects so that each user will see only their own prior questions.

#### AI question and answering
Open AI api and Lang Chain are used for answering questions only using information from provided sources. (I followed [This article](https://dagster.io/blog/chatgpt-langchain) to figure out how to do this)

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
I deployed this using GCP Cloud Run. This keeps the app on an archived Docker image that can be run when/as needed. This means I don't have to continueously rent GCP resources.
1) First I followed the [quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service) to deploy a python service using cloud run. In this you will use google CLI to build and deploy the service to cloud run.
   1) You will need to set the environment variables on GCP for your project
2) Next I followed the [quickstart](https://cloud.google.com/run/docs/quickstarts/deploy-continuously#cloudrun_deploy_continuous_code-python) to continuously deploy from a git repository. This will re-deploy every time a new revision pushed to github. I followed this guide except that I selected docker image rather than google build packs. (This code will not work with google build packs in it's current form and you will need to look at the proper templates for python if you want to use google build packs.)
This provides more flexibility if I were to switch hosting services, and if there are any errors in deployment it allows me to build and run the docker image locally for debugging.


