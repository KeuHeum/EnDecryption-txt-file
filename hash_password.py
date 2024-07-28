import re
from hashlib import md5


print('Notice: Password must be Engilsh and Number ( [a-z], [A-Z], [0-9] )\n')

def main():
    answer = input('Enter your password: ')

    if len(answer) > 43:
        print('Password must be 43 characters or less.')
        return main()

    elif re.compile('[A-Za-z0-9]+').fullmatch(answer) is None:
        print('Password must be Engilsh and Number ( [a-z], [A-Z], [0-9] )')
        return main()
    
    print(f"Your Password Hash: {md5(answer.encode('utf-8')).hexdigest()}")

if __name__ == '__main__':
    main()
