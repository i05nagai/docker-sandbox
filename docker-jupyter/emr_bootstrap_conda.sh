#!/bin/bash

ANACONDA_VERSION=3-5.0.1
JUPYTER_NOTEBOOK_DIR="/opt/local/jupyter"

# yum packages:
sudo yum install -y htop tmux

# download and install anaconda:
wget -q https://repo.continuum.io/archive/Anaconda${ANACONDA_VERSION}-Linux-x86_64.sh -O ~/anaconda3.sh
/bin/bash ~/anaconda3.sh -b -p $HOME/anaconda
echo -e '\nexport SPARK_HOME=/usr/lib/spark\nexport PATH=$HOME/anaconda/bin:$PATH' >> ~/.bashrc && source ~/.bashrc

# cleanup:
rm ~/anaconda3.sh

# Install addtional python libraries
conda install --yes seaborn

# enable https://github.com/mozilla/jupyter-spark:
sudo mkdir -p ${JUPYTER_NOTEBOOK_DIR}
sudo chmod -R 777 ${JUPYTER_NOTEBOOK_DIR}
pip install jupyter-spark
jupyter serverextension enable --py jupyter_spark
jupyter nbextension install --py jupyter_spark
jupyter nbextension enable --py jupyter_spark
jupyter nbextension enable --py widgetsnbextension

