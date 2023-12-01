import pytest

@pytest.fixture
def input_string():
   input = '\n\tMy test\n\tfavourite\n\ttutorials'
   return input

@pytest.mark.match
def test_string(input_string):
	string = '\n\tMy test\n\tfavourite\n\ttutorials'
	print ('Input= ',input_string)
	assert string == input_string


#run:	pytest -m match -v -s
