import pytest
from sorting import sort_by_title, sort_by_year
from movies import movies

def test_sort_by_year():
    # Expected test output of test #1
    expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento",
                 "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

    assert sort_by_year(movies) == expected1

def test_sort_by_title():
    # Expected test output of test #2
    expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento",
                 "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];
    assert sort_by_title(movies) == expected2




