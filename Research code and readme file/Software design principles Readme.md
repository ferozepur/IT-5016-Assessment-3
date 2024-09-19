                              Software design principles Readme
                                      Food Delivery System
Overview
The Food Delivery System is a console application that allows users to place food orders, view all orders, and check the details of specific orders. It follows key software design principles, including KISS (Keep It Simple, Stupid) and DRY (Don't Repeat Yourself), ensuring maintainability and ease of understanding.

Features
User Information Collection: Gathers user details (name and delivery address) to process orders.
Order Management: Users can input food items and their costs, with automatic total cost calculation.
Unique Order Identification: Generates unique order IDs and reference numbers for easy tracking.
Order Status: Provides a status (confirmed) based on the total cost of the order.
Neatly Displayed Orders: Presents all orders and specific order details in a clear format.
Software Design Principles
KISS (Keep It Simple, Stupid)
The design of the Food Delivery System is intentionally simple to enhance usability and maintainability:

Clear Class Responsibilities: The FoodDeliverySystem class encapsulates all functionalities related to food order processing, minimizing complexity.
Straightforward User Interaction: The console interface is user-friendly, allowing easy navigation for placing orders.
Minimal Logic Complexity: Each method has a single responsibility, reducing cognitive load for understanding the code.
DRY (Don't Repeat Yourself)
The Food Delivery System adheres to the DRY principle to eliminate redundancy and enhance maintainability:

Modular Methods: Each functionality is encapsulated in dedicated methods, such as user_info(), order_details(), and submit_order(), preventing code repetition and promoting reusability.
Single Source of Truth: Unique order ID generation and order reference creation are handled by specific methods, ensuring any changes are made in one place only.
Code Structure
Classes
FoodDeliverySystem: The main class that handles all operations related to food orders.
Methods
user_info(): Collects the user's name and delivery address.
order_details(): Gathers food item details and calculates the total cost.
generate_unique_order_id(): Generates a unique order ID for each order.
generate_order_ref(): Creates an order reference number based on the last three characters of the user's name and the unique ID.
order_status(): Determines the status of the order based on the total cost.
submit_order(): Manages the order submission process, including data collection and storage.
display_orders_neatly(): Prints all orders in a structured format.
display_order_details(): Displays detailed information for a specific order.
Usage
Run the program in a Python environment.
Follow the prompts to submit a new order, view all orders, or check details of a specific order.
To exit the program, select the appropriate option from the menu.
Conclusion
The Food Delivery System exemplifies a clean and efficient implementation of an order management system, adhering to essential software design principles. The KISS and DRY methodologies ensure that the code is simple, maintainable, and free from redundancy.