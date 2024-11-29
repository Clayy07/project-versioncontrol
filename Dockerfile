# image dasar Python
FROM python:3.9-slim

# working directory di dalam container
WORKDIR /app

# Salin file aplikasi ke dalam container
COPY . /app

# Install dependensi
RUN pip install -r requirements.txt

# Ekspose port aplikasi
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
