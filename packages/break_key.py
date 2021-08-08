from pynput.keyboard import Key

def break_key():
    key_br = int(input("Need a Break key: \n1. Space\n2. Enter\n3. Specify other\n"))
    if key_br == 1:
        br_key = Key.space
    elif key_br == 2:
        br_key = Key.enter
    elif key_br == 3:
        br_key = str(input("Key: "))
    else:
        print("Invalid.")
        return break_key()
    return br_key