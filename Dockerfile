FROM jfloff/alpine-python:3.6-onbuild 
COPY requirements.txt /tmp 
WORKDIR /tmp 
ENV TZ=Australia/Melbourne
RUN pip install -r requirements.txt 
WORKDIR /.
ADD observations_polling.py /
CMD [ "python", "-u", "./observations_polling.py" ]