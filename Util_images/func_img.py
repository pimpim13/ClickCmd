from PIL import Image
from glob import glob
import os
import click
from pathlib import Path


@click.command()
@click.argument('path', default='.', type=click.Path(exists=True))
@click.argument('destination_path', default='.')
@click.option('--size', '-s', 'size', help="Tailles des images", multiple=True, required=True)
def multisize(path=".", destination_path=".", size=(4,)):

    """ redimensionne les images du dossier path passé en parametre
     suivant les coefficients passés aussi en parametres (size)
     Et stocke le resultat dans le dossier destination_path"""
    print(size)

    dossier = glob(f"{path}/*.*")
    chemin = os.path.join(path, destination_path)
    if not os.path.isdir(chemin):
        os.makedirs(chemin)

    for image in dossier:
        im = Image.open(image)
        fichier = os.path.basename(image)
        nom_fichier, extension = os.path.splitext(fichier)
        for facteur in size:
            x, y = im.size
            x_facteur, y_facteur = round(x / float(facteur)), round(y / float(facteur))
            im_resize = im.resize((x_facteur, y_facteur))
            new_filename = f"{chemin}/{nom_fichier}-{x_facteur}x{y_facteur}{extension}"
            im_resize.save(new_filename)
    return

@click.command()
# @click.option('--dest','-d', help='chemin relatif du dossier de destination', default = '.')
@click.argument('origine', default='.', type=click.Path(exists=True))
@click.argument('size', nargs=-1)
def multipixel(origine, size, dest="."):
# def multipixel(origine='.', size=(1024,) ,dest='.'):
    """ redimensionne les images du dossier path passé en parametre
         suivant les tailles en pixel passées aussi en paramètres
         Et stocke le résultat dans le dossier d'origine des images"""
    print(dest)


    types = ["jpg", "JPG", "png", "PNG"]
    images = []
    for type_ in types:
        path = f"{origine}**/*.{type_}"
        images.extend(glob(path, recursive=True))

    for image in images:
        im = Image.open(image)
        name, ext = os.path.splitext(image)
        reduc = im.height / im.width


        for taille in size:
            taille = int(taille)
            if im.width >= im.height:
                (width, height) = (taille, int(taille * reduc))
            else:
                (width, height) = (int(taille / reduc), taille)


            im_2 = im.resize((width, height))
            im_2.save(f"{name}_{taille}{ext}")

if __name__ == '__main__':
   pass
