def rotation(a,e):
	b = ""
	d = int(e%26)
	for i in a:
		if  i.isupper():
			c = ord(i)+d
			c = chr(c)
			if c.isupper():
				b+=c
			else:
				z=26-d
				b+=chr(ord(i)-z)
		elif  i.islower():
			c = ord(i)+d
			c = chr(c)
			if c.islower():
				b+=c
			else:
				z=26-d
				b+=chr(ord(i)-z)
		else :
			b+=i
	return b
