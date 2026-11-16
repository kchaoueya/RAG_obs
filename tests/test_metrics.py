from src.eval.metrics import recall_at_k, reciprocal_rank, mrr


def test_recall_page_dans_le_top_k():
    assert recall_at_k(["ch6#p17"], ["ch6#p14", "ch6#p17", "ch5#p5"], k=3) == 1.0


def test_recall_page_hors_du_top_k():
    # la bonne page est 3e, mais on ne regarde que les 2 premières
    assert recall_at_k(["ch6#p17"], ["ch6#p14", "ch5#p5", "ch6#p17"], k=2) == 0.0


def test_reciprocal_rank_deuxieme_position():
    assert reciprocal_rank(["ch6#p17"], ["ch6#p14", "ch6#p17"]) == 0.5


def test_reciprocal_rank_page_absente():
    assert reciprocal_rank(["ch6#p17"], ["ch6#p14", "ch5#p5"]) == 0.0


def test_mrr_ignore_hors_corpus():
    attendus  = [["a#p1"], ["b#p2"], []]                  # la 3e question est hors corpus
    recuperes = [["a#p1"], ["x#p9", "b#p2"], ["z#p1"]]
    # scores : 1/1 et 1/2 → moyenne = 0.75 ; la question hors corpus est ignorée
    assert mrr(attendus, recuperes) == 0.75