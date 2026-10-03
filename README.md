# 🍕 PizzaRP – Pizzeria Reference Project (Console)

> 🚧 This is a template repository for student project in the course Programming Foundations at FHNW, BSc BIT.  
> 🚧 Do not keep this section in your final submission.

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# 🍕 TEMPLATE for documentation
> 🚧 Please remove this paragraphs having "🚧". These are comments for preparing the documentations.
## 📝 Analysis

**Problem**
> 🚧 Describe the real-world problem your application solves. (Not HOW, but WHAT)

💡 Example: In a small local pizzeria, the staff writes orders and calculates totals by hand. This causes mistakes and inconsistent orders or discounts.

**Scenario**
> 🚧 Describe when and how a user will use your application

💡 Example: PizzaRP solves the part of the problem where orders and totals are created by letting a user select items from a menu and automatically generating a correct invoice.

### 👤 User Roles

> 🚧 Identify *who* uses your application before writing stories. Writing every story for a generic "user" hides the fact that different people need different things (M. Cohn, *User Stories Applied*, ch. 3 "User Role Modeling"). Name your roles and use them consistently in your stories.

| Role | Description |
|------|-------------|
| **Customer** | Orders pizzas and wants to know what they have ordered and how much they need to pay. |
| **Staff member** | Takes orders at the counter and enters them into the console application. |
| **Owner** | Runs the pizzeria, maintains the menu, and keeps records of all sales. |

### 📖 User Stories

> 🚧 **How to write a good user story**
>
> - Use the scheme **"As a *&lt;role&gt;*, I want *&lt;capability&gt;*, so that *&lt;benefit&gt;*."**
>   The benefit ("so that …") explains *why* the story is valuable. If you cannot name a benefit, question whether the story is needed.
> - A story consists of three parts, the "three Cs": the **Card** (the short sentence), the **Conversation** (the details discussed within the team), and the **Confirmation** (the acceptance criteria, which show when the story is done).
> - Check each story against **INVEST**: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable.
> - **Acceptance criteria** must be *specific* and *testable*. Use concrete values (e.g., "CHF 25.00", "two decimal places") and avoid vague words such as "fast", "easy", "correct", or "user-friendly". A good criterion can be turned directly into a test case with an input and an expected output.
> - Write acceptance criteria either as a **checklist** of observable rules or in the **Given–When–Then** structure:
>   *Given* a starting situation, *when* an action happens, *then* a specific, observable result occurs.
> - Include at least one criterion for the **normal case** and one for an **edge case or invalid input** (e.g., a quantity of 0, an empty order, a missing file).
>
> 💡 The stories below are examples for PizzaRP. Replace them with the stories of your own project.

All prices are in Swiss francs (CHF). The examples use the following menu from `menu.txt`:

| No. | Pizza | Size | Unit price |
|-----|-------|------|-----------:|
| 1 | Margherita | Medium | CHF 12.50 |
| 2 | Salami | Large | CHF 15.00 |
| 3 | Funghi | Small | CHF 9.00 |
| 4 | Hawaii | Medium | CHF 14.00 |
| 5 | Diavola | Large | CHF 17.50 |

---

#### US-01: Show the pizza menu

**As a** customer, **I want** to see a numbered list of all available pizzas with their size and price, **so that** I can decide what to order.

**Acceptance criteria**
- The menu is displayed when the staff member selects option `1` ("Show menu") in the main menu.
- The menu is also displayed automatically before a new order is started (option `2`).
- Each pizza is shown on its own line in the format `<No>. <Name> (<Size>) - CHF <Price>`, e.g., `1. Margherita (Medium) - CHF 12.50`.
- The numbering starts at `1` and follows the order of the lines in `menu.txt`.
- All prices are displayed with exactly two decimal places.
- *Given* `menu.txt` contains the five pizzas listed above, *when* the menu is displayed, *then* exactly five numbered lines are shown, from `1. Margherita (Medium) - CHF 12.50` to `5. Diavola (Large) - CHF 17.50`.

---

#### US-02: Maintain the menu in a file

**As an** owner, **I want** the menu to be read from the text file `menu.txt`, **so that** I can change pizzas and prices without changing the program code.

**Acceptance criteria**
- The application reads `menu.txt` at startup.
- Each line has the format `Name;Size;Price` (three fields separated by `;`), e.g., `Margherita;Medium;12.50`.
- *Given* the owner adds the line `Quattro Formaggi;Large;18.00` to `menu.txt`, *when* the application is restarted and the menu is displayed, *then* `6. Quattro Formaggi (Large) - CHF 18.00` appears as the last line of the menu.
- *Given* `menu.txt` contains the line `Calzone;Large;abc`, *when* the menu is loaded, *then* the warning `⚠️ Skipping invalid line: Calzone;Large;abc` is displayed, the line is not added to the menu, and all valid lines are still loaded.
- *Given* a line in `menu.txt` does not contain exactly three fields (e.g., `Marinara;Small`), *when* the menu is loaded, *then* that line is not added to the menu and the application does not crash.
- *Given* `menu.txt` does not exist, *when* the application starts, *then* a new `menu.txt` is created containing the three starter pizzas Margherita (Medium, 12.50), Salami (Large, 15.00), and Funghi (Small, 9.00), and these three pizzas are displayed in the menu.

---

#### US-03: Order pizzas with a quantity

**As a** customer, **I want** to order several pieces of the same pizza and see the total price for each item, **so that** I know how much each item of my order costs.

**Acceptance criteria**
- The staff member selects a pizza by entering its menu number.
- After selecting a pizza, the staff member enters a quantity (a whole number).
- Each selected pizza has a unit price taken from the menu.
- The system multiplies the unit price by the quantity to calculate the item total.
- The item total is displayed with two decimal places, e.g., `2x Margherita (Medium) - CHF 25.00`.
- *Given* a pizza with a unit price of CHF 12.50 and a quantity of 2, *when* the item total is calculated, *then* the result is CHF 25.00.
- *Given* a pizza with a unit price of CHF 17.50 and a quantity of 3, *when* the item total is calculated, *then* the result is CHF 52.50.
- *Given* a quantity of 0 or smaller (e.g., `0` or `-2`), *when* the item total is calculated, *then* the result is always CHF 0.00 (the calculation never returns a negative amount).
- Entering `done` instead of a pizza number finishes the order.

---

#### US-04: Reject invalid input

**As a** staff member, **I want** the application to reject invalid input with a clear message and let me try again, **so that** a typing mistake does not crash the program or create a wrong order.

**Acceptance criteria**
- *Given* the menu has five pizzas, *when* the staff member enters `0`, `6`, `-1`, `abc`, or an empty input as pizza number, *then* the message `⚠️ Invalid choice.` is displayed, nothing is added to the order, and the staff member is asked for a pizza number again.
- *Given* a valid pizza was selected, *when* the staff member enters `0`, a negative number, a decimal number (e.g., `1.5`), or text (e.g., `two`) as quantity, *then* the message `⚠️ Invalid quantity.` is displayed, the pizza is not added to the order, and the staff member is asked for the quantity again.
- *Given* the main menu is displayed, *when* the staff member enters anything other than `1`, `2`, or `3`, *then* the message `⚠️ Invalid choice.` is displayed and the main menu is shown again.
- Input is accepted regardless of surrounding spaces and upper/lower case for the keyword, e.g., ` DONE ` finishes the order just like `done`.
- In none of the cases above does the program terminate with an error (no Python traceback is shown).

---

#### US-05: See the running subtotal

**As a** customer, **I want** to see the current subtotal after each pizza is added, **so that** I can keep track of my spending while ordering.

**Acceptance criteria**
- After each successfully added item, the message `Added! Current subtotal: CHF <amount>` is displayed.
- The subtotal is the sum of all item totals (unit price × quantity) in the current order, before any discount.
- The subtotal is displayed with two decimal places.
- *Given* the order already contains 1x Salami (CHF 15.00), *when* 2x Margherita (CHF 12.50 each) are added, *then* the message `Added! Current subtotal: CHF 40.00` is displayed.
- An invalid input (see US-04) does not change the subtotal.

---

#### US-06: Apply discounts automatically

**As an** owner, **I want** the pizzeria's discounts to be applied automatically, **so that** every customer receives the same discounts and staff do not make calculation mistakes.

**Acceptance criteria**
- **Rule 1 – Free pizza:** If an order contains **more than 3** pizzas in total (sum of all quantities), the cheapest pizza (one piece) is free.
- **Rule 2 – 10 % discount:** If the amount after Rule 1 is **CHF 50.00 or more**, a discount of 10 % is deducted from that amount.
- Rule 1 is always applied before Rule 2.
- Each applied discount is listed with its name and amount, e.g., `Free pizza: Funghi (-CHF 9.00)` or `10% discount (-CHF 5.25)`.
- The final total is displayed with two decimal places.

| Given this order | Subtotal | Discount(s) applied | Then the total is |
|------------------|---------:|---------------------|------------------:|
| 2x Margherita | 25.00 | none | **CHF 25.00** |
| 1x Margherita, 1x Salami, 1x Funghi, 1x Hawaii (4 pizzas) | 50.50 | Free pizza: Funghi (-9.00) → 41.50 is below 50.00, so no 10 % | **CHF 41.50** |
| 3x Diavola (3 pizzas) | 52.50 | 10% discount (-5.25) | **CHF 47.25** |
| 1x Salami, 2x Diavola (exactly CHF 50.00) | 50.00 | 10% discount (-5.00) | **CHF 45.00** |
| 2x Diavola, 1x Hawaii (CHF 49.00) | 49.00 | none | **CHF 49.00** |
| 4x Diavola, 1x Funghi (5 pizzas) | 79.00 | Free pizza: Funghi (-9.00) → 70.00; 10% discount (-7.00) | **CHF 63.00** |

---

#### US-07: See an order summary

**As a** customer, **I want** to see a summary of my complete order before the invoice is created, **so that** I can check that everything is correct.

**Acceptance criteria**
- The summary is shown after the staff member enters `done`.
- The summary starts with the heading `--- ORDER SUMMARY ---`.
- It lists every ordered item with quantity, name, size, and item total, e.g., `2x Margherita (Medium) - CHF 25.00`.
- It lists every applied discount (see US-06).
- It ends with the final amount in the format `TOTAL: CHF <amount>` with two decimal places.
- *Given* the staff member enters `done` without having added any pizza, *when* the order is finished, *then* the message `⚠️ No pizzas selected.` is displayed, no summary and no invoice are created, and the main menu is shown again.

---

#### US-08: Save the invoice as a file

**As an** owner, **I want** each completed order to be saved as a numbered invoice file, **so that** I have a permanent record of all sales.

**Acceptance criteria**
- An invoice file is created automatically for every order that contains at least one pizza.
- The file name follows the pattern `invoice_<NNN>.txt` with a three-digit number, e.g., `invoice_001.txt`.
- *Given* no invoice file exists yet, *when* an order is completed, *then* the file `invoice_001.txt` is created.
- *Given* `invoice_001.txt` and `invoice_002.txt` already exist, *when* an order is completed, *then* the file `invoice_003.txt` is created and the existing files remain unchanged.
- The invoice contains the heading `🍕 PIZZA RP INVOICE`, one line per ordered item (quantity, name, size, item total), all applied discounts, and the line `TOTAL: CHF <amount>`.
- The amounts in the invoice file are identical to the amounts shown in the order summary (US-07).
- After saving, the message `✅ Invoice saved as invoice_<NNN>.txt` is displayed.

---

#### US-09: Exit the application

**As a** staff member, **I want** to close the application via the main menu, **so that** I can end my shift in a controlled way.

**Acceptance criteria**
- *Given* the main menu is displayed, *when* the staff member enters `3`, *then* the message `Goodbye 👋` is displayed and the program ends.
- All invoices created during the session remain saved after the program has ended.

---


**Use cases:**
- Show Menu (from `menu.txt`)
- Create Order (choose pizzas)
- Show Current Order and Total
- Print Invoice (to `invoice_xxx.txt`)

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

> 🚧 In this section, document how your project fulfills each criterion.  
---
The application interacts with the user via the console. Users can:
- View the pizza menu
- Select pizzas and quantities
- See the running total
- Receive an invoice generated as a file

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main-invoice.py` as follows:

- **Menu selection:** When the user enters a pizza number, the program checks if the input is a digit and within the valid menu range:
	```python
	if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
			print("⚠️ Invalid choice.")
			continue
	```
	This ensures only valid menu items can be ordered.

- **Quantity input:** After a pizza is selected, the program asks for the quantity until a whole number of at least 1 is entered:
	```python
	if not quantity.isdigit() or int(quantity) < 1:
			print("⚠️ Invalid quantity.")
			continue
	```
	This rejects `0`, negative numbers, decimal numbers, and text.

- **Menu file validation:** When reading the menu file, the program checks for valid price values and skips invalid lines:
	```python
	try:
			menu.append({"name": name, "size": size, "price": float(price)})
	except ValueError:
			print(f"⚠️ Skipping invalid line: {line.strip()}")
	```

- **Main menu options:** The main menu checks for valid options and handles invalid choices gracefully:
	```python
	else:
			print("⚠️ Invalid choice.")
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.

---

---


### 3. File Processing

The application reads and writes data using files:

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		Margherita;Medium;12.50
		Salami;Large;15.00
		Funghi;Small;9.00
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
	- Example:
		```
		🍕 PIZZA RP INVOICE
		---------------------
		3x Diavola (Large) - CHF 52.50
		---------------------
		Discount: 10% discount (-CHF 5.25)
		TOTAL: CHF 47.25
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Menu reading (file input) and displaying menu|
| Student B  | Order logic and data validation              |
| Student C  | Invoice generation (file output) and slides  |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
