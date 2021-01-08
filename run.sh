#!/bin/sh
#SBATCH -t 1-00:00:00
#SBATCH --cpus-per-task=1
#SBATCH -o /home/bakrinski/segtool/log.out
#SBATCH --job-name=segtool_train
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 1d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/error.out
#SBATCH --mem=20G

module load libraries/cuda/10.1

srun python main.py --configs configs/resnet50_unet_cihp_fold0.yml
#srun python main.py
