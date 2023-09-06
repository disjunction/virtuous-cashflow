import math
import pandas as pd
from random import random, seed

def random_for_month(year: int, month_index: int) -> float:
    seed(year * 12 + month_index)
    return random()

class GenerationModel:
    """ Simulates energy generation of a power plant """
    def __init__(self,
            start_year: int,         # in which year the plant was built
            peak_energy: float,      # energy production per month in best conditions
            degradation: float,      # how much panels degrade per month (as unit interval)
            seasonality: float,      # interval 0..1, 0 - winter has no effect, 1 - in winter there is no sun at all
            uncertainty: float = 0.1 # interval 0..1, how much production varies from a mean expected value
            ) -> None:
        self.start_year = start_year
        self.peak_energy = peak_energy
        self.degradation = degradation
        self.seasonality = seasonality
        self.uncertainty = uncertainty

    def calculate_month (self, year: int, month_index: int) -> float:
        """
        Calculates energy  produced within a specific month
        month_index starts with 0 for Jan
        """
        month_in_year = month_index / 12
        irradiance_scale = (1 - math.cos((month_in_year - 0.5) * 2 * math.pi)) / 2
        base_value = self.peak_energy * (1 - self.seasonality * irradiance_scale)

        # apply degradation
        months_passed = (year - self.start_year) * 12 + month_in_year
        base_value *= 1 - months_passed * self.degradation

        # apply pseudo-random deviation based on uncertainty
        seed(year * 12 + month_index)
        return base_value * (1 + self.uncertainty * 2 * random() - self.uncertainty)

    def calculate_year (self, year: int) -> pd.DataFrame:
        """
        Generates a DataFrame containing monthly time series of energy produced for each month
        """
        monthly_dates = pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31', freq='M')
        data = {
            'date': monthly_dates,
            'energy': [self.calculate_month(year=year, month_index=m) for m in range(12)],
        }
        df = pd.DataFrame(data)
        df.set_index('date', inplace=True)
        return df
