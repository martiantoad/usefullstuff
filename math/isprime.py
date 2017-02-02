def main(number):
    for x in range(3, int(number**0.5)+1, 2):
        if number % x == 0:
            print 'false'
        else:
            print 'true'
