from functions.queries import get_random_words


is_exit = False
is_success = True
the_word = ''

def EvaluateCommand(input, dictionary_word):
    if not input:
        return
    input = input.strip().lower()
    if input == 'q':
        return True

    global is_success
    is_success = True
    if input != dictionary_word.lower():
        is_success = False
    return False

while not is_exit:
    if is_success:
        for row in get_random_words(1):
            the_word = row[0]
            print(the_word)
    else:
        print("Error, try again!")
        print(the_word)

    command = input("Type the word: ")
    is_exit = EvaluateCommand(command, the_word)
