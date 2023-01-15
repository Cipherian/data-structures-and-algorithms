import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable



def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected



def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    for item in hashtable._buckets:
        if item:
            actual.append(item)

    expected = [["silent", True], ["listen", "to me"], ["ahmad", 30]]

    assert actual == expected


def test_hash_function_type():
    hashtable = Hashtable(1024)
    key = "test_key"
    assert isinstance(hashtable.hash_function(key), int)


def test_hash_function_size():
    hashtable = Hashtable(1024)
    key = "test_key"
    assert hashtable.hash_function(key) <= hashtable.size


def test_hash_delete_function():
    hashtable = Hashtable(1024)
    key = "test_key"
    value = "test_value"
    hashtable.set(key, value)
    hashtable.delete(key)
    assert hashtable._buckets[hashtable.hash_function(key)] is None
