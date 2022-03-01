FROM python:3
ADD version_app.py /
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD [ "python", "./version_app.py" ]
