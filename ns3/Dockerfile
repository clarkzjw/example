FROM ubuntu:21.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y \
    build-essential python3 python3-dev git wget

RUN mkdir ~/workspace && cd ~/workspace && \
    wget https://www.nsnam.org/release/ns-allinone-3.35.tar.bz2 && \
    tar xjf ns-allinone-3.35.tar.bz2

WORKDIR /root/workspace/ns-allinone-3.35/ns-3.35

RUN ./waf configure && \
    ./waf build

ADD hello.cc ./scratch/

RUN ./waf configure && \
    ./waf build

CMD ["./waf", "--run", "hello"]
