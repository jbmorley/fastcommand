#!/bin/bash

export VERSION=$(scripts/changes/changes version)
python -m build
