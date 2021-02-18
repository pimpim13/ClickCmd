#!/usr/bin/env python3

import os
from glob import glob
import zipfile
import click
import logging
import shutil


@click.command()
@click.argument('origine', default=".")
@click.argument('destination', default="./extraction")
def extract_zip(origine=".", destination="./extraction"):

    if not os.path.isdir(origine) and not origine.endswith(".zip"):
        return False
    elif os.path.isdir(origine) and not origine.endswith('/'):
        origine += '/'
    if os.path.isdir(origine):
        origine = f"{origine}**/*.zip"
        lst = glob(origine, recursive=True)
    else:
        lst = [origine]

    if not os.path.isdir(destination):
        os.makedirs(destination)

    for item in lst:
        zfile = zipfile.ZipFile(item)
        zfile.extractall(path=destination)


@click.command()
@click.argument('origine', default='.', type=click.Path(exists=True))
@click.argument('destination', default='.')
@click.option('--copycontent', '-c', is_flag=True, help='les fichiers sont copiés dans le dossier de destination')
@click.option('--reste', '-r', help="dossier par defaut pour les fichiers dont le type n'est pas à trier")
@click.option('--ext', '-e', multiple=True, help='spécifie les types de fichiers à trier')
@click.option('--all', '-a', is_flag=True, help='Traite toutes les extensions - incompatible avec --ext')
def infolder(origine=".", destination=".", copycontent=False, reste='Autres', ext=("jpg",), all=False):
    """ Cette fonction separe dans des dossiers les fichiers dont l'extension est passée option -e
    Elle prend en parametre le dossier qui doit etre traité et le dossier de destination
    dans lequel les dossiers separés seront créés
    Si aucun paramètre n'est passé c'est le dossier courant qui sera pris en compte"""

    extensions = [item.upper() for item in ext]
    if destination == ".":
        destination = origine

    images = glob(f"{origine}/*.*")
    for i in images:
        root, ext = os.path.splitext(os.path.basename(i))
        type_ = ext[1:].upper()

        if not all and type_ not in extensions:
            type_ = reste or None

        if type_:
            destin = os.path.join(destination, type_.upper())

            if not os.path.exists(destin):
                os.makedirs(destin)
                click.echo(f"le dossier {destin} vient d'être créé")
            if copycontent:
                shutil.copy(i, destin)
            else:
                shutil.move(i, destin)


if __name__ == '__main__':
    de = "/Users/alainzypinoglou/Documents/CFDT/tracts/tract"
    vers = "/Users/alainzypinoglou/Documents/CFDT/Extraction"
    extract_zip(origine=de, destination=vers)
