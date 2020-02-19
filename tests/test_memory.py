from inferkit.memory import ConversationMemory


def test_bounded_window():
    mem = ConversationMemory(max_messages=2)
    mem.add_user("one")
    mem.add_user("two")
    mem.add_user("three")
    assert len(mem) == 2


def test_clear():
    mem = ConversationMemory()
    mem.add_user("one")
    mem.clear()
    assert len(mem) == 0
