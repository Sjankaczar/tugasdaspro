def calculate_bill(weekday_minutes, night_minutes, weekend_minutes):
    # Constants
    base_rate_cents = 3999  # $39.99 in cents
    included_weekday_minutes = 600
    additional_minute_rate_cents = 40  # $0.40 in cents
    tax_rate = 0.0525

    # Calculate additional weekday minutes
    additional_minutes = max(0, weekday_minutes - included_weekday_minutes)
    additional_charges_cents = additional_minutes * additional_minute_rate_cents

    # Calculate pretax bill
    pretax_bill_cents = base_rate_cents + additional_charges_cents

    # Calculate taxes
    taxes_cents = round(pretax_bill_cents * tax_rate)

    # Calculate total bill
    total_bill_cents = pretax_bill_cents + taxes_cents

    # Calculate average cost per minute before taxes
    total_minutes = weekday_minutes + night_minutes + weekend_minutes
    average_cost_per_minute_cents = round(pretax_bill_cents / total_minutes)

    # Convert cents to dollars for display
    pretax_bill_dollars = pretax_bill_cents / 100
    taxes_dollars = taxes_cents / 100
    total_bill_dollars = total_bill_cents / 100
    average_cost_per_minute_dollars = average_cost_per_minute_cents / 100

    return (pretax_bill_dollars, average_cost_per_minute_dollars, taxes_dollars, total_bill_dollars)

# Example usage
weekday_minutes = int(input("Enter the number of weekday minutes used: "))
night_minutes = int(input("Enter the number of night minutes used: "))
weekend_minutes = int(input("Enter the number of weekend minutes used: "))

pretax_bill, average_cost_per_minute, taxes, total_bill = calculate_bill(weekday_minutes, night_minutes, weekend_minutes)

print(f"Weekday minutes: {weekday_minutes}")
print(f"Night minutes: {night_minutes}")
print(f"Weekend minutes: {weekend_minutes}")
print(f"Pretax bill: ${pretax_bill:.2f}")
print(f"Average cost per minute (before taxes): ${average_cost_per_minute:.2f}")
print(f"Taxes: ${taxes:.2f}")
print(f"Total bill: ${total_bill:.2f}")
