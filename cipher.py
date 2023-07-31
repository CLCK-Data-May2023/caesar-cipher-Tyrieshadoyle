# add your code here
shift_num = 5
user_phrase = input("Please enter a sentence: ")
user_phrase = user_phrase.lower()
new_phrase = ''
reg_alp = "abcdefghijklmnopqrstuvwxyz"
shifted_alp = reg_alp*2
for letter in user_phrase:
    if letter in reg_alp:
            new_phrase += shifted_alp[reg_alp.find(letter) + int(shift_num)]
    else:
            new_phrase += letter
else:
    print("The encrypted sentence is:", new_phrase)