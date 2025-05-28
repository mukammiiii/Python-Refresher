import pandas as pd

path = input("Enter path to your dataset:")
df = pd.read_csv(path)
print(df)

# Define the Node class for the linked list
class Node:
    def _init_(self, country, year, total_emission):
        self.country = country
        self.year = year
        self.total_emission = total_emission
        self.next = None

# Define the LinkedList class
class LinkedList:
    def _init_(self):
        self.head = None

    def insert_in_chronological_order(self, new_country, new_year, new_emission):
        new_node = Node(new_country, new_year, new_emission)

        # Case 1: Empty list
        if not self.head:
            self.head = new_node
            return

        # Case 2: Insert at the beginning
        if (new_country < self.head.country) or (new_country == self.head.country and new_year < self.head.year):
            new_node.next = self.head
            self.head = new_node
            return

        # Case 3: Insert in the middle or end
        current = self.head
        while current.next and (current.next.country < new_country or (current.next.country == new_country and current.next.year < new_year)):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def max_emission_year(self):
        max_year = self.head.year
        max_emission = self.head.total_emission
        max_country = self.head.country
        current = self.head.next

        while current:
            if current.total_emission > max_emission:
                max_emission = current.total_emission
                max_year = current.year
                max_country = current.country
            current = current.next
        return max_year, max_emission, max_country

    def average_emission(self):
        total_emission = 0
        count = 0
        current = self.head

        while current:
            total_emission += current.total_emission
            count += 1
            current = current.next

        return total_emission / count if count > 0 else 0

    def get_list(self):
        current = self.head
        count = 0
        if not current:
            print("List is empty")
            return
        print("CO₂ EMISSION DATA:")
        print("\t\tCOUNTRY\t\tYEAR\t\tTOTAL EMISSION EXCLUDING LUCF(Mt)")
        print("\n")
        while current:
            count += 1
            print(f"{count}\t\t{current.country}\t\t{current.year}\t\t{current.total_emission}")
            current = current.next


# Main execution
if _name_ == "_main_":
    filename = path

    emission_list = LinkedList()

    try:
        for index, row in df.iterrows():
            try:
                country = row["Country"]
                year = int(row["Year"])
                total_emission = float(row["Total CO2 Emission excluding LUCF (Mt)"])
                emission_list.insert_in_chronological_order(country, year, total_emission)

            except ValueError:
                print(f"ERROR: Invalid data in row {index + 1}")
    except FileNotFoundError:
        print(f"ERROR: The file {filename} was not found")

    while True:
        add_more = input("Do you want to insert more data? (yes/no):")
        if add_more == "no":
            emission_list.get_list()

            max_emission_data = emission_list.max_emission_year()
            print(f"\nYear with Maximum Emission: {max_emission_data[0]}, Emission: {max_emission_data[1]}, Country: {max_emission_data[2]}")

            average_emission = emission_list.average_emission()
            print(f"\nAverage Emission across the years and all countries: {average_emission:.5f}")
            break

        elif add_more == "yes":
            while True:
                African_countries = ["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic","Chad",
                    "Comoros","Democratic Republic of the Congo","Republic of the Congo","Côte d'Ivoire","Djibouti","Egypt",
                    "Equatorial Guinea","Eritrea","Eswatini","Ethiopia","Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho",
                    "Liberia","Libya","Madagascar","Malawi","Mali","Mauritania","Mauritius","Morocco","Mozambique","Namibia",
                    "Niger","Nigeria","Rwanda","Sao Tome and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa",
                    "South Sudan","Sudan", "Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe",]

                country = str(input("Enter the country: "))
                if country not in African_countries:
                    print(f"{country} is not an African country!\nHint: must be string and starts with a capital letter.")
                    continue
                try:
                    year = int(input("Enter the year:"))
                    if year < 2021 or year > 2025:
                        print(f"{year} is not a valid year!\nHint: must range from 2021 to current year.")
                        continue
                except ValueError:
                    print(f"Error: Input is not numeric.")
                    continue
                try:
                    total_emission = float(input("Enter the total emission:"))
                    break
                except ValueError:
                    print(f"Error: Input is not numeric.")
                    continue
            emission_list.insert_in_chronological_order(country, year, total_emission)

            # Display the linked list
            emission_list.get_list()
            print("INSERTION SUCCESSFUL!")
            
            # Display the year with maximum emission
            max_emission_data = emission_list.max_emission_year()
            print(f"\nYear with Maximum Emission: {max_emission_data[0]}, Emission: {max_emission_data[1]}, Country: {max_emission_data[2]}")

            # Display the average emission
            average_emission = emission_list.average_emission() 
            print(f"\nAverage Emission across the years and all countries: {average_emission:.5f}")