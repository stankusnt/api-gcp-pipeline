FROM python:3.12
WORKDIR /desktop/api-test-dir
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "-u", "main.py"]