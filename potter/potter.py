price_per_book = 8
discount_per_set_item = .05
discounts = {
    1: 0,
    2: .05,
    3: .10,
    4: .20,
    5: .25
}

def price(book_numbers):
    sets = []
    print 'now {0}'.format(book_numbers)
    for book in book_numbers:
        stored = False
        for set in filter(lambda (set): len(set) == 3, sets):
            if not book in set:
                set.add(book)
                stored = True
                break;
        if not stored:
            for set in sets:
                if not book in set:
                    set.add(book)
                    stored = True
                    break;
        if not stored:
            sets.append({book})
    price = 0
    for set in sets:
        print set
        discount = 1-(discounts[len(set)])
        print discount
        price += len(set) * price_per_book * discount

    return price