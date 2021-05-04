#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/medseg_timm-regnetx_004_log.out
#SBATCH --job-name=medseg_timm-regnetx_004
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_timm-regnetx_004_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_004_fold0.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_004_fold1.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_004_fold2.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_004_fold3.yml
srun python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_004_fold4.yml
srun python main.py --configs configs/train_medseg_unet_timm-regnetx_004_fold0.yml
srun python main.py --configs configs/train_medseg_unet_timm-regnetx_004_fold1.yml
srun python main.py --configs configs/train_medseg_unet_timm-regnetx_004_fold2.yml
srun python main.py --configs configs/train_medseg_unet_timm-regnetx_004_fold3.yml
srun python main.py --configs configs/train_medseg_unet_timm-regnetx_004_fold4.yml
srun python main.py --configs configs/train_medseg_fpn_timm-regnetx_004_fold0.yml
srun python main.py --configs configs/train_medseg_fpn_timm-regnetx_004_fold1.yml
srun python main.py --configs configs/train_medseg_fpn_timm-regnetx_004_fold2.yml
srun python main.py --configs configs/train_medseg_fpn_timm-regnetx_004_fold3.yml
srun python main.py --configs configs/train_medseg_fpn_timm-regnetx_004_fold4.yml
srun python main.py --configs configs/train_medseg_pspnet_timm-regnetx_004_fold0.yml
srun python main.py --configs configs/train_medseg_pspnet_timm-regnetx_004_fold1.yml
srun python main.py --configs configs/train_medseg_pspnet_timm-regnetx_004_fold2.yml
srun python main.py --configs configs/train_medseg_pspnet_timm-regnetx_004_fold3.yml
srun python main.py --configs configs/train_medseg_pspnet_timm-regnetx_004_fold4.yml
srun python main.py --configs configs/train_medseg_linknet_timm-regnetx_004_fold0.yml
srun python main.py --configs configs/train_medseg_linknet_timm-regnetx_004_fold1.yml
srun python main.py --configs configs/train_medseg_linknet_timm-regnetx_004_fold2.yml
srun python main.py --configs configs/train_medseg_linknet_timm-regnetx_004_fold3.yml
srun python main.py --configs configs/train_medseg_linknet_timm-regnetx_004_fold4.yml
srun python main.py --configs configs/train_medseg_manet_timm-regnetx_004_fold0.yml
srun python main.py --configs configs/train_medseg_manet_timm-regnetx_004_fold1.yml
srun python main.py --configs configs/train_medseg_manet_timm-regnetx_004_fold2.yml
srun python main.py --configs configs/train_medseg_manet_timm-regnetx_004_fold3.yml
srun python main.py --configs configs/train_medseg_manet_timm-regnetx_004_fold4.yml
