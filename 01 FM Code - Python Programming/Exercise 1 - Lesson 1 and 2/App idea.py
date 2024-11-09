# Import necessary libraries
import zbarlight
from PIL import Image
import requests

def scan_barcode(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Scan the barcode
        codes = zbarlight.scan_codes('ean13', image)
        if codes:
            return codes[0].decode("utf-8")
        return None

def get_price(barcode):
    # Example API endpoint; you'll need the actual Pick n Pay API endpoint
    api_url = f"https://api.picknpay.com/prices/{barcode}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json().get("price")
    return "Price not found"

if __name__ == "__main__":
    image_path = input("Enter the path to the barcode image: ")
    barcode = scan_barcode(image_path)
    
    if barcode:
        price = get_price(barcode)
        print(f"The price of the item is: {price}")
    else:
        print("No barcode detected")
