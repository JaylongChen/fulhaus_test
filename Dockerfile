# start by pulling the python image
FROM python:3.6-alpine
RUN apk add g++ 
RUN pip install numpy
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file

RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]