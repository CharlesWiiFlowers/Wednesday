# syntax=docker/dockerfile:1

FROM python:3.10.9
WORKDIR /src
COPY . .
RUN pip install flet
RUN pip install pytube
CMD [ "py", "index.py" ]
EXPOSE 3000