import requests

SOURCE = "https://api.exchangeratesapi.io/latest?"

def print_all(base):
    source = SOURCE + f"base={base}"
    data = requests.get(source).json()
    for key, value in data['rates'].items():
        print(key + " rate: " + str(round(value,4)))
        
def print_specfic(currency1, currency2):
    source = SOURCE + f"base={currency1}&symbols={currency2}"
    data = requests.get(source).json()
    print(str(round(data['rates'][currency2],4)) + f" {currency2} to 1 {currency1}")


def convert_amount(amount, currency1, currency2):
    source = SOURCE + f"base={currency1}&symbols={currency2}"
    data = requests.get(source).json()
    rate = data['rates'][currency2]
    converted_amount = str(round(amount*rate, 2))
    print(f"Converted Amount: {currency2} " + converted_amount)

def print_codes(codes):
    for key, value in codes.items():
        print(f"Currency: {key} | Code: {value}")

