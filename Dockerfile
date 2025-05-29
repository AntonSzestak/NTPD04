# 1. Baza: oficjalny obraz Pythona
FROM python:3.9-slim

# 2. Katalog roboczy w kontenerze
WORKDIR /app

# 3. Kopiowanie zależności
COPY requirements.txt .

# 4. Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiowanie pozostałych plików
COPY . .

# 6. Komenda startowa – uruchomienie API przez uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
