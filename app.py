def bond_price(face_value, coupon_rate, ytm, years_to_maturity):
    """
    Calculate the price of a bond.

    Parameters:
    face_value (float): The face value (par value) of the bond, typically $1000.
    coupon_rate (float): The annual coupon rate as a decimal (e.g., 5% = 0.05).
    ytm (float): The yield to maturity as a decimal (e.g., 5% = 0.05).
    years_to_maturity (int): The number of years remaining until maturity.

    Returns:
    float: The price of the bond.
    """
    # Annual coupon payment
    coupon_payment = face_value * coupon_rate

    # Calculate the present value of the coupon payments
    coupon_pv = sum([coupon_payment / (1 + ytm)**t for t in range(1, years_to_maturity + 1)])

    # Calculate the present value of the face value at maturity
    face_value_pv = face_value / (1 + ytm)**years_to_maturity

    # Bond price is the sum of the present value of the coupons and face value
    bond_price = coupon_pv + face_value_pv

    return bond_price


# Example usage:
face_value = 1000  # Face value of the bond (typically $1,000)
coupon_rate = 0.05  # Coupon rate (5%)
ytm = 0.04  # Yield to maturity (4%)
years_to_maturity = 10  # Years to maturity

price = bond_price(face_value, coupon_rate, ytm, years_to_maturity)
print(f"The bond price is: ${price:.2f}")
