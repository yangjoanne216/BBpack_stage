import requests
import csv

# API key
api_token = "51385e266fcc120d6be9636cb4690415efac5c99633a06a2"
base_url = "https://api.pappers.fr/v2/recherche"

# Get NAF code from user
code_naf = input("Please enter NAF code: ").strip()
# Validate NAF code
valid_naf_codes = []
with open('code_NAF.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    valid_naf_codes = [row['Code'] for row in reader]

if code_naf not in valid_naf_codes:
    print("The entered NAF code is not valid, please enter a valid NAF code.")
    exit(1)

# Validate department code
valid_department_codes = []
with open('departements.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        valid_department_codes.append(row[0])

department = input("Please enter the department code (press Enter directly if you do not want to restrict the department): ")
# Validate department code
if department and department not in valid_department_codes:
    print("The entered department code is not valid")
    exit(1)

# Set API query parameters
query_params = {
    'api_token': api_token,
    'code_naf': code_naf,
    'par_page': 200,  # Set the number of returned companies, can be adjusted according to needs
    'page': 1,  # Set the number of returned pages, loops can be used for paging in subsequent codes
}

# If the user has entered the department number, add it to the query parameters
if department:
    query_params['departement'] = department

try:
    # Send request and get response
    response = requests.get(base_url, params=query_params)

    # Check response status
    response.raise_for_status()

    # Parse response data using .json() method
    data = response.json()
except (requests.exceptions.RequestException, ValueError) as e:
    print(f"Error in request or parsing JSON data: {e}")
else:
    # Open CSV file, ready to write
    filename = f"companies_{code_naf}_{department}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["siren","nom","adress_siege","code_postal_siege","code_NAF","activité"])

        # Write company information step by step
        for company in data["resultats"]:
            siege_info = company.get("siege", {})
            '''
            leaders = company.get("dirigeants", [])
            '''
            siren = company.get("siren", "")
            nom = company.get("denomination", "")
            '''
            if leaders:  # Determine whether leaders is non-empty
                leaders_info = leaders[0]
                leader_country = leaders_info.get("pays", "N/A")  # Return the default value "N/A" if there is no country information
                leader_address = leaders_info.get("adresse_ligne_1", "N/A")  # Return the default value "N/A" if there is no address information
            else:
                leader_country = "N/A"
                leader_address = "N/A"
            '''
            # Get the company's address and postal code
            siege_address = siege_info.get("adresse_ligne_1", "N/A")
            siege_postal_code = siege_info.get("code_postal", "N/A")

            code_NAF = company.get("code_naf", "")
            activity = company.get("domaine_activite", "")

            writer.writerow(
                [siren, nom, siege_address, siege_postal_code, code_NAF, activity])
