FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r req.txt




