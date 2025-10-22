# Python-Keylogger
## Usage
1. Ensure your MySQL server is running and the database is set up using the provided SQL script.
2. Copy `.env.example` to `.env` and fill in your MySQL credentials.
3. Install dependencies:
   ```bash
   pip install pynput mysql-connector-python python-dotenv
   ```
4. Run the keylogger:
   ```bash
   python keylogger.py
   ```
5. Keystrokes will be logged to the MySQL database. You can view them with a SQL query such as:
   ```sql
   SELECT * FROM logs;
   ```

# Keylogger Project (Cybersecurity Educational Tool)

**Author:** Jack (Personal Project)

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [Technologies Used](#technologies-used)
7. [License](#license)
8. [Contact](#contact)
9. [Acknowledgements](#acknowledgements)
10. [Troubleshooting / FAQ](#troubleshooting--faq)
11. [Status](#status)

## Project Description
This Python keylogger was developed as a personal, self-guided project to demonstrate my understanding of cybersecurity concepts, Python programming, and secure software practices. It is intended as a portfolio piece and proof of hands-on learning for my resume. The project showcases my ability to design, document, and implement a security-related tool from scratch.
## Cybersecurity Relevance
- Understand how keyloggers operate and interact with operating systems.
- Learn about the risks and detection of keyloggers in real-world environments.
- Practice secure coding and configuration management (e.g., using environment variables).
- Explore database logging and event analysis for digital forensics.

## Features
- Logs all keystrokes (letters, numbers, symbols, and special keys)
- Stores logs in a MySQL database for analysis
- Handles special keys (e.g., [enter], [shift], [backspace])
- Secure configuration using environment variables
- Minimal, clear sample data for demonstration

## Ethical Use Notice
**This project is for educational and ethical penetration testing purposes only.**
**This project is for my personal education and portfolio only.**
Do not deploy or use this tool on any system without explicit permission. Unauthorized use of keyloggers is illegal and unethical.

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   - Python packages: `pip install -r requirements.txt` (or install `pynput`, `mysql-connector-python`, `python-dotenv`)
3. **Set up your environment variables**
   - Copy `.env.example` to `.env` and fill in your MySQL credentials
4. **Set up the database**
   - Run the SQL script: `mysql -u <user> -p < keylogger.sql`
5. **Run the keylogger**
   - `python keylogger.py`

## Sample Data
The `keylogger.sql` file includes a minimal set of sample data to demonstrate the types of key events that can be logged:
- Lowercase letter: `a`
- Uppercase letter: `A`
- Digit: `1`
- Symbol: `!`
- Space: ` `
- Special key: `[enter]`

## Security Best Practices
- **Never commit your real credentials to version control.** Use the `.env.example` file as a template and add `.env` to your `.gitignore`.
- Always use such tools in a controlled, authorized environment.
- Study and understand the legal and ethical implications of keylogging.

