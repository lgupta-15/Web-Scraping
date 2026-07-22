#!/usr/bin/env python3
"""
Example usage of the ProductScraper class.
Demonstrates different ways to use the scraper programmatically.
"""

from scraper import ProductScraper
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def example_1_basic_scraping():
    """Example 1: Basic scraping with automatic detection."""
    print("\n" + "="*60)
    print("Example 1: Basic Scraping (Auto-detection)")
    print("="*60)
    
    try:
        scraper = ProductScraper("https://example-ecommerce.com")
        
        # Fetch and extract with auto-detection
        output_file = scraper.scrape()
        
        products = scraper.get_products()
        print(f"✅ Scraped {len(products)} products")
        print(f"💾 Saved to {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def example_2_custom_selectors():
    """Example 2: Scraping with custom CSS selectors."""
    print("\n" + "="*60)
    print("Example 2: Scraping with Custom Selectors")
    print("="*60)
    
    try:
        scraper = ProductScraper("https://example-store.com")
        
        # Scrape with specific selectors
        output_file = scraper.scrape(
            name_selector=".product-title",
            price_selector=".product-price",
            rating_selector=".product-rating",
            output_file="custom_products.csv"
        )
        
        print(f"✅ Scraping completed successfully")
        print(f"💾 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def example_3_container_selector():
    """Example 3: Scraping with product container selector."""
    print("\n" + "="*60)
    print("Example 3: Scraping with Container Selector")
    print("="*60)
    
    try:
        scraper = ProductScraper("https://shop.example.com")
        
        # Use container selector to identify product elements
        output_file = scraper.scrape(
            product_container=".product-item",
            name_selector=".item-name",
            price_selector=".item-price",
            rating_selector=".item-rating",
            output_file="shop_products.csv"
        )
        
        print(f"✅ Scraping completed successfully")
        print(f"💾 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def example_4_programmatic_access():
    """Example 4: Accessing and processing scraped data programmatically."""
    print("\n" + "="*60)
    print("Example 4: Programmatic Data Access")
    print("="*60)
    
    try:
        scraper = ProductScraper("https://example-store.com")
        
        # Fetch page
        soup = scraper.fetch_page()
        
        # Extract products
        scraper.extract_products(
            soup,
            name_selector=".product-name",
            price_selector=".price",
            rating_selector=".rating"
        )
        
        # Get products
        products = scraper.get_products()
        
        # Process products
        print(f"Total products: {len(products)}\n")
        
        for idx, product in enumerate(products[:5], 1):
            print(f"{idx}. {product['name']}")
            print(f"   Price: {product['price']}")
            print(f"   Rating: {product['rating']}")
            print()
        
        if len(products) > 5:
            print(f"... and {len(products) - 5} more products")
        
        # Save to CSV
        scraper.save_to_csv("processed_products.csv")
        print(f"\n💾 Saved to CSV")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def example_5_multiple_scraping_sessions():
    """Example 5: Multiple scraping sessions."""
    print("\n" + "="*60)
    print("Example 5: Multiple Scraping Sessions")
    print("="*60)
    
    websites = [
        ("https://store1.example.com", "store1_products.csv"),
        ("https://store2.example.com", "store2_products.csv"),
        ("https://store3.example.com", "store3_products.csv"),
    ]
    
    total_products = 0
    
    for url, output_file in websites:
        try:
            print(f"\n🔄 Scraping: {url}")
            scraper = ProductScraper(url)
            
            scraper.scrape(
                name_selector=".product-name",
                price_selector=".price",
                rating_selector=".stars",
                output_file=output_file
            )
            
            count = len(scraper.get_products())
            total_products += count
            print(f"✅ Extracted {count} products → {output_file}")
            
        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
    
    print(f"\n📊 Total products scraped across all stores: {total_products}")


def example_6_error_handling():
    """Example 6: Handling errors gracefully."""
    print("\n" + "="*60)
    print("Example 6: Error Handling")
    print("="*60)
    
    test_urls = [
        "https://invalid-url-that-does-not-exist-12345.com",
        "https://example.com",
    ]
    
    for url in test_urls:
        print(f"\nTrying to scrape: {url}")
        
        try:
            scraper = ProductScraper(url)
            soup = scraper.fetch_page()
            print("✅ Successfully fetched page")
            
        except Exception as e:
            print(f"❌ Failed to fetch: {type(e).__name__}: {e}")


if __name__ == '__main__':
    print("🕷️  Web Scraper - Example Usage\n")
    
    # Run examples (uncomment to use)
    # example_1_basic_scraping()
    # example_2_custom_selectors()
    # example_3_container_selector()
    # example_4_programmatic_access()
    # example_5_multiple_scraping_sessions()
    # example_6_error_handling()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)
    print("\nNote: Uncomment examples in main.py to run them.")
    print("You can also use: python main.py -u <URL> [options]")
