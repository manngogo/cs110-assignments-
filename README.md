# Homework 3: Mozart Waltz Generator
 
Small Python programs that build up to Mozart's dice game: generate a random two-part waltz (a 16-measure minuet and a 16-measure trio), then play it.
 
## Requirements
 
- Python 3
- The course `stdio`, `stdarray`, `stdrandom` and `stdaudio` libraries on your Python path
- For `playwaltz.py`: `numpy` and `pygame` (or `pygame-ce`), which `stdaudio` uses
- The `data/` folder in this directory: `mozart.txt` (the minuet and trio tables) and the audio files `M1.wav`–`M176.wav` and `T1.wav`–`T96.wav`
Run every command from this folder.
 
## Warmup programs
 
### reverse.py
Reads strings from standard input and writes them in reverse order.
 
```
$ python3 reverse.py
b o l t o n
<ctrl-d>
n o t l o b
```
 
### distance.py
Takes `n` as a command-line argument, reads two vectors of `n` numbers from standard input, and writes the Euclidean distance between them.
 
```
$ python3 distance.py 2
1 0
0 1
1.4142135623730951
```
 
### birthday.py
Takes the number of `trials` as a command-line argument and writes the average number of people who must enter a room before two share a birthday (integer division). For a large number of trials it is usually 24 or 25.
 
```
$ python3 birthday.py 1000
24
```
 
### transpose.py
Takes `m` (rows) and `n` (columns) as command-line arguments, reads an m-by-n matrix from standard input, and writes its transpose.
 
```
$ python3 transpose.py 2 3
1 2 3
4 5 6
1.0 4.0
2.0 5.0
3.0 6.0
```
 
### pascal.py
Takes `n` as a command-line argument and writes the first `n + 1` rows of Pascal's triangle.
 
```
$ python3 pascal.py 4
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```
 
## Waltz programs
 
### generatewaltz.py
Reads the minuet and trio tables from standard input and writes a random sequence of 32 measure numbers (16 minuet, then 16 trio) on one line. The output is different each run.
 
```
$ python3 generatewaltz.py < data/mozart.txt
69 95 27 103 105 129 21 24 66 155 48 34 43 18 89 78 72 39 59 68 29 7 15 94 76 34 93 77 12 95 47 10
```
 
### playwaltz.py
Reads 32 measure numbers from standard input and plays the waltz. It checks the input first and exits with an error message, playing no audio, if:
 
- there are not exactly 32 measures,
- a minuet measure (the first 16) is not in [1, 176], or
- a trio measure (the last 16) is not in [1, 96].
Generate and play a waltz in one step:
 
```
$ python3 generatewaltz.py < data/mozart.txt | python3 playwaltz.py
```
 
## Notes
 
`notes.txt` holds the written description of each problem.