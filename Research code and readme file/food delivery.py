class FoodDeliverySystem:
    unique_order_id_counter = 1000  # Global unique order ID counter

    def __init__(self):
        self.orders = []  # List to store all orders

    def user_info(self):
        """Collect basic user information."""
        name = input("Enter your name: ")
        address = input("Enter your delivery address: ")
        return {"name": name, "address": address}

    def order_details(self):
        """Collects food item details and calculates total cost."""
        total_cost = 0
        items = []
        while True:
            item = input("Enter food item name (or 'done' to finish): ")
            if item.lower() == 'done':
                break
            cost = float(input(f"Enter cost for {item}: "))
            items.append({"item": item, "cost": cost})
            total_cost += cost
        return total_cost, items

    def generate_unique_order_id(self):
        """Generate a unique order ID and increment the global counter."""
        unique_order_id = FoodDeliverySystem.unique_order_id_counter + 1
        FoodDeliverySystem.unique_order_id_counter += 1
        return unique_order_id

    def generate_order_ref(self, name, unique_order_id):
        """Generate an order reference number based on the last 3 characters of the name and unique ID."""
        name_part = name[-3:] if len(name) >= 3 else name
        id_part = str(unique_order_id)[-3:]
        return f"{name_part}{id_part}"

    def order_status(self, total_cost):
        """Determine order status based on total cost."""
        return "confirmed" if total_cost > 0 else "pending"

    def submit_order(self):
        """Submit a new food order."""
        user = self.user_info()
        total_cost, items = self.order_details()
        status = self.order_status(total_cost)
        unique_order_id = self.generate_unique_order_id()
        order_ref = self.generate_order_ref(user["name"], unique_order_id)

        order = {
            "id": unique_order_id,
            "user": user,
            "items": items,
            "total": total_cost,
            "status": status,
            "order_ref": order_ref
        }
        self.orders.append(order)
        print(f"Order submitted with ID {unique_order_id} and status '{status}'.")
        print(f"Order reference number: {order_ref}")

    def display_orders_neatly(self):
        """Prints all the orders neatly with headers."""
        print("\n============================")
        print("        All Orders         ")
        print("============================")
        if not self.orders:
            print("No orders have been submitted yet.")
        else:
            print(f"{'ID':<5} {'Name':<15} {'Total Cost':<12} {'Status':<10} {'Order Ref':<15}")
            print("-" * 60)
            for order in self.orders:
                print(f"{order['id']:<5} {order['user']['name']:<15} ${order['total']:<12.2f} {order['status']:<10} {order['order_ref']:<15}")
            print("============================")

    def display_order_details(self, order_id):
        """Prints the details of a specific order."""
        for order in self.orders:
            if order['id'] == order_id:
                print("\n============================")
                print("        Order Details        ")
                print("============================")
                print(f"ID: {order['id']}")
                print(f"Name: {order['user']['name']}")
                print(f"Address: {order['user']['address']}")
                print("Items:")
                for item in order['items']:
                    print(f"- {item['item']}: ${item['cost']:.2f}")
                print(f"Total Cost: ${order['total']:.2f}")
                print(f"Status: {order['status']}")
                print(f"Order Ref: {order['order_ref']}")
                print("============================")
                return
        print("Order not found.")

# Main program
def main():
    system = FoodDeliverySystem()

    while True:
        choice = input("\n1. Submit Order\n2. Display Orders\n3. Display Order Details\n4. Exit\nChoose an option: ")
        if choice == "1":
            system.submit_order()
        elif choice == "2":
            system.display_orders_neatly()
        elif choice == "3":
            order_id = int(input("Enter the order ID: "))
            system.display_order_details(order_id)
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
