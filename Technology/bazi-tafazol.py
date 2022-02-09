def game(number):
    a = int(str(number)[1:])
    b = int(str(number)[:1])
    
    if a > b:
    	sum = a - b
    	return sum
    else:
    	sum = b - a
    	return sum