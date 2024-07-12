FROM python:3.10-alpine
COPY . /web
WORKDIR /web
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]