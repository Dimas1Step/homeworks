import time
import unittest

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
def test_func_1():
    time.sleep(1)
    return "Done"

def test_func_2(x, y):
    time.sleep(2)
    return x + y

def test_func_3(n):
    total = 0
    for i in range(n):
        total += i
    return total

class TestMeasureTime(unittest.TestCase):

    def test_test_func_1(self):
        result, exec_time = measure_time(test_func_1)
        self.assertEqual(result, "Done")
        self.assertTrue(exec_time >= 1)

    def test_test_func_2(self):
        result, exec_time = measure_time(test_func_2, 3, 4)
        self.assertEqual(result, 7)
        self.assertTrue(exec_time >= 2)

    def test_test_func_3(self):
        n = 1000000
        result, exec_time = measure_time(test_func_3, n)
        self.assertEqual(result, sum(range(n)))
        self.assertTrue(exec_time > 0)

if __name__ == '__main__':
    unittest.main()