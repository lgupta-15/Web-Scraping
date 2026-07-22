import requests
from bs4 import BeautifulSoup
import csv
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ProductScraper:
    """
    A web scraper for extracting product information from e-commerce websites.
    Extracts product names, prices, ratings, and stores data in CSV format.
    """
    
    def __init__(self, url: str, headers: Dict = None):
        """
        Initialize the scraper with a target URL.
        
        Args:
            url (str): The URL of the e-commerce website to scrape
            headers (dict): Optional HTTP headers for the request
        """
        self.url = url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.products = []
    
    def fetch_page(self) -> BeautifulSoup:
        """
        Fetch the webpage and return a BeautifulSoup object.
        
        Returns:
            BeautifulSoup: Parsed HTML content
            
        Raises:
            requests.RequestException: If the request fails
        """
        try:
            logger.info(f"Fetching page: {self.url}")
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            logger.info("Page fetched successfully")
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error fetching the page: {e}")
            raise
    
    def extract_products(self, soup: BeautifulSoup, 
                        name_selector: str = None,
                        price_selector: str = None,
                        rating_selector: str = None,
                        product_container: str = None) -> List[Dict]:
        """
        Extract product information from the parsed HTML.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            name_selector (str): CSS selector for product name
            price_selector (str): CSS selector for product price
            rating_selector (str): CSS selector for product rating
            product_container (str): CSS selector for product container
            
        Returns:
            List[Dict]: List of extracted product information
        """
        try:
            logger.info("Extracting product information...")
            
            if product_container:
                products = soup.select(product_container)
            else:
                products = soup.find_all(class_=lambda x: x and 'product' in x.lower())
            
            logger.info(f"Found {len(products)} products")
            
            for product in products:
                product_info = {}
                
                # Extract product name
                if name_selector:
                    name_elem = product.select_one(name_selector)
                    product_info['name'] = name_elem.text.strip() if name_elem else 'N/A'
                else:
                    product_info['name'] = product.text.strip()[:100]
                
                # Extract price
                if price_selector:
                    price_elem = product.select_one(price_selector)
                    product_info['price'] = price_elem.text.strip() if price_elem else 'N/A'
                else:
                    product_info['price'] = 'N/A'
                
                # Extract rating
                if rating_selector:
                    rating_elem = product.select_one(rating_selector)
                    product_info['rating'] = rating_elem.text.strip() if rating_elem else 'N/A'
                else:
                    product_info['rating'] = 'N/A'
                
                self.products.append(product_info)
            
            logger.info(f"Successfully extracted {len(self.products)} products")
            return self.products
            
        except Exception as e:
            logger.error(f"Error extracting products: {e}")
            raise
    
    def save_to_csv(self, filename: str = 'products.csv') -> str:
        """
        Save extracted products to a CSV file.
        
        Args:
            filename (str): Name of the output CSV file
            
        Returns:
            str: Path to the saved file
        """
        try:
            if not self.products:
                logger.warning("No products to save")
                return None
            
            logger.info(f"Saving {len(self.products)} products to {filename}")
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'price', 'rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(self.products)
            
            logger.info(f"Products saved successfully to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")
            raise
    
    def scrape(self, name_selector: str = None,
               price_selector: str = None,
               rating_selector: str = None,
               product_container: str = None,
               output_file: str = 'products.csv') -> str:
        """
        Complete scraping workflow: fetch, extract, and save.
        
        Args:
            name_selector (str): CSS selector for product name
            price_selector (str): CSS selector for product price
            rating_selector (str): CSS selector for product rating
            product_container (str): CSS selector for product container
            output_file (str): Output CSV filename
            
        Returns:
            str: Path to the saved CSV file
        """
        soup = self.fetch_page()
        self.extract_products(soup, name_selector, price_selector, rating_selector, product_container)
        return self.save_to_csv(output_file)
    
    def get_products(self) -> List[Dict]:
        """
        Get the list of extracted products.
        
        Returns:
            List[Dict]: List of product dictionaries
        """
        return self.products
    
    def clear_products(self):
        """Clear the products list."""
        self.products = []
        logger.info("Products list cleared")
