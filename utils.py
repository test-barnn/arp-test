def calculate_discount(price, rate):
    # Validate inputs
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    if rate > 1:
        raise ValueError("Rate cannot be greater than 1")
    
    # Calculate discount
    discount = price * rate
    return discount
