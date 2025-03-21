#!/bin/bash

#SBATCH --job-name=Tkldrive
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=16384
#SBATCH --partition=wcpu

# in case the job crashes we know where it was
cd /swdata/poindron/SIMU/250318/REIN_ad_003

# a  d
# t n d

python3 -u DDDAO_3.py > output.txt 2> error.txt