import unittest
import re
import os.path


#Tests are based on input file and output file, which is the result of run of application

class Tests(unittest.TestCase):

    #test if input file exists
    def test_file_input(self):
        assert os.path.exists('dane_wejsciowe.txt')

    #test if output file exists
    def test_file_output(self):
        assert os.path.exists('wynik.txt')

    #test if numbers in pairs did not repeat
    def test_no_repeat(self):
        with open('dane_wejsciowe.txt') as f:
            start_list_input = [line.rstrip() for line in f]
            final_list_input = [int(x) for x in start_list_input]
        f.close()
        dict_input = dict((x, final_list_input.count(x)) for x in set(final_list_input))

        final_list_output = []
        with open('wynik.txt', 'r') as f:
            for line in f:
                start_list_output = line.strip()
                s = [int(s) for s in re.findall(r'-?\d+\.?\d*', start_list_output)]
                final_list_output.extend(s)
        f.close()
        dict_output = dict((x, final_list_output.count(x)) for x in set(final_list_output))

        check = []
        for key_input, value_input in dict_input.items():
            for key_output, value_output in dict_output.items():
                if (key_input == key_output and value_input >= value_output):
                    check.append(True)
                elif (key_input == key_output and value_input < value_output):
                    check.append(False)
                else:
                    pass

        assert all(check)

    #test if sum of pair is equal to 12
    def test_are_correct_pairs(self):
        with open('wynik.txt', 'r') as f:
            for line in f:
                abc = line.strip()
                the_sum = [int(s) for s in re.findall(r'-?\d+\.?\d*', abc)]
                assert sum(the_sum) == 12
if __name__ == '__main__':
    unittest.main()
