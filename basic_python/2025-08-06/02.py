def imprime_primeiro_char(char):
    if len(char) > 0:
        print(f'O primeiro caractere: ({char[0]})')
    else:
        print("Caractere vazio")
        
        
char = "b bb"

imprime_primeiro_char(char)


def test_double_char(char, char2):
    if len(char) > 0:
        print(f'O primeiro caractere: ({char[0]}) e segundo {char2}')
    else:
        print("Caractere vazio")
        
test_double_char(char2='2', char='B')