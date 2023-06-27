import re

inp_word = input().lower()

total_count = len(re.findall('sand', inp_word)) + len(re.findall('water', inp_word)) + \
              len(re.findall('fish', inp_word)) + len(re.findall('sun', inp_word))

# another solution:
# total_count = inp_word.count('sand') + inp_word.count('water') + inp_word.count('fish') + inp_word.count('sun')

print(total_count)
