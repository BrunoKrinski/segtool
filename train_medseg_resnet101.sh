#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/logs/medseg_resnet101_log.out
#SBATCH --job-name=medseg_resnet101
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_resnet101_error.out

export CUDA_VISIBLE_DEVICES=1
export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_medseg_unet_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_unet_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_unet_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_unet_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_unet_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_fpn_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_fpn_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_fpn_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_fpn_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_fpn_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_pspnet_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_pspnet_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_pspnet_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_pspnet_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_pspnet_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_linknet_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_linknet_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_linknet_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_linknet_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_linknet_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_pan_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_pan_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_pan_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_pan_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_pan_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_manet_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_manet_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_manet_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_manet_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_manet_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold4.yml
srun python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold0.yml
srun python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold1.yml
srun python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold2.yml
srun python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold3.yml
srun python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold4.yml
