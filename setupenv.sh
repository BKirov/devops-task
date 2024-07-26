
#!/bin/bash

VENV_DIR="myenv"
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate
pip install --upgrade pip
pip install boto3
echo "Virtual environment setup complete and boto3 installed."
source $VENV_DIR/bin/activate
