Instalación en entorno docker
=============================

Instalación desde github
------------------------

Asumiendo la imagen oficial de ckan: ``ckan/ckan`` correr: ::

    ckan-pip install git+https://github.com/chrodriguez/ckanext-senasa_theme.git

Probar la instalacion desde una carpeta
---------------------------------------
Correr los siguientes comandos, asumiendo se dispone del directorio con este
repo en /tmp/senasa_theme: ::

    source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/
    cp -r /tmp/senasa_theme .
    cd senasa_theme
    pip install -r requirements.txt
    python setup.py install && python setup.py develop


Configuración de CKAN para usar el tema
----------------------------------------

Luego agregar el plugin en la configuracion de ckan ``/etc/ckan/{ckan,production}.ini`` ::

    ckan.plugins = stats text_view image_view recline_view senasa_theme

Luego reiniciar la imagen del contenedor: `docker-compose restart ckan`
