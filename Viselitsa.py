import random

list_words = ["математика", "конструктор"]


def get_word():
    word = list_words[random.randint(0, len(list_words)) - 1]
    return word.upper()


def chek_letter(letter):
    if letter.isalpha() == False:
        return False


def display_hangman(tries):
    stages = ['''
    -----------
    |         |
    |         O
    |       \\ | /
    |         | 
    |        / \\
    |
    __
    ''',
              ''' 
    -----------
    |         |
    |         O
    |       \\ | /
    |         | 
    |        / 
    |
    __
    ''',
              ''' 
    -----------
    |         |
    |         O
    |       \\ | /
    |         | 
    |        
    |
    __
    ''',
              '''
    -----------
    |         |
    |         O
    |       \\ | /
    |          
    |        
    |
    __
    ''', ''' 
    -----------
    |         |
    |         O
    |       \\ | 
    |         
    |        
    |
    __
    ''', '''
    -----------
    |         |
    |         O
    |       
    |         
    |        
    |
    __
    ''', ''' 
    -----------
    |         |
    |         
    |      
    |        
    |       
    |
    __
    ''', '''
    -----------
    |         
    |        
    |       
    |        
    |       
    |
    __
    '''
              ]

    return stages[tries]
def countinue_game(answer):


def play(word):
    word = get_word()
    word_completion = ["_"] * len(word)
    guessed_letters = []
    tries = 7
    print("Давайте сыграем в виселицу!")
    print(display_hangman(tries))
    print(f"Вот загаданное слово: {' '.join(word_completion)} У вас {tries} попыток!")
    while True:
        letter = input("Введите букву или слово целиком: ")
        if len(letter) == len(word):
            for i in range(len(word)):  # если игрок вводит все слово целиком
                if letter[i].upper() == word[i].upper():  # игра заканчивается
                    word_completion[i] = letter.upper()
                else:
                    print("Не верное слово! Попробуйте еще раз!")
                    continue
            print(f"Поздравляю, Вы отгадали слово {word.upper()}")
            answer = input("Хотите сыграть еще раз? д - да, н - нет: ")
            if answer == "д":
                play(get_word())
            else:
                print("До свидания!")
            break
        elif letter.upper() in word:
            if letter in guessed_letters:
                print("Эта буква уже отгадана!")
                continue
            else:
                print("Отлично! Такая буква есть!")
                for i in range(len(word)):
                    if letter.upper() == word[i]:
                        word_completion[i] = letter.upper()
                        guessed_letters.append(letter)
                print(*word_completion)
                if "_" not in word_completion:
                    print(f"Поздравляю, Вы отгадали слово {word.upper()}")
                    answer = input("Хотите сыграть еще раз? д - да, н - нет: ")
                    if answer == "д":
                        play(get_word())
                    else:
                        print("До свидания!")
                        break
                else:
                    continue
        else:
            tries -= 1
            if tries == 0:
                print("НЕВЕРНО!!! Вы проиграли! Вас повесили!")
                print(display_hangman(tries))
                answer = input("Хотите сыграть еще раз? д - да, н - нет: ")
                if answer == "д":
                    play(get_word())
                else:
                    print("До свидания!")
                    break
            print("Такой буквы нет! Минус попытка!")
            print(display_hangman(tries))
            print(*word_completion)
            continue


play(get_word())
