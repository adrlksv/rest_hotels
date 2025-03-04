FROM python:3.10

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /booking/docker/*.sh

EXPOSE 8000

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
