#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/medseg_timm-regnetx_002_optical_distortion_log.out
#SBATCH --job-name=medseg_timm-regnetx_002_optical_distortion
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_timm-regnetx_002_optical_distortion_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold0_optical_distortion.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold1_optical_distortion.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold2_optical_distortion.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold3_optical_distortion.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold4_optical_distortion.yml
