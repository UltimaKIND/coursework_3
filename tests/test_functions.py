from utils import functions as func

expected_result = ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']

def test_viewer():
    assert func.viewer('test_data.json', 5) == expected_result
