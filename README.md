# sports-ai-scraper
# Sports AI Scraper

Service backend de scraping pour l'application SPORTS AI ANALYZER.

## Statut actuel

Phase 1 : squelette FastAPI minimal. Une seule route disponible :

- `GET /health` : verifie que le service est en ligne.

Les routes de scraping (`/discover`, `/scrape-match`) et le moteur de
recuperation historique (`/historical-recovery/*`) seront ajoutes dans
les phases suivantes.

## Lancer en local (optionnel, non obligatoire pour deployer)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Puis ouvrir : http://127.0.0.1:8000/health

## Deploiement

Ce service est deploye automatiquement sur Render a chaque `git push`
sur la branche `main`, via le fichier `render.yaml`.

## Variables d'environnement

| Nom | Description | Obligatoire |
|---|---|---|
| `SCRAPER_API_SECRET` | Secret partage avec Google Apps Script | Oui (Phase 2+) |
| `PORT` | Fourni automatiquement par Render | Automatique |
| `ENVIRONMENT` | `production` ou `development` | Non (defaut: production) |
