words_number, input_vocabulary, hangman_state_end,  won = int(input()), [], "o>-<", False

for i in range(words_number):
    input_vocabulary.append(input())

template, checked_letters, hangman_state, answer = input(), set(), "", ""

checked_letters.add(template[0])
vocabulary = [word for word in input_vocabulary if len(word) == len(template) and word[0] == template[0]]

while True:
    line = ""
    try:
        line = input()
    except(ValueError, EOFError):
        won = True
        break

    answer = input().split()
    if len(answer) == 1 and answer[0] == "YES":
        checked_letters.add(line)
        continue
    else:
        hangman_state = answer[1]
        if hangman_state == hangman_state_end:
            print("LOST")
            break

if won:
    for word in vocabulary:
        if set(word) == checked_letters:
            print("WON")
            print(word)
            break
