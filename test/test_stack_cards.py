from kitten import winner


def test_one_defuse_in_stack_explode_last():
    assert winner("Kamil", "Daniel", 0, 0, ["explode", "defuse"]) == "Kamil"
    assert winner("Daniel", "Kamil", 0, 0, ["explode", "defuse"]) == "Daniel"


def test_one_defuse_in_stack_explode_first():
    assert winner("Kamil", "Daniel", 0, 0, ["defuse", "explode"]) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 0, ["defuse", "explode"]) == "Kamil"
