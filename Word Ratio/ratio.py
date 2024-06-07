import keyboard

def wait():
    while True:
        if keyboard.read_key() == 'space':
            break

x = 0
file = open("words.txt", "r")
results = open("results.txt", "w")
bigboy = open("bigboy.txt", "w")
for i in file:
    stripped_word = i.strip()
    unique_char_count = len(set(stripped_word))
    length = (len(stripped_word))
    Ratio = length / unique_char_count
    if Ratio >= 2.7:
        bigboy.write(stripped_word + " Has a word ratio of " + str(Ratio) + "\n")
    else:
        results.write(stripped_word + " Has a word ratio of " + str(Ratio) + "\n")
    x += 1
    if x == 194444:
        break
print("Check results file for the list of ratios. ")
print("Press space to end program")
wait() 