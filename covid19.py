import csv
class COVID19Uganda:
    def __init__(self):
        self.districts = []

    def add_district(self, district):
        self.districts.append(district)

    def get_district_data(self, district_name):
        with open("covid19_data.csv", "r") as f:
            reader = csv.reader(f)
            next(reader) # skip the header row
            for row in reader:
                if row[0] == district_name:
                    cases = int(row[1])
                    hospitalizations = int(row[2])
                    deaths = int(row[3])
                    return (cases, hospitalizations, deaths)

        return None

    def get_total_data(self):
        total_cases = 0
        total_hospitalizations = 0
        total_deaths = 0
        with open("cleaned_data.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)  # skip the header row
            if header != ["District Name", "Confirmed Cases", "Hospitalizations", "Deaths"]:
                raise ValueError("The header in the csv file is invalid")
            for row in reader:
                total_cases += int(row[1])
                total_hospitalizations += int(row[2])
                total_deaths += int(row[3])

        return total_cases, total_hospitalizations, total_deaths

    def get_average_data(self):
        total_cases, total_hospitalizations, total_deaths = self.get_total_data()
        district_count = len(self.districts)
        if district_count == 0:
            return (0, 0, 0)
        average_cases = total_cases / district_count
        average_hospitalizations = total_hospitalizations / district_count
        average_deaths = total_deaths / district_count

        return (average_cases, average_hospitalizations, average_deaths)

