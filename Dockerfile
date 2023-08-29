FROM python:3.9

WORKDIR /prueba

COPY requirements.txt /prueba/
COPY . /prueba/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]