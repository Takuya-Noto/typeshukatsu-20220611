for num in range(1, 101):
    string = ''

    # ここから記述

    # 15の倍数であればFizzBuzz
    if num % 15 == 0:
        string = 'FizzBuzz'

    # 15の倍数ではなくて、3の倍数であればFizz
    elif num % 3 == 0:
        string = 'Fizz'

    # 15の倍数ではなくて、5の倍数であればBuzz
    elif num % 5 == 0:
        string = 'Buzz'

    # 上記以外ならそのまま
    else:
        string = str(num)

    # ここまで記述

    print(string)