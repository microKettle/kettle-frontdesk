FROM debian:8
RUN apt-get update -y && apt-get install python-pip python-dev build-essential -y
RUN mkdir -p /opt/docker
ADD resources/startDockerDev.sh /root
WORKDIR /opt/docker
EXPOSE 5000
ENTRYPOINT ["/bin/bash"] 
