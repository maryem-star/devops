# Exercices Git DevOps

Coche chaque exercice une fois termine. Utilise `git log --oneline --graph --all` souvent.
Convention de commits : `feat:` `fix:` `docs:` `chore:` `ci:` `refactor:` `test:`

## Partie 1 - Bases
- [ ] 1. `git init -b main`, configure `user.name` et `user.email`
- [ ] 2. Premier commit de tous les fichiers : `chore: initial commit`
- [ ] 3. Lance `python -m unittest`, puis verifie que `__pycache__` n'apparait pas dans `git status`
- [ ] 4. Modifie `README.md`, regarde `git diff`, puis `git add -p` et commit `docs: ...`

## Partie 2 - Branches
- [ ] 5. `git switch -c feature/greeting` : ajoute un parametre de langue a `hello()` + un test, commit `feat:` puis `test:`
- [ ] 6. Retourne sur `main` et fusionne avec `git merge --no-ff feature/greeting`
- [ ] 7. Supprime la branche : `git branch -d feature/greeting`

## Partie 3 - Conflit
- [ ] 8. Cree `feature/a` : change la ligne 2 de `messages.txt` en "Version A", commit
- [ ] 9. Depuis `main`, cree `feature/b` : change la meme ligne en "Version B", commit
- [ ] 10. Fusionne `feature/a` puis `feature/b` dans `main` -> conflit
- [ ] 11. Resous-le a la main (enleve `<<<<<<<`, `=======`, `>>>>>>>`), `git add`, `git commit`

## Partie 4 - Corriger ses erreurs
- [ ] 12. Fais un commit volontairement faux, annule-le avec `git revert <hash>`
- [ ] 13. Fais un commit, puis `git reset --soft HEAD~1` et recommit proprement
- [ ] 14. `git stash` un travail en cours, change de branche, puis `git stash pop`
- [ ] 15. Cree 3 petits commits puis `git rebase -i HEAD~3` (squash en 1)
- [ ] 16. Cree une branche `feature/x` avec un commit, supprime-la avec `git branch -D`, retrouve-la avec `git reflog` + `git switch -c feature/x <hash>`
- [ ] 17. Cree un commit sur une branche `hotfix`, recupere-le sur `main` avec `git cherry-pick <hash>`
- [ ] 18. `git bisect` : introduis un bug dans `add()` sur un commit, puis retrouve-le avec `git bisect start`, `bad`, `good`, ou `git bisect run python -m unittest`

## Partie 5 - Versioning
- [ ] 19. Mets a jour `CHANGELOG.md`, commit `docs: changelog 1.0.0`
- [ ] 20. `git tag -a v1.0.0 -m "Release 1.0.0"` puis `git tag` et `git show v1.0.0`
- [ ] 21. Lance `./scripts/deploy.sh` et observe la version affichee

## Partie 6 - GitHub et CI
- [ ] 22. Cree un depot vide sur GitHub, `git remote add origin <url>`, `git push -u origin main`
- [ ] 23. `git push origin --tags`
- [ ] 24. Cree `feature/ci-badge`, ajoute un badge dans le README, pousse la branche
- [ ] 25. Ouvre une Pull Request, attends la CI verte, merge
- [ ] 26. Protege `main` (Settings > Branches > Branch protection)
- [ ] 27. `git pull --rebase` apres le merge, puis `git branch -d feature/ci-badge`

## Bonus
- [ ] 28. Hook `.git/hooks/pre-commit` qui lance `python -m unittest` et bloque le commit si les tests echouent
- [ ] 29. Alias : `git config --global alias.lg "log --oneline --graph --all"`
- [ ] 30. Fork + `git remote add upstream` + `git fetch upstream`

## Checklist finale
- [ ] 10+ commits propres
- [ ] 1 merge `--no-ff`, 1 conflit resolu
- [ ] 1 revert, 1 cherry-pick, 1 rebase -i, 1 reflog, 1 bisect
- [ ] Tag `v1.0.0`
- [ ] 1 PR mergee avec CI verte
