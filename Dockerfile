FROM python:3.12.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /blog

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /blog

CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ]