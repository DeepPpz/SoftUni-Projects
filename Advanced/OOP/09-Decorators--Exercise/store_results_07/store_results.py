import os

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, 'results.txt')


class store_results:
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args):
        result = self.function(*args)

        with open(file_path, 'a') as result_file:
            result_file.write(f"Function '{self.function.__name__}' was called. Result: {result}\n")


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
