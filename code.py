# pip install colorthief
#pip install matplotlib -- to see the plot of the colours

from colorthief import ColorThief
import matplotlib.pyplot as plt

import colorsys   #to convert the rgb values to hex and hsv, hls etc


ct = ColorThief("testing.jpg")
dominant_color = ct.get_color(quality=1)  #gets 1 dominant color
print(dominant_color)  # givess rgb values for the color

plt.imshow([[dominant_color]]) #pass a list of list
plt.show()

#to get more dominant colors

palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

#to convert the rgb values to hex and hsv, hls etc

for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))