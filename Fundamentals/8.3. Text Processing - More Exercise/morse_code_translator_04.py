MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
                   '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K',
                   '.-..': 'L', '--': 'M', '-.': 'N',
                   '---': 'O', '.--.': 'P', '--.-': 'Q',
                   '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W',
                   '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

morse_code = input().split(" | ")
translated_text = ""

for word in morse_code:
    curr_word = [x for x in word.split(' ')]

    for l in curr_word:
        if l != '':
            translated_text += MORSE_CODE_DICT.get(l)

    translated_text += ' '

print(translated_text)
