FROM python:3.10

RUN pip3 install runpod

COPY handler.py handler.py

CMD ['python3', 'handler.py']
