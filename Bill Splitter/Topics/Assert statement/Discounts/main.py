# standardPrice = int(input())
# discountPrice = int(input())


def discounts(x, y):
    discount = ((x - y) * 100) / x
    assert discount > 50
    return "I will buy it!"


# discounts(standardPrice, discountPrice)
