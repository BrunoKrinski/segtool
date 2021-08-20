#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_timm-regnetx_002_Random_brightness_contrast_log.out
#SBATCH --job-name=covid20cases_timm-regnetx_002_Random_brightness_contrast
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_timm-regnetx_002_Random_brightness_contrast_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_Random_brightness_contrast.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_Random_brightness_contrast.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_Random_brightness_contrast.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_Random_brightness_contrast.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_Random_brightness_contrast.yml
