FROM python:3.7
WORKDIR /docker-backend
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
