#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_vgg16_log.out
#SBATCH --job-name=mosmed_vgg16
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_vgg16_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_mosmed_unetplusplus_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_unet_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_unet_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_unet_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_unet_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_unet_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_fpn_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_fpn_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_fpn_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_fpn_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_fpn_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_pspnet_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_pspnet_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_pspnet_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_pspnet_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_pspnet_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_linknet_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_linknet_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_linknet_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_linknet_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_linknet_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_pan_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_pan_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_pan_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_pan_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_pan_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_manet_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_manet_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_manet_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_manet_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_manet_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_vgg16_fold4.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_vgg16_fold0.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_vgg16_fold1.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_vgg16_fold2.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_vgg16_fold3.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_vgg16_fold4.yml
