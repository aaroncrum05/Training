import pytest
from working import convert

def test_hourwithzero():

    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5 PM") == "09:30 to 17:00"

def test_badnumber():
    with pytest.raises(ValueError):
        convert ("9:65 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert ("19:35 AM to 12:75 PM")

def test_othercharacters():
    with pytest.raises(ValueError):
        convert ("9 AM - 5 PM")
    with pytest.raises(ValueError):
            convert ("cat AM - doggie PM")



def test_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_noto():
    with pytest.raises(ValueError):
        convert ("5:00 AM 12:00 PM")

def test_toomanynumbers():
    with pytest.raises(ValueError):
        convert ("1111:00 AM to 510:15 PM")

