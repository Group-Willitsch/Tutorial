#!/bin/bash

# Name of the job
#SBATCH --job-name=NewDesign

# These commands choose how much ressources are allocated
#SBATCH --nodes=1    # number of nodes 
#SBATCH --ntasks=1   # number of cores
#SBATCH --cpus-per-task=48  # number of cores
#SBATCH --mem-per-cpu=2625  # MB of RAM allocated by cores (ntasks)
#SBATCH --partition=wcpu    # partition where to run the program

# activate conda env for python
. "/swdata/poindron/miniconda3/etc/profile.d/conda.sh"
conda activate py313
export DISPLAY="" # needed to avoid Java license error...

cd /swdata/poindron/COMSOL/250321

python3 -u job_comsol.py > output.txt 2> error.txt