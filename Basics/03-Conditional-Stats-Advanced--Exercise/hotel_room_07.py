month = input()
nights = int(input())

st_price = 0
ap_price = 0

if month in ['May', 'October']:
    st_price = nights * 50
    ap_price = nights * 65
    if nights > 14:
        st_price -= st_price * 0.3
        ap_price -= ap_price * 0.1
    elif nights > 7:
        st_price -= st_price * 0.05

elif month in ['June', 'September']:
    st_price = nights * 75.20
    ap_price = nights * 68.70
    if nights > 14:
        st_price -= st_price * 0.2
        ap_price -= ap_price * 0.1

elif month in ['July', 'August']:
    st_price = nights * 76
    ap_price = nights * 77
    if nights > 14:
        ap_price -= ap_price * 0.1

print(f'Apartment: {ap_price:.2f} lv.')
print(f'Studio: {st_price:.2f} lv.')
