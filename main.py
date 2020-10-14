from SymbolTable import ST

if __name__ == '__main__':
    symtable = ST()
    symtable.add("b")
    symtable.add("c")
    symtable.add("a")

    symtable.print()
