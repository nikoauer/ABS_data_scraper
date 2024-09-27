import requests
import re
from bs4 import BeautifulSoup
import ABS_2016_functions
import ABS_2021_functions
import Professions_scrapers
from flask import Flask, jsonify

app = Flask(__name__)

# scrape the whole website
def scrape_abs_data(url):
    # Send request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Determine whether to process 2016 or 2021 data based on the URL
    if '2016' in url:
        return process_2016_data(soup)
    elif '2021' in url:
        return process_2021_data(soup)
    else:
        {"error": "The year could not be determined from the URL."}

# this function manages all the functions to retrieve all the 2016 data and collects the results in one spot
def process_2016_data(soup):
    # Find the table related to 'Median weekly incomes'
    weekly_household_income = ABS_2016_functions.median_weekly_income_2016(soup)
    professionals = Professions_scrapers.no_of_Professionals(soup)
    household_rent_payment = ABS_2016_functions.rent_weekly_payments_2016(soup)
    mortage_repayments = ABS_2016_functions.mortage_repayments_2016(soup)
    total_data = [weekly_household_income, professionals, household_rent_payment, mortage_repayments]
    return total_data

# this function manages all the functions to retrieve all the 2021 data and collects the results in one spot
def process_2021_data(soup):
    weekly_household_income = ABS_2021_functions.median_weekly_income_2021(soup)
    professionals = Professions_scrapers.no_of_Professionals(soup)
    household_rent_payment = ABS_2021_functions.rent_weekly_payments_2021(soup)
    mortage_repayments = ABS_2021_functions.mortage_repayments_2021(soup)
    total_data = [weekly_household_income, professionals, household_rent_payment, mortage_repayments]
    return total_data


# Flask route for scraping 2016 and 2021 data
@app.route('/census/<int:sa2_code>', methods=['GET'])
def get_census_data(sa2_code):
    # URLs for the census data based on SA2 code
    url_2016 = f"https://www.abs.gov.au/census/find-census-data/quickstats/2016/{sa2_code}"
    url_2021 = f"https://www.abs.gov.au/census/find-census-data/quickstats/2021/{sa2_code}"

    # Scraping 2016 and 2021 data
    abs_data_2016 = scrape_abs_data(url_2016)
    abs_data_2021 = scrape_abs_data(url_2021)

    # Return JSON response with both 2016 and 2021 data
    return jsonify({
        "2016": abs_data_2016,
        "2021": abs_data_2021
    })

if __name__ == "__main__":
    app.run(debug=False)
