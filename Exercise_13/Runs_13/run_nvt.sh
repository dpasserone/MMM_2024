#!/bin/bash -l
#
# CP2K on Piz Daint: 64 nodes, 1 MPI task per node, 12 OpenMP threads per task
#
#SBATCH --job-name=md
#SBATCH --time=01:30:00
#SBATCH --nodes=1
#SBATCH --partition=normal
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --constraint=gpu
#SBATCH --account=crs01
#========================================
# load modules and run simulation
module load daint-gpu
module load CP2K
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
ulimit -s unlimited
INP=gr2hno3_nvt
export CRAY_CUDA_MPS=1
srun  cp2k.psmp -i $INP.inp -o $INP.out
