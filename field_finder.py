import requests
from bs4 import BeautifulSoup

def find_input_fields(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all form tags
    forms = soup.find_all('form')

    for form in forms:
        print(f"Form Action: {form.get('action')}")
        inputs = form.find_all('input')
        
        # Loop through each input element in the form
        for input_tag in inputs:
            input_type = input_tag.get('type', 'text')  # Default to 'text' if type is not specified
            input_name = input_tag.get('name', 'No name attribute')
            print(f"Input Field - Type: {input_type}, Name: {input_name}")

        # Check if the form contains text areas
        textareas = form.find_all('textarea')
        for textarea in textareas:
            print(f"Textarea Field - Name: {textarea.get('name')}")

        # Check if the form contains select/dropdown fields
        selects = form.find_all('select')
        for select in selects:
            print(f"Select Field - Name: {select.get('name')}")

# Test the function with a website URL
find_input_fields('https://demo.testfire.net/')
