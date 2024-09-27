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