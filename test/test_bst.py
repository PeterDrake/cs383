from bst import BST
import random

def test_adds():
    t = BST()
    assert t.is_empty()
    assert not t.contains(3)
    t.add(3)
    assert not t.is_empty()
    assert t.contains(3)

def test_adds_multiple():
    keys = set(random.randint(1, 10000) for _ in range(100))
    t = BST()
    for k in keys:
        assert not t.contains(k)
        t.add(k)
        assert t.contains(k)
    for k in keys:
        assert t.contains(k)

def test_removes():
    t = BST()
    t.add('cat')
    t.remove('cat')
    assert not t.contains('cat')

def test_removes_multiple():
    t = BST()
    keepers = list(set(random.randint(1, 10000) for _ in range(100)))
    rejects = keepers[:len(keepers) // 2]
    for k in keepers:
        t.add(k)
    for r in rejects:
        t.remove(r)
    for k in keepers:
        assert t.contains(k) == (k not in rejects)
