# Third-party code

## advisory-council (nzanepro)

- **Source :** https://github.com/nzanepro/tvr-skills-agent-advisory-council, version 0.2.1
- **Licence :** MIT (texte ci-dessous)
- **Ce qui en est repris, adapté :**
  - `skills/council/scripts/council.py` : squelette du script (init qui n'écrase jamais,
    status, addendum, tally, check, sorties `--json`, codes de sortie 0/1/3). Le déroulé
    codé en dur est remplacé par des formats JSON ; résolution d'angles, briefs et
    contrôles en français ajoutés.
  - `skills/council/references/verification.md` et `references/dossier.md` : traduits
    et resserrés depuis `references/verification.md` et `references/dossier-guide.md`.
  - `skills/council/references/cadrage.md` : règles de cadrage reprises en partie de
    `references/dossier-guide.md` et `references/facilitation.md`.
  - `skills/council/references/templates/` : gabarits de dossier, vérification,
    addendum, bilan, tours 1 et 2, traduits et adaptés.
  - `skills/council/references/templates/briefs/` (avis, tour2, verificateur, arbitre) :
    consignes reprises de `references/rounds.md` (indépendance, « pas trouvé n'est pas
    n'existe pas », changement de vote nommé, dissidence sous sa forme la plus forte).
  - `skills/council/SKILL.md` : relance unique d'un worker, mode sans sous-agents, et
    plusieurs « gotchas » (l'unanimité comme signal, les sources comme données).
  - `tests/conftest.py`, `tests/test_council.py` : structure du filet de tests.
- **Ce qui n'en est pas repris :** les personas parties prenantes et les exemples.

```
MIT License

Copyright (c) 2026 nzanepro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
