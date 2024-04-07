import datetime
import json

def viewer(filepath, amt):
    new_line = '\n'
    date_entry_pattern = '%Y-%m-%dT%H:%M:%S.%f'
    date_outlet_pattern = '%d.%m.%Y'
    reformed_data = []
    executed_transaction = []
    with open(filepath) as file:
        data = json.loads(file.read())
    for transaction in data:
        if 'state' in transaction.keys():
            if transaction['state'] == 'EXECUTED':
                transaction['datetime'] = datetime.datetime.strptime(transaction['date'], date_entry_pattern)
                executed_transaction.append(transaction)
    executed_transaction.sort(key=lambda x: x['datetime'], reverse=True)
    for transaction in executed_transaction[:amt]:
        regen_trans = {}
        regen_trans['date'] = transaction['datetime'].strftime(date_outlet_pattern)
        if 'from' in transaction.keys():
            p_account_from = [i for i in transaction['from'].split()]
            prefix_from = ' '.join(p_account_from[:-1])
            account_from = p_account_from[-1]
            if account_from.isnumeric() and len(account_from) == 16:
                account_from = f'{account_from[:4]} {account_from[4:6]}** **** {account_from[12:]}'
            else:
                account_from = f'**{account_from[-4:]}'
            data_from = f'{prefix_from} {account_from}'
        else:
            data_from = ''
        if 'to' in transaction.keys():
            p_account_to = [i for i in transaction['to'].split()]
            prefix_to = ' '.join(p_account_to[:-1])
            account_to =p_account_to[-1]
            if account_to.isnumeric() and len(account_to) == 16:
                account_to = f'{account_to[:4]} {account_to[4:6]}** **** {account_to[12:]}'
            else:
                account_to = f'**{account_to[-4:]}'
            data_to = f'{prefix_to} {account_to}'
        else:
            data_to = ''
        regen_trans['from'] = data_from
        regen_trans['to'] = data_to
        regen_trans['transfer_amount'] = f'{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}'
        regen_trans['description'] = transaction['description']
        result = f'{regen_trans["date"]} {regen_trans["description"]}{new_line}{regen_trans["from"]} -> {regen_trans["to"]}{new_line}{regen_trans["transfer_amount"]}{new_line}'
        reformed_data.append(result)
    return reformed_data

