import requests
from bs4 import BeautifulSoup

#fetch content from amazon
def fetch_product_page(url):
  try:
      response = requests.get(url)
      response.raise_for_status()
      return response.text
  except requests.exceptions.RequestException as e:
      print(f"Error fetching the product page: {e}")
      return None

#parse the content
def extract_price(html):
  try:
      soup = BeautifulSoup(html, 'html.parser')
      price_element = soup.find('span', {'class': 'a-offscreen'})
      if price_element:
          return price_element.text.strip()
      else:
          return "Price not found"
  except Exception as e:
      print(f"Error extracting the price: {e}")
      return "Error"


#price display
def main():
  product_url = input("Enter the Amazon product URL: ")
  html = fetch_product_page(product_url)
  if html:
      price = extract_price(html)
      print(f"The current price of the product is: {price}")
  else:
      print("Unable to fetch the product page.")

if __name__ == "__main__":
  main()
