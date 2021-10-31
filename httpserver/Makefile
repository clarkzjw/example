build:
	docker build -t httpserver:py -f Dockerfile.py .
	docker build -t httpserver:ubuntu -f Dockerfile.ubuntu .

run: build 
	docker run -d -p 8000:8000 httpserver:py 
	docker run -d -P httpserver:ubuntu

clean:
	docker ps -aq | xargs docker rm -f