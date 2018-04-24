#!/bin/bash

# Environments
SPARK_PACKAGES=com.databricks:spark-avro_2.10:2.0.1,com.databricks:spark-csv_2.10:1.4.0
ANACONDA_VERSION=3-5.0.1
JUPYTER_LOG=/home/hadoop/.jupyter/jupyter.log
JUPYTER_PORT="8080"
JUPYTER_NOTEBOOK_DIR="/opt/local/jupyter/"


##Configure Jupyter
jupyter notebook --generate-config

JUPYTER_NOTEBOOK_CONFIG=/home/hadoop/.jupyter/jupyter_notebook_config.py
sed -i -e "3a c.NotebookApp.ip = '*'" $JUPYTER_NOTEBOOK_CONFIG
sed -i -e "3a c.NotebookApp.open_browser = False" $JUPYTER_NOTEBOOK_CONFIG
sed -i -e "3a c.NotebookApp.port = ${JUPYTER_PORT}" $JUPYTER_NOTEBOOK_CONFIG
sed -i -e "3a c.NotebookApp.notebook_dir = '${JUPYTER_NOTEBOOK_DIR}'" $JUPYTER_NOTEBOOK_CONFIG
sed -i -e "3a c = get_config()" $JUPYTER_NOTEBOOK_CONFIG


IPYTHON_KERNEL_CONFIG=/home/hadoop/.ipython/profile_default/ipython_kernel_config.py
ipython profile create
sed -i -e "3a c.InteractiveShellApp.matplotlib = 'inline'" $IPYTHON_KERNEL_CONFIG


##Launch Jupyter by executing "pyspark"
JUPYTER_PYSPARK_BIN=/home/hadoop/.jupyter/start-jupyter-pyspark.sh

cat << EOF > $JUPYTER_PYSPARK_BIN
export SPARK_HOME=/usr/lib/spark/
export PYSPARK_PYTHON=$PYENV/versions/anaconda$ANACONDA_VERSION/bin/python
export PYSPARK_DRIVER_PYTHON=ipython
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
export SPARK_PACKAGES=$SPARK_PACKAGES
nohup pyspark --packages $SPARK_PACKAGES > $JUPYTER_LOG 2>&1 &
EOF

chmod +x $JUPYTER_PYSPARK_BIN

