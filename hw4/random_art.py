# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

from random import randint
import math
import Image

def build_random_function(min_depth, max_depth):
    """
    Builds a function of many random nested functioned composed together as a nested list.
    Returns a list of composed functions represented as strings
    Inputs are min_depth, which is the minimum nested-ness of the function
    and max_depth, which is the maximum nested-ness of the function
    Nest distance will be between min and max. Once the nested-ness passes min_depth,
    there is a 50% chance that it will nest again until it hits max_depth
    
    The possible functions are:
    sin_pi(x) which is sin(pi*x)
    cos_pi(x) which is cos(pi*x)
    prod(x,y) which is x*y
    x(x,y) which is x
    y(x,y) which is y
    sqrt(x) which is the square root of x
    sqr(x) which is x^2
    """

    functions = ["sin_pi","cos_pi","prod","x","y","sqrt","sqr"]
    twof = ["prod","x","y"]
    i = randint(0,len(functions)-1)
    func = functions[i]    
    
    if max_depth > 2:
        if(min_depth>0 or randint(0,1)==1):
            if func in twof:
                return [func,build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
            else:
                return [func,build_random_function(min_depth-1,max_depth-1)]
    
    if func in twof:
        return [func,["x"],["y"]]
    else:
        if randint(0,1)==1:
            return [func,["x"]]
        else:
            return [func,["y"]]
    

    

def evaluate_random_function(f, m, n):
    """
    Takes a function f of nested lists and evaluates it at values x=m and y=n.
    Returns a single value that is the value of the funtion at the (m,n) coordinate
    
    The possible functions are:
    sin_pi(x) which is sin(pi*x)
    cos_pi(x) which is cos(pi*x)
    prod(x,y) which is x*y
    x(x,y) which is x
    y(x,y) which is y
    sqrt(x) which is the square root of x
    sqr(x) which is x^2
    """
   
    def sin_pi(a):
        return math.sin(math.pi * a)
    
    def cos_pi(a):
        return math.cos(math.pi * a)
        
    def prod(a,b):
        return a*b
        
    def x(a,b):
        return a
        
    def y(a,b):
        return b

    def sqrt(a):
        return abs(a)**.5
    
    def sqr(a):
        return a**2
        
    if f[0]=="y" and len(f)==1:
        return n
    elif f[0]=="x" and len(f)==1:
        return m
    else:
        if f[0]=="cos_pi":
            return cos_pi(evaluate_random_function(f[1],m,n))
        if f[0]=="sin_pi":
            return sin_pi(evaluate_random_function(f[1],m,n))
        if f[0]=="prod":
            return prod(evaluate_random_function(f[1],m,n), evaluate_random_function(f[2],m,n))
        if f[0]=="x":
            return x(evaluate_random_function(f[1],m,n), evaluate_random_function(f[2],m,n))
        if f[0]=="y":
            return y(evaluate_random_function(f[1],m,n), evaluate_random_function(f[2],m,n))
        if f[0]=="sqrt":
            return sqrt(evaluate_random_function(f[1],m,n))
        if f[0]=="sqr":
            return sqr(evaluate_random_function(f[1],m,n))


def evaluateMovie(f, m, n, t):
    """
    Includes a t input that represents the frame number, causing the function to shift
    with different t inputs as the movie progresses.  The function edits m and n to
    be a function of t, and then evaluates the functions at the new m and n values, returning
    a single value for the evaluated function
    
    The possible functions are:
    sin_pi(x) which is sin(pi*x)
    cos_pi(x) which is cos(pi*x)
    prod(x,y) which is x*y
    x(x,y) which is x
    y(x,y) which is y
    sqrt(x) which is the square root of x
    sqr(x) which is x^2
    """
    
    tNew = remap_interval(t,0,40,-1,1)
 
    # when you multiply m and n by tNew, the movie zooms in and out on the image
    # when you add tNew to m and n, the image translates across the movie
    m = m*tNew
    n = n*tNew
    
    def sin_pi(a):
        return math.sin(math.pi * a)
    
    def cos_pi(a):
        return (math.cos(math.pi * a))
        
    def prod(a,b):
        return (a*b)
        
    def x(a,b):
        return a
        
    def y(a,b):
        return a
        
    def sqrt(a):
        return abs(a)**.5
    
    def sqr(a):
        return a**2

    if f[0]=="y" and len(f)==1:
        return n
    elif f[0]=="x" and len(f)==1:
        return m
    else:
        if f[0]=="cos_pi":
            return cos_pi(evaluateMovie(f[1],m,n,tNew))
        if f[0]=="sin_pi":
            return sin_pi(evaluateMovie(f[1],m,n,tNew))
        if f[0]=="prod":
            return prod(evaluateMovie(f[1],m,n,tNew), evaluateMovie(f[2],m,n,tNew))
        if f[0]=="x":
            return x(evaluateMovie(f[1],m,n,tNew), evaluateMovie(f[2],m,n,tNew))
        if f[0]=="y":
            return y(evaluateMovie(f[1],m,n,tNew), evaluateMovie(f[2],m,n,tNew))
        if f[0]=="sqrt":
            return sqrt(evaluateMovie(f[1],m,n))
        if f[0]=="sqr":
            return sqr(evaluateMovie(f[1],m,n))



def remap_interval(val,input_start,input_end,output_start,output_end):
    """
    Takes a value val in the interval [input_start, input_end] and remaps it 
    proportionally to the range [output_start, output_end]
    Returns a single value in the desired output range
    """
    rangeIn = input_end - input_start
    rangeOut = output_end - output_start
    adjustVal = float(val-input_start)
    prop = adjustVal/rangeIn
    return prop*rangeOut + output_start
    
def drawImage():
    """
    Draws and saves an Image object made up of three randomly built functions,
    one to represent each part of red, blue, and green.  For each pixel in the image,
    the RGB functions are evaluated at that pixel's [x,y] location.  Then, the outputs
    are remapped to the RGB 255 scale, and the resulting colour is assigned to that pixel
    """
    
    n = 600
    q = 600
    im = Image.new("RGB",(n,q))
    red = build_random_function(5,12)
    green = build_random_function(5,10)
    blue = build_random_function(4,11)
    pixels = im.load() 
    for x in range(0,n-1):
        for y in range (0,q-1):
            inscaleX = remap_interval(x,0,n-1,-1,1)
            inscaleY = remap_interval(y,0,q-1,-1,1)
            redVal = evaluate_random_function(red,inscaleX,inscaleY)
            greenVal = evaluate_random_function(green,inscaleX,inscaleY)
            blueVal = evaluate_random_function(blue,inscaleX,inscaleY)

            redPix= int(remap_interval(redVal,-1,1,1,255))
            greenPix= int(remap_interval(greenVal,-1,1,1,255))
            bluePix= int(remap_interval(blueVal,-1,1,1,255))

            pixels[x,y] = (redPix,greenPix,bluePix)
    im.save('p38.jpg', 'JPEG')
    
def drawForMovie(red,green,blue,t):
    """
    A helper funtion to makeMovie, this is nearly identical to the drawImage function, except it takes a t input
    as well, which is passes into the evaluateMovie function to change the x and y 
    inputs as a function of frame number.  It saves each frame of the movie individually
    with the filename format frame001.jpg, with increasing numbers.
    """
    n = 100
    im = Image.new("RGB",(n,n))
 
    pixxes = im.load() 
    for x in range(0,n-1):
        for y in range (0,n-1):
            inscaleX = remap_interval(x,0,n-1,-1,1)
            inscaleY = remap_interval(y,0,n-1,-1,1)
            redVal = evaluateMovie(red,inscaleX,inscaleY,t)
            greenVal = evaluateMovie(green,inscaleX,inscaleY,t)
            blueVal = evaluateMovie(blue,inscaleX,inscaleY,t)

            redPix= int(remap_interval(redVal,-1,1,1,255))
            greenPix= int(remap_interval(greenVal,-1,1,1,255))
            bluePix= int(remap_interval(blueVal,-1,1,1,255))

            pixxes[x,y] = (redPix,greenPix,bluePix)
    filename = "frame" + "0"*(3-len(str(t))) + str(t) + ".jpg"
    im.save(filename,"JPEG")
    
def makeMovie():
    """
    This builds three functions, then cycles through t, the desired number of
    frames in the movie, calling drawForMovie on each one to create an image for 
    that frame number.
    """
    red = build_random_function(6,10)
    green = build_random_function(7,9)
    blue = build_random_function(8,12)
    for t in range(40):
        drawForMovie(red,green,blue,t)


if __name__ == "__main__":
    #makeMovie()
    drawImage()