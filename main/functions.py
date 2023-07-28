from datetime import date
import json


def reading_json():
    with open('operation.json', 'r', encoding='utf-8') as operation_list:
        operation_list_python = json.load(operation_list)

    return operation_list_python


def performed_operation(state):
    """проверяет выполнена ли операция"""
    if state == "EXECUTED":
        return True
    else:
        return False


def date_format(date_str):
    """переводит дату в удобный формат"""
    date_time_list = date_str.split('T')
    del date_time_list[1]
    date_not_time_str = ''.join(date_time_list)
    thedate = date.fromisoformat(date_not_time_str)
    year = thedate.year
    month = thedate.month
    day = thedate.day
    date_form = date(year, month, day)
    date_formatted = date_form.strftime("%d %m %Y")
    date_formatted_1 = date_formatted.replace(' ', '.')
    return date_formatted_1


def list_reversal(lists):
    """разворачивает дату в формат ГГ.ММ.ДД"""
    lists_data = lists['date'].split('.')
    date_formatted = f"{lists_data[2]}.{lists_data[1]}.{lists_data[0]}"
    return date_formatted


def masking_card_number(card):
    """маскирует номер карты"""
    lists = card.split(" ")
    card_count_world = len(lists)
    if card_count_world == 3:
        world = f'{lists[0]} {lists[1]}'
    elif card_count_world == 2:
        world = f'{lists[0]}'

    card_list = lists[-1]
    card_lists = list(card_list)
    num_card = [card_lists[i:i + 4] for i in range(0, len(card_lists), 4)]

    list_num = []
    for num in num_card:
        num_card_1 = ''.join(num)
        list_num.append(num_card_1)

    list_nums_card = ' '.join(list_num)

    masking_number = list_nums_card.replace(list_nums_card[7:-4], '** **** ')

    return f"{world} {masking_number}"


def masking_account_number(number):
    """маскирует номер счета"""
    "Счет 21969751544412966366"
    lists = number.split(" ")
    count_world = len(lists)
    if count_world == 3:
        world = f'{lists[0]} {lists[1]}'
    elif count_world == 2:
        world = f'{lists[0]}'

    number_list = lists[-1]
    num_score = number_list[-6:]
    masking_num = num_score.replace(num_score[0:2], "**")

    return f"{world} {masking_num}"
