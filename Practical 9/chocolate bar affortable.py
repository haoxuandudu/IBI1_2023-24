def calculate_chocolate_bars(total_money, price_per_bar):
    bars_affordable = total_money // price_per_bar
    change_left = total_money % price_per_bar
    return bars_affordable, change_left

# Example usage:
total_money = 100
price_per_bar = 7
bars, change = calculate_chocolate_bars(total_money, price_per_bar)
print(f"With {total_money} money, you can afford {bars} chocolate bars and have {change} left over.")
