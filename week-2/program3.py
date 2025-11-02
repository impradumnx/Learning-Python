import time #to import time module
# function to print each line letter by letter
def type_line(line) :
    for ch in line :
        print (ch, end='', flush=True)
        time.sleep(0.07) # very small pauses between each character for typing effect
    print() # to move to next line after printing the whole line

# a list of lists containing lyrics and delay after each line
lyrics_with_delay = [
    ["bo manzar,", 1],
    ["abb bhi aankho se jaata nahi...", 3],
    ["tera kehna,", 1],
    ["ki tu mujhko chahta nahi...", 1.5],
    ["dil bhi mein pesh karu, ", 1],
    ["tu agar teer bane...", 2],
    ["hass ke mein raanjha banu, ", 1],
    ["tu agar heer bane...", 2]
]
# to print each line with typing effect and delay
for line,delay in lyrics_with_delay :
    type_line(line)
    time.sleep(delay)


