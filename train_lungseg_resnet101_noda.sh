#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/lungseg_resnet101_noda_log.out
#SBATCH --job-name=lungseg_resnet101_noda
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/lungseg_resnet101_noda_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_lungseg_unetplusplus_resnet101_fold0_noda.yml
srun python main.py --configs configs/train_lungseg_unetplusplus_resnet101_fold1_noda.yml
srun python main.py --configs configs/train_lungseg_unetplusplus_resnet101_fold2_noda.yml
srun python main.py --configs configs/train_lungseg_unetplusplus_resnet101_fold3_noda.yml
srun python main.py --configs configs/train_lungseg_unetplusplus_resnet101_fold4_noda.yml
