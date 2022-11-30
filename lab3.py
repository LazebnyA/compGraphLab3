from PIL import Image, ImageDraw
import math 

image = Image.new("RGBA", (960, 960), (250, 250, 250))    

draw = ImageDraw.Draw(image)

rotationAngle = math.radians(50)

with open('C:\compGraphics\compGraphLab3\DS4.txt', 'r') as file:  # в першому аргументі потрібно змінити шлях, на відповідний шлях до файлу DS4.txt

    for line in file:
        coordinatesTuple = (int(line[0:3]), int(line[4:7]))
        
        i = coordinatesTuple[0] - 480
        j = coordinatesTuple[1] - 480

        x = i * math.cos(rotationAngle) - j * math.sin(rotationAngle)
        y = i * math.sin(rotationAngle) + j * math.cos(rotationAngle)

        draw.line((x + 480, y + 480, x + 485, y + 485), fill = (0,0,255))


image.save("C:\compGraphics\compGraphLab3\\result.png")
        
        

#del draw
#image.save("C:\compGraphics\compGraphLab3\img.png", "PNG")  # в першому аргументі потрібно змінити/поставити шлях, по якому ви хочете зберегти зображення і відповідно назву файлу
        
