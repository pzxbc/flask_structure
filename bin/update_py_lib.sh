#!/bin/bash

CUR_FILE_DIR=$(cd "$(dirname "$0")"; pwd)

# 引入环境变量
source "$CUR_FILE_DIR/common_env.sh"

cd "$PROJECT_DIR"
source .env/bin/activate
pip freeze >pylib_requirements.txt

# install requirements
# pip install -r pylib_requirements.txt

