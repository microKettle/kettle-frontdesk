FROM python:3.5
ADD . /opt/kettle
RUN cd /opt/kettle && pip install -r requirements.txt
WORKDIR /opt/kettle
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"] 
