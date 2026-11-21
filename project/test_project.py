import pytest
from project import userlogin, user_choice, too_few_tools


def test_userlogin():

    with pytest.raises(SystemExit):
        userlogin("Tim")
    with pytest.raises(SystemExit):
        userlogin("test_test_test")
    assert userlogin("Brad") == None   #this is a good answer
    assert userlogin("sTeVe") == None  #this is also ok

def test_user_choice():

    with pytest.raises(ValueError):
        user_choice("4")
    with pytest.raises(ValueError):
        user_choice("Cat Dog Fish")

def test_too_few_tools():
    assert too_few_tools(1, 100) == 1
    with pytest.raises(ValueError):
        too_few_tools(100, 1)

