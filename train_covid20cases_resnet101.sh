#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_resnet101_log.out
#SBATCH --job-name=covid20cases_resnet101
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_resnet101_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_unet_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_unet_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_unet_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_unet_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_unet_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_fpn_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_linknet_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_pan_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_pan_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_pan_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_pan_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_pan_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_manet_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_manet_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_manet_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_manet_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_manet_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold4.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold0.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold1.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold2.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold3.yml
srun python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold4.yml
