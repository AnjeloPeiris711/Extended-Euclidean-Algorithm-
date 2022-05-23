#Warning: this version can't handle b=0. See extendedeuclideanalgorithm.com/code for a version that can.
import math
def gcd_iterative(a, b):
   """ Calculating the greatest common divisor 
   using the Euclidean Algorithm (non-recursive) 
   (Source: extendedeuclideanalgorithm.com/code) 
   """
  
   #Set default values for the quotient and the remainder
   q = 0
   r = 1
   '''
   In each iteration of the loop below, we
   calculate the new quotient, remainder, a and b.
   r decreases, so we stop when r = 0 
   '''
   while(b > 0):
      #The calculations
      q = math.floor(a/b)
      r = a - q * b
      #The values for the next iteration
      a = b
      b = r
      try:
        print("\n{}=({})*{}+{}".format(a,b,math.floor(a/b),a -(math.floor(a/b)) * b))
      except ZeroDivisionError:
         print("ZeroDivision")
   #return abs(a)
   #print(abs(a))
def xgcd_nonrecursive(a, b):
	""" Calculates the gcd and Bezout coefficients, 
	using the Extended Euclidean Algorithm (non-recursive).
	(Source: extendedeuclideanalgorithm.com/code) 
	"""
	x=a
	y=b
	#Set default values for the quotient, remainder, 
	#s-variables and t-variables
	q = 0
	r = 1
	s1 = 1 
	s2 = 0
	s3 = 1 
	t1 = 0 
	t2 = 1
	t3 = 0
	'''
	In each iteration of the loop below, we
	calculate the new quotient, remainder, a, b,
	and the new s-variables and t-variables.
	r decreases, so we stop when r = 0
	'''
	while(r > 0):
		#The calculations
		q = math.floor(a/b)
		r = a - q * b
		s3 = s1 - q * s2
		t3 = t1 - q * t2
		#print(t3)
		'''
		The values for the next iteration, 
		(but only if there is a next iteration)
		'''
		#print("\n{}*({}) {}*({})=1".format(q,s2,s3,t2))
		#print("\n{}*({}) {}*({})=1".format(q * s2 -s1,t2,t3,s2))
		#print("\n{}*({}) {}*({})=1".format(q * s2 -s1,t2,s2,(-t3)))
		if(t3 > 0):
		   n = t3
		else:
                   n = -t3
		m=q * s2 -s1
		if(m<0):
			m=-m
		if(n&t2!=0):
			print("\n{}*({}) {}*({})=1".format(m,t2,s2,n))
		if(r > 0):
			a = b
			b = r
			s1 = s2
			s2 = s3
			t1 = t2
			t2 = t3
	#return abs(b), s2, t2
	print("equation:{}={}*({}) {}*({})".format(abs(b), s2, x, t2, y))
value=int(input("""
        If you want Euclidean Algorithm press 1
        If you want Extended Euclidean Algorithm press 2
        If you want All press 3
:"""))
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if value==1:
    gcd_iterative(a,b)
elif value==2:
  xgcd_nonrecursive(a,b)
elif value==3:
    print("\nEuclidean Algorithm")
    gcd_iterative(a,b)
    print("\nExtended Euclidean Algorithm")
    xgcd_nonrecursive(a,b)
