import numpy as np

a, b = 1, 100

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    cnt = 0
    left, rigth = a, b
    while left <= rigth:
        cnt += 1
        predict = (left + rigth) // 2
        if predict == number:
            break
        elif predict < number:
            left = predict + 1
        else:
            rigth = predict - 1
    return cnt
    

def score_game(random_predict) -> int:
    """Функция для сбора статистики расчетов нашего когда.
        Принимает функцию, выдает сообщение о максимальном, минимальном и среднем
        количестве результатов выполнения нашего кода за 1000 запусков

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    random_array = np.random.randint(a, b + 1, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    print(f'Среднее число попыток {int(np.mean(count_ls))}')   # Ожидаемо 6
    print(f'Максимальное количество попыток {max(count_ls)}')  # Ожидаемо 8
    print(f'Минимальное количество попыток {min(count_ls)}')   # Ожидаемо 1

    
    
print('Run benchmarking for game_core_v3: ')
score_game(game_core_v3)

