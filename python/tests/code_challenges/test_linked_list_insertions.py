import pytest
import inspect
from data_structures.linked_list import LinkedList, TargetError, DoublyLinkedList


def test_double_list_static():
    linked_list = DoublyLinkedList()
    is_static = isinstance(inspect.getattr_static(linked_list, "list_print"), staticmethod)
    assert is_static == True

def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NONE"



def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NONE"



def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NONE"



def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NONE"



def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")



def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")



def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")



def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")
