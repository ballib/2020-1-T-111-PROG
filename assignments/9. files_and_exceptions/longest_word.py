# This program finds the longest word from an input file

def open_file(filename):
  file_object = open(filename, 'r')
  return file_object

def find_longest(file_object):
    ''' Returns the longest word and its length found in the given file '''
    max_length = 0		# The length of the longest word found so far
    longest_word = "" 	# The longest word found so far

    for word in file_object:	# process each line/word
        word = word.strip()     # strip leading and trailing white space
        length = len(word)	
        if length > max_length:	 # A new maximum length?
            longest_word = word
            max_length = length
    return longest_word, max_length

# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
longest, length = find_longest(file_object)

print("Longest word is '{:s}' of length {:d}".format(longest, length))
file_object.close()