
using python

read earing.html and parse it with beautifulsoup

find all 
div with class="product-item-info"

for all the li
try find div with class="product-brand " and  store it in brandName
except brandNames = ""

try find <a  with class="product-item-link" and store it in Title
except Title = ""

try find div with class="value" and store it in Description 
except Description = ""


try find <span with  class="price" and store it in Prices
except Prices = ""

try find img with class="js-image-to-magnify d-mobile-hide" and store it in Image
except Image = " " 

open an excel file and write brandNames , Title and Prices in it