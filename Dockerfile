FROM python:3.7

WORKDIR /opt/

COPY app .

ENV STRINGS="ab,ab,abc"

ENTRYPOINT [ "python", "-m", "main", "ab,abc,bc" ]