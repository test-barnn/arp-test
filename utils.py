def calculate_discount(price, rate):
    # BUG: no validation, returns negative for rate > 1
    discount = price * rate
    return price - discount
```
