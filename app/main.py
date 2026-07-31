"""
Point d'entree principal de l'application FastAPI.
En Phase 1, ce fichier ne fait qu'exposer /health.
Les routes /discover, /scrape-match et /historical-recovery/*
seront ajoutees dans les phases suivantes, chacune dans son propre
fichier sous app/routes/, sans jamais toucher a ce fichier plus que
pour ajouter une ligne d'inclusion de routeur.
"""

from fastapi import FastAPI

from app.config import settings
from app.routes import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Chaque nouveau module de routes (discover.py, scrape_match.py...)
# sera ajoute ici de la meme maniere dans les phases suivantes.
app.include_router(health.router)


@app.get("/")
def root():
    """
    Route racine, purement informative. Utile si quelqu'un ouvre
    juste l'URL de base par erreur au lieu de /health.
    """
    return {
        "message": f"{settings.APP_NAME} est en ligne. Consultez /health pour verifier l'etat du service.",
        "version": settings.APP_VERSION,
    }
