#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_timm-regnetx_002_shift_scale_rotate_log.out
#SBATCH --job-name=covid20cases_timm-regnetx_002_shift_scale_rotate
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_timm-regnetx_002_shift_scale_rotate_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_shift_scale_rotate.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_shift_scale_rotate.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_shift_scale_rotate.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_shift_scale_rotate.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_shift_scale_rotate.yml
