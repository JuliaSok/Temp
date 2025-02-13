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
    l, r = a, b
    while l <= r:
        cnt += 1
        predict = (l + r) // 2
        if predict == number:
            return cnt
        elif predict < number:
            l = predict + 1
        else:
            r = predict - 1
    

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    random_array = np.random.randint(a, b + 1, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

