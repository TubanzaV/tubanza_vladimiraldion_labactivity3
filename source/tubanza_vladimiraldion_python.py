"""
AI Usage Disclosure:
Generative AI tools were used during the drafting of this code to provide syntax 
examples, suggest class structures, and implement the interactive terminal menu. 
The final code has been thoroughly tested, modified, and validated.
"""

class HardwareItem:
    
    def __init__(self, item_id, name, category, quantity, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"  [+] Restocked {amount}x {self.name}. New stock: {self.quantity}")
        else:
            print("  [!] Invalid restock amount.")

    def dispense(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"  [-] Dispensed {amount}x {self.name}. Remaining: {self.quantity}")
        else:
            print(f"  [!] Failed to dispense {amount}x {self.name}: Insufficient stock.")

    def get_total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"[{self.item_id}] {self.name} ({self.category}) | Qty: {self.quantity} | Unit Price: ${self.price:.2f}"


class InventorySystem:
    
    def __init__(self):
        self.items = {}

    def register_item(self, item):
        if item.item_id not in self.items:
            self.items[item.item_id] = item
            print(f"[*] Registered new item: {item.name}")
        else:
            print(f"[!] Item ID {item.item_id} already exists.")

    def process_transaction(self, item_id, action, amount):
        if item_id in self.items:
            if action == 'restock':
                self.items[item_id].restock(amount)
            elif action == 'dispense':
                self.items[item_id].dispense(amount)
        else:
            print(f"[!] Item ID {item_id} not found in system.")

    def generate_report(self):
        print("\n____SYSTEM INVENTORY REPORT____")
        if not self.items:
            print("No items in inventory.")
        else:
            for item in self.items.values():
                print(item)
        print("_________________________________")
        total = sum(item.get_total_value() for item in self.items.values())
        print(f"TOTAL SYSTEM VALUATION: ${total:.2f}\n")

def main():
    lab_inventory = InventorySystem()

    while True:
        print("\n" + "="*30)
        print(" HARDWARE INVENTORY MENU")
        print("="*30)
        print("1. Register new item")
        print("2. Restock item")
        print("3. Dispense item")
        print("4. View Inventory Report")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            print("\n____Register New Item____")
            item_id = input("Enter Item ID (e.g., RAM-01): ")
            name = input("Enter Item Name: ")
            category = input("Enter Category: ")
            
            try:
                qty = int(input("Enter Initial Quantity: "))
                price = float(input("Enter Unit Price: "))
                new_item = HardwareItem(item_id, name, category, qty, price)
                lab_inventory.register_item(new_item)
            except ValueError:
                print("[!] Error: Quantity must be an integer and Price must be a number.")

        elif choice == '2':
            print("\n____Restock Item____")
            item_id = input("Enter Item ID to restock: ")
            try:
                amount = int(input("Enter amount to add: "))
                lab_inventory.process_transaction(item_id, "restock", amount)
            except ValueError:
                print("[!] Error: Amount must be an integer.")

        elif choice == '3':
            print("\n____Dispense Item____")
            item_id = input("Enter Item ID to dispense: ")
            try:
                amount = int(input("Enter amount to remove: "))
                lab_inventory.process_transaction(item_id, "dispense", amount)
            except ValueError:
                print("[!] Error: Amount must be an integer.")

        elif choice == '4':
            lab_inventory.generate_report()

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("[!] Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
