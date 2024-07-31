def msg_convertor():
    import random
    import string
    chars = list(string.ascii_letters + string.digits+ string.punctuation + ' ')
    keys = chars.copy()
    random.shuffle(keys)
    while True:
        king = input('Enter a Msg: ')
        Option_1 = int(input(f'Select a Option:\n 1. Encrypting a Message\n 2. Decrypting a Message \n 3.Stop \n 4.Save to a file \n'))
        if Option_1 == 1:
            new_msg = ""
            for letters in king:
                index = chars.index(letters)
                new_msg += keys[index]
            print(new_msg)
        elif Option_1 == 2:
            new_msg = ""
            for letters in king:
                index = keys.index(letters)
                new_msg += chars[index]
            print(new_msg)
        elif Option_1 == 3:
            print('Exited')
            break
        else:
            print('Error: Invalid option')

msg_convertor()