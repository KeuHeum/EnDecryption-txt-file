import re
from hashlib import md5

print('Warning: Password must be Engilsh and Number ( [a-z], [A-Z], [0-9] )\n')

def main(message):
    print(f'>>> {message}\n' if message != '' else '', end='')
    input_answer = input('Enter your password: ')

    if len(input_answer) > 43:
        main('Password must be 43 characters or less.')

    elif re.compile('[A-Za-z0-9]+').fullmatch(input_answer) is None:
        main('Password must be Engilsh and Number ( [a-z], [A-Z], [0-9] )')
    
    else:
        print(f"Your Password Hash: {md5(input_answer.encode('utf-8')).hexdigest()}")
if __name__ == '__main__':
    main('')
