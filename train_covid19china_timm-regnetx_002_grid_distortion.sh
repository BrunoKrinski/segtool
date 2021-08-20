#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid19china_timm-regnetx_002_grid_distortion_log.out
#SBATCH --job-name=covid19china_timm-regnetx_002_grid_distortion
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid19china_timm-regnetx_002_grid_distortion_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold0_grid_distortion.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold1_grid_distortion.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold2_grid_distortion.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold3_grid_distortion.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold4_grid_distortion.yml
