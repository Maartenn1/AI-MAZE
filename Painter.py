from PIL import Image
import os
import numpy as np
import imageio



path = os.path.abspath(__file__)   # De directory wordt ingesteld op de pathatie
dname = os.path.dirname(path)      # van het programma, zodat het programma op
os.chdir(dname)                    # elke computer werkt.


color = [(169, 169, 169), (255, 255, 255), (0, 255, 0), (255, 0, 0),
         (0, 0, 255)]  #RGB colors of the maze


def paint(maze, mx, my, imgx, imgy, image, pixels, name):
    # paint the maze
    for ky in range(imgy):
        for kx in range(imgx):
            pixels[kx, ky] = color[
                maze[int(my * ky / imgy)][int(mx * kx / imgx)]]
    image.save(name, "PNG")

def once(maze):
    maze = maze
    mx = len(maze[0])
    my = len(maze)
    imgx = 100;
    imgy = 100
    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()
    number = int(np.loadtxt('Mazes\\Number.txt'))
    nf = open('Mazes\\Number.txt', "w+")
    nf.write(str(number+1))
    nf.close()
    name = "Mazes\Maze_" + str(mx) + "x" + str(my) +".#"+ str(number) + ".png"
    paint(maze, mx, my, imgx, imgy, image, pixels, name)
    img = Image.open(name)
    img.show()

def gif(maze, path):
    mx = len(maze[0])
    my = len(maze)
    imgx = mx*3
    imgy = my*3
    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()
    for i in range(len(path)):
        if i < 10:
            name = "Gifs\\Temp\Maze_" + str(mx) + "x" + str(my) + ".#" +\
                   "00" + str(i) + ".png"
        elif i < 100:
            name = "Gifs\\Temp\Maze_" + str(mx) + "x" + str(my) + ".#" +\
                   "0" + str(i) + ".png"
        else:
            name = "Gifs\\Temp\Maze_" + str(mx) + "x" + str(my) + ".#" + \
                    str(i) + ".png"
        mazet = np.copy(maze)
        mazet[path[i][0]][path[i][1]] = 4
        paint(mazet, mx, my, imgx, imgy, image, pixels, name)
    png_dir = ".\Gifs\Temp\\"
    images = []
    number = int(np.loadtxt('Gifs\\Number.txt'))
    nf = open('Gifs\\Number.txt', "w+")
    nf.write(str(number + 1))
    nf.close()
    name = '.\Gifs\Hiero\Gif#' + str(number) + '.gif'
    for subdir, dirs, files in os.walk(png_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith(".png"):
                images.append(imageio.imread(file_path))
    imageio.mimsave(name, images)
    dirPath = "Gifs//Temp"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath + "/" + fileName)