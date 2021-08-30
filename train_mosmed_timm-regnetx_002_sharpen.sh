#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_timm-regnetx_002_sharpen_log.out
#SBATCH --job-name=mosmed_timm-regnetx_002_sharpen
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_timm-regnetx_002_sharpen_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold0_sharpen.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold1_sharpen.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold2_sharpen.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold3_sharpen.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold4_sharpen.yml
