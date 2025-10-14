def convert_currency(amount, source, target):
    if source == "USD" and target == "EUR":
        return amount * 0.86
    elif source == "USD" and target == "CAD":
        return amount * 1.4
    elif source == "EUR" and target == "USD":
        return amount * 1.15
    elif source == "EUR" and target == "CAD":
        return amount * 1.6
    elif source == "CAD" and target == "USD":
        return amount * 0.71
    elif source == "CAD" and target == "EUR":
        return amount * 0.61
    else:
        return amount  # No conversion needed if source and target are the same


currency_amt = float(input("Enter the amount: "))
currency_src = input("Source currency (USD/EUR/CAD): ").upper()

if currency_src == "USD":
    print(f"{currency_amt:.2f} {currency_src} is equal to {currency_amt * 0.86:.2f} EUR")
    print(f"{currency_amt:.2f} {currency_src} is equal to {currency_amt * 1.4:.2f} CAD")
elif currency_src == "EUR":
    print(f"{currency_amt:.2f} {currency_src} is equal to {currency_amt * 1.15:.2f} USD")
    print(f"{currency_amt:.2f} {currency_src} is equal to {currency_amt * 1.6:.2f} CAD")
elif currency_src == "CAD":
    print(f"{currency_amt:.2f} {currency_src} is equal to {currency_amt * 0.71:.2f} USD")
    print(f"{currency_amt:.2f} {currency_src} is equal to {currency_amt * 0.61:.2f} EUR")

currency_tgt = input("Target currency (USD/EUR/CAD): ").upper()

converted_amount = convert_currency(currency_amt, currency_src, currency_tgt)

print(f"{currency_amt:.2f} {currency_src} is equal to {converted_amount:.2f} {currency_tgt}")
