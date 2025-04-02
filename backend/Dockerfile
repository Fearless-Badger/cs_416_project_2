FROM python:3.9-slim
RUN python -m venv venv .
ENV PATH = "/venv/bin:$PATH"
RUN pip install --upgrade pip setuptools
WORKDIR /backend
COPY requirements.txt .
RUN pip install --nocache-dir -r requirements.txt
COPY . .
