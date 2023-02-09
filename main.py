import csv, os

from district import District
from covid19 import COVID19Uganda

c = COVID19Uganda()

def add_district():
    district_name = input("Enter district name: ")
    cases = int(input("Enter number of confirmed cases: "))
    hospitalizations = int(input("Enter number of hospitalizations: "))
    deaths = int(input("Enter number of deaths: "))

    d = District(district_name, cases, hospitalizations, deaths)
    c.add_district(d)

def save_data():
    if not os.path.exists("covid19_data.csv"):
        with open("covid19_data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["District Name", "Confirmed Cases", "Hospitalizations", "Deaths"])
    
    with open("covid19_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["District Name", "Confirmed Cases", "Hospitalizations", "Deaths"])
        for district in c.districts:
            writer.writerow([district.name, district.cases, district.hospitalizations, district.deaths])

    print("Data saved to covid19_data.csv")

def get_district_data(district):
    print("\n Total data for your choosen district")
    print(c.get_district_data(district))

def show_total_data():
    print("\nTotal COVID-19 data for all districts:")
    print(c.get_total_data())

def show_average_data():
    print("\nAverage COVID-19 data for all districts:")
    print(c.get_average_data())


def read_data_from_csv(filename):
    districts = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader) # skip the header row
        for row in reader:
            district_name = row[0]
            cases = int(row[1])
            hospitalizations = int(row[2])
            deaths = int(row[3])
            district = District(district_name, cases, hospitalizations, deaths)
            districts.append(district)

    return districts

while True:
    print("\nMenu:")
    print("1. Add District")
    print("2. Save Data")
    print("3. Get Specific District Data")
    print("4. Show Total Data")
    print("5. Show Average Data")
    print("6. Read Data from CSV")
    print("Q. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_district()
    elif choice == "2":
        save_data()
    elif choice == "3":
        district = input("Enter your preferred district...")
        get_district_data(district)
    elif choice == "4":
        show_total_data()
    elif choice == "5":
        show_average_data()
    # elif choice == "6":
    #     d = read_data_from_csv("covid19_data.csv")
    #     c = COVID19Uganda()
    #     print(c.get_total_data())
    elif choice.upper() == "Q":
        break
    else:
        print("Invalid choice.")

