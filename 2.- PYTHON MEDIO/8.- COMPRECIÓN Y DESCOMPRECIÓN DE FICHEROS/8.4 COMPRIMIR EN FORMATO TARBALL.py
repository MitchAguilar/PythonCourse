import tarfile

archivo_tar=tarfile.open('8.4 archivo.tar.gz','w:gz')
archivo_tar.add('archivo.xml')
archivo_tar.close()
