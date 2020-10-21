from ProgramInternalForm import ProgramInternalForm
from SymbolTable import SymbolTable
from Scanner import *

if __name__ == '__main__':
    file = open('p1', 'r')
    st = SymbolTable()
    pif = ProgramInternalForm()

    line_index = 0
    for line in file:
        line_index += 1

        if line[-1] == '\n':
            line = line[0:-1]  # Skip \n

        for token in Scanner.get_tokens_from_line(line):
            if token in operators_separator_words:
                pif.add(codes[token], -1)
            elif Scanner.is_identifier(token):
                # Add and return id or just return id
                pif.add(codes['identifier'], st.add(token))
            elif Scanner.is_constant(token):
                # Add and return id or just return id
                pif.add(codes['constant'], st.add(token))
            else:
                print("Unknown token '{}' at line {}!".format(token, line_index))

    print("Symbol table:")
    st.print()
    print(f"Program internal form: {pif}")
