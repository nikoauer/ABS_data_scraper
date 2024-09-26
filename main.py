import requests
import re
from bs4 import BeautifulSoup

# Find and return households where mortgage repayments are less than 30% of household from 2021 ABS data
def mortage_repayments_2021(soup):
    # find the row with mortage households spending under 30% on repayment
    mortage_repayment_title = soup.find('th', string='Renter households where rent payments are less than or equal to 30% of household income (b)')
    # if found, find the parent and extract the data for the state and suburb
    if mortage_repayment_title:
        mortage_row = mortage_repayment_title.find_parent('tr')
        mortage_data = mortage_row.find_all('td')
        Suburb_mortage_payments = float(mortage_data[1].get_text(strip=True))
        State_mortage_payments = float(mortage_data[3].get_text(strip=True))
        rent_metrics = {'suburb renter households where rent payments are less than or equal to 30% of household income (b)': Suburb_mortage_payments,
                                'state renter households where rent payments are less than or equal to 30% of household income (b)': State_mortage_payments}
        return rent_metrics
    else:
        print('Households where mortgage repayments are less than 30% of household income row could not be found')

# Find and return households where mortgage repayments are less than 30% of household from 2016 ABS data
def mortage_repayments_2016(soup):
    # find the row with mortage households spending under 30% on repayment
    mortage_repayment_title = soup.find('th', string='Households where mortgage repayments are less than 30% of household income')
    # if found, find the parent and extract the data for the state and suburb
    if mortage_repayment_title:
        mortage_row = mortage_repayment_title.find_parent('tr')
        mortage_data = mortage_row.find_all('td')
        Suburb_mortage_payments = float(mortage_data[1].get_text(strip=True))
        State_mortage_payments = float(mortage_data[3].get_text(strip=True))
        rent_metrics = {'suburb households where mortgage repayments are less than 30% of household income': Suburb_mortage_payments,
                                'state households where mortgage repayments are less than 30% of household income': State_mortage_payments}
        return rent_metrics
    else:
        print('Households where mortgage repayments are less than 30% of household income row could not be found')

# Find and return renter households where rent payments are less than or equal to 30% of household income from 2016 ABS data
def rent_weekly_payments_2016(soup):
    # find the row with renter households spending under 30%
    weekly_rent_title = soup.find('th', string='Households where rent payments are less than 30% of household income')
    # if found, find the parent and extract the data for the state and suburb
    if weekly_rent_title:
        rent_row = weekly_rent_title.find_parent('tr')
        rent_data = rent_row.find_all('td')
        Suburb_household_payments = float(rent_data[1].get_text(strip=True))
        State_household_payments = float(rent_data[3].get_text(strip=True))
        rent_metrics = {'suburb rent payments les that 30% of household income': Suburb_household_payments,
                                'state rent payments les that 30% of household income': State_household_payments}
        return rent_metrics
    else:
        print('Households where rent payments are less than 30% of household income row could not be found')

# Find and return renter households where rent payments are less than or equal to 30% of household income (b) from 2021 ABS data
def rent_weekly_payments_2021(soup):
    # find the row with renter households spending under 30%
    weekly_rent_title = soup.find('th', string='Renter households where rent payments are less than or equal to 30% of household income (b)')
    # if found, find the parent and extract the data for the state and suburb
    if weekly_rent_title:
        rent_row = weekly_rent_title.find_parent('tr')
        rent_data = rent_row.find_all('td')
        Suburb_household_payments = float(rent_data[1].get_text(strip=True))
        State_household_payments = float(rent_data[3].get_text(strip=True))
        rent_metrics = {'suburb rent payments les that 30% of household income': Suburb_household_payments,
                                'state rent payments les that 30% of household income': State_household_payments}
        return rent_metrics
    else:
        print('Households where rent payments are less than 30% of household income row could not be found')

# Since both 2021 and 2016 data is the same structure for Professionals this function does both years
def no_of_Professionals(soup):
    # find the row containing professionals
    professional_row_title = soup.find('th', string='Professionals')
    if professional_row_title:
        # proceed to find the parent of the professional row
        professional_row = professional_row_title.find_parent('tr')
        professional_data = professional_row.find_all('td')
        # find specific data for state and suburb and save to a dictionary
        Suburb_professionals = int(professional_data[0].get_text(strip=True).replace(',', ''))
        State_professionals = int(professional_data[2].get_text(strip=True).replace(',', ''))
        professional_metrics = {'suburb professionals': Suburb_professionals,
                                          'state professionals': State_professionals}
        return professional_metrics
    else:
        print("Professional row could not be found")

# This will find households weekly median income for 2021 ABS data sets
def median_weekly_income_2021(soup):
    # find all the tables on the page
    household_row = soup.find('th', string='Household (d)')
    if household_row:
        # proceed to get the state and suburb values and return a these values in a dictionary
        parent_row = household_row.find_parent('tr')
        income_columns = parent_row.find_all('td')
        Suburb_income = int(income_columns[0].get_text(strip=True).replace('$', '').replace(',', ''))
        State_income = int(income_columns[2].get_text(strip=True).replace('$', '').replace(',', ''))
        median_weekly_household_income = {'suburb household income': Suburb_income,
                                          'state household income': State_income}
        return median_weekly_household_income
    else:
        print("Could not find the income for the suburb or state cells.")

# This will find households weekly median income for 2016 ABS data sets
def median_weekly_income_2016(soup):
    # Find the row that contains 'Household'
    household_row = soup.find('th', string='Household')
    if household_row:
        # find the parent row
        parent_row = household_row.find_parent('tr')
        # Find all td tags to get the numbers for suburb and state and save them to variables
        income_columns = parent_row.find_all('td')
        Suburb_income = int(income_columns[0].get_text(strip=True).replace('$', '').replace(',', ''))
        State_income = int(income_columns[2].get_text(strip=True).replace('$', '').replace(',', ''))
        if State_income or Suburb_income is False:
            # return a dictionary with the suburb and state median weekly household incomes
            median_weekly_household_income = {'suburb household income': Suburb_income, 'state household income': State_income}
            return median_weekly_household_income
        else:
            print("Could not find the income for the suburb or state cells.")
    else:
        print("Could not find the 'Household' row.")

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
        print("The year could not be determined from the URL.")

# this function manages all the functions to retrieve all the 2016 data and collects the results in one spot
def process_2016_data(soup):
    # Find the table related to 'Median weekly incomes'
    weekly_household_income = median_weekly_income_2016(soup)
    professionals = no_of_Professionals(soup)
    household_rent_payment = rent_weekly_payments_2016(soup)
    mortage_repayments = mortage_repayments_2016(soup)
    total_data = [weekly_household_income, professionals, household_rent_payment, mortage_repayments]
    return total_data

# this function manages all the functions to retrieve all the 2021 data and collects the results in one spot
def process_2021_data(soup):
    weekly_household_income = median_weekly_income_2021(soup)
    professionals = no_of_Professionals(soup)
    household_rent_payment = rent_weekly_payments_2021(soup)
    mortage_repayments = mortage_repayments_2021(soup)
    total_data = [weekly_household_income, professionals, household_rent_payment, mortage_repayments]
    return total_data


def main():
    SA2_code_2016 = 801111140
    SA2_code_2021 = 801111140
    # URLs for 2016 and 2021 census data for Kelso
    url_2016 = f"https://www.abs.gov.au/census/find-census-data/quickstats/2016/{SA2_code_2016}"
    url_2021 = f"https://www.abs.gov.au/census/find-census-data/quickstats/2021/{SA2_code_2021}"

    # Scrape data for 2016
    print("Scraping 2016 Census Data:")
    ABS_data_2016 = scrape_abs_data(url_2016)
    print(ABS_data_2016)


    # Scrape data for 2021
    print("\nScraping 2021 Census Data:")
    ABS_data_2021 = scrape_abs_data(url_2021)
    print(ABS_data_2021)

if __name__ == "__main__":
    main()
