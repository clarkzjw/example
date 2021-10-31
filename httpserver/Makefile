build:
	# by default, Docker daemon looks for `Dockerfile` in the directory to build images
	docker build -t httpserver:ubuntu .
	# you can also specify which Dockerfile to use using `-f` flag
	docker build -t httpserver:py -f Dockerfile.py .

run: 
	# you can use `-p` flag to specify port mapping
	docker run -d -p 8000:8000 httpserver:py 
	# or use `-P` flag to let Docker choose automatically
	docker run -d -P httpserver:ubuntu

clean:
	docker ps -aq | xargs docker rm -f
