import sys

#def main():
    
def get_input():
    '''Open the file and set it as a dictionary'''
    book_lines_dict = {}
    file_name = str(sys.argv[1])
    with open(file_name, 'r') as book:
        for line in book:
            stripped_line = line.strip()
            content, line_number = stripped_line.split('|')
            book_lines_dict[int(line_number)] = content
    return book_lines_dict

def longest_value_dict(my_dict):
    '''Take the dictionary and find the longest value'''
    longest_value = max(my_dict.items(), key=lambda item: (len(item[1]), -item[0]))
    return longest_value

def average_length_dict(dict):
    '''Take the dictionary and find the average length of the values'''
    dict_values = dict.values()
    num_lines = 0
    num_characters = 0
    for i in dict_values:
        num_lines += 1
        num_characters += len(i)
    average_length = num_characters/num_lines
    return average_length


book_lines_dict = get_input()
x = longest_value_dict(book_lines_dict)
y = average_length_dict(book_lines_dict)
print(x, x[0], x[1])
print(y)
#for line_number, content in book_lines_dict.items():
    #print(f"Line Number: {line_number}, Content: {content}")



