from abc import ABC, abstractmethod

# The Base Class
class RepairService(ABC):
    def __init__(self, name, labor_cost):
        self.name = name
        self.__labor_cost = labor_cost  # Private attribute
        self.__status = "Pending"       # Private attribute

    #accessing labor cost through getter and setter methods
    @property
    def labor_cost(self):
        return self.__labor_cost

    @labor_cost.setter
    def labor_cost(self, value):
        if value < 0:
            print("Error: Labor cost cannot be negative.")
        else:
            self.__labor_cost = value
     
    #accessing status through getter and setter methods 
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status in valid_statuses:
            self.__status = new_status
        else:
            print(f"Error: '{new_status}' is not a valid status.")

    #core methods
    @abstractmethod
    def calculate_service_cost(self):
        pass

    @abstractmethod
    def display_service_info(self):
        pass


# Type A: Hardware Repair
class HardwareRepair(RepairService):
    def __init__(self, name, labor_cost, part_cost):
        super().__init__(name, labor_cost)
        self.part_cost = part_cost

    def calculate_service_cost(self):
        # Labor + Part Cost + 10% Physical Goods Tax
        return (self.labor_cost + self.part_cost) * 1.10

    def display_service_info(self):
        return f"[Hardware] {self.name} (Part: ${self.part_cost:.2f})"

# Type B: Software Repair
class SoftwareRepair(RepairService):
    def __init__(self, name, labor_cost, os_version):
        super().__init__(name, labor_cost)
        self.os_version = os_version

    def calculate_service_cost(self):
        # Labor + $5 Digital Processing Fee
        return self.labor_cost + 5.00

    def display_service_info(self):
        return f"[Software] {self.name} (OS: {self.os_version})"

#invoice class
class CustomerInvoice:
    def __init__(self):
        self.items = []

    def add_repair(self, repair_obj):
        self.items.append(repair_obj)

    def print_final_bill(self):
        if not self.items:
            print("\nYour invoice is empty!")
            return

        print("\n" + "_"*70)
        print("\n                      OFFICIAL REPAIR RECEIPT")
        print("_"*70)
        total = 0
        for item in self.items:
            #calculate the cost for each item and print it
            cost = item.calculate_service_cost()
            print(f"{item.display_service_info():<50} ${cost:>8.2f}")
            total += cost
        print("-"*70)
        print(f"{'TOTAL DUE:':<50} ${total:>8.2f}")
        print("_"*70 + "\n")

# main function to run the program
def main():
    #available services
    catalog = {
        "1": HardwareRepair("Screen Replacement", 50, 120),
        "2": HardwareRepair("Battery Swap", 30, 45),
        "3": SoftwareRepair("Virus Removal", 60, "Windows 11"),
        "4": SoftwareRepair("OS Reinstall", 80, "macOS Sonoma")
    }
    
    invoice = CustomerInvoice()

    while True:
        print("--- Tech Repair Shop Management ---")
        print("1. View Services")
        print("2. Add Service to Invoice")
        print("3. View Current Invoice")
        print("4. Print Final Bill & Exit")
        print("5. Exit Without Saving")
        
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            print("\nAvailable Services:")
            for key, service in catalog.items():
                print(f"[{key}] {service.display_service_info()} - Base Labor: ${service.labor_cost}")
            print()

        elif choice == "2":
            svc_id = input("Select the ID of the service to add: ")
            if svc_id in catalog:
                invoice.add_repair(catalog[svc_id])
                print(f"Added {catalog[svc_id].name} to invoice.\n")
            else:
                print("Invalid ID. Please try again.\n")

        elif choice == "3":
            if not invoice.items:
                print("\nInvoice is currently empty.\n")
            else:
                print("\nItems in current session:")
                for item in invoice.items:
                    print(f"- {item.name} (Labor: ${item.labor_cost})")
                print()

        elif choice == "4":
            invoice.print_final_bill()
            print("Thank you for choosing our shop. Goodbye!")
            break

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Error: Please enter a valid number (1-5).\n")

if __name__ == "__main__":
    main()