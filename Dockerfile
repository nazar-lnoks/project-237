FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . ./app
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]