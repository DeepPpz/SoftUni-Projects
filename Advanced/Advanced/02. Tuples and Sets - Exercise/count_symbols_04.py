text = input()
symbols_dict = {}

for symbol in text:
    if symbol not in symbols_dict:
        symbols_dict[symbol] = 0
    symbols_dict[symbol] += 1

sorted_symbols = dict(sorted(symbols_dict.items(), key=lambda x: x[0]))

for (sym, value) in sorted_symbols.items():
    print(f"{sym}: {value} time/s")
