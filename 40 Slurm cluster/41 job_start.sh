#!/bin/bash

#SBATCH --job-name=NewDesign
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --mem-per-cpu=2625
#SBATCH --partition=wcpu

# activate conda env for python
. "/swdata/poindron/miniconda3/etc/profile.d/conda.sh"
conda activate py313
export DISPLAY="" # needed to avoid Java license error...

cd /swdata/poindron/COMSOL/250321

python3 -u job_comsol.py > output.txt 2> error.txt