# ABS Census Data Scraper API

## Overview
This project is a Flask-based API designed to scrape Australian Bureau of Statistics (ABS) census data from the 2016 and 2021 datasets. The API allows you to fetch specific data related to:

- **Median weekly household income**
- **Number of professionals**
- **Households where rent payments are less than or equal to 30% of household income**
- **Households where mortgage repayments are less than 30% of household income**

The goal of the API is to return this data in a structured JSON format, which can be consumed by external services like Google Sheets. This will assist users in making informed decisions about property purchases based on the census data of different areas.

## Key Features
- **Scrapes ABS Census Data**: Fetches data from the ABS website for both 2016 and 2021.
- **Processes Census Metrics**: Extracts key metrics related to income, rent, and mortgage payments.
- **Flask API**: Provides a RESTful API to retrieve data based on a specific SA2 code.
- **Supports Google Sheets**: Can be integrated with Google Sheets, allowing users to pull census data into their spreadsheets for analysis.

## Usage

### Running the API
1. **Run the Flask API**: Start the API by running the Flask app:
    ```bash
    python app.py
    ```

2. **Make API Calls**: Use a tool like `curl` or a REST client to make a GET request to the `/census/<sa2_code>` endpoint.
   - **Example**: `GET /census/206041122`
   - This will return the census data for the given SA2 code for both 2016 and 2021.

3. **Google Sheets Integration**: Use the Google Sheets API to send the SA2 code to this API, fetch the relevant data, and populate your spreadsheet.

### API Endpoint
- **GET /census/<int:sa2_code>**
  - **Description**: Returns census data for the specified SA2 code.
  - **Params**: `sa2_code` – The SA2 code of the region to fetch data for.
  - **Response**: JSON object containing census data from both 2016 and 2021.

### Core Functions
1. **`scrape_abs_data(url)`**  
   - Scrapes the ABS census data from the specified URL (either 2016 or 2021) and calls the appropriate processing function.

2. **`process_2016_data(soup)`**  
   - Retrieves the median household income, number of professionals, rent payments, and mortgage payments from 2016 data.

3. **`process_2021_data(soup)`**  
   - Similar to `process_2016_data`, but for 2021.

4. **`median_weekly_income_2016(soup)` / `median_weekly_income_2021(soup)`**  
   - Extracts and returns median weekly income for the suburb and state from the relevant year.

5. **`rent_weekly_payments_2016(soup)` / `rent_weekly_payments_2021(soup)`**  
   - Finds the percentage of renter households paying less than 30% of their income on rent for the given year.

6. **`mortgage_repayments_2016(soup)` / `mortgage_repayments_2021(soup)`**  
   - Extracts data on households spending less than 30% of their income on mortgage repayments.

7. **`no_of_Professionals(soup)`**  
   - Fetches the number of professionals in the suburb and state for both years.

### Installation

1. **Install dependencies**:
    ```bash
    pip install Flask requests BeautifulSoup4
    ```

2. **Run the app**:
    ```bash
    python app.py
    ```

### How to Integrate with Google Sheets
To integrate with Google Sheets:
- Use Google Sheets' built-in functions or Google Apps Script to make an API call to the Flask app's `/census/<sa2_code>` route.
- Parse the returned JSON data and populate the relevant cells with the census metrics.

This setup allows users to pull in live data and use it to make more informed decisions regarding property investments in different areas.

## Example Response:
```json
{
  "2016": {
    "median_weekly_household_income": {
      "suburb": 1200,
      "state": 1500
    },
    "professionals": {
      "suburb": 500,
      "state": 20000
    },
    "households_rent_30_percent": {
      "suburb": 30.5,
      "state": 25.1
    },
    "mortgage_repayments_30_percent": {
      "suburb": 45.7,
      "state": 40.3
    }
  },
  "2021": {
    "median_weekly_household_income": {
      "suburb": 1500,
      "state": 1800
    },
    "professionals": {
      "suburb": 600,
      "state": 25000
    },
    "households_rent_30_percent": {
      "suburb": 28.9,
      "state": 22.7
    },
    "mortgage_repayments_30_percent": {
      "suburb": 42.3,
      "state": 37.8
    }
  }
}

