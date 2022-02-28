FROM python:3

ADD main.py /

RUN pip install pygame

CMD [ "python", "./main.py" ]
