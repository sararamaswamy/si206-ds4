import unittest
# function to return the factorial of a number
# Add comments
def factorial(num):
    ans = 1
    if num < 0:
        return None
    elif num < 2:
        return ans
    else:
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                isLeap = True
        else:
            isLeap = True
    return isLeap

print("factorial(0): {}".format(factorial(0)))
print("factorial(1): {}".format(factorial(1)))
print("factorial(5): {}".format(factorial(5)))
print("factorial(-3): {}".format(factorial(-3)))

print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))

class ClassTests(unittest.TestCase):
    def test_factorial_type(self):
        ## Test that the return type is int
        type_int = 2
        self.assertEqual(type(factorial(2)), type(type_int))
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
        ## Test that return len is 1
    def test_factorial_neg_5(self):
        self.assertEqual(factorial(-5), None)
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)
    
   

unittest.main(verbosity=2) 