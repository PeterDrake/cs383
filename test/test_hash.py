from hash import ChainedHashSet


def test_adds():
    t = ChainedHashSet(10)
    assert not t.contains(5)
    t.add(5)
    assert t.contains(5)


def test_removes():
    t = ChainedHashSet(10)
    t.add(2)
    t.remove(2)
    assert not t.contains(2)


def test_multiple_addition_does_not_interfere_with_removal():
    t = ChainedHashSet(10)
    t.add(3)
    t.add(3)
    t.remove(3)
    assert not t.contains(3)


def test_can_store_more_keys_than_table_size():
    t = ChainedHashSet(10)
    for i in range(20):
        t.add(i)
    for i in range(5, 10):
        t.remove(i)
    for i in range(5):
        assert t.contains(i)
    for i in range(5, 10):
        assert not t.contains(i)
    for i in range(10, 20):
        assert t.contains(i)
