# E-Commerce-Competitor-Price-Tracker-eBay---Collectible-Sneakers-
this project scrapes prices of collectible sneakers from eBay using **Selenium**, allowing users to track competitors in a specific niche.
---

## 🎯 Features

- Targets: [eBay - Collectible Sneakers](https://www.ebay.com/b/Collectible-Sneakers/bn_7000259435)
- User input for number of pages to scrape
- Extracts:
  - Sneaker title
  - Price
  - Item URL
  - Link to product
- Outputs to `sneakers_prices.csv`

---

## 🛠️ Tech Stack

- Python 3
- Selenium
- ChromeDriver
- pandas (optional, for CSV handling)

---
## 💻 How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```
### 2. Run the Tracker
```bash
python tracker.py
```
### 3. View Output
The file sneakers_prices.csv will be saved
