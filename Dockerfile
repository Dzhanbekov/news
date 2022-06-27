FROM python:3.9.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN apt update && apt install -y postgresql-client && pip install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /code/


CMD ["sh", "-c", "python manage.py collectstatic --no-input; \
                  python manage.py migrate; \
                  python manage.py runserver 0.0.0.0:8000"]
