def cel_to_fharen(cel):
    fha = ( cel*(9/5))+32
    print(f"Fahrenheit = {fha}")

cel = int(input("Enter temperature in celsius : "))

cel_to_fharen(cel)

