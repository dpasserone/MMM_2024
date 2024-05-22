#!/bin/bash -l
#
#
#SBATCH --job-name="static_met"
#SBATCH --time=01:00:00
#SBATCH --nodes=4
#SBATCH --partition=normal
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --constraint=gpu
#========================================
# load modules and run simulation

module load daint-gpu
module load CP2K
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
export CRAY_CUDA_MPS=1
ulimit -s unlimited

srun cp2k.psmp -i vibmet.inp -o vibmet.out
