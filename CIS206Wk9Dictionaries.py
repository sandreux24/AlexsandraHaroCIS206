def read_customers(filename):
    """Reads customer data from a file and returns a list of customer dictionaries."""
    customers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 11:  
                    customer = {
                        'CustomerID': parts[0],
                        'CompanyName': parts[1],
                        'ContactName': parts[2],
                        'ContactTitle': parts[3],
                        'Address': parts[4],
                        'City': parts[5],
                        'Region': parts[6],
                        'PostalCode': parts[7],
                        'Country': parts[8],
                        'Phone': parts[9],
                        'Fax': parts[10]
                    }
                    customers.append(customer)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return customers

def display_all_customers(customers):
   
    if customers:
        for customer in customers:
            print(f"Company Name: {customer['CompanyName']}")
            print(f"Contact Name: {customer['ContactName']}")
            print(f"Phone: {customer['Phone']}")
            print("--------")
    else:
        print("No customers to display.")

def sort_by_company(customers):
    
    return sorted(customers, key=lambda x: x['CompanyName'].lower())

def sort_by_contact_name(customers):
    
    return sorted(customers, key=lambda x: x['ContactName'].lower())

def search_by_company(customers, search_term):
    
    return [customer for customer in customers if search_term.lower() in customer['CompanyName'].lower()]

def search_by_contact_name(customers, search_term):
    """Searches customers by contact name."""
    return [customer for customer in customers if search_term.lower() in customer['ContactName'].lower()]

def main():
    filename = "northWindCustomers.txt"  
    customers = read_customers(filename)

    
    while True:
        print("\nCustomer Management System")
        print("1. Display all customers")
        print("2. Sort customers by company name")
        print("3. Sort customers by contact name")
        print("4. Search by company name")
        print("5. Search by contact name")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print("\nDisplaying all customers:")
            display_all_customers(customers)

        elif choice == '2':
            print("\nDisplaying customers sorted by company name:")
            sorted_customers = sort_by_company(customers)
            display_all_customers(sorted_customers)

        elif choice == '3':
            print("\nDisplaying customers sorted by contact name:")
            sorted_customers = sort_by_contact_name(customers)
            display_all_customers(sorted_customers)

        elif choice == '4':
            search_term = input("\nEnter a company name to search for: ")
            search_results = search_by_company(customers, search_term)
            print(f"\nSearch results for company name '{search_term}':")
            display_all_customers(search_results)

        elif choice == '5':
            search_term = input("\nEnter a contact name to search for: ")
            search_results = search_by_contact_name(customers, search_term)
            print(f"\nSearch results for contact name '{search_term}':")
            display_all_customers(search_results)

        elif choice == '6':
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
