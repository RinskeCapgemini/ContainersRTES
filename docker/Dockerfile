FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev \
    && pip install psutil numpy \
    && apt-get remove -y gcc python3-dev \
    && apt-get autoremove -y && apt-get clean

# Set the entrypoint to allow passing a custom script
ENTRYPOINT ["python3"]

