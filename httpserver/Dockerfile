FROM ubuntu:21.04

RUN apt-get update && apt-get install -y python3

ADD hello.py /app/

EXPOSE 8000

CMD ["python3", "-u", "/app/hello.py"]
