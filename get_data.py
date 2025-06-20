import requests
import json

API_KEY = 'Nws4gMRlDhC40i5tnL7RYrS2Q9vPN3ZDhwmvzxJN'
url = 'https://api.nal.usda.gov/fdc/v1/foods/list'

# Include nutrient IDs for protein, fat, carbs, and calories
params = {
    'api_key': API_KEY,
    'pageSize': 199,
    'dataType': 'Foundation',
    'nutrients': ['203', '204', '205', '208']
}

def get_raw_data(url, params):
    """Fetch data from the USDA API."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

def get_macro_data(food_list):
    """Extract protein, fat, carbs, and calorie content from each food item."""
    for food in food_list:
        food_name = food.get('description')
        fdc_id = food.get('fdcId')
        
        macros = {'Protein': 0, 'Fat': 0, 'Carbs': 0, 'Calories': 0}

        for nutrient in food.get('foodNutrients', []):
            if nutrient.get('number') == '203':
                macros['Protein'] = nutrient.get('amount', 0)
            elif nutrient.get('number') == '204':
                macros['Fat'] = nutrient.get('amount', 0)
            elif nutrient.get('number') == '205':
                macros['Carbs'] = nutrient.get('amount', 0)
        
        print(f"{food_name} (ID: {fdc_id}) has "
              f"Protein: {macros['Protein']}g, "
              f"Fat: {macros['Fat']}g, and "
              f"Carbs: {macros['Carbs']}g. ")

# Run
data = get_raw_data(url, params)
print(get_macro_data(data))






