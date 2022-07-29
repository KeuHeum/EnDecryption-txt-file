import os
import re
from hashlib import md5#sha1, sha224, sha256, sha384, sha512
from cryptography.fernet import Fernet

Password_Hash_Key = 'you can made this from "setting pwd.py" file'#password must be under 43
dir_Path = os.path.dirname(os.path.realpath(__file__))
file_Path = os.listdir(dir_Path)

def endecrypt(password):
    key = (password+'m8dpBUDcgiGA2pwdwdd25iALUreXCJ8ZecDQEGw0H1c'[0:43 - len(password)]+'=').encode('utf-8')
    
    for i in file_Path:
        if i.endswith('.txt'):
            with open(i, 'rt', encoding='utf-8') as f:
                file_content_bytes = bytes(f.read(), "utf-8")

            if i.startswith("encry"):# decryption
                with open(i,'wt', encoding='utf-8') as f:
                    decryption_data = str(Fernet(key).decrypt(file_content_bytes), 'utf-8')
                    f.write(decryption_data)
                    print(f"{i.replace('.txt', '')} | Decryption Success: {decryption_data[0:20]+'...' if len(decryption_data) > 20 else decryption_data}")
                os.rename(i, i.replace('encry - ', ''))

            else:# encryption
                with open(i,'wt', encoding='utf-8') as f:
                    encryption_data = str(Fernet(key).encrypt(file_content_bytes), 'utf-8')
                    f.write(encryption_data)
                    print(f"{i.replace('.txt', '')} | Encryption Success: {encryption_data[0:20]+'...' if len(encryption_data) > 20 else encryption_data}")

                    #option to back up the data
                    if not os.path.exists('encryptData'):
                        os.makedirs('encryptData')
                    with open(f'encryptData/{i}', 'wt', encoding='utf-8') as dir_f:
                        dir_f.write(encryption_data)
                        print(f"{i.replace('.txt', '')} | Encryption Back up Success")

                os.rename(i, 'encry - '+i)

def main(message):
    print(f'>>> {message}\n' if message != '' else '', end='')
    input_answer = input('Please enter the password: ')

    if len(input_answer) > 43:
        main('Password must be 43 characters or less.')
    
    elif re.compile('[A-Za-z0-9]+').fullmatch(input_answer) is None: #https://stackoverflow.com/questions/57011986/how-to-check-that-a-string-contains-only-a-z-a-z-and-0-9-characters
        main('Password must be Engilsh and Number. ( [a-z], [A-Z], [0-9] )')

    elif md5(input_answer.encode('utf-8')).hexdigest() == Password_Hash_Key:
        print('Correct password')
        endecrypt(input_answer)

    else:
        main('Wrong password.')


if __name__ == '__main__':
    os.chdir(dir_Path)
    main('')
