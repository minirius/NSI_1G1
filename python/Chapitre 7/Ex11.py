# coding: utf-8

from PIL import Image

def negatif(image):
    """
    fonction qui prend en paramètre une image
    et retourne l'image en négatif
    Utilise les images importées via le module PIL
    """
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    
    for i in range(ligne):
        for j in range(colonne):
            pixel = image.getpixel((j,i)) # récupération du pixel
            
            r=255-pixel[0]
            v=255-pixel[1]
            b=255-pixel[2]
            
            p = (r,v,b)
            # composition de la nouvelle image
            imgtransformee.putpixel((j,i), p)
    print(pixel,type(pixel))
    return(imgtransformee)

def gris(image):
    """
    fonction qui prend en paramètre une image
    et retourne l'image en niveaux de gris
    Utilise les images importées via le module PIL
    """
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    
    for i in range(ligne):
        for j in range(colonne):
            r, v, b = image.getpixel((j,i)) # récupération du pixel
            g = int((r+v+b)/3)
            p = (g, g, g)
            # composition de la nouvelle image
            imgtransformee.putpixel((j,i), p)
    return(imgtransformee)

def equations(x):
    return int(-(2/65025)*x**3 + (1/85)*x**2)

def ameliorer(image):
    """
    fonction qui prend en paramètre une image
    et retourne l'image en niveaux de gris
    Utilise les images importées via le module PIL
    """
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    
    for i in range(ligne):
        for j in range(colonne):
            r, v, b = image.getpixel((j,i)) # récupération du pixel
            r = equations(r)
            v = equations(v)
            b = equations(b)
            

            p = (r, v, b)
            # composition de la nouvelle image
            imgtransformee.putpixel((j,i), p)
    return(imgtransformee)

def mirroir_v(image):
    """
    fonction qui prend en paramètre une image
    et retourne l'image en niveaux de gris
    Utilise les images importées via le module PIL
    """
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    
    for i in range(ligne):
        for j in range(colonne):
            r, v, b = image.getpixel((j,i)) # récupération du pixel
            # composition de la nouvelle image
            if(colonne%10): r, v, b = 255
            imgtransformee.putpixel((colonne - j - 1,i), (r, v, b))
    return(imgtransformee)

def mirroir_h(image):
    """
    fonction qui prend en paramètre une image
    et retourne l'image en niveaux de gris
    Utilise les images importées via le module PIL
    """
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    
    for i in range(ligne):
        for j in range(colonne):
            r, v, b = image.getpixel((j,i)) # récupération du pixel
            # composition de la nouvelle image
            imgtransformee.putpixel((j, ligne-1-i), (r, v, b))
    return(imgtransformee)

def filtre_chelou(image):
    """
    fonction qui prend en paramètre une image
    et retourne l'image en niveaux de gris
    Utilise les images importées via le module PIL
    """
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    
    for i in range(ligne):
        for j in range(colonne):
            r, v, b = image.getpixel((j,i)) # récupération du pixel
            # composition de la nouvelle image
            if(r>130): r = 255
            if(v>130): v = 255
            if(b>130): b = 255
            imgtransformee.putpixel((j,i), (r, v, b))
    return(imgtransformee)

def teinte(image):
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size) 
    for i in range(ligne):
        for j in range(colonne):
            color = list(image.getpixel((j,i))) # récupération du pixel
            color.sort()
            b, v, r = color
            # composition de la nouvelle image
            
            imgtransformee.putpixel((j,i), (r, v, b))
    return(imgtransformee)

# ouverture du fichier image
ImageFile = './python/Chapitre 7/escargot.png'

img = Image.open(ImageFile)

# affichage des caractéristiques de l'image
print (img.format,img.size, img.mode)

ameliorer(img).show()
