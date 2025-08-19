
inventory = [
    {'sku': 'P101', 'name': 'Pencil', 'quantity': 50},
    {'sku': 'P102', 'name': 'Pen', 'quantity': 20},
    {'sku': 'P103', 'name': 'Eraser', 'quantity': 10},
    {'sku': 'P104', 'name': 'Marker', 'quantity': 15},
    {'sku': 'P105', 'name': 'Notebook', 'quantity': 30}
]

# Insert new product with validation
def insert_product():
    sku = input("Enter SKU: ").strip()
    if not sku:
        print("SKU cannot be empty.")
        return
    for item in inventory:
        if item['sku'] == sku:
            print("Product with this SKU already exists!")
            return
    name = input("Enter Product Name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return
    try:
        quantity = int(input("Enter Quantity: ").strip())
        if quantity < 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return
    inventory.append({'sku': sku, 'name': name, 'quantity': quantity})
    print("Product inserted successfully.")


# check the duplicate SKU

def insert_duplicate_sku():

    sku = input("Enter SKU: ")
    if any(item['SKU'] == sku for item in inventory):
        print("Rejecting duplicate SKU.")
        return
      
# Insert multiple products
def insert_multiple_products():
    try:
        count = int(input("How many products to insert? ").strip())
        if count <= 0:
            print("Enter a positive number!")
            return
    except ValueError:
        print("Invalid number.")
        return
    for i in range(count):
        print(f"\nInsert product {i+1}:")
        insert_product()

# Display inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nInventory List:")
    print("SKU\tName\tQuantity")
   
    for item in inventory:
        print(f"{item['sku']}\t{item['name']}\t{item['quantity']}")

# Search by SKU
def search_by_sku():
    sku = input("Enter SKU to search: ").strip()
    for item in inventory:
        if item['sku'] == sku:
            print(f"Found: SKU: {item['sku']}, Name: {item['name']}, Quantity: {item['quantity']}")
            return
    print("Product not found.")

# Search by Name
def search_by_name():
    name = input("Enter product name to search: ").strip().lower()
    found = False
    for item in inventory:
        if item['name'].lower() == name:
            print(f"Found: SKU: {item['sku']}, Name: {item['name']}, Quantity: {item['quantity']}")
            found = True
    if not found:
        print("Product not found.")

# Update quantity for existing SKU
def update_quantity():
    sku = input("Enter SKU to update quantity: ").strip()
    for item in inventory:
        if item['sku'] == sku:
            try:
                new_qty = int(input("Enter new quantity: ").strip())
                if new_qty < 0:
                    print("Quantity must be positive.")
                    return
                item['quantity'] = new_qty
                print("Quantity updated successfully.")
                return
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                return
    print("Product not found.")

    #  Delete product by SKU
def delete_product():
    sku = input("Enter SKU to delete: ").strip()
    for i, item in enumerate(inventory):
        if item['sku'] == sku:
            del inventory[i]
            print("Product deleted successfully.")
            return
    print("Product not found.")

    # Main menu to test different cases
def main():
    while True:
        print("\nInventory Management System")
        print("1. Insert Multiple Products")
        print("2. Display Inventory")
        print("3. Search Product by SKU")
        print("4. Search Product by Name")
        print("5. Update Product Quantity")
        print("6. Delete Product by SKU")
        print("7. Exit")
        print("8. Duplicate SKU Check: Enter SKU to check for duplicates")
        choice = input("Choose an option (1-7): ").strip()
        if choice == '1':
            insert_multiple_products()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            search_by_sku()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            update_quantity()
        elif choice == '6':
            delete_product()
        elif choice == '7':
            print("Exiting program.")
            break
        elif choice == '8':
            insert_duplicate_sku()
            break
        
        else:
            print("Invalid choice. Please select 1-7.")

main()
