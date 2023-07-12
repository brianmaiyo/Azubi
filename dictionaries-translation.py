#creted a dictionary which consisted of colors red,green, blue, yellow as the keys 
#and the german translation rot,grun,blau,gelb as values.
#Using the input, asked  for another english color 
#and its german translation and added the pair to the dictionary

colors={}
colors['red']='rot'
colors['green']='grun'
colors['blue']='blau'
colors['yellow']='gelb'
print( colors)

english_input =input('Enter another color in English: \n')
german_input =input('Enter the corresponding color in German: \n')
colors[english_input]=german_input

print( colors)
#translation for the user
query = input('which color should be translated?: \n')
print(f'The German word for {query} is {colors[query]}')