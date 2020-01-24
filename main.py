import converter

currency_codes = {'Canadian Dollar':'CAD', 'Hong Kong Dollar':'HKD', 'Iceland Krona':'ISK', 
                  'Philippine Peso':'PHP', 'Danish Krone':'DKK', 'Forint':'HUF', 
                  'Czech Koruna':'CZK', 'Great British Pound':'GBP', 'Romanian Leu':'RON', 
                  'Swedish Krona':'SEK', 'Rupiah':'IDR', 'Indian Rupee':'INR', 'Brazilian Real':'BRL', 
                  'Russian Ruble':'RUB', 'Kuna':'HRK', 'Yen':'JPY', 'Thai Baht':'THB', 'Swiss Franc':'CHF', 
                  'Euro':'EUR', 'Malaysian Ringgit':'MYR', 'Bulgarian Lev':'BGN', 'Turkish Lira':'TRY', 
                  'Yuan Renminbi':'CNY', 'Norwegian Krone':'NOK', 'New Zealand Dollar':'NZD', 'Rand':'ZAR', 
                  'US Dollar':'USD', 'Mexican Peso':'MXN', 'Singapore Dollar':'SGD', 'Singapore Dollar':'AUD', 
                  'New Israeli Sheqel':'ILS', 'Won':'KRW', 'Polish Zloty':'PLN'}



def line_break():
    print("____________________")

def menu():
    print("Menu\nEnter 1 to view currency codes")
    print("Enter 2 to see a base currency compared with all currencies")
    print("Enter 3 to see a base currency compared with a single currency")
    print("Enter 4 to convert an amount from one currency to another")
    print("Enter 'quit' to leave the program")
    line_break()


def interface(response):
    while response.lower() != 'quit':
        if response == '1':
            converter.print_codes(currency_codes)
            line_break()
        
        elif response == '2':
            base = input("Pick your base currency code\n>> ").upper()
            converter.print_all(base)
            line_break()
        
        elif response == '3':
            base = input("Pick your base currency code\n>> ").upper()
            other = input("Pick your other currency code\n>> ").upper()
            converter.print_specfic(base, other)
            line_break()

        elif response == '4':
            base = input("Pick your base currency code\n>> ").upper()
            other = input("Pick your converted to currency code\n>> ").upper()
            amount = float(input("Amount\n>> "))
            converter.convert_amount(amount, base, other)
            line_break()
        
        else:
            print("Function not recognized. Try again.")
            line_break()
        menu()
        response = input(">> ")  

print("Welcome to Nick's Currency Converter!\n")
menu()
response = input(">> ")
interface(response)
