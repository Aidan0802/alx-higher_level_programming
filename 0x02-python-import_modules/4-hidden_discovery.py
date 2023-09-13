#!/usr/bin/python3
if __name__ == "__main__":
    import dis

    with open('hidden_4.pyc:Zone.Identifier', 'rb') as file:
        code = file.read()
        dis.dis(code)

    if i in code:
        if i[0] != '_' and i[1] != '_':
            print("{}".format(i))
