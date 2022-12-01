# terms = 35
# a = 0
# b = 1
# count = 0
# while count < terms:
#     c = a + b
#     a = b
#     b = c
#     count += 1
#     print("{:2} -  {:9,}".format(terms,a))

terms=35
a=0
b=1
count=0
def rec_fibonacci(terms,a,b,count):
    if count < terms:
        c = a + b
        a = b
        b = c
        count += 1
        print("{:2} -  {:9,}".format(terms,a))
        rec_fibonacci(terms,a,b,count)
rec_fibonacci(terms,a,b,count)