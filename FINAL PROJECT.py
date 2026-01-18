from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(Fore.CYAN + prompt))
            if value <= 0:
                print(Fore.RED + "Value must be positive!")
            else:
                return value
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")

def get_readings(label):
    readings = []
    print(Fore.MAGENTA + f"\nEnter {label} voltage readings")
    count = int(get_positive_float("How many readings? "))

    for i in range(count):
        value = get_positive_float(f"Reading {i + 1}: ")
        readings.append(value)

    return readings

def average(values):
    return sum(values) / len(values)

# Header
print(Fore.YELLOW + Style.BRIGHT + "==============================================")
print(Fore.YELLOW + Style.BRIGHT + "  POWER SUPPLY PERFORMANCE & RIPPLE ANALYZER  ")
print(Fore.YELLOW + Style.BRIGHT + "==============================================")

# No-load and full-load readings
vnl = get_readings("NO-LOAD")
vfl = get_readings("FULL-LOAD")

vnl_avg = average(vnl)
vfl_avg = average(vfl)

# Ripple measurements
print(Fore.MAGENTA + "\nEnter ripple voltage values")
vmax = get_positive_float("Maximum voltage (Vmax): ")
vmin = get_positive_float("Minimum voltage (Vmin): ")

vr_pp = vmax - vmin
vr_rms = vr_pp / 2.828
ripple_factor = vr_rms / vfl_avg

# Calculations
voltage_drop = vnl_avg - vfl_avg
load_regulation = (voltage_drop / vfl_avg) * 100

# Grading
if load_regulation < 5 and ripple_factor < 0.05:
    grade = Fore.GREEN + "A (Excellent)"
elif load_regulation < 10 and ripple_factor < 0.10:
    grade = Fore.BLUE + "B (Good)"
elif load_regulation < 15:
    grade = Fore.YELLOW + "C (Fair)"
else:
    grade = Fore.RED + "D (Poor)"

# Report
report = f"""
{Fore.CYAN}POWER SUPPLY ANALYSIS REPORT
----------------------------
No-Load Voltage (avg):   {vnl_avg:.2f} V
Full-Load Voltage (avg): {vfl_avg:.2f} V
Voltage Drop:            {voltage_drop:.2f} V
Load Regulation:         {load_regulation:.2f} %

Ripple Peak-to-Peak:     {vr_pp:.2f} V
Ripple RMS Voltage:      {vr_rms:.3f} V
Ripple Factor:           {ripple_factor:.4f}

Overall Grade:           {grade}
"""

print(report)

