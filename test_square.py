import pytest
import math

@pytest.mark.square
def test_sqrt():
	num = 25
	assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
	num = 7
	try:
		assert 7*7 == 40
	except:
		print ('Assert error')
	assert 7*7 == 49

@pytest.mark.others
def test_equality():
   assert 10 == 10



#testsquare()
