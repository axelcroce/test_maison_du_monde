FROM python:3.7

WORKDIR /opt/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app .

ENV STRINGS="ab,ab,abc"

CMD [ "python","main.py" ]