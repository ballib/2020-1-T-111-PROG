def open_file(filename):
  file_object = open(filename, 'r')
  return file_object

def process_file(file_object):  
  line_str = ""

  for line in file_object:
    line = line.strip()
    line = line.replace(" ", "")
    line_str += line
  
  print(line_str)

# Main starts here
file_object = open_file('test.txt')
process_file(file_object)
file_object.close()