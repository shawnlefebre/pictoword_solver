Script to provide solutions to the iOS puzzle game Pictoword.

Example usage:
```
Enter letters: hoatwpdozctsx
How many letters in answer?: 9
Took 0.409678 seconds
2 possible answers:
stopwatch
woodchats
```

To improve effectiveness of finding a solution, download some number of dictionaries (more dictionaries = more possible answers). 
Update the word_dicts list with your dictionary location(s).


Dictionaries I've used:
- /usr/share/dict/words: Included with Linux distros
- 3esl.txt 23k words from http://wordlist.aspell.net/12dicts/
- 6of12.txt: 34k words from http://wordlist.aspell.net/12dicts/
- 2of12.txt: 41k words fom http://wordlist.aspell.net/12dicts/
- 2of12inf.txt: 82k words from http://wordlist.aspell.net/12dicts/
- en_US.dic: 49k words from https://sourceforge.net/projects/hunspell/files/Spelling%20dictionaries/en_US/
- words.txt: 467k words from https://github.com/dwyl/english-words
