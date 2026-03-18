print("Trading tracker")

# Me kriju ni tracker qe i track sa trades i kom bo gjat ni
# javes edhe sa fitore e sa humbje edhe sa pip fitim sa humbje"


def number_of_days():
    days_add = int(
        input("Write the number of days you want to add this week: "))
    return days_add


def days_of_week():
    # maybe a lit here to save days
    for nr in range(number_of_days()):
        days = input("Write your day: ")
    return days
