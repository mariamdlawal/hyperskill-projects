try:
    def even(x):
        assert x % 2 == 0
        print(x)
except AssertionError as err:
    print(err)
