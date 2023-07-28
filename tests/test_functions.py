from main import functions


def test_performed_operation():
    assert functions.performed_operation("EXECUTED") == True
    assert functions.performed_operation("CANCELED") == False


def test_date_format():
    assert functions.date_format("2018-09-12T21:27:25.241689") == '12.09.2018'
    assert functions.date_format("2019-09-11T17:30:34.445824") == '11.09.2019'


def test_masking_card_number():
    assert functions.masking_card_number("Счет 44812258784861134719") == "Счет 4481 22** **** 4719"
    assert functions.masking_card_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_masking_account_number():
    assert functions.masking_account_number("Visa Platinum 8990922113665229") == "Visa Platinum **5229"
    assert functions.masking_account_number("Счет 38976430693692818358") == "Счет **8358"
