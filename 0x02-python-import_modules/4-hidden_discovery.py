#!/usr/bin/python3
import dis
import marshal

if __name__ == "__main__":
    with open('hidden_4.pyc:Zone.Identifier', 'rb') as file:
        Bcode = file.read()
        code = marshal.loads(Bcode)

    dis.dis(code)
    names = dir(code)

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
