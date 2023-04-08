from kitten import winner


def test_no_defuses():
    assert winner("Kamil", "Daniel", 0, 0) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 0) == "Kamil"


def test_player1_has_defuse():
    assert winner("Kamil", "Daniel", 1, 0) == "Kamil"
    assert winner("Daniel", "Kamil", 1, 0) == "Daniel"


def test_player2_also_has_defuse():
    assert winner("Kamil", "Daniel", 1, 1) == "Daniel"
    assert winner("Daniel", "Kamil", 1, 1) == "Kamil"


def test_player2_only_has_defuse():
    assert winner("Kamil", "Daniel", 0, 1) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 1) == "Kamil"


def test_player1_has_two_defuses():
    assert winner("Kamil", "Daniel", 2, 1) == "Kamil"
    assert winner("Daniel", "Kamil", 2, 1) == "Daniel"


def test_player2_has_two_defuses():
    assert winner("Kamil", "Daniel", 1, 2) == "Daniel"
    assert winner("Daniel", "Kamil", 1, 2) == "Kamil"


def test_players_have_two_defuses():
    assert winner("Kamil", "Daniel", 2, 2) == "Daniel"
    assert winner("Daniel", "Kamil", 2, 2) == "Kamil"
