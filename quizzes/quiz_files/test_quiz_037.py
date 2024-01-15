# test_quiz_038.py

import pytest
from quiz_037 import Account

def test_empty_account():
    new_account = Account()
    assert new_account.balance == 0
    assert new_account.holder_name == ""
    assert new_account.holder_email == ""
    assert new_account.number == ['000', '00000', '0']
    number = new_account.number
    assert isinstance(number, list)
    assert isinstance(number, list)
    acc_no = new_account.get_account_no().split('-')
    assert len(acc_no) == 3 and len(acc_no[0]) == 3 and len(acc_no[1]) == 5 and len(acc_no[2]) == 1

def test_create_account():
    new_a = Account()
    assert new_a.get_balance() == 0
    assert new_a.set_holder_name(name="Bob") == "Holder's name is Bob"
    assert new_a.set_holder_email(email="bob123@gmail.com") == "Holder's email is bob123@gmail.com"
    assert new_a.deposit(amount=100) == "New balance: 100 USD"