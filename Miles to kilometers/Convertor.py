def miles_to_km(miles):
    return round(miles * 1.60934)


def convertor(sentence):
    numbers = [num for num in range(1, 20)] + [10 * num for num in range(2, 10)] + [100 * num for num in range(1, 10)]
    names_miles = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
                   "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
                   "девятнадцать", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят",
                   "восемьдесят",
                   "девяносто", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                   "девятьсот"]
    names_km = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
                "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
                "девятнадцать", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                "девятьсот"]

    miles_words_to_numbers = dict(zip(names_miles, numbers))
    km_numbers_to_words = dict(zip(numbers, names_km))

    key_words_miles = ["милю", "миль", "мили", "миля"]
    key_words_km = ["километров", "километр", "километра"]
    left, right, miles = [], 0, 0

    for idx in range(len(sentence) - 4):
        if sentence[idx:idx + 4] in key_words_miles:
            left = sentence[:idx - 1].rsplit(maxsplit=3)
            right = sentence[idx + 4:]
            break

    while left[-1] in names_miles:
        miles += miles_words_to_numbers[left.pop()]

    kilometers, kilometers_words = list(map(int, list(str(miles_to_km(miles))))), []

    if len(kilometers) >= 2 and kilometers[-2] == 1:
        kilometers[-2] = 10 * kilometers[-2] + kilometers[-1]
        kilometers.pop()
        if len(kilometers) == 1:
            kilometers_words.append(km_numbers_to_words[kilometers[0]])
        else:
            kilometers_words.append(km_numbers_to_words[100 * kilometers[0]])
            kilometers_words.append(km_numbers_to_words[kilometers[1]])
    else:
        for idx in range(len(kilometers)):
            if kilometers[idx] != 0:
                kilometers_words.append(km_numbers_to_words[10 ** (len(kilometers) - idx - 1) * kilometers[idx]])

    exceptions = ["два", "три", "четыре"]
    if kilometers_words[-1] == "один":
        kilometers_words.append(key_words_km[1])
    elif kilometers_words[-1] in exceptions:
        kilometers_words.append(key_words_km[2])
    else:
        kilometers_words.append(key_words_km[0])

    left += kilometers_words

    return " ".join(left) + right


sent = input()

print(convertor(sent))

