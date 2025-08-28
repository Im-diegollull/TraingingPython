# Input values
luz = float(input("CUANTO SALIÓ LA LUZ: "))
agua = float(input("CUANTO SALIÓ EL AGUA: "))
gc = float(input("CUANTO SALIERON LOS GASTOS COMUNES: "))
wifi = float(input("CUANTO SALIÓ EL WIFI: "))
gas = float(input("CUANTO SALIÓ EL GAS: "))

# Format agua value to 3 decimal places
agua_ = f"{agua:.3f}"
gas_ = f"{gas:.3f}"
wifi_ = f'{wifi:.3f}'

# Calculate total
total = luz + agua + gc + wifi + gas
total_ = f"{total:.3f}"


# Calculate deuda_cada_uno (debt per person)
deuda_cada_uno = total / 4
deuda = f"{deuda_cada_uno:.3f}"

# Print results
print("++++++++++++++++++++++++\n")
print(f"LUZ SALIÓ = {luz}")
print(f"AGUA SALIÓ = {agua_}")
print(f"Gastos Comunes Salieron = {gc}")
print(f"Wifi SALIÓ = {wifi_}")
print(f"GAS SALIÓ = {gas_}")
print(f"Total = {total_}")
print(f"C/U DEBE = {deuda}")