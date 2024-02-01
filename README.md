**Deployment to Render:**

1.  Create a account in Render, can use github login to create one that way all github repos are automatically available)
2.  Create a new webserivce in Render
3.  Specify the URL to your git repository.
4.  Render will automatically detect that you are deploying a Python service and use pip to download the dependencies.
5.  Specify the following as the Start Command.
6.  uvicorn main:app --host 0.0.0.0 --port $PORT
7.  click Create Web Service.
