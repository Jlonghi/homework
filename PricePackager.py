import re
def pricePackager(price, people, itemType):
    reg = re.compile('[0-9]+ (person|people)')
    if price <= 0:
        raise ValueError('Price must be greater than 0')
    if reg.match(people) is None:
        raise ValueError('argument must be number of people e.g 1 person or 10 people')

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

    #calculating and rounding final total
    return round(flatMarkupTotal + personMarkup + typeMarkupPrice,2)