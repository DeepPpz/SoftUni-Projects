length = float(input())
input_metric = input().lower()
output_metric = input().lower()

if input_metric == 'mm':
    length /= 1000
elif input_metric == 'cm':
    length /= 100
elif input_metric == 'mi':
    length /= 0.000621371192
elif input_metric == 'in':
    length /= 39.3700787
elif input_metric == 'km':
    length /= 0.001
elif input_metric == 'ft':
    length /= 3.2808399
elif input_metric == 'yd':
    length /= 1.0936133

if output_metric == 'mm':
    length *= 1000
elif output_metric == 'cm':
    length *= 100
elif output_metric == 'mi':
    length *= 0.000621371192
elif output_metric == 'in':
    length *= 39.3700787
elif output_metric == 'km':
    length *= 0.001
elif output_metric == 'ft':
    length *= 3.2808399
elif output_metric == 'yd':
    length *= 1.0936133

print(length)