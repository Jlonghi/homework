import re

#flat markup
fMarkup = 0.05
#people markup
pMarkup = 0.012
#type markups
typeMarkups = {'pharmaceutical': .075, "food": 0.13, "electronics": .02} 

def pricePackager(price, people, itemType):
    """
    Price Packager takes a price and adds a markup to it specified by the parameters
    
    Parameters
    ----------
    price : float
        the price to be marked up
    people : string
        the amount of people who worked on an item
    itemType: string
        the items type
    
    Returns
    -------
    float
        a marked up price rounded to two decimals
    
    Raises
    ------
    ValueError
        when price is <=0 or when people is negative or entered incorrectly
    """
    reg = re.compile('[0-9]+ (person|people)')
    if price <= 0:
        raise ValueError('Price must be greater than 0')
    if reg.match(people) is None or people[0] < 0:
        raise ValueError('argument must be number of people e.g 1 person or 10 people and positive')

    #flat markup total
    flatMarkupTotal = price*(1 + fMarkup)

    #person markup total
    personMarkup = flatMarkupTotal * (int(people[0])*pMarkup)

    #type markups total
    typeMarkup = 0
    for item in typeMarkups:
        if item == itemType:
            typeMarkup = typeMarkups[item]
            break
    typeMarkupPrice = flatMarkupTotal * typeMarkup

    #calculating and rounding final total
    return round(flatMarkupTotal + personMarkup + typeMarkupPrice,2)