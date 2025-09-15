# Gunakan base image Python 3.10 slim
FROM python:3.10-slim

# Tetapkan direktori kerja di dalam kontainer
WORKDIR /app

# Salin file requirements.txt ke dalam direktori kerja
COPY requirements.txt .

# Instal dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file dari repositori ke dalam kontainer
COPY . .

# Perintah untuk menjalankan aplikasi ketika kontainer dimulai
CMD ["python", "model.py"]
