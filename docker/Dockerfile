FROM python:3.7

# Create directory for Bond in the container
RUN mkdir /app
WORKDIR app/

# Install dependencies and set the PYTHONPATH appropriately so that dependencies can be found by the runtime
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the source files into the the container
COPY . .

ENV FLASK_APP hello.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
