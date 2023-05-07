FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR destin
EXPOSE 8000

COPY new_requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r "new_requirements.txt"

#COPY . .

# running migrations
#RUN python manage.py migrate

# gunicorn
CMD ["python", "manage.py", "runserver"]
