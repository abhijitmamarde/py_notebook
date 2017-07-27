class MessageLengthError(Exception):

	def __init__(self, msg):
		super().__init__(msg)

def hello(msg):
	if len(msg) < 3:
		# raise Exception("Length of msg should be >= 3")
		raise MessageLengthError("Length of msg should be >= 3")
	print("Hello " + msg)

hello("world")
obj = 123

try:
	hello(obj)
except TypeError as err:
	print("Error occured, handled...")
	hello(str(obj))

obj = "hi"
try:
	hello(obj)
# except TypeError as err:
# 	print("Error occured, handled...")
# 	hello(str(obj))
# except MessageLengthError as err:
# 	print("MessageLengthError occured:", err)
except Exception as err:
	print("Exception occured:", err)
else:
	print("After try - 1")
finally:
	print("Ok done, this part! - 1")



obj = "hey there"
try:
	hello(obj)
except TypeError as err:
	print("Error occured, handled...")
	hello(str(obj))
except Exception as err:
	print("Exception occured:", err)
else:
	print("After try - 2")
finally:
	print("Ok done, this part! - 2")


print("Last line of prgoram")