import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


def test_instantiate():
    assert LinkedList()



def test_empty_head():
    linked = LinkedList()
    assert linked.head is None



def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"



def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NONE"



def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NONE"


def test_linked_list_append():
    linked_list = LinkedList()

    linked_list.append("apple")

    assert str(linked_list) == "{ apple } -> NONE"

def test_linked_list_insert_before():
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert_before(3, 5)

    assert str(linked_list) == '{ 4 } -> { 5 } -> { 3 } -> { 1 } -> NONE'

def test_linked_list_insert_after():
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert_after(2, 4)

    assert str(linked_list) == '{ 3 } -> { 2 } -> { 4 } -> { 1 } -> NONE'

def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NONE"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NONE"



def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def test_linked_list_add_one():
    ll = LinkedList()
    ll.append(9)
    ll.append(9)
    ll.append(9)
    ll.add_one_to_ll()

    assert str(ll) == "{ 1 } -> { 0 } -> { 0 } -> { 0 } -> NONE"


def test_linked_list_add_one_2():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.add_one_to_ll()

    assert str(ll) == "{ 2 } -> { 3 } -> { 5 } -> NONE"
