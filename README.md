# 📦 Inventory Stock Manager

A simple console-based Inventory Management System written in Python. This tool allows users to add, search, update, and manage products using their SKU, name, and quantity.

---

## 🚀 Features

- Add a single or multiple products
- Prevents duplicate SKUs
- View the current inventory
- Search products by SKU or Name
- Update the quantity of a product
- Delete a product by SKU
- Input validation for quantity and product name
- Inventory limit of 100 products

---

## 🧾 How It Works

The system uses a list of dictionaries to store product records, where each product contains:
- `sku`: A unique identifier for the product
- `name`: The product name
- `quantity`: The quantity in stock

---

## 🖥️ Menu Options

When you run the script, you'll see the following options:

1. **Insert New Product**  
   Adds a new product after checking for a unique SKU.

2. **Display Inventory**  
   Lists all current products in the inventory.

3. **Insert N Products**  
   Allows batch input of multiple products.

4. **Search Product by SKU**  
   Finds a product using its SKU.

5. **Search Product by Name**  
   Finds a product using its name.

6. **Delete Product**  
   Deletes a product from inventory using its SKU.

7. **Update Product Quantity**  
   Updates the quantity of a specific product.

8. **Exit**  
   Exits the program.

---

## ✅ Requirements

- Python 3.x

No external libraries required.

---

## ▶️ How to Run

1. Save the script in a `.py` file (e.g., `inventory_manager.py`)
2. Open a terminal and run:

```bash
python inventory_manager.py
Maximum inventory size is set to 100 products.

Empty product names and negative quantities are not allowed.

SKU must be unique across all products.
{
    'sku': 'ABC123',
    'name': 'Wireless Mouse',
    'quantity': 15
}
🔧 Possible Improvements

Save/load inventory to/from a file (e.g., JSON or CSV)

Add product categories or pricing

Implement a GUI using Tkinter or web interface with Flask
