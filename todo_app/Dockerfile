# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /todo_app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# RUN python manage.py collectstatic --noinput
# RUN python manage.py collectstatic --noinput
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Collect static files
# Copy the rest of the application code into the container
COPY . /todo_app/

RUN python manage.py collectstatic --noinput

# Expose the port that the app runs on
EXPOSE 9000

# Run the command to start the application
CMD ["gunicorn","--bind", "0.0.0.0:8000", "todo_app.wsgi:application"]
