def recall_at_k(attendus: list[str], recuperes: list[str], k: int) -> float:
    """1.0 si au moins une page attendue est dans les k premières pages récupérées, sinon 0.0."""
    top_k = recuperes[:k]
    for page in attendus:
        if page in top_k:
            return 1.0
    return 0.0


def reciprocal_rank(attendus: list[str], recuperes: list[str]) -> float:
    """1/rang de la première page récupérée qui fait partie des attendues, 0.0 si aucune."""
    for rang, page in enumerate(recuperes, start=1):
        if page in attendus:
            return 1.0 / rang
    return 0.0


def mrr(liste_attendus: list[list[str]], liste_recuperes: list[list[str]]) -> float:
    """Moyenne des reciprocal ranks sur plusieurs questions (hors corpus exclues)."""
    scores = []
    for attendus, recuperes in zip(liste_attendus, liste_recuperes):
        if not attendus:          # question hors corpus : rien à trouver, on l'ignore
            continue
        scores.append(reciprocal_rank(attendus, recuperes))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)