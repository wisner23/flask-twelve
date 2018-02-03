FROM python:3

COPY . /twelve-app
WORKDIR /twelve-app

RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD [ "/twelve-app/start.sh" ]