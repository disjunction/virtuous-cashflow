# Virtuous Cashflow - Interview Task

## Installation

1. Setup and activate virtual environment

2. Install requirements

```bash
pip install -r requirement.txt
```

3. Open the project in an IDE, e.g. in VisualStudio Code and use the same
virtual environment as the Python environment

4. When running Jupyter install the needed dependencies.
They are not part of `requirements.txt`


## Project description

The `virtuous` directory contains code for simulation of a solar power plant:
- `GenerationModel` can produce monthly time series for the energy produced
- `FinancialModel` can take this data and calculate the revenue for selling this
  energy and also estimate operational costs: maintenance and cleaning

The Jupyter Notebooks (see `notebooks`) folder use this models to produce concrete
results in the form of charts.

Your colleague has implemented the models and started working with notebooks,
when his work was interrupted. Now you need to take over the project and finish
it according to the tasks listed below.

You can change any code - both in notebooks or in models.

## Tasks


### Task 1

In `notebooks/one-year.ipynb` show the **financial** time series as a **stacked bar chart**
- costs are expected to be shown as negatives, revenues as positives
- X-axis should show months
- Y-axis should show money in EUR

### Task 2

In `notebooks/cashflow.ipynb` show the cashflow calculated for the next 20 years
(Currently there is only an example based on some hard coded values)

### Task 3

At the moment our solution uses a fixed energy price to calculate the revenues. We want
to use a CSV file `price_forecast.csv` as the source of prices for each year
and update the cashflow using this data.

### Task 4

Add a new chart showing a part of cashflow from 2025 to 2035 (inclusively) with
energy price curve on top of the cashflow bar chart for comparison (second Y-axis)
