# Image de base Python legere. On fixe une version precise (pas
# "latest") pour que le comportement soit toujours identique entre
# ton ordinateur, GitHub et Render.
FROM python:3.11-slim

# Dossier de travail a l'interieur du conteneur.
WORKDIR /app

# On copie d'abord uniquement requirements.txt (et pas tout le code)
# pour que Docker puisse reutiliser le cache d'installation des
# dependances si seul le code change ensuite - cela accelere les
# futurs deploiements.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Puis on copie le reste du code de l'application.
COPY app ./app

# Render fournit la variable d'environnement PORT au demarrage.
# On l'utilise directement dans la commande de lancement ci-dessous
# via le shell, pour ne jamais coder un port en dur.
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
