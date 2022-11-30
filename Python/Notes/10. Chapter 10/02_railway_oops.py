import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

MiskatursApplication = RailwayForm()
MiskatursApplication.name = "Miskatur"
MiskatursApplication.train = "Rajdhani Express"
MiskatursApplication.printData()