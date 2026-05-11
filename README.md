# Tech Repair Shop Management System

A robust Python-based Command Line Interface (CLI) application designed to automate the billing and management of hardware and software repair services. The system leverages advanced Object-Oriented Programming (OOP) principles to ensure data integrity and scalable architecture.

* Explanation video: https://drive.google.com/file/d/1p-L33eRA0znXglsBG0SBAM0J_QOitCNW/view?usp=sharing

## Project Overview

The Tech Repair Shop System serves as a centralized tool for technicians to catalog services, manage customer sessions, and generate itemized invoices. The application distinguishes between physical hardware repairs and digital software services, applying unique fiscal logic to each category automatically.

## Technical Architecture

The system is engineered using the four pillars of Object-Oriented Programming to meet high-level software engineering standards:

* **Abstraction:** An Abstract Base Class (`RepairService`) defines the mandatory interface for all repair types, preventing the instantiation of incomplete service objects.
* **Inheritance:** Specialized subclasses (`HardwareRepair` and `SoftwareRepair`) extend the base class, inheriting core functionality while implementing unique attributes such as part costs and operating system versions.
* **Encapsulation:** Sensitive data members, including labor costs and service statuses, are protected using private attributes. Access is managed through property decorators (getters and setters) that enforce strict validation rules.
* **Polymorphism:** The `CustomerInvoice` class processes a heterogeneous list of service objects. By invoking the `calculate_service_cost()` method, the system executes the specific logic relevant to each object type at runtime.

## Key Features

* **Standardized Service Catalog:** A pre-defined registry of common repairs with transparent base labor rates.
* **Session-Based Invoicing:** Ability to aggregate multiple service items into a single customer transaction.
* **Dynamic Cost Calculation:**
* Hardware Logic: (Labor + Parts) + 10% physical goods tax.
* Software Logic: Labor + $5.00 flat digital processing fee.


* **Data Validation:** Integrated logic to prevent negative financial values and illogical service status updates.

## Installation and Execution

### Prerequisites

* Python 3.6 or higher.

### Running the Application

1. Clone or download the source code to your local directory.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Execute the program:
```bash
python Tech Repair Shop System.py

```



## User Operation Guide

The application utilizes a state-driven main loop. Follow the numbered menu prompts to perform the following actions:

1. **View Services:** Displays the available catalog, including the specific repair type and base labor cost.
2. **Add Service to Invoice:** Prompts for a Service ID to append a specific repair object to the current session.
3. **View Current Invoice:** Lists all items currently held in the invoice buffer to verify selection.
4. **Print Final Bill & Exit:** Triggers the polymorphic calculation engine to generate a formatted receipt and terminates the session gracefully.
5. **Exit Without Saving:** Closes the application immediately without generating a bill.

## Error Handling and Robustness

To ensure system stability, the following safeguards are implemented:

* **Input Sanitization:** The menu system handles non-numeric and out-of-range inputs without crashing, providing clear feedback to the user.
* **Integrity Constraints:** The invoice engine checks for empty datasets before attempting to generate a final bill.
* **Attribute Protection:** Backend logic prevents the assignment of invalid states (e.g., negative labor costs), ensuring the financial accuracy of all generated receipts.
