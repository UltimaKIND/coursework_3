from utils import functions as func

file = 'operations.json'
amount = 5

re_data = func.viewer(file, amount)
for i in re_data:
    print(i)

