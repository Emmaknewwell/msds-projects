class District:
    def __init__(self, name, cases, hospitalizations, deaths):
        self.name = name
        self.cases = cases
        self.hospitalizations = hospitalizations
        self.deaths = deaths

    def __str__(self):
        return f"District: {self.name}, Confirmed Cases: {self.cases}, Hospitalizations: {self.hospitalizations}, Deaths: {self.deaths}"
