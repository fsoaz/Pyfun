# Remeber My trial
# This app will remind users when their trial period for a service is about to expire
# Trial Tracking: Create a list of services with their trial start and end dates.
# Notifications: Send an email to the user as a reminder before their trial expires.
# Simple Interface: The app will have a clean and easy-to-use design.
# No Login Required: There will be no need for a password or user ID.


# Service Name
# User Email
# Start date
# End Date (This could be entered manually or calculated by selecting the number of trial days)

import datetime

# List of dictionaries of services

def get_user_info():
    while True:
        name = input("Tell me your name: ").strip().lower()
        if name:
            break
        else:
            print("Please enter your name")

    while True:
        email = input("Enter your email: ").strip()
        if "@" in email and "." in email and email.count("@") == 1 and len(email) > 5:
            break
        else:
            print("Please enter a valid email address.")

    return name, email

def parse_date(prompt):
    """
    Gets a date from user input with validation.
    
    Args:
        prompt: The message to show the user
    
    Returns:
        A date object in the format dd/mm/yyyy
    """
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            print("❌ Please enter the date in the correct format (dd/mm/yyyy).")

def get_service_info():
    while True:
        service_name = input("Tell me what service do you use: ").lower().strip()
        if service_name:
            break
        else:
            print("Please enter a service name")
#insert second loop instead recursion
    while True:
        start_date = parse_date("Start date (dd/mm/yyyy): ")
        end_date = parse_date("End date (dd/mm/yyyy): ")

        # Ensure trial dates make sense
        if end_date <= start_date:
            print("⚠️ End date must be after start date. Please try again.")
            # Continue the loop instead of recursion
        else:
            break
    
    return service_name, start_date, end_date

def check_expirations(services, days_before=3):
    """
    Check each service and print a reminder if it's close to expiring.
    
    Args:
        services: list of dictionaries with trial info
        days_before: how many days in advance to warn
    """
    today = datetime.date.today()
    for s in services:
        days_left = (s['end_date'] - today).days
        if days_left <= days_before:
            print(f"⚠️ Reminder: {s['service_name'].title()} trial ends in {days_left} day(s)! "
                  f"({s['end_date']})")
        else:
            print(f"✅ {s['service_name'].title()} is safe for now ({days_left} days left).")

#add save data ti a file but not yet

def main():
    """
    Collects user and service trial information, stores it, and displays the collected data.
    Note: This function collects information for only a single service per run.
    """
    name, email = get_user_info()
    services = []

    while True:
        service_name, start_date, end_date = get_service_info()

        # Store in list of dictionaries    
        services.append({
            "service_name": service_name,
            "start_date": start_date,
            "end_date": end_date,
            "user_email": email
        })
        
        another = input("\nAdd another service? (yes/no): ").strip().lower()
        if another not in ("yes", "y"):
            break

    print("\n📋 Services list so far:")
    print("\n✅ Info collected successfully:")
    print(f"User: {name} ({email})")

    for s in services:
        print(f"Service: {s['service_name'].title()} | Trial: {s['start_date']} ➝ {s['end_date']} | User Email: {s['user_email']}")

    # 🔔 New feature here
    print("\n🔔 Expiration check:")
    check_expirations(services, days_before=3)

if __name__ == "__main__":
    main()