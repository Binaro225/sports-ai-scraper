"""
Route /health : permet de verifier rapidement que le service Render
est en vie et repond. C'est la toute premiere chose a tester apres
chaque deploiement, avant de toucher a quoi que ce soit d'autre.
"""

from datetime import datetime, timezone

from fastapi import APIRouter

from app.config import settings

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Reponse attendue :
    {
        "status": "ok",
        "service": "Sports AI Scraper",
        "version": "0.1.0",
        "environment": "production",
        "timestamp": "2026-07-30T12:34:56.789012+00:00"
    }
    """
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
