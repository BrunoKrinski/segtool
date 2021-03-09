#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid19china_resnet50_log.out
#SBATCH --job-name=covid19china_resnet50
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/logs/covid19china_resnet50_error.out

export CUDA_VISIBLE_DEVICES=1
export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid19china_unet_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_unet_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_unet_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_unet_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_unet_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_fpn_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_fpn_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_fpn_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_fpn_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_fpn_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_pspnet_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_pspnet_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_pspnet_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_pspnet_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_pspnet_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_linknet_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_linknet_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_linknet_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_linknet_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_linknet_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_pan_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_pan_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_pan_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_pan_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_pan_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_manet_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_manet_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_manet_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_manet_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_manet_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_deeplabv3_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_deeplabv3_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_deeplabv3_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_deeplabv3_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_deeplabv3_resnet50_fold4.yml
srun python main.py --configs configs/train_covid19china_deeplabv3plus_resnet50_fold0.yml
srun python main.py --configs configs/train_covid19china_deeplabv3plus_resnet50_fold1.yml
srun python main.py --configs configs/train_covid19china_deeplabv3plus_resnet50_fold2.yml
srun python main.py --configs configs/train_covid19china_deeplabv3plus_resnet50_fold3.yml
srun python main.py --configs configs/train_covid19china_deeplabv3plus_resnet50_fold4.yml
