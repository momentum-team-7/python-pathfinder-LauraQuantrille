from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
# link pillow module

file_small = 'elevation_small.txt'
file_large = 'elevation_large.txt'

file_test = 'testgrid.txt'


coordinates= []

with open(file_large) as file:
        for line in file.readlines():
                coordinates.append(line.split())
        # print(coordinates)

# from PIL import Image
# lightest(max_el) white
# darkest (min_el) black - in the grayscale range


min_el = int(min(map(min, coordinates)))
# print(min_el)

max_el = int(max(map(max, coordinates)))
# print(max_el)

minmax_range = int(max_el - min_el)
# print(minmax_range)


def grayscale(elevation):
        int_elevation = int(elevation)
        diff = (int_elevation - min_el)
#     print(diff)
        percent_of_range = (diff/minmax_range)
#     print(percent_of_range)
        grayscale_value = (percent_of_range * 255)
#     print(grayscale_value)
        render_pixel = RGB(grayscale_value)
#     print(render_pixel)
        return render_pixel



def RGB(grayscale_value):
        return (int(grayscale_value), int(grayscale_value), int(grayscale_value))

dimensions = len(coordinates[0]), len(coordinates)


im = Image.new('RGB', dimensions)
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        im.putpixel((x, y), grayscale(coordinates[y][x]))
im.save('elevation_large.png')
print(im)



# use im.putpixel to draw a line - function needed to compare elevation values and map the lowest values across

def map_footpath():
# foot_path - loop to map a lowest elevation path & link to ImageDraw 
# draw = ImageDraw.Draw(im) 
# draw.line((100,200, 150,300), fill=128)
# im.show()




#  find elevation, and then find grayscale for that elevation which will then get passed given x & y you figure out the elevation using index in list of lists
#  
# im.save('putPixel.png')
# im = Image.new('RGB', (1201, 1201))
# for row in coordinates:
#         for elevation in row:
#                 im.putpixel((row.index(elevation), coordinates.index(row)), grayscale(elevation))
# im.save('elevation_large.png')
# print(im) ---- rendered image with black spots