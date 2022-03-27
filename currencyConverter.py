import json
import requests


def initiation():  # create the initial json save file
    with open("Currencies.json", 'w') as initialJson:
        json.dump({
            "Currencies": [

            ]
        }, initialJson)


def prompt(value) -> str:  # prompts the user for an input
    return input(f'Enter the {value}: ')


def rates(currency, exchange):  # gets the USD and EUR rates from floatrates.com
    rate = json.loads(requests.get(f'http://www.floatrates.com/daily/{currency}.json').text)
    return rate[f'{exchange}']['rate']


def save(rateName, rate):  # cashes the rates in currencies.txt

    with open('Currencies.json') as jsonFile:
        data = json.load(jsonFile)
        temp = data['Currencies']
        y = {f'{rateName}': rate}
        temp.append(y)
    with open("Currencies.json", 'w') as f:
        json.dump(data, f, indent=4)


def cacheChecker(currency):
    print('Checking the cache...')
    with open("Currencies.json") as f:
        currencies = json.load(f)
        alreadySaved = False
        for x in currencies["Currencies"]:
            if str(currency) in x:
                alreadySaved = True
                break
        if alreadySaved:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
    return alreadySaved


def output(exchange, amount):
    with open('Currencies.json') as f:
        currencies = json.load(f)
        for x in currencies['Currencies']:
            if str(exchange) in x:
                print(f'You received {round(amount * list(dict.values(x))[0], 2)} {exchange.upper()}.')
                break


def main():
    if currency != 'usd':
        usdRate = rates(currency, 'usd')
        save('usd', usdRate)
    if currency != 'eur':
        eurRate = rates(currency, 'eur')
        save('eur', eurRate)
    exchange = prompt('currency you want to exchange for').lower()
    if exchange == '':
        exit()
    amount = eval(prompt('amount you want to exchange'))
    cached = cacheChecker(exchange)

    if cached:
        output(exchange, amount)
    else:
        rate = rates(currency, exchange)
        save(exchange, rate)
        output(exchange, amount)
    main()


initiation()
currency = prompt('currency that you have').lower()
main()
