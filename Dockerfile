FROM python:3.9.13

LABEL "creator"="Rolik Denis"

WORKDIR /test_project/

COPY requrements.txt .

RUN pip install -r requrements.txt

ENV ENV=dev

CMD pytest -s -v