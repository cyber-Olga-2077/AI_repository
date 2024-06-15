FROM python:3.10.12-slim-bookworm
WORKDIR /flask-app
COPY ./requirements.txt /flask-app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=vision_app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
