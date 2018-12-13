#!/bin/bash

BIN_DIR=$(dirname $(readlink -f "$0"))
export PROJECT_DIR=$(dirname "$BIN_DIR")
