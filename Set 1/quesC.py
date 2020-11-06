sentence = input('Enter the sentence: ')
count = 0
for letter in sentence:
    if letter in 'aeoiu':
        count = count + 1
        print(count)