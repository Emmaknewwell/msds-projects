from covid_stat import COVID19Statistics


def display_menu():
    print("COVID-19 Data Collection from API ")
    print("---" * 20)
    print("1. Make API call")
    print("2. Export data to CSV")
    print("3. Quit")
    print("---" * 20)

def quit_program():
    print("Quitting the program...")
    exit()

def main():
    covid19_data = COVID19Statistics('country_name', 'cases', 'deaths', 'region', 'total_recovered', 'new_deaths', 'new_cases', 'serious_critical', 'active_cases', 'total_cases_per_1m_population')
    
    data = None
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            data = covid19_data.fetch_covid19_data()
            print("Data collected successfully")
        elif choice == "2":
            data = covid19_data.fetch_covid19_data()
            if data is None:
                print("Please make an API call first")
            else:
                covid19_data.export_to_csv(data)
                print("Data exported successfully")
        elif choice in ["Q", "QUIT"]:
            quit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
