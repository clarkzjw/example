FROM python:3

ADD hello.py /app/

EXPOSE 8000

CMD ["python3", "-u", "/app/hello.py"]
