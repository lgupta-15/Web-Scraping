# 🕷️ Web Scraping Project

A Python-based web scraper that extracts product information (names, prices, and ratings) from e-commerce websites and saves the data to a CSV file.

## 📋 Features

- **Product Information Extraction**: Automatically extracts product names, prices, and ratings
- **Flexible CSS Selectors**: Support for custom CSS selectors to adapt to different website structures
- **CSV Export**: Saves scraped data in structured CSV format for easy analysis
- **Error Handling**: Robust error handling with detailed logging
- **CLI Interface**: Command-line interface for easy usage
- **Scalable Design**: Modular architecture for easy extension and customization

## 🔧 Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lgupta-15/Web-Scraping.git
   cd Web-Scraping
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Basic Usage

```bash
python main.py -u "https://example-ecommerce.com"
```

### With Custom CSS Selectors

```bash
python main.py -u "https://example.com" \
  -n ".product-name" \
  -p ".product-price" \
  -r ".product-rating"
```

### With Product Container Selector

```bash
python main.py -u "https://example.com" \
  -c ".product-item" \
  -n ".name" \
  -p ".price" \
  -r ".rating"
```

### Save to Custom File

```bash
python main.py -u "https://example.com" -o my_products.csv
```

## 📚 Command-Line Options

```
usage: main.py [-h] -u URL [-n NAME_SELECTOR] [-p PRICE_SELECTOR] 
               [-r RATING_SELECTOR] [-c CONTAINER_SELECTOR] [-o OUTPUT]

Optional arguments:
  -h, --help              Show this help message and exit
  -u, --url URL           URL of the e-commerce website (required)
  -n, --name-selector     CSS selector for product name
  -p, --price-selector    CSS selector for product price
  -r, --rating-selector   CSS selector for product rating
  -c, --container         CSS selector for product container
  -o, --output            Output CSV filename (default: products.csv)
```

## 📖 Examples

### Example 1: Scrape without specifying selectors

```bash
python main.py -u "https://example-shop.com/products"
```

The scraper will attempt to automatically find product information.

### Example 2: Scrape with specific selectors

```bash
python main.py \
  -u "https://amazon.example.com" \
  -c ".s-result-item" \
  -n ".a-price-whole" \
  -p ".a-price" \
  -r ".a-star-small"
```

### Example 3: Save results with custom filename

```bash
python main.py -u "https://shop.com" -o electronics.csv
```

## 🔍 Finding CSS Selectors

To find the correct CSS selectors for a website:

1. Open the website in your browser
2. Right-click on a product element (name, price, or rating)
3. Select "Inspect" or "Inspect Element"
4. Look for the HTML tags and class/id attributes
5. Use the class name or id as your selector (e.g., `.product-name` or `#price`)

**Common selector examples**:
- `.product-name` - class selector
- `#product-id` - id selector
- `div.item p.price` - combined selector

## 📊 Output Format

The scraper generates a CSV file with the following columns:

| name | price | rating |
|------|-------|--------|
| Product Name 1 | $29.99 | 4.5 |
| Product Name 2 | $39.99 | 4.8 |
| Product Name 3 | $19.99 | 4.2 |

## 📝 Code Structure

```
Web-Scraping/
├── main.py              # CLI entry point and argument parsing
├── scraper.py           # Core ProductScraper class
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

### `scraper.py` - ProductScraper Class

**Main Methods**:

- `fetch_page()` - Fetches and parses the webpage
- `extract_products()` - Extracts product information using CSS selectors
- `save_to_csv()` - Saves extracted data to CSV file
- `scrape()` - Complete workflow (fetch → extract → save)
- `get_products()` - Returns the list of extracted products
- `clear_products()` - Clears the products list

### `main.py` - CLI Interface

Provides command-line argument parsing and orchestrates the scraping process with user-friendly output.

## 🛡️ Legal & Ethical Considerations

- **Respect `robots.txt`**: Check if the website allows scraping in its `robots.txt` file
- **Rate Limiting**: Avoid making too many requests in a short time
- **Terms of Service**: Review the website's ToS before scraping
- **User-Agent**: The scraper includes a User-Agent header to identify itself
- **Responsible Scraping**: Use the tool responsibly and ethically

## 🔧 Advanced Usage

### Using the Scraper as a Module

```python
from scraper import ProductScraper

# Initialize scraper
scraper = ProductScraper("https://example.com")

# Fetch and extract
soup = scraper.fetch_page()
products = scraper.extract_products(
    soup,
    name_selector=".product-name",
    price_selector=".price",
    rating_selector=".rating"
)

# Save to CSV
scraper.save_to_csv("my_products.csv")

# Access products programmatically
for product in scraper.get_products():
    print(f"{product['name']}: {product['price']} ({product['rating']})")
```

## 🐛 Troubleshooting

**Issue**: No products found
- **Solution**: Verify the CSS selectors are correct by inspecting the website's HTML

**Issue**: Connection timeout
- **Solution**: Check your internet connection and ensure the website is accessible

**Issue**: Permission denied errors
- **Solution**: Check the website's `robots.txt` and Terms of Service

**Issue**: Empty CSV file
- **Solution**: Ensure you're using the correct container selector or let the scraper auto-detect

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy Scraping! 🕷️**
