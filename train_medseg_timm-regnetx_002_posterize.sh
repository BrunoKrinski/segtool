#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/medseg_timm-regnetx_002_posterize_log.out
#SBATCH --job-name=medseg_timm-regnetx_002_posterize
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_timm-regnetx_002_posterize_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold0_posterize.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold1_posterize.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold2_posterize.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold3_posterize.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold4_posterize.yml
