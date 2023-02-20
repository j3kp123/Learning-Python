priColors = ['blue', 'red', 'yellow']
Color1 =str(input("Pick a color: blue, red, or yellow."));\
Color2 =str(input("Pick a different color: blue, red, or yellow."))

if Color1=='blue' and Color2=='red': print('You have created the color Purple!')
elif Color1=='red' and Color2=='yellow': print('You have created the color Orange!')
elif Color1=='blue' and Color2=='yellow': print('You have created the color Green!')
elif Color1=='red' and Color2=='blue': print('You have created the color Purple!')
elif Color1=='yellow' and Color2=='red': print('You have created the color Orange!')
elif Color1=='yellow' and Color2=='blue': print('You have created the color Green!')
