import pandas as pd

class FinancialModel:
    def __init__(self,
            start_year: int,         # year the plant has been built
            energy_price: float,     # price for a unit of produced energy
            cleaning_cost: float,    # cleaning cost in January and July of each year
            maintenance_cost: float, # maintenance costs every 4 years in January
            ) -> None:
        self.start_year = start_year
        self.energy_price = energy_price
        self.cleaning_cost = cleaning_cost
        self.maintenance_cost = maintenance_cost

    def extend_with_financial (self, monthly_data: pd.DataFrame, year: int) -> pd.DataFrame:
        """
        Takes DataFrame produced by GenerationModel
        and adds the costs and revenue to it producing a new DataFrame
        """
        year_index = year - self.start_year
        additional = {
            'cleaning_cost': [],
            'maintenance_cost': [],
            'revenue': [],
        }
        for index, row in monthly_data.iterrows():
            month = index.date().month
            energy = row['energy']
            additional['cleaning_cost'].append(-self.cleaning_cost if month == 7 or month == 1 else 0)
            additional['maintenance_cost'].append(
                -self.maintenance_cost
                if month == 1 and year_index > 0 and year_index % 4 == 0
                else 0)
            additional['revenue'].append(energy * self.energy_price)

        result = pd.DataFrame(monthly_data)

        for name, data in additional.items():
            result[name] = data

        return result
