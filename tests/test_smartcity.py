import pytest
from project3 import project3

def test_read():
    result = project3.readPdf()
    assert result is None
def test_cityraw():
    result = project3.cityandrawtext()
    assert result is None
