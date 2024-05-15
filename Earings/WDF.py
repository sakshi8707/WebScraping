from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("earing.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all <div> elements with class="product-item-info"
product_items = soup.find_all("div", class_="product-item-info")

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers to the Excel file
sheet.append(["Brand Name", "Title", "Description", "Price", "Image"])

# Loop through each product item and extract data
for item in product_items:
    # Extract brand name
    brand_name_tag = item.find("div", class_="product-brand")
    brand_name = brand_name_tag.text.strip() if brand_name_tag else ""

    # Extract title
    title_tag = item.find("a", class_="product-item-link")
    title = title_tag.text.strip() if title_tag else ""

    # Extract description
    description_tag = item.find("div", class_="prod-desc-content")  # Adjust this line
    description = description_tag.text.strip() if description_tag else ""

    # Extract price
    price_tag = item.find("span", class_="price")
    price = price_tag.text.strip() if price_tag else ""

    # Extract image URL
    image_tag = item.find("img", class_="js-image-to-magnify d-mobile-hide")
    image = image_tag['src'] if image_tag else ""

    # Write data to the Excel file
    sheet.append([brand_name, title, description, price, image])

# Save the Excel file
workbook.save("earing_data.xlsx")
