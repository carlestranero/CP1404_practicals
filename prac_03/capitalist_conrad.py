"""CP1404 | randoms.py | Carl Estranero
This function is a stock price simulator that outputs the output to a file."""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "capitalist_conrad.txt"
number_of_days = 0


price = INITIAL_PRICE

out_file = open(OUTPUT_FILE, 'w')
print(f"Starting price: ${price:,.2f}", file=out_file)
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: {price:,.2f}", file=out_file)
out_file.close()