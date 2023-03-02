import math

volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

fill_p1 = p1 * hours
fill_p2 = p2 * hours
total = (p1 + p2) * hours

fill_p1 = fill_p1 / total * 100
fill_p2 = fill_p2 / total * 100
total_perc = total / volume * 100

if total <= volume:
    print("The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%."
          .format(math.trunc(total_perc), math.trunc(fill_p1), math.trunc(fill_p2)))
else:
    print("For {0} hours the pool overflows with {1} liters."
          .format(hours, total - volume))