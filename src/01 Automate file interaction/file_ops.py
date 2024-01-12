''' Analyze input file and group students depending on the exam results: passed ('P') and failed ('F').
    Save the data into two new files.

    Output:
    Two new files:
        testPassedFile.txt contains a list of students that has passed the exam
        testFailedFile.txt contains a list of students that has failed the exam
'''
def read_file(file_path):
    ''' Read file and save data to the new files'''
    test_passed = ".\\src\\01 Automate file interaction\\testPassedFile.txt"
    test_failed =  ".\\src\\01 Automate file interaction\\testFailedFile.txt"
    with open(file_path, 'r', encoding='utf-8') as input_file:
        with open(test_passed, 'w', encoding='utf-8') as output_passed, open(test_failed, 'w', encoding='utf-8') as output_failed:
            for line in input_file:
                # split data in the line on whitespace chars
                if line.split()[2] == 'P':
                    output_passed.write(line)
                else:
                    output_failed.write(line)



if __name__ == '__main__':
    file_path = ".\\src\\01 Automate file interaction\\inputFile.txt"
    read_file(file_path)
