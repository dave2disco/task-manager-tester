# Immagine base: Python 3.13 leggera
FROM python:3.13-slim

# Cartella di lavoro dentro il container
WORKDIR /app

# Copia prima requirements.txt e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del progetto
COPY . .

# Espone la porta 5000 (quella di Flask)
EXPOSE 5000

# Comando di avvio
CMD ["python", "main.py"]