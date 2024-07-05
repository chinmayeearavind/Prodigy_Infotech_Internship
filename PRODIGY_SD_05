import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def scrape_product_info(url, num_pages=1):
    products = []
    
    for page in range(1, num_pages + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            name = card.find('h2', class_='product-name').text.strip()
            price = card.find('span', class_='product-price').text.strip()
            rating = card.find('div', class_='product-rating').get('data-rating', 'N/A')
            
            product_url = card.find('a', class_='product-link')['href']
            full_product_url = urljoin(url, product_url)
            
            products.append({
                'name': name,
                'price': price,
                'rating': rating,
                'url': full_product_url
            })
    
    return products

def save_to_csv(products, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price', 'rating', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def main():
    base_url = 'https://example-ecommerce-site.com/products'
    num_pages = 5  # Adjust this to scrape more or fewer pages
    
    print("Scraping product information...")
    products = scrape_product_info(base_url, num_pages)
    
    output_file = 'product_info.csv'
    save_to_csv(products, output_file)
    
    print(f"Scraped {len(products)} products.")
    print(f"Data saved to {output_file}")

if __name__ == '__main__':
    main()
