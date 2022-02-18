import transliterate
from num2words import num2words
import re
import gtts

speach_txt = """\
Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame \
once in a lifetime and I guess that this is mine. People have also told me to \
make these next few minutes escruciatingly embarrassing and to take vengeance \
of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic \
Storage for last 40. When I was 8...
"""

lines_list = speach_txt.splitlines()

result_string = ""

for line in lines_list:
    words_list = line.split()
    for word in words_list:
        word = word.replace(".", "")
        is_digit = re.match("[-+]?\d", word)
        if is_digit is not None:
            result_string += (word
                              + " - "
                              + transliterate.translit(num2words(word,
                                                       to="cardinal"),
                                                       "ru")
                              + "\n")

tr_speach = transliterate.translit(speach_txt, "ru")
print(tr_speach, "\n", result_string, sep="", end="")

voice = gtts.gTTS(tr_speach)
voice.save('speach.mp3')
