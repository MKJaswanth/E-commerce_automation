# 🎭 Playwright E-Commerce Automation

### End-to-End Test Automation using Python + Playwright + pytest

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-latest-green?logo=playwright)
![pytest](https://img.shields.io/badge/pytest-7.x-orange)
![CI](https://github.com/MKJaswanth/E-commerce_automation/actions/workflows/playwright.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


## About
A professional end-to-end automation framework built with **Python**, **Playwright**, and **pytest** for the [SauceDemo](https://www.saucedemo.com) e-commerce application.

- 21 automated test cases across 4 modules
- Page Object Model (POM) design pattern
- Cross-browser: Chromium, Firefox, WebKit
- GitHub Actions CI/CD — runs on every push
- HTML reports with failure screenshots


## Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11 | Core language |
| Playwright | Latest | Browser automation |
| pytest | 7.x | Test runner |
| pytest-playwright | Latest | Playwright-pytest plugin |
| pytest-html | Latest | HTML reporting |
| python-dotenv | Latest | Env variable management |
| GitHub Actions | — | CI/CD pipeline |

## Project Structure

```text
playwright-ecommerce-automation/
├── .github/workflows/playwright.yml ← CI/CD
├── pages/                           ← Page Object Models
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── test_data/users.json
├── pytest.ini
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- Git

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/MKJaswanth/E-commerce_automation.git
cd E-commerce_automation

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install browsers
playwright install

# 5. Set up environment variables
cp .env.example .env
```


## Running Tests

```bash
# Run all tests
pytest

# Run with visible browser
pytest --headed

# Run on Firefox
pytest --browser firefox

# Run on all 3 browsers
pytest --browser chromium --browser firefox --browser webkit

# Run specific test file
pytest tests/test_login.py -v

# Run a single test
pytest tests/test_login.py::TestLogin::test_tc001_valid_login

# Run by keyword
pytest -k "checkout" -v
```

## Test Reports

HTML reports are auto-generated after every run:

```bash
pytest --html=reports/report.html --self-contained-html
# Open reports/report.html in your browser
```

CI/CD reports are uploaded as GitHub Actions artifacts after every push. Download from the Actions tab.

## Test Coverage

| Module | Test Cases | Status |
|--------|-----------|--------|
| Authentication | 6 | ✅ Passing |
| Product Inventory | 5 | ✅ Passing |
| Shopping Cart | 5 | ✅ Passing |
| Checkout Flow | 5 | ✅ Passing |
| **Total** | **21** | ✅ **All passing** |

## Author

**Jaswanth MK**  
QA Engineer | Playwright | Python | pytest  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/mkjaswanth)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/MKJaswanth)

---
⭐ If this project helped you, give it a star!