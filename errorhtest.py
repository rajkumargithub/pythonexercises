print 'Subtraction program, v0.0.3 (beta)'
loop = 1
while loop == 1:
    try:
        a = input('Enter a number to subtract from > ')
        b = input('Enter the number to subtract > ')
    except NameError:
        print "\nYou cannot subtract a letter"
	continue
    except SyntaxError:
        print "\nPlease enter a number only."
	continue
    print a - b
    try:
        loop = input('Press 1 to try again > ')
    except (NameError,SyntaxError):
        loop = 0