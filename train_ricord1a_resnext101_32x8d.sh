#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/ricord1a_resnext101_32x8d_log.out
#SBATCH --job-name=ricord1a_resnext101_32x8d
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/ricord1a_resnext101_32x8d_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold3.yml
srun python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold4.yml
srun python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold0.yml
srun python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold1.yml
srun python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold2.yml
srun python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold3.yml
srun python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold4.yml