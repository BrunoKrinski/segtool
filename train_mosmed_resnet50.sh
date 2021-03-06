#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_resnet50_log.out
#SBATCH --job-name=mosmed_resnet50
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_resnet50_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_mosmed_unetplusplus_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_unet_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_unet_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_unet_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_unet_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_unet_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_fpn_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_fpn_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_fpn_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_fpn_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_fpn_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_pspnet_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_pspnet_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_pspnet_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_pspnet_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_pspnet_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_linknet_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_linknet_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_linknet_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_linknet_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_linknet_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_pan_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_pan_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_pan_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_pan_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_pan_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_manet_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_manet_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_manet_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_manet_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_manet_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_resnet50_fold4.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_resnet50_fold0.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_resnet50_fold1.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_resnet50_fold2.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_resnet50_fold3.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_resnet50_fold4.yml
