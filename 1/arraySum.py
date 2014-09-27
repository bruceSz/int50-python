def assertIsIterate(x):
    try:
        someObject = iter(x)
    except TypeError,e:
        print x,'is not iterable'

def arrSum(arr):
    assertIsIterate(arr)
    reduce(lambda x,y: x+y,arr)

