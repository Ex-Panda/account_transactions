from functions import reading_json, performed_operation, date_format, list_reversal, masking_card_number, \
    masking_account_number

list_performed_operations = []
count_operations = 0
operation_list_python = reading_json()

# перебор списка словарей, замена по ключу и добавление в новый список измененных словарей
for dictionary in operation_list_python:
    if dictionary != dict() and performed_operation(dictionary["state"]):
        dictionary["date"] = date_format(dictionary["date"])
        if "from" in dictionary.keys():
            dictionary["from"] = masking_card_number(dictionary["from"])
        dictionary["to"] = masking_account_number(dictionary["to"])
        list_performed_operations.append(dictionary)

# сортирует список по дате
list_performed_operations.sort(key=list_reversal, reverse=True)


for dictionary in list_performed_operations:
    count_operations += 1
    if "from" in dictionary.keys():
        print(f"""{dictionary["date"]} {dictionary["description"]}
{dictionary["from"]} -> {dictionary["to"]}
{dictionary["operationAmount"]["amount"]} {dictionary["operationAmount"]["currency"]["name"]}
""")
    else:
        print(f"""{dictionary["date"]} {dictionary["description"]}
{dictionary["to"]}
{dictionary["operationAmount"]["amount"]} {dictionary["operationAmount"]["currency"]["name"]}
""")
    if count_operations == 5:
        break
