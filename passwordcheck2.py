def check_password(password: str):
    try:
        with open('passwords.txt', 'r') as file:
            common_passwords: list[str] = file.read().splitlines()
    except FileNotFoundError:
        print('The file was not found!')
        return
    except IOError:
        print('An error occurred while reading passwords.txt!')
        return

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return

    print(f'{password}: ✅ (Unique)')


def main():
    user_password = input('Enter password: ')
    try:
        if user_password == '':
            raise ValueError('Password cannot be empty')
    except ValueError as e:
        print(e)
        return

    check_password(user_password)


if __name__ == '__main__':
    main()
