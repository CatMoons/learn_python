import pytest

from src.masks import get_mask_account

def test_get_mask_account_valid_input():
    '''
    проверяет стандартный случай.
    :return:
    '''
    account_number = "123456789012"
    expected_output = "9012"
    assert get_mask_account(account_number) == expected_output

def test_get_mask_account_short_input():
    '''
    проверяет случай, когда номер счета чуть длиннее 4 символов.
    :return:
    '''
    account_number = "98765"
    expected_output = "8765"
    assert get_mask_account(account_number) == expected_output

def test_get_mask_account_exact_four_digits():
    '''
    проверяет случай, когда номер счета состоит ровно из 4 символов.
    :return:
    '''
    account_number = "4321"
    expected_output = "4321"
    assert get_mask_account(account_number) == expected_output

def test_get_mask_account_less_than_four_digits():
    '''
    проверяет случай, когда номер счета содержит меньше 4 символов.
    :return:
    '''
    account_number = "12"
    expected_output = "12"
    assert get_mask_account(account_number) == expected_output

def test_get_mask_account_empty_input():
    '''
    проверяет случай, когда номер счета пустой.
    :return:
    '''
    account_number = ""
    expected_output = ""
    assert get_mask_account(account_number) == expected_output
