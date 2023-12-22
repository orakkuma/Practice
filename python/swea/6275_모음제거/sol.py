words = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

vowels = 'AEIOUaeiou'
result = ''

for word in words:
    if word not in vowels:
        result += word
    else:
        result += ''
print(result)