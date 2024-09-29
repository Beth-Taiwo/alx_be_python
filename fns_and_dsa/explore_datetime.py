from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

no_of_days = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date(no_of_days):
    future_date = datetime.datetime.now() + timedelta(days=no_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
  