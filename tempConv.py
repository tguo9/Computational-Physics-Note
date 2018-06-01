''''


'''

def tempConv(C):
	'''
		>>> tempConv(-40) == -40
		True
		>>> tempConv(-300)
		Traceback (most recent call last):
			...
		ValueError: Absolute zero. Crashing...
	'''
	if C < -273.15:
		raise ValueError("Absolute zero. Crashing...")
	F = (9./5)*C+ 32
	return F

if __name__ == "__main__":

    import doctest
    import argparse
    import math

    parser = argparse.ArgumentParser()

    parser.add_argument('-c', type = float)

    args = parser.parse_args()

    c = args.c

    F = tempConv(c)
    print(F)