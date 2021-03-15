#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_resnext50_32x4d_log.out
#SBATCH --job-name=covid20cases_resnext50_32x4d
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_resnext50_32x4d_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid20cases_unetplusplus_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_unet_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_unet_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_unet_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_unet_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_unet_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_pan_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_pan_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_pan_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_pan_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_pan_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_manet_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_manet_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_manet_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_manet_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_manet_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnext50_32x4d_fold4.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnext50_32x4d_fold0.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnext50_32x4d_fold1.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnext50_32x4d_fold2.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnext50_32x4d_fold3.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnext50_32x4d_fold4.yml
