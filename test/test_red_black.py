from red_black import RedBlackBST
import random


def test_adds():
    t = RedBlackBST()
    assert t.is_empty()
    assert not t.contains(3)
    t.add(3)
    assert not t.is_empty()
    assert t.contains(3)


def test_adds_multiple():
    keys = set(random.randint(1, 10000) for _ in range(100))
    t = RedBlackBST()
    for k in keys:
        assert not t.contains(k)
        t.add(k)
        assert t.contains(k)
    for k in keys:
        assert t.contains(k)
