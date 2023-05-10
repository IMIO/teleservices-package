#!/bin/sh

set -e # Exit immediately if a command exits with a non-zero status.

# installation path
install_path="/usr/lib/teleservices_package"

echo "--- Install passerelle settings"
if [ ! -f "/etc/passerelle/settings.d/casier_judiciaire.py" ]
then
  cp $install_path/passerelle/casier_judiciaire.py /etc/passerelle/settings.d/
  service passerelle restart
fi

sudo -u hobo hobo-manage imio_indus_deploy --directory $install_path
