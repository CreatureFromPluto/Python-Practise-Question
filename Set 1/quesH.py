# snake = 'I love python but java is better'
# snakes = (snake.replace('python','java',4))
# print(snakes)

sentence = "I love python but java is better"
words = sentence.split()
print(words)
n = len(words)

#Loop to iterate from one word to another
for i in range(0,n):
    if (words[i]=='python'):
        words[i]='java' #Replacing python with java
    elif (words[i]=='java'):
        words[i]='python'

changedString = " " #Specifying the delimiter (ie, the space which will come between two words)
# print(words)
changedString = changedString.join(words)

print("lolo",changedString)