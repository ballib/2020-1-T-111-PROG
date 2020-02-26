LEFT_BRACE = "{"
RIGHT_BRACE = "}"
COMMA = ","
QUOTE = "'"
COLON = ":"
STRING = "STRING"
INTEGER = "INTEGER"

def tokenize(json_string):
    token_list = []
    parsing_string_bool = False
    parsing_integer_bool = False

    for c in json_string:

        if parsing_string_bool:
            if c == QUOTE:
                token_list.append(STRING)
                parsing_string_bool = False
            continue
        
        if parsing_integer_bool:
            if not c.isnumeric():
                token_list.append(INTEGER)
                parsing_integer_bool = False
            else:
                continue

        if c == LEFT_BRACE:
            token_list.append(LEFT_BRACE)
        elif c == RIGHT_BRACE:
            token_list.append(RIGHT_BRACE)
        elif c == COMMA:
            token_list.append(COMMA)
        elif c == QUOTE:
            parsing_string_bool = True
        elif c == COLON:
            token_list.append(COLON)
        elif c.isnumeric():
            parsing_integer_bool = True
        elif c == ' ':
            continue
        else:
            return None

    if not parsing_string_bool and not parsing_integer_bool:
        return token_list
        
def main():
    input_str = input('Enter JSON object: ')
    print(tokenize(input_str))
    
main()