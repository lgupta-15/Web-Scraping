#!/usr/bin/env python3
"""
Web Scraping Application - Main Entry Point
Scrapes product information from e-commerce websites and exports to CSV.
"""

from scraper import ProductScraper
import argparse
import sys


def main():
    """Main application entry point."""
    
    parser = argparse.ArgumentParser(
        description='Web Scraper for E-commerce Product Information',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Basic usage with default selectors
  python main.py -u "https://example-ecommerce.com"
  
  # With custom CSS selectors
  python main.py -u "https://example.com" \\
    -n ".product-name" \\
    -p ".product-price" \\
    -r ".product-rating"
  
  # With product container selector
  python main.py -u "https://example.com" \\
    -c ".product-item" \\
    -n ".name" \\
    -p ".price" \\
    -r ".rating"
  
  # Save to custom CSV file
  python main.py -u "https://example.com" -o custom_products.csv
        '''
    )
    
    parser.add_argument(
        '-u', '--url',
        required=True,
        help='URL of the e-commerce website to scrape'
    )
    
    parser.add_argument(
        '-n', '--name-selector',
        default=None,
        help='CSS selector for product name (e.g., ".product-name")'
    )
    
    parser.add_argument(
        '-p', '--price-selector',
        default=None,
        help='CSS selector for product price (e.g., ".price")'
    )
    
    parser.add_argument(
        '-r', '--rating-selector',
        default=None,
        help='CSS selector for product rating (e.g., ".rating")'
    )
    
    parser.add_argument(
        '-c', '--container-selector',
        default=None,
        help='CSS selector for product container (e.g., ".product-item")'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='products.csv',
        help='Output CSV filename (default: products.csv)'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize scraper
        print(f"🕷️  Initializing scraper for: {args.url}")
        scraper = ProductScraper(args.url)
        
        # Perform scraping
        print("⏳ Starting scrape operation...")
        output_file = scraper.scrape(
            name_selector=args.name_selector,
            price_selector=args.price_selector,
            rating_selector=args.rating_selector,
            product_container=args.container_selector,
            output_file=args.output
        )
        
        # Display results
        products = scraper.get_products()
        print(f"\n✅ Scraping completed successfully!")
        print(f"📊 Total products extracted: {len(products)}")
        print(f"💾 Data saved to: {output_file}")
        
        if products:
            print("\n📋 Sample of extracted data:")
            for idx, product in enumerate(products[:3], 1):
                print(f"\n  {idx}. Name: {product['name']}")
                print(f"     Price: {product['price']}")
                print(f"     Rating: {product['rating']}")
            
            if len(products) > 3:
                print(f"\n  ... and {len(products) - 3} more products")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during scraping: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
