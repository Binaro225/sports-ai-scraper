"""
Configuration centralisee du service.
Toutes les valeurs sensibles (secrets, cles API) doivent venir des
variables d'environnement Render, JAMAIS ecrites en dur dans le code.
"""

import os


class Settings:
    # Nom affiche dans les reponses /health, utile pour verifier
    # rapidement quelle version du service tourne.
    APP_NAME: str = "Sports AI Scraper"
    APP_VERSION: str = "0.1.0"

    # Secret partage entre Google Apps Script et ce service.
    # Sera utilise a partir de la Phase 2 pour proteger /discover et
    # /scrape-match. Pour l'instant, /health reste public (pas besoin
    # de secret pour verifier que le service est en vie).
    SCRAPER_API_SECRET: str = os.environ.get("SCRAPER_API_SECRET", "")

    # Port d'ecoute. Render fournit automatiquement la variable
    # d'environnement PORT - on ne doit JAMAIS coder un port fixe
    # comme 8000, sinon Render ne pourra pas router le trafic vers
    # le service.
    PORT: int = int(os.environ.get("PORT", 8000))

    # Environnement d'execution (utile plus tard pour activer/
    # desactiver des logs de debug).
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "production")


settings = Settings()
