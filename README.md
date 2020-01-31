# Demo Flask App

Used for https://broadworkbench.atlassian.net/browse/CA-660 

Build Docker image:

    docker build -f docker/Dockerfile -t iam_poc/flask_app .

Run the image:

    docker run --rm -p 5000:5000 iam_poc/flask_app

Access the app at: http://localhost:5000/