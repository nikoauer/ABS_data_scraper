
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
