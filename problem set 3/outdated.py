def main():
    months = ["January","February",
        "March","April","May","June","July","August",
        "September","October","November","December"]

    while True:
        date_str = input("Date: ")

        # Try format 1: month/day/year
        if "/" in date_str:
            parts = date_str.split('/')
            if len(parts) == 3:
                try:
                    month = int(parts[0])
                    day = int(parts[1])
                    year = int(parts[2])
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        formatted_month = f"{month:02}"
                        formatted_day = f"{day:02}"
                        print(f"{year}-{formatted_month}-{formatted_day}")
                        break  
                except ValueError:
                    pass  

        # Try format 2: Month Day, Year
        elif ',' in date_str:
            parts = date_str.replace(',','').split()
            if len(parts) == 3: # handle cases like "September 8,1636" by just checking for at least 3 parts after comma removal and split
                month_str = parts[0]
                day_str = parts[1]
                year_str = parts[2] 

                if month_str in months:
                    try:
                        day = int(day_str)
                        year = int(year_str)
                        if 1 <= day <= 31 and year >= 0:
                            month = months.index(month_str) + 1 # month number is index + 1
                            formatted_month = f"{month:02}"
                            formatted_day = f"{day:02}"
                            print(f"{year}-{formatted_month}-{formatted_day}")
                            break  
                    except ValueError:
                        pass
main()