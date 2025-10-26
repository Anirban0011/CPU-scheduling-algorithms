<<<<<<< HEAD
FROM python:3.11-slim
=======
FROM python:3.12
>>>>>>> 96bb6c4cec6ceeafdd0b60c7fbe6568034b4bca5

WORKDIR /app

# Install gcc, make, and build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy files
COPY . .

# Install Python dependencies
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Build your C logic
RUN gcc -shared -o c_file.so -fPIC scheduler.c

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]