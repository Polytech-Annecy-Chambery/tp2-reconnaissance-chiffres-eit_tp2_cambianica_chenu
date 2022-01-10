from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im=Image.binarisation(image,S)
    im=Image.localisation(im)
    chiffre=0
    s=0
    for l in range (len(liste_modeles)):
        im=Image.resized(im,liste_modeles[l].H, liste_modeles[l].W)
        if Image.similitude(im,liste_modeles[l])>s:
            s=Image.similitude(im,liste_modeles[l])
            chiffre=l
    return chiffre
    
