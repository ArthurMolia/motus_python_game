# Motus python game
A game based on Motus, to be played on Unix terminals.

## How to play?
Before playing, you need to install all the requirements needed by the game to run.
To do so, just type: 
```bash
pip3 install -r requirements.txt
```

Then all you have to do to run the game is to type:
```bash
python3 motus.py
```

The goal of the game is to guess the word in a defined number of turns (5 by default).

## Custom game
You can add several arguments to the command above to customize the game's parameters.

### Arguments 

#### --min
The minimum size of the word to guess, its default value is 5.

#### --max
The maximum size of the word to guess, its default value is 10.

Note that if min > max, both will be switched (min will become max and vice-versa).
Changing the min and max value can make the chose of the word much longer.

#### --turns
The number of turn you have to guess the word, its default value is 5.

#### --language
The language of the word to guess. by default, the word will be in French. The following languages are available:
| Language           | Command |
| ------------------ | ------- |
| English            | en      |
| Español / Spanish  | es      |
| Italiano / Italian | it      |
| Euskara / Basque   | eus     |

### Example
By typing:
```bash
python3 motus.py --min 4 --max 9 --turns 8 --en
```
You will be seaching for an English word, from 4 to 9 letters long in 8 turns.