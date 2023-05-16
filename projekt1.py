"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Marek Dembicky
email: marodembo@gmail.com
discord: Mak D. #8143
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#registrovany uzivatelia - existujuce ucty - mena, hesla:
usernames = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

name = input('Please log-on - enter username: ') #Step0 - Prihlasenie existujuceho usera:
if name not in usernames:
    print('unregistered user, terminating the program..')
else:
    password = input('Enter password: ')
    if password != passwords[usernames.index(name)]:
        print('wrong password.')
    if password == passwords[usernames.index(name)]:
        # Zobrazenie nazvu projektu, username a password, a pozdrav:
        print(f'\npython projekt1.py')
        print(f'username:{name}\npassword:{password}')
        print('-' * 40)
        print(f'Welcome to the app, {name}.', sep='\n')
        print(f'We have 3 texts to be analyzed.')
        print('-' * 40)

        #Selection of texts from 1-3:
        text_number = input('Enter a number btw. 1 and 3 to select: ')
        if not text_number.isdigit() or int(text_number) not in range(1,4):
            print('wrong selection, terminating the program.. ')
        else:
            text_number = int(text_number)
            if text_number == 1:
                text_choice = TEXTS[0]
            elif text_number == 2:
                text_choice = TEXTS[1]
            elif text_number == 3:
                text_choice = TEXTS[2]

            #Step1 - vycistenie slov a vklad do listu 'words' a zistenie poctu slov v texte:
            words = []
            text_choice = text_choice.replace('\n', ' ')
            for item in text_choice.split():
                words.append(item.strip(' ,.;!?:'))
            print(f'There are {len(words)} words in the selected text.')

            #Step2 - number of titlecase words v texte:
            words_titlecase = []
            for item in words:
                if item.isalpha() and item[0].isupper():
                    words_titlecase.append(item)
            print(f'There are {len(words_titlecase)} titlecase words.')

            #Step3 - number of uppercase words v texte:
            words_uppercase = []
            for item in words:
                if item.isalpha() and item.isupper():
                    words_uppercase.append(item)
            print(f'There are {len(words_uppercase)} uppercase words.')

            # Step4 - number of lowercase words v texte:
            words_lowercase = []
            for item in words:
                if item.islower():
                    words_lowercase.append(item)
            print(f'There are {len(words_lowercase)} lowercase words.')

            # Step5 - number of numeric strings v texte:
            words_numerics = []
            for item in words:
                if item.isdigit():
                    words_numerics.append(item)
            print(f'There are {len(words_numerics)} numeric strings.')

            # Step6 - the sum of all the numbers v texte:
            words_numbers = []
            for item in words_numerics:
                words_numbers.append(int(item))
            sum_numbers = sum(words_numbers)
            print(f'The sum of all the numbers {sum_numbers}')

            # Step7 - cetnost ruznych delek slov v texte:
            word_length_list = []#delka jednotlivych slov v texte
            counts1 = []  # zoradenie delek jednotlivych slov do listu
            counts2 = []
            for word in (words):
                word_length_list.append(len(word))#pre kazde slovo tam daj jeho dlzku

            for i in sorted(word_length_list):
                counts1.append(i)#zoradeny list vsetkych dlzok slov od min do max

            all_word_lengths = list(sorted(set(word_length_list)))
            x = min(counts1)
            for i in all_word_lengths:
                if i == x:
                    counts2.append(counts1.count(x))
                    x += 1

            print('-' * 40)
            print('LEN|', '  OCCURENCES        |', 'NR.')
            print('-' * 40)

            for i,j in zip(all_word_lengths, counts2):
                x = 20 #nastavenie odriadkovania cisel j aby boli pod sebou a pod NR. v tabulke
                if int(i) < 10:
                    print('', i, '|', j * '*', (x - j) * ' ', j)
                elif int(i) >= 10:
                    print(i, '|', j * '*', (x - j) * ' ', j)