conv_sum = float(input())
in_curr = input()
out_curr = input()


if in_curr == 'BGN':
    if out_curr == 'USD':
        conv_sum /= 1.79549
    elif out_curr == 'EUR':
        conv_sum /= 1.95583
    elif out_curr == 'GBP':
        conv_sum /= 2.53405

elif in_curr == 'USD':
    conv_sum *= 1.79549
    if out_curr == 'BGN':
        conv_sum = conv_sum
    elif out_curr == 'EUR':
        conv_sum /= 1.95583
    elif out_curr == 'GBP':
        conv_sum /= 2.53405

elif in_curr == 'EUR':
    conv_sum *= 1.95583
    if out_curr == 'BGN':
        conv_sum = conv_sum
    elif out_curr == 'USD':
        conv_sum /= 1.79549
    elif out_curr == 'GBP':
        conv_sum /= 2.53405

elif in_curr == 'GBP':
    conv_sum *= 2.53405
    if out_curr == 'BGN':
        conv_sum = conv_sum
    elif out_curr == 'USD':
        conv_sum /= 1.79549
    elif out_curr == 'EUR':
        conv_sum /= 1.95583

print(f'{conv_sum:.2f} {out_curr}')