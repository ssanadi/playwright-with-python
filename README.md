# Playwright with Python E2E Automation Test Project

This repository contains an end-to-end automated test suite for a sample web application. It demonstrates the use of Playwright with Python for test automation while adhering to best practices like the Page Object Model (POM) design pattern.

---

## Features Covered

1. **Login Page:**
   - Valid login.
   - Invalid login handling.
2. **Product Listing Page:**
   - Navigation to product listings after login.
3. **Product Details Page:**
   - Verification of navigation from product listing to product details.
4. **Shopping Cart:**
   - Adding products to the shopping cart.

---

## Key Highlights

- **Test Design:**
  - Tests are structured using the **Page Object Model (POM)** for modularity and maintainability.
  - Assertions are included to validate the expected outcomes for each scenario.

- **Reporting:**
  - Integrated test reporting using **pytest-html**.
  - Reports include test name, status, execution time and screenshots for failed tests.

- **Continuous Integration (CI):**
  - Configured using **GitHub Actions**.
  - Automatically installs dependencies, runs tests and generates reports on every push or pull request.

---

## Setup Instructions

### Prerequisites
- Python 3.11 or higher.
- Git installed on your system.

### Steps to Set Up
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd playwright-with-python

2. Install dependencies:
   ```sh
   pip install pipenv
   pipenv install
   pipenv run playwright install --with-deps

3. Running the Application Locally at http://127.0.0.1:5000:
   ```sh
   pipenv run python store/app.py

4. Set up environment variables in tests\config\secret_config.py file:
      ```env
      PASSWORD=<application password>

5. Run all tests parallelly using:
   ```sh
   pipenv run python -m pytest ./tests --html=reports/report.html --self-contained-html --base-url=http://127.0.0.1:5000 -n auto

5. The generated test report can be found in the reports/ directory

---
## Continuous Integration
The repository includes a GitHub Actions workflow file (`.github/workflows/playwright.yml`) that:

1.  Sets up Python and installs dependencies.
2.  Starts the Flask application in the background.
3.  Runs the Playwright tests.
4.  Uploads the test report as an artifact.

---
## Key Files and Directories
-   **`store/`**: Contains the Flask application.
-   **`tests/specs/`**: Test scripts for the defined scenarios.
-   **`tests/pages/`**: Page Object classes implementing POM.
-   **`reports/`**: Generated test reports.
-   **`Pipfile`**: Project dependencies.