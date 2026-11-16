J1-Phase0 complète
Remarques:
conteneur → noyau Linux de WSL 2 → Windows

J2-Phase1 complete 
Remarques:
on a fait principalement src/eval/metrics.py qui sert de voir l assiduit=dité du rag a travers la page a chaque question 
parmi les metrique utilisée:
recall@k : verifie si la page est dans les k premiers fichiers 
reciprocal rank : donne la position exxacte de la page juste 
mrr: la moyenne des reciprocal raanks

ausssi on a fait tests/test_metrics.py pour s'assurer de la justessse de metrics.py