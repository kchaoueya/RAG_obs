# RAG LLMOps — un assistant RAG observable et évalué en continu

Assistant qui répond à des questions sur un corpus de cours en citant ses sources.
Chaque version est notée automatiquement, chaque requête est tracée,
et une version moins bonne ne peut pas être déployée.

> 🚧 Projet en cours — Phase 0 : mise en place de l'environnement.

## Objectifs
- Mesurer la qualité du RAG (retrieval et génération) sur un jeu de référence
- Tracer chaque requête : passages récupérés, tokens, latence
- Déployer dans le cloud avec un pipeline CI/CD qui bloque toute régression

## Règle de budget
**0 $, aucune carte bancaire.** Tous les services utilisés ont une offre gratuite
(Gemini ou Groq, Langfuse, Qdrant Cloud, Render, GitHub Actions).

## Stack
Python 3.13 · FastAPI · fastembed · Chroma puis Qdrant · Ragas · Langfuse · Docker · Render · GitHub Actions

## Installation (Windows)
```powershell
git clone https://github.com/kchaoueya/rag-llmops.git
cd rag-llmops
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env    # puis remplir les clés dans .env
```

## Données
Placer les documents PDF du corpus dans `data/raw/` (non versionné).

## Avancement
- [x] Phase 0 — Environnement
- [ ] Phase 1 — Jeu de référence et métriques
- [ ] Phase 2 — RAG de base
- [ ] Phase 3 — Évaluation automatique
- [ ] Phase 4 — Observabilité
- [ ] Phase 5 — Expérimentations
- [ ] Phase 6 — Docker et déploiement
- [ ] Phase 7 — CI/CD avec quality gate