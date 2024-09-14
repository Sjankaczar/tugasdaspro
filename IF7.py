def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def day_of_year(day, month_name, year):
    # List of month names
    names_of_month = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]
    # Create a dictionary to map month names to their corresponding numbers
    month_to_number = {month: index + 1 for index, month in enumerate(names_of_month)}
    # Get the month number from the dictionary
    month_number = month_to_number.get(month_name, "Invalid month name")
    # Days in each month for a non-leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust for leap year
    if is_leap_year(year):
        days_in_month[1] = 29

    # Calculate the day number
    day_number = sum(days_in_month[:month_number - 1]) + day
    return day_number

# Example usage
day = int(input("Masukkan hari (1-31): "))
month_name = input("Masukkan nama bulan: ").lower()
year = int(input("Masukkan tahun: "))

day_number = day_of_year(day, month_name, year)
print(f"nomor hari untuk {day}/{month_name}/{year} adalah {day_number}.")
