# Homework 1
 
Short command-line programs for basic input, arithmetic, math functions and conditionals.
 
## Requirements
 
- Python 3
- The course `stdio` and `stdrandom` libraries on your Python path
Run every command from this folder. Inputs are given as command-line arguments.
 
## Programs
 
### name_age.py
Takes a name and an age and writes a sentence with both.
 
```
$ python3 name_age.py Alice 20
 Alice is 20 years old.
```
 
### greet_three.py
Takes three names and greets them in reverse order.
 
```
$ python3 greet_three.py Alice Bob Carol
 Hi Carol, Bob, and Alice.
```
 
### bmi.py
Takes a weight and a height and writes the body mass index (weight divided by height squared). Use the units the course formula expects (for example kilograms and meters).
 
```
$ python3 bmi.py 68 1.7
23.529411764705884
```
 
### cartesian.py
Takes polar coordinates, a radius `r` and an angle in degrees, and writes the Cartesian `x y` coordinates.
 
```
$ python3 cartesian.py 5 60
2.5000000000000004 4.330127018922193
```
 
### gravitational_force.py
Takes two masses and the distance between them and writes the gravitational force between them (G × m1 × m2 / r²).
 
```
$ python3 gravitational_force.py 5.972e24 7.348e22 3.844e8
1.9820216361078958e+20
```
 
### great_circle.py
Takes the latitude and longitude of two points in degrees (`x1 y1 x2 y2`) and writes the great-circle distance between them.
 
```
$ python3 great_circle.py 48.87 -2.33 37.8 -122.4
8701.387455462233
```
 
### snell.py
Takes an angle of incidence in degrees and the two refractive indices `n1` and `n2`, and writes the angle of refraction in degrees (Snell's law).
 
```
$ python3 snell.py 30 1.0 1.5
19.47122063449069
```
 
### triangle.py
Takes three integer side lengths and writes `True` if each side is no longer than the sum of the other two, `False` otherwise.
 
```
$ python3 triangle.py 3 4 5
True
$ python3 triangle.py 1 2 5
False
```
 
### waiting_time.py
Takes a rate `λ` and a time `t` and writes the probability `e^(-λt)` that the wait is longer than `t`.
 
```
$ python3 waiting_time.py 0.5 2
0.36787944117144233
```
 
### gambler.py
Takes two integers `n1` and `n2` and a probability `p` (strictly between 0 and 1, and not 0.5) and writes two probabilities computed from the gambler's-ruin formulas.
 
```
$ python3 gambler.py 5 10 0.5001
 0.6659997782135659 0.3340002217864445
```
 
### die.py
Takes no arguments. Rolls a die and draws the face with asterisks.
 
```
$ python3 die.py
*    
  *  
    *
```
 
The face is random, so the output changes each run.