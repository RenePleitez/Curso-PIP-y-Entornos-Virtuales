FROM python:3.9

WORKDIR /App
COPY requirements.txt /App/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /App/requirements.txt

COPY . /App

CMD bash -c "while true; do sleep 1; done"