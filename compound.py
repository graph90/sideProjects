def calculate_compound_interest(principal, rate, time, n=1):
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / n) ** (n * time)
    return amount

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

total_amount = calculate_compound_interest(principal, rate, time, n)
compound_interest = total_amount - principal

print(f"\nTotal amount after {time} years: ${total_amount:.2f}")
print(f"Compound interest earned: ${compound_interest:.2f}")
