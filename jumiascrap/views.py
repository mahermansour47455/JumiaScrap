from django.shortcuts import redirect, render
from .models import smartphoness
import requests
from bs4 import BeautifulSoup

def ListeSmartphonesJumia(request):
    url = "https://www.jumia.com.tn/smartphones/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the divs that contain information about the smartphones
    product_cards = soup.find_all("article", {"class": "prd _fb col c-prd"})

    # Extract the relevant information from each smartphone div
    smartphones = []
    marques=[]
    for div in product_cards:
        name = div.find("h3", {"class": "name"}).text.strip()
        price = div.find("div", {"class": "prc"}).text.strip()
        image = div.find("img", {"class": "img"})["data-src"]
        link=div.find("a", {"class": "core"})["href"]
        smartphones.append({'name': name, 'price': price, 'image_path': image,'link':link})

    for brand in soup.find_all('a', class_='fk-cb -me-start -fsh0'):
        if(brand.attrs.get("data-value", None) != None):
            brandname = brand.next
            marques.append(brandname)
    
    context={
        'products':smartphones,
        'marques':marques,
        
    }

    # Output the list of smartphones as a response
    return render(request,'home.html',context)

def search(request):
   
    
    marque=request.GET.get('q')
    minprice=request.GET.get('minprice')
    maxprice=request.GET.get('maxprice')

    if marque is None:
        marque = ""  # Set an empty string if marque is None
    if minprice is None:
        minprice = ""  # Set an empty string if minprice is None
    if maxprice is None:
        maxprice = ""  # Set an empty string if maxprice is None
        #https://www.jumia.com.tn/catalog/?q=samsung+a03&price=10-455#catalog-listing
        #https://www.jumia.com.tn/smartphones/apple/?price=2299-2299#catalog-listing

    url = "https://www.jumia.com.tn/smartphones/" + str(marque)+"/" + "?price=" + str(minprice) + "-" + str(maxprice)+"#catalog-listing"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the divs that contain information about the smartphones
    product_cards = soup.find_all("article", {"class": "prd _fb col c-prd"})

    # Extract the relevant information from each smartphone div
    smartphones = []
    marques=[]
    for div in product_cards:
        name = div.find("h3", {"class": "name"}).text.strip()
        price = div.find("div", {"class": "prc"}).text.strip()
        image = div.find("img", {"class": "img"})["data-src"]
        link=div.find("a", {"class": "core"})["href"]   
        smartphones.append({'name': name, 'price': price, 'image_path': image,'link':link})
    for brand in soup.find_all('a', class_='fk-cb -me-start -fsh0'):
        if(brand.attrs.get("data-value", None) != None):
            brandname = brand.next
            marques.append(brandname)

    context={
        'products':smartphones,
        'marques':marques,
        'selectedbrand': marque
    }

    # Output the list of smartphones as a response
    return render(request,'home.html',context)



    

    


    

