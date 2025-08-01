FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

# Create staticfiles directory
RUN mkdir -p /code/lekalgroup/staticfiles
