#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_timm-res2net50_26w_4s_log.out
#SBATCH --job-name=mosmed_timm-res2net50_26w_4s
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_timm-res2net50_26w_4s_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_mosmed_unetplusplus_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_unet_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_unet_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_unet_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_unet_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_unet_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_fpn_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_fpn_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_fpn_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_fpn_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_fpn_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_pspnet_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_pspnet_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_pspnet_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_pspnet_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_pspnet_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_linknet_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_linknet_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_linknet_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_linknet_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_linknet_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_pan_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_pan_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_pan_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_pan_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_pan_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_manet_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_manet_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_manet_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_manet_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_manet_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_deeplabv3_timm-res2net50_26w_4s_fold4.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_timm-res2net50_26w_4s_fold0.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_timm-res2net50_26w_4s_fold1.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_timm-res2net50_26w_4s_fold2.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_timm-res2net50_26w_4s_fold3.yml
srun python main.py --configs configs/train_mosmed_deeplabv3plus_timm-res2net50_26w_4s_fold4.yml
