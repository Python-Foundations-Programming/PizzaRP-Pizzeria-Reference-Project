#  Flashcards for language learning
  

Group members: Laura Manni
			   Sümeyya Güclü-Babür
			   Berfin Menes

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# TEMPLATE for documentation

## 📝 Analysis

**Problem**

 Learning languages can be difficult and takes a lot of time. To be able to communicate in a language you need to have sufficient vocabulary.

**Scenario**

 The app is mobile and easy to use, so it can be used while commuting and anytime users need a quick study-session. It is a good way to enlarge your vocabulary or if there is a test soon to study for.

**User stories:**
1. As a user, I want to be able to change the main language.
2. As a user, I want to have study-mode flashcards which I can flip to see the translation.
3. As a user, I want to be able to test the learning progress so far by writing the answer.
4. As a user, I want to repeat the test with the wrong answers.

**Use cases:**
- Study-mode with normal flashcards
- Test-mode with "right" / "wrong" feedback
- Show percentage of rightly asnwered words

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

  
---
The application interacts with the user via the console. Users can:
- Flip the flashcards
- Write down translations
- Swipe to the next card
- Repeat wrong answers

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. The goal is to write down translations, so numbers and special characters will not work.
**Test-mode:** When a user enters a number, an error message will pop up and direct users to enter letters.



### 3. File Processing

The application reads and writes data using files:

- **Input file:** List of German - English vocabulary
	
	

- **Output file:** The flashcards

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- Dictionary


### How to Run

1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used



These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions



| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Make a vocabulry file and create study-mode	|
| Student B  | programm test-mode           			  	 |
| Student C  | programm test-mode 							 |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
