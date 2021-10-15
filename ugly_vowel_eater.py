word_without_vowels = ""
# Prompt the user to enter a word
word = input("enter a word: ")
# and assign it to the user_word variable.
user_word = word.upper()

for letter in user_word:
	if letter != 'A' and letter != 'E' \
	and letter != 'I' and letter != 'O' \
	and letter != 'U':
		print(letter)
		continue
        
# improved ugly vowel eater
        word_without_vowels = ''
# Prompt the user to enter a word
word = input("enter a word: ")
# and assign it to the user_word variable.
user_word = word.upper()

for letter in user_word:
	if letter != 'A' and letter != 'E' \
	and letter != 'I' and letter != 'O' \
	and letter != 'U':
	    word_without_vowels += letter
	    continue
print(word_without_vowels)