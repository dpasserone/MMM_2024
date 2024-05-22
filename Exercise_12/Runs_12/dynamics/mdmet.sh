#!/bin/bash -l
#
# CP2K on Piz Daint: 64 nodes, 1 MPI task per node, 12 OpenMP threads per task
#
#SBATCH --job-name=mdmet
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --partition=normal
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=12
#SBATCH --constraint=gpu
#========================================
# load modules and run simulation
module load daint-gpu
module load CP2K
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
ulimit -s unlimited
srun -n $SLURM_NTASKS --ntasks-per-node=$SLURM_NTASKS_PER_NODE -c $SLURM_CPUS_PER_TASK cp2k.psmp -i mdmet.inp -o mdmet.out
