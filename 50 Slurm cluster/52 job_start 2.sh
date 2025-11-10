#!/bin/bash

# Name of the job
#SBATCH --job-name=Tkldrive

# These commands choose how much ressources are allocated
#SBATCH --nodes=1    # number of nodes 
#SBATCH --ntasks=1   # number of tasks
#SBATCH --mem-per-cpu=16384   # MB of RAM allocated by cores (ntasks)
#SBATCH --partition=wcpu # partition where to run the program

# where to output the slurm file
cd /swdata/poindron/SIMU/250318/REIN_ad_003

# the command that the job should execute
# execute DDDAO_3.py with python3
python3 -u DDDAO_3.py > output.txt 2> error.txt

# > output.txt is to output the main prints in the file output.txt file
# 2> error.txt is to output the error message in the error.txt file