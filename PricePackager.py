def pricePackager(price, people, itemtype):
    flatMarkupTotal = price*1.05

    personMarkup = flatMarkupTotal * (int(people[0])*0.012)
    #debug
    print('flatMarkupTotal: ', flatMarkupTotal)
    print('personMarkup: ', personMarkup)
pricePackager(1299.99, '3 people', 'food')