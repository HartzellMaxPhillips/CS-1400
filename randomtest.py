from random import *

color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", 
"skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
ran_color = choice(color_list)
ran_size1 = randrange(30, 100)
ran_size2 = randrange(1,4)
print(ran_color, ran_size1, ran_size2)