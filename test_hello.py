from hello import toyou, add, subtract

def setup_function(function):
	print ("Running Setup: %s" % function.__name__)
	function.x = 10

def teardowm_function(function):
	print ("Running Teardowm: %s" % function.__name__)
	del function.x

#Will cause an assert error
def test_hello_add():
	assert add (test_hello_add.x) == 12

def test_hello_subtract():
	assert subtract (test_hello_subtract.x) == 9

