def pricePackager(price, people, itemType):
    #flat markup total
    flatMarkupTotal = price*1.05
    #person markup total
    personMarkup = flatMarkupTotal * (int(people[0])*0.012)
    #type markups and total
    typeMarkups = {'pharmaceutical': .075, "food": 0.13, "electronics": .02} 
    typeMarkup = 0
    for item in typeMarkups:
        if item == itemType:
            typeMarkup = typeMarkups[item]
            break
    typeMarkupPrice = flatMarkupTotal * typeMarkup
    #debug
    print('flatMarkupTotal: ', flatMarkupTotal)
    print('personMarkup: ', personMarkup)
    print('typeMarkupPrice: ', typeMarkupPrice)
pricePackager(1299.99, '3 people', 'food')