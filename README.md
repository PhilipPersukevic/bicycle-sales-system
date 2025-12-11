# 🚴 Bicycle Sales System: Python OOP Project

A comprehensive console-based bicycle sales management system developed using **Python's Object-Oriented Programming (OOP)** principles, abstract classes, inheritance, the Factory pattern, and CSV data storage.

This project is designed to demonstrate **solid OOP principles**, a **modular code structure**, and **practical file handling**. It is an excellent example for coursework, university projects, or learning Python architecture.

---

## ✨ Features

### Multiple Bicycle Types

The system supports creating bicycles across various categories, all deriving from the abstract base class `Bicycle`:

* **Downhill**
* **Ebike**
* **XC**
* **Enduro**
* **Trail**
* **Gravel**

### Add Sales

The user can input detailed specifications for each bicycle sold:

* **Year**
* **Model**
* **Color**
* **Frame size**
* **Wheel size**
* **Number of gears**
* **Price**
* **Quantity**

Every completed sale is persistently saved to the `sales.csv` file.

### Calculate Total Sales Revenue

The program includes functionality to read the sales data from the CSV file, calculate, and display the **total sales revenue**.

### Robust Input Validation

User input is strictly validated to ensure data integrity:

* **Valid bicycle type** selection.
* **Year** not exceeding the current year (e.g., 2025).
* **Color** must not contain digits.
* Validation for **frame and wheel sizes**.
* **Gears** must match allowed values.
* **Price** and **Quantity** must be positive numbers.

---

## 📂 Project Structure

The project is organized into a modular structure:

project/│├── models/│   ├── bicycle.py          # Abstract base class and common logic│   ├── bicycle_types.py    # Concrete bicycle type classes (Downhill, Ebike, etc.)│   └── factory.py          # Implementation of the Factory Pattern│├── sales/│   ├── sale.py             # Sale class for individual transactions│   └── sales_manager.py    # Logic for managing sales and revenue calculation│├── main.py                 # Entry point and console interface└── sales.csv               # Sales data store (automatically created after first sale)
---

## ⚙️ How to Run

1.  **Install Python 3.9+** on your system.
2.  **Download** the entire project repository.
3.  Navigate to the project directory in your terminal.
4.  Run the main file:

```bash
python main.py
🧱 OOP Concepts UsedOOP ConceptImplementation LocationDescriptionAbstractionBicycleAbstract base class defining the interface for all bicycles.InheritanceAll concrete bicycle classesConcrete classes (e.g., Downhill, Ebike) inherit from Bicycle.PolymorphismOverridden display_info() methodsDifferent bicycle types implement their own specific display logic.EncapsulationPrivate attributesUse of private attributes (e.g., _year, _price) to control data access.Factory PatternBicycleFactoryDecouples the client code from the concrete bicycle class creation.Modular StructureCode split into multiple modulesEnhances maintainability and readability.💻 Technologies UsedPython 3ABC (Abstract Base Class) moduleCSV ModuleFactory PatternModular Code Architecture📊 Example CSV OutputThe sales.csv file, after adding some sales, looks like this:TypeYearModelColorFrame sizeWheel sizeNumber of gearsPriceQuantityTotalEnduro2023RallonBluel2912350027000Ebike2024LevoRedm2912890018900👤 AuthorCreated by Philipp — Electronics Faculty, Vilnius Tech.📄 LicenseThis project is Open for educational and academic use.