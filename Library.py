import sys

def main():
    
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
        longest_value = max(my_dict.items(), key=lambda item: (len(item[1]), item[0]))
        return longest_value

    def average_length_dict(dict):
        '''Take the dictionary and find the average length of the values'''
        dict_values = dict.values()
        num_lines = 0
        num_characters = 0
        for i in dict_values:
            num_lines += 1
            num_characters += len(i)
        average_length = round(num_characters/num_lines)
        return average_length

    def get_title():
        '''Take the file name and get the title without the .txt'''
        my_title  = str(sys.argv[1])
        file_name_without_extension = my_title.split('.')
        title = file_name_without_extension[0].upper()
        return title

    def write_output_file(title, longest_line, average_length, line_dict):
        '''write a file in the specified output'''
        output_filename  = f'{title}_book.txt'
        with open(output_filename, 'w') as output_file:
            output_file.write(f'{title}\n')
            output_file.write(f'Longest line ({longest_line[0]}): {longest_line[1]}\n')
            output_file.write(f'Average length: {average_length}\n')
            sorted_lines = sorted(line_dict.items(), key=lambda item: item[0])           
            for line_number, content in sorted_lines:
                output_file.write(f'{content}\n')

    def finalize():
        book_lines_dict = get_input()
        write_output_file(get_title(), longest_value_dict(book_lines_dict), average_length_dict(book_lines_dict), book_lines_dict)

    finalize()

main()




