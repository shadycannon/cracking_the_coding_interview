import pytest
from hashtable import HashTable


def test_should_always_pass():
    assert 2 + 2 == 4, 'this is just a dummy test'


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100


def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]


def test_should_insert_key_value_pairs(hashtable: HashTable):
    hashtable["hola"] = "hello"
    hashtable[98.6] = 37
    hashtable[False] = True
    assert "hello" in hashtable.values
    assert 37 in hashtable.values
    assert True in hashtable.values

    assert len(hashtable) == 100


def test_should_get_key_value_pairs(hashtable: HashTable):
    assert 'hello' == hashtable['hola']
    with pytest.raises(KeyError):
        hashtable["missing_key"]


def test_should_get_value(hashtable: HashTable):
    assert hashtable.get("hola") == "hello"


def test_should_get_none_when_missing_key(hashtable: HashTable):
    assert hashtable.get("missing_key") is None


def test_should_get_default_value_when_missing_key(hashtable: HashTable):
    assert hashtable.get("missing_key", "default") == "default"


def test_should_get_value_with_default(hashtable: HashTable):
    assert hashtable.get("hola", "default") == "hello"