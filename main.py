import os
import re
import math
from hashlib import md5
from cryptography.fernet import Fernet


# Setting
ENCRYPT_FILE_NAME = True
# USE_ENCRYPTION_BACK_UP = True
PASSWARD_HASH_KEY = '84ff66b0fadbecf1f8c2e13b10096c37' #'you can made this from "hash_password.py" file'

dir_Path = os.path.dirname(os.path.realpath(__file__))


def password_input_checker() -> str:
    answer = input('\nPlease enter the password: ')

    if len(answer) > 43:
        print('Password must be 43 characters or less.')
        return password_input_checker()
    
    elif re.compile('[A-Za-z0-9]+').fullmatch(answer) is None:
        print('Password must be Engilsh and Number. ( [a-z], [A-Z], [0-9] )')
        return password_input_checker()

    elif md5(answer.encode('utf-8')).hexdigest() != PASSWARD_HASH_KEY:
        print('Wrong password.')
        return password_input_checker()
    
    print('>>> Correct password')
    return answer


def preview_text(text: str) -> str:
    return text[0:20]+'...' if len(text) > 20 else text


def endecrypt():
    global fernet

    for file_name in os.listdir(dir_Path):
        if not file_name.endswith('.txt'):
            continue
        
        with open(file_name, 'rb') as f:
            file_content = f.read()

        # decryption
        if file_name.startswith('encry -'):
            with open(file_name, 'wb') as f:
                f.write(fernet.decrypt(file_content))
                print(f"{preview_text(file_name.replace('.txt', ''))} | Decryption Success")

            dst_file_name = file_name.replace('encry - ', '')
            if ENCRYPT_FILE_NAME:
                dst_file_name = fernet.decrypt(bytes(dst_file_name, 'utf-8')).decode('utf-8')
            
            os.rename(file_name, dst_file_name+'.txt')

        # encryption
        else:
            with open(file_name, 'wb') as f:
                f.write(fernet.encrypt(file_content))
                print(f"{preview_text(file_name.replace('.txt', ''))} | Encryption Success")

            dst_file_name = file_name.replace('.txt', '')
            if ENCRYPT_FILE_NAME:
                dst_file_name = fernet.encrypt(bytes(dst_file_name, 'utf-8')).decode('utf-8')
            os.rename(file_name, 'encry - '+dst_file_name+'.txt')

            # if USE_ENCRYPTION_BACK_UP:
            #     if not os.path.exists('encryptData'):
            #         os.makedirs('encryptData')
            #     with open(f'encryptData/{file_name}', 'wb') as f:
            #         f.write(fernet.encrypt(file_content))
            #         print(f"{file_name.replace('.txt', '')} | Encryption Back up Success")


def main():
    global fernet

    os.chdir(dir_Path)

    password = password_input_checker()

    multiply_num = math.ceil(43 / len(password))
    key = ((password*multiply_num)[:43] + '=').encode('utf-8')
    fernet = Fernet(key)

    endecrypt()


if __name__ == '__main__':
    main()
