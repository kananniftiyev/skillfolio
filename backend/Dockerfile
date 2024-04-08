# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run Django migrations and start the Django development server
CMD python manage.py makemigrations && python manage.py migrate && python manage.py test && python manage.py runserver 0.0.0.0:8000
