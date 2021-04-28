import datetime


def binary_search(sorted_list, expected_number):
    low = 0
    high = len(sorted_list)-1
    iter = 1
    while low <= high:
        mid = int((low+high)/2)
        guess = sorted_list[mid]
        if guess == expected_number:
            return f"Загаданное число {mid},\
                сколько потребовалось операций для поиска {iter}"
        if guess > expected_number:
            high = mid-1
        else:
            low = mid+1
        iter += 1
    return None


def main():
    start_time = datetime.datetime.now()
    massive_list = []
    for elem in range(0, 128):
        massive_list.append(elem)
    print(binary_search(massive_list, 2))
    stop_time = datetime.datetime.now()
    print(f"Затраченное время на поиск: {stop_time-start_time}")
    return 0


if __name__ == "__main__":
    main()
