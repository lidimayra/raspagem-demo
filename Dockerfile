FROM continuumio/anaconda3

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

# Execute future commands from /app folder
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

# Copy everthing from current directory relative to the Dockerfile, over to
# working directory (/app)
COPY . .

CMD ["gunicorn", "-b", ":8000", "app.wsgi"]
