import unittest
import main
from operator import itemgetter

class TestTasks(unittest.TestCase):

    def test_task1(self):
        input_data = [('Pycharm', 2013, 'Python'), ('CLion', 2014, 'Python'), ('Visual Studio', 1997, 'C++'), ('QT Creator', 1991, 'C++'), ('Vim', 1988, 'C++'), ('Visual Studio Code', 2015, 'Rust')]
        expected_output = sorted(input_data, key=itemgetter(1))
        self.assertEqual(main.task1(input_data), expected_output)

    def test_task2(self):
        input_data = [('Pycharm', 2013, 'Python'), ('CLion', 2014, 'Python'), ('Visual Studio', 1997, 'C++'), ('QT Creator', 1991, 'C++'), ('Vim', 1988, 'C++'), ('Visual Studio Code', 2015, 'Rust')]
        expected_output = [('Rust', 1), ('Python', 2), ('C++', 3)] 
        self.assertEqual(main.task2(input_data), expected_output)

    def test_task3(self):
        input_data = [('Pycharm', 2013, 'Python'), ('CLion', 2014, 'Python'), ('Visual Studio', 1997, 'C++'), ('QT Creator', 1991, 'C++'), ('Vim', 1988, 'C++'), ('Visual Studio Code', 2015, 'Rust')]
        expected_output = [('Pycharm', 'Python'), ('Visual Studio', 'C++'), ('QT Creator', 'C++'), ('Vim', 'C++')]
        self.assertEqual(main.task3(input_data), expected_output)



if __name__ == '__main__':
    unittest.main()
