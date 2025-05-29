# lab03-api – Aplikacja FastAPI z modelem ML w Dockerze

##  Wymagania

- Python 3.9+ (jeśli uruchamiasz lokalnie)
- Docker
- Docker Compose

---

## Uruchomienie lokalne

1. Stwórz środowisko:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
   Aplikacja dostepna pod adresem
  
   http://localhost:8000/docs
   
   
   Uruchomienie za pomoca Docker
   
   
   docker build -t lab03-api .
docker run -d -p 8000:8000 lab03-api

    Przez docker compose 
    
    docker-compose up --build -d
    
    by zatrzymac:
    docker compose down
