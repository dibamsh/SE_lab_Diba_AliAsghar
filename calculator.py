while True:
    phrase = input()

    if ('+' in phrase):
        op1, op2 = phrase.split('+')
        try:
            op1 = float(op1)
            op2 = float(op2)
            print("answer:", op1 + op2)
        except:
            print("Invalid command!")
    elif ('-' in phrase):
        op1, op2 = phrase.split('-')
        try:
            op1 = int(op1)
            op2 = int(op2)
            print("answer:", op1 + op2)
        except:
            print("Invalid command!")
    else:
        print("Invalid command!")
    print()
