#version 2.0.0
import os
import re
from hashlib import md5#sha1, sha224, sha256, sha384, sha512
from cryptography.fernet import Fernet

Password_Hash_Key = 'ce85b1d12f2a644cbd199cec4e8c801e'#password must be under 43
dir_Path = os.path.dirname(os.path.realpath(__file__))
EnDe_Key = ''

def endecrypt(type, message):
    global EnDe_Key

    message_bytes = bytes(message, 'utf-8')

    if type == 'en': return str(Fernet(EnDe_Key).encrypt(message_bytes), 'utf-8')
    elif type == 'de': return str(Fernet(EnDe_Key).decrypt(message_bytes), 'utf-8')
    

def endecrypt_file(password):
    global EnDe_Key

    EnDe_Key = (password+'m8dpBUDcgiGA2pwdwdd25iALUreXCJ8ZecDQEGw0H1c'[0:43 - len(password)]+'=').encode('utf-8')
    
    for i in os.listdir(dir_Path):
        if i.endswith('.txt'):
            with open(i, 'rt', encoding='utf-8') as f:# read file content
                file_content = f.read()

            if i.startswith("encry"):# decryption
                with open(i,'wt', encoding='utf-8') as f:
                    decryption_data = endecrypt('de', file_content)
                    f.write(decryption_data)#write decryption data

                    file_name = endecrypt('de', i.replace('.txt', '').replace('encry - ', ''))
                    decryption_data = decryption_data.replace('\n', '')
                    print(f"{file_name} | Decryption Success: {decryption_data[0:20]+'...' if len(decryption_data) > 20 else decryption_data}")
                
                os.rename(i , file_name+'.txt')

            else:# encryption
                with open(i,'wt', encoding='utf-8') as f:#write encryption data
                    encryption_data = endecrypt('en', file_content)
                    f.write(encryption_data)

                    print(f"{i.replace('.txt', '')} | Encryption Success: {encryption_data[0:20]+'...' if len(encryption_data) > 20 else encryption_data}")

                    #option to back up the data
                    encoding_file_name = endecrypt("en", i.replace(".txt", ""))

                    if not os.path.exists('encryptData'):
                        os.makedirs('encryptData')
                    
                    with open(f'encryptData/{encoding_file_name}.txt', 'wt', encoding='utf-8') as dir_f:
                        dir_f.write(encryption_data)
                        print(f"{i.replace('.txt', '')} | Encryption Back up Success")

                os.rename(i, f'encry - {encoding_file_name}.txt')

    print('>>> Everything was done Successfully')
    os.system('pause')

def password_input_check(message):
    print(f'>>> {message}\n' if message != '' else '', end='')
    input_answer = input('Please enter the password: ')

    if len(input_answer) > 43:
        password_input_check('Password must be 43 characters or less.')
    
    elif re.compile('[A-Za-z0-9]+').fullmatch(input_answer) is None: #https://stackoverflow.com/questions/57011986/how-to-check-that-a-string-contains-only-a-z-a-z-and-0-9-characters
        password_input_check('Password must be Engilsh and Number. ( [a-z], [A-Z], [0-9] )')

    elif md5(input_answer.encode('utf-8')).hexdigest() == Password_Hash_Key:
        os.system('cls')
        print('>>> Correct password\n')
        endecrypt_file(input_answer)

    else:
        password_input_check('Wrong password.')


if __name__ == '__main__':
    os.chdir(dir_Path)
    password_input_check('')
