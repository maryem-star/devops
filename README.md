# devops-git-lab

Mini projet pour pratiquer Git dans un workflow DevOps.
Le code est volontairement simple : l'objectif est l'historique Git.

## Contenu

| Fichier | Role |
|---|---|
| `app.py` | Application Python (fonctions hello, add, status) |
| `test_app.py` | Tests unitaires |
| `messages.txt` | Fichier utilise pour provoquer des conflits |
| `config/app.env.example` | Exemple de configuration (ne jamais commiter `.env`) |
| `scripts/deploy.sh` | Faux script de deploiement |
| `.github/workflows/ci.yml` | Pipeline CI GitHub Actions |
| `EXERCICES.md` | Les exercices Git a realiser |

## Demarrage

```bash
git init -b main
git add .
git commit -m "chore: initial commit"
python -m unittest
```

Puis suis `EXERCICES.md` dans l'ordre.
