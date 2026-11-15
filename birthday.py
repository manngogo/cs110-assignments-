import stdio
import stdrandom
import sys
#imported to use
# num of experiments to run, from the command line.
trials = int(sys.argv[1])
DAYS = 365   # we ignore leap years, like the standard birthday problem does
# add how many ppl enter room each trial for all trials
# find average of number
total_people = 0
 
for t in range(trials):
    # seen[d] is True if someone in the room already has birthday d.
    #reset it for every trial, bc each trial starts with an empty room.
    seen = [False] * DAYS
    people = 0
 
    # let ppl in until new person shares a birthday w/ someone already in the room
    while True:
        birthday = stdrandom.uniformInt(0, DAYS)   # random day from 0 to 364
        people += 1                         # person has entered
 
        if seen[birthday]:
            # match found, they count toward the total, and we stop this trial.
            break
 
        # No match yet: remember this birthday and let the next person in.
        seen[birthday] = True
 
    total_people += people
# average number of people per trial, using integer division as the spec says.
stdio.writeln(total_people // trials)