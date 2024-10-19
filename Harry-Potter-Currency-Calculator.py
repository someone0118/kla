import requests

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # API for exchange rate
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['rates']['THB']
    else:
        print("!!! Cannot exchange because no data available !!!")
        return None

state_tax_rates = {
    1: ('Alabama', 0.04),
    2: ('Alaska', 0.00),
    3: ('Arizona', 0.056),
    4: ('Arkansas', 0.065),
    5: ('California', 0.0725),
    6: ('Colorado', 0.029),
    7: ('Connecticut', 0.0635),
    8: ('Delaware', 0.00),
    9: ('Florida', 0.06),
    10: ('Georgia', 0.04),
    11: ('Hawaii', 0.04),
    12: ('Idaho', 0.06),
    13: ('Illinois', 0.0625),
    14: ('Indiana', 0.07),
    15: ('Iowa', 0.06),
    16: ('Kansas', 0.065),
    17: ('Kentucky', 0.06),
    18: ('Louisiana', 0.0445),
    19: ('Maine', 0.055),
    20: ('Maryland', 0.06),
    21: ('Massachusetts', 0.0625),
    22: ('Michigan', 0.06),
    23: ('Minnesota', 0.06875),
    24: ('Mississippi', 0.07),
    25: ('Missouri', 0.04225),
    26: ('Montana', 0.00),
    27: ('Nebraska', 0.055),
    28: ('Nevada', 0.0685),
    29: ('New Hampshire', 0.00),
    30: ('New Jersey', 0.06625),
    31: ('New Mexico', 0.05125),
    32: ('New York', 0.04),
    33: ('North Carolina', 0.0475),
    34: ('North Dakota', 0.05),
    35: ('Ohio', 0.0575),
    36: ('Oklahoma', 0.045),
    37: ('Oregon', 0.00),
    38: ('Pennsylvania', 0.06),
    39: ('Rhode Island', 0.07),
    40: ('South Carolina', 0.06),
    41: ('South Dakota', 0.045),
    42: ('Tennessee', 0.07),
    43: ('Texas', 0.0625),
    44: ('Utah', 0.0485),
    45: ('Vermont', 0.06),
    46: ('Virginia', 0.053),
    47: ('Washington', 0.065),
    48: ('West Virginia', 0.06),
    49: ('Wisconsin', 0.05),
    50: ('Wyoming', 0.04),
    51: ('District of Columbia', 0.06)
}

while True:
    print("Harry Potter Currency Calculator")
    
    try:
        g = float(input("Enter Galleons: "))
        if g < 0:
            print("!!! Please enter a non-negative value.")
            continue
            
        s = float(input("Enter Sickles: "))
        if s < 0:
            print("!!! Please enter a non-negative value.")
            continue
            
        k = float(input("Enter Knuts: "))
        if k < 0:
            print("!!! Please enter a non-negative value.")
            continue

        # Convert Harry Potter currency to USD
        galleon_to_usd = g * 7
        sickle_to_usd = (s / 17) * 7
        knut_to_usd = (k / 493) * 7
        total_usd = galleon_to_usd + sickle_to_usd + knut_to_usd

        # Get exchange rate
        exchange_rate = get_exchange_rate()
        
        if exchange_rate is not None:
            print("Please choose a state in the USA for tax:")
            for key, (state, rate) in state_tax_rates.items():
                print(f"{key}. {state} (Tax Rate: {rate * 100:.2f}%)")

            state_choice = int(input("Enter the number of your state: "))
            if state_choice in state_tax_rates:
                state_name, tax_rate = state_tax_rates[state_choice]
                total_usd_with_tax = total_usd * (1 + tax_rate)

                # Convert to Thai Baht
                total_bath = total_usd_with_tax * exchange_rate
                print(f"Total after tax in {state_name}: {total_usd_with_tax:.2f} USD")
                print(f"Exchange Harry Potter Currency To THB in {state_name}: {total_bath:.2f}\n")
            else:
                print("!!! Invalid choice. No tax applied. !!!")
        else:
            print("!!! Could not retrieve exchange rate. Please try again.\n!!!")

    except ValueError:
        print("!!! Please enter valid numeric values.\n!!!")
    except KeyboardInterrupt:
        print("\nExiting the calculator. Goodbye!")
        break
