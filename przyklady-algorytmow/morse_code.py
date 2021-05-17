# ref = https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg
# - : no signal
# O : signal


# HELLO
morse_in = 'o-o-o-o---o---o-ooo-o-o---o-ooo-o-o---ooooooooo'

def intepreter(morse):
    words = morse.split('-------')  # split words
    for i, w in enumerate(words):
        words[i] = w.split('---') # split letters

    print(words)


intepreter(morse_in)

# nie chciało mi się przepisywać alfabetu, więc zostawiam tak nie dokończone
