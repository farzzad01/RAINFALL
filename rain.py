NUM_MONTHS = 12

MONTH_NAMES = [
    "Farvardin", "Ordibehesh", "Khordad", "Tir", "Amordad", "Shahriver",
    "Mehr", "Aban", "Azar", "Day", "Bahman", "Esfand"
]

def enterRainfall(rainfall, numYears):
    for year in range(numYears):
        for month in range(NUM_MONTHS):
            rainfall[year][month] = float(input("Enter the rainfall for year {}, month {}: ".format(year + 1, MONTH_NAMES[month])))
        print("-----------------------------\n")

def show_Rainfall(rainfall, numYears):
    print("Rainfall information for all entered years:")
    for year in range(numYears):
        for month in range(NUM_MONTHS):
            print("Year --> {}, Month --> {}: {}".format(year + 1, MONTH_NAMES[month], rainfall[year][month]))
            print("-----------------------------\n")

def show_YearlyRainfall(rainfall, numYears):
    selectedYear = int(input("Enter the year: "))
    selectedMonth = input("Enter the month: ")

    monthIndex = MONTH_NAMES.index(selectedMonth.title())
    selectedRainfall = rainfall[selectedYear - 1][monthIndex]
    print("-----------------------------\n")
    print("Rainfall for year --> {}, month --> {}: {}".format(selectedYear, selectedMonth, selectedRainfall))
    print("-----------------------------\n")

def show_RainiestYear(rainfall, numYears):
    maxRainfall = 0
    maxYear = 0
    for year in range(numYears):
        totalRainfall = sum(rainfall[year])
        if totalRainfall > maxRainfall:
            maxRainfall = totalRainfall
            maxYear = year + 1
    print("-----------------------------\n")
    print("Rainiest year --> {}".format(maxYear))
    print("-----------------------------\n")

def show_RainiestMonth(rainfall, numYears):
    maxRainfall = 0
    maxMonth = 0
    for month in range(NUM_MONTHS):
        totalRainfall = sum(rainfall[year][month] for year in range(numYears))
        if totalRainfall > maxRainfall:
            maxRainfall = totalRainfall
            maxMonth = month + 1
    print("-----------------------------\n")
    print("Rainiest month: {}".format(MONTH_NAMES[maxMonth - 1]))
    print("Total rainfall: {}".format(maxRainfall))
    print("-----------------------------\n")

def show_AverageRainfall(rainfall, numYears):
    for year in range(numYears):
        totalRainfall = sum(rainfall[year])
        averageRainfall = totalRainfall / NUM_MONTHS
        print("-----------------------------\n")
        print("Average rainfall for year --> {}: {}".format(year + 1, averageRainfall))
        print("-----------------------------\n")

numYears = int(input("Enter the number of years: "))
print("-----------------------------\n")

rainfall = [[0] * NUM_MONTHS for _ in range(numYears)]

choice = 0
while choice != 7:
    print("Choice Menu:")
    print("1. Enter rainfall information")
    print("2. Show rainfall information for all entered years")
    print("3. Show rainfall for a specific year and month")
    print("4. Show the rainiest year")
    print("5. Show the rainiest month")
    print("6. Show average rainfall for each year")
    print("7. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        enterRainfall(rainfall, numYears)
    elif choice == 2:
        show_Rainfall(rainfall, numYears)
    elif choice == 3:
        show_YearlyRainfall(rainfall, numYears)
    elif choice == 4:
        show_RainiestYear(rainfall, numYears)
    elif choice == 5:
        show_RainiestMonth(rainfall, numYears)
    elif choice == 6:
        show_AverageRainfall(rainfall, numYears)
    elif choice == 7:
        print("Exit")
    else:
        print("Please try again.")
