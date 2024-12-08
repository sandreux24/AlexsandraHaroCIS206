def loadCustomerInfo(filename):
    customers = []

    try:
        with open(filename, 'r') as file:
        
            for line in file:
                customerData = line.strip().split(',')
                if len(customerData) == 11:
                    customers.append(tuple(customerData))

                else:
                    print(f"Warning: Skipping invalid line {line.strip()}")
        return customers
    
    except IOError:
        print(f"Error: The file {filename} was not found.")
        return []
    
    except Exception as e:
        print(f"An error occurred: {e} ")
        return []
    
def displayCustomers (customers):

    if not customers:
        print(f"No customers to display.")
        return
    
    print(f"{'Company':<30}{'Contact':<30}{'Phone':20}")
    print("-" * 80)
    
    for customer in customers:
        print(f"{customer[1]:<30}{customer[2]:<30}{customer[6]:<20}")


def sortCustomer(customers, sortBy):
    if sortBy == 'company':
        return sorted(customers, key=lambda customer: customer[1])
    elif sortBy == 'contact':
        return sorted(customers, key=lambda customer: customer[2])
    else:
        print(f"Invalid sorting field.")
        return customers
    
def searchCustomer(customers, searchTerm, searchField):
    if searchField == 'company':
        return[customer for customer in customers if searchTerm.lower() in customer[1].lower()]
    elif searchField == 'contact':
        return[customer for customer in customers if searchTerm.lower() in customer[2].lower()]
    else:
        print(f"Invalid search field.")
        return[]

def displaySearchResults(matchedCustomers):
    if matchedCustomers:
        print(f"{'Company':<30}{'Contact':<30}{'Phone':<20}")
        print("-" * 80)
        for customer in matchedCustomers:
            print(f"{customer[1]:<30}{customer[2]:<30}{customer[6]:<20}")

    else:
        print(f"No matching records found.")

def validationInput(choice, validChoice):
    return choice in validChoice        

""""
def sortCustomersByCompany(customers):
    return sorted(customers, key=lambda customer: customer[1])

def sortCustomersByContact(customers):
    return sorted(customers, key=lambda customer: customer[2])

def searchByCompany(customers, searchTerm):
    matchedCustomers = [customer for customer in customers if searchTerm.lower() in customer[1].lower()]
    return matchedCustomers

def searchByContact(customers, searchTerm):
    matchedCustomers = [customer for customer in customers if searchTerm.lower() in customer[2].lower()]
    return matchedCustomers

def displaySearchResults(matchedCustomers):
    if matchedCustomers:
        print(f"{'Company':<30}{'Contact':<30}{'Phone':<20}")
        print("-" * 80)

        for customer in matchedCustomers:
            print(f"{customer[1]:<30}{customer[2]:<30}{customer[6]:<20}")

        else:
            print(f"No matching records found.")
            """

def userInterface():

    filename = "northWindCustomers.txt"
    customers = loadCustomerInfo(filename)

    if not customers:
        return
    
    while True:
        print(f"\nSelect an option on the list:")
        print(f"1. Display customers sorted by company name.")
        print(f"2. Display customers sorted by contact name.")
        print(f"3. Search for company.")
        print(f"4. Search for a contact.")
        print(f"5. Exit")

        choice = input("Enter your choice: ")

        if not validationInput(choice, ['1', '2', '3', '4', '5']):
            print(f"Invalid Choice, Try again.")
            continue

        
        if choice == "1":
            sortByCompany = sortCustomer(customers, 'company')
            print(f"\nDisplaying customers sorted by company name:")
            displayCustomers(sortByCompany)

        elif choice =="2":
            sortByContact = sortCustomer(customers, 'contact')
            print(f"Displaying customers by contact name: ")
            displayCustomers(sortByContact)

        elif choice =="3":
            searchTerm = input(f"Enter company name: ")
            matchedCompany = searchCustomer(customers, searchTerm, 'company')
            print(f"\nSearch results for company '{searchTerm}': ")
            displaySearchResults(matchedCompany)

        elif choice =="4":
            searchTerm = input(f"Enter contact name: ")
            matchedContact = searchCustomer(customers, searchTerm, 'contact')
            print(f"\nSearch results for contact '{searchTerm}': ")
            displaySearchResults(matchedContact)

        elif choice =="5":
            print(f"Exiting program.")
            break

        

def main():
    userInterface()


if __name__ == "__main__":
    main()            



