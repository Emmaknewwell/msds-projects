import requests,csv
class COVID19Statistics:
    def __init__(self, country_name, cases, deaths, region, total_recovered, new_deaths, new_cases, serious_critical, active_cases, total_cases_per_1m_population):
        self.__country_name = country_name
        self.__cases = cases
        self.__deaths = deaths
        self.__region = region
        self.__total_recovered = total_recovered
        self.__new_deaths = new_deaths
        self.__new_cases = new_cases
        self.__serious_critical = serious_critical
        self.__active_cases = active_cases
        self.__total_cases_per_1m_population = total_cases_per_1m_population
    
    @property
    def country_name(self):
        return self.__country_name
    
    @country_name.setter
    def country_name(self, country_name):
        self.__country_name = country_name
    
    @property
    def cases(self):
        return self.__cases
    
    @cases.setter
    def cases(self, cases):
        self.__cases = cases
    
    @property
    def deaths(self):
        return self.__deaths
    
    @deaths.setter
    def deaths(self, deaths):
        self.__deaths = deaths
    
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region):
        self.__region = region
    
    @property
    def total_recovered(self):
        return self.__total_recovered
    
    @total_recovered.setter
    def total_recovered(self, total_recovered):
        self.__total_recovered = total_recovered
    
    @property
    def new_deaths(self):
        return self.__new_deaths
    
    @new_deaths.setter
    def new_deaths(self, new_deaths):
        self.__new_deaths = new_deaths
    
    @property
    def new_cases(self):
        return self.__new_cases
    
    @new_cases.setter
    def new_cases(self, new_cases):
        self.__new_cases = new_cases
    
    @property
    def serious_critical(self):
        return self.__serious_critical
    
    @serious_critical.setter
    def serious_critical(self, serious_critical):
        self.__serious_critical = serious_critical
    
    @property
    def active_cases(self):
        return self.__active_cases
    
    @active_cases.setter
    def active_cases(self, active_cases):
        self.__active_cases = active_cases
    
    @property
    def total_cases_per_1m_population(self):
        return self.__total_cases_per_1m_population
    
    @total_cases_per_1m_population.setter
    def total_cases_per_1m_population(self, total_cases_per_1m_population):
        self.__total_cases_per_1m_population = total_cases_per_1m_population


    def fetch_covid19_data(self):
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
        headers = {
            "X-RapidAPI-Key": "90165b2056msh5218e1ec6e762c2p1b30b0jsn0b7be9272e36",
            "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            # print(data)

            for country in data['countries_stat']:
                print(f"Country: {country['country_name']}")
                print(f"Total cases: {country['cases']}")
                print(f"Total deaths: {country['deaths']}")
                print(f"Total recovered: {country['total_recovered']}")
                print(f"Total Cases per 1m Population: {country['total_cases_per_1m_population']}")
                print("---" * 20)

            
        else:
            print("Request failed with status code: ", response.status_code)


    def export_to_csv(self, data):
        print("Adding data to the csv file...")
        with open("covid19_stats.csv", "w", newline="") as csvfile:
            fieldnames = ["Country", "Cases", "Deaths", "Recovered"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for country in data['countries_stat']:
                writer.writerow({
                    "Country": country['country_name'],
                    "Cases": country['cases'],
                    "Deaths": country['deaths'],
                    "Recovered": country['total_recovered']
                })