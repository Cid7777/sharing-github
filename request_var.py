"grab api"
import requests

res = requests.get("http://www.themealdb.com/api/json/v1/1/random.php?")
data = res.json()

print(data)
datashort = data['meals'][0]


meal_name = datashort['strMeal']
category = datashort['strCategory']
instructions = datashort['strInstructions']
meal_photo = datashort['strMealThumb']
youtube_video = datashort['strYoutube']

ingredient1 = datashort['strIngredient1']
ingredient2 = datashort['strIngredient2']
ingredient3 = datashort['strIngredient3']
ingredient4 = datashort['strIngredient4']
ingredient5 = datashort['strIngredient5']
ingredient6 = datashort['strIngredient6']
ingredient7 = datashort['strIngredient7']
ingredient8 = datashort['strIngredient8']
ingredient9 = datashort['strIngredient9']
ingredient10 = datashort['strIngredient10']
ingredient11 = datashort['strIngredient11']
ingredient12 = datashort['strIngredient12']
ingredient13 = datashort['strIngredient13']
ingredient14 = datashort['strIngredient14']
ingredient15 = datashort['strIngredient15']
ingredient16 = datashort['strIngredient16']
ingredient17 = datashort['strIngredient17']
ingredient18 = datashort['strIngredient18']
ingredient19 = datashort['strIngredient19']
ingredient20 = datashort['strIngredient20']


measurement1 = datashort['strMeasure1']
measurement2 = datashort['strMeasure2']
measurement3 = datashort['strMeasure3']
measurement4 = datashort['strMeasure4']
measurement5 = datashort['strMeasure5']
measurement6 = datashort['strMeasure6']
measurement7 = datashort['strMeasure7']
measurement8 = datashort['strMeasure8']
measurement9 = datashort['strMeasure9']
measurement10 = datashort['strMeasure10']
measurement11 = datashort['strMeasure11']
measurement12 = datashort['strMeasure12']
measurement13 = datashort['strMeasure13']
measurement14 = datashort['strMeasure14']
measurement15 = datashort['strMeasure15']
measurement16 = datashort['strMeasure16']
measurement17 = datashort['strMeasure17']
measurement18 = datashort['strMeasure18']
measurement19 = datashort['strMeasure19']
measurement20 = datashort['strMeasure20']

ingredients = {ingredient1:measurement1,ingredient2:measurement2,ingredient3:measurement3,ingredient4:measurement4,ingredient5:measurement5,ingredient6:measurement6,ingredient7:measurement7,ingredient8:measurement8,
                ingredient9:measurement9,ingredient10:measurement10,ingredient11:measurement11,ingredient12:measurement12,ingredient13:measurement13,
                ingredient14:measurement14,ingredient15:measurement15,ingredient16:measurement16,ingredient17:measurement17,ingredient18:measurement18,ingredient19:measurement19,ingredient20:measurement20,}

print(meal_name)
print(category)
print(instructions)
print(meal_photo)
print(youtube_video)
print(ingredients)

