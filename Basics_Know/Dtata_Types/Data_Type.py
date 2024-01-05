x = "Hello World"	                   # str	
y = 20	                                 #int	
z = 20.5	                             #float	
a = 1j	                                 #complex	
b = ["apple", "banana", "cherry"]	     #list	
c = ("apple", "banana", "cherry")	     #tuple	
d = range(6)	                         #range	
e = {"name" : "John", "age" : 36}	     #dict	
f = {"apple", "banana", "cherry"}	    #set	
g = frozenset({"apple", "banana", "cherry"})	#frozenset	
h = True	                            #bool	
i = b"Hello"	                        #bytes	
j = bytearray(5)	                    #bytearray	
k = memoryview(bytes(5))	            #memoryview	
l = None	                            #NoneType	
print(x,y,z,a,b,c,d,e,f,g,h,i,j,k,l)

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	Data Type	Try it
x = str("Hello World")	                    #str	
a = int(20)	                                #int	
b = float(20.5)                             #float	
c = complex(1j)	                            #complex	
d = list(("apple", "banana", "cherry"))	     #list	
e  = tuple(("apple", "banana", "cherry"))	   #tuple	
f = range(6)	                                # range	
g = dict(name="John", age=36)	               #dict	
h = set(("apple", "banana", "cherry"))	       #set	
i= frozenset(("apple", "banana", "cherry"))	#frozenset	
j = bool(5)	                                      #  bool	
k = bytes(5)	                                  #  bytes	
i = bytearray(5)	                              #bytearray	
j = memoryview(bytes(5))	                      #memoryview	
print(x,y,z,a,b,c,d,e,f,g,h,i,)