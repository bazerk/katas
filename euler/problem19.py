import euler


def generate_days():
    current_date = euler.EulerDate(1, 1, 1900, 0)  # 1 Jan 1900 Monday
    while 1:
        yield current_date
        days_in_month = euler.days_in_month(current_date)
        day = current_date.day + 1
        month = current_date.month
        year = current_date.year
        weekday = (current_date.weekday + 1) % 7
        if day > days_in_month:
            day = 1
            month = month + 1
        if month > 12:
            year += 1
            month = 1
        current_date = euler.EulerDate(day, month, year, weekday)


def euler_problem19():
    count = 0
    for date in generate_days():
        if date.year > 2000:
            break
        if date.year >= 1901 and date.day == 1 and date.weekday == 6:
            count += 1
    return count


if __name__ == '__main__':
    print euler_problem19()
