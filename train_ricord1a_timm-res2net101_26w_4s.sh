#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/ricord1a_timm-res2net101_26w_4s_log.out
#SBATCH --job-name=ricord1a_timm-res2net101_26w_4s
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/ricord1a_timm-res2net101_26w_4s_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_ricord1a_unetplusplus_timm-res2net101_26w_4s_fold0.yml
srun python main.py --configs configs/train_ricord1a_unetplusplus_timm-res2net101_26w_4s_fold1.yml
srun python main.py --configs configs/train_ricord1a_unetplusplus_timm-res2net101_26w_4s_fold2.yml
srun python main.py --configs configs/train_ricord1a_unetplusplus_timm-res2net101_26w_4s_fold3.yml
srun python main.py --configs configs/train_ricord1a_unetplusplus_timm-res2net101_26w_4s_fold4.yml
srun python main.py --configs configs/train_ricord1a_unet_timm-res2net101_26w_4s_fold0.yml
srun python main.py --configs configs/train_ricord1a_unet_timm-res2net101_26w_4s_fold1.yml
srun python main.py --configs configs/train_ricord1a_unet_timm-res2net101_26w_4s_fold2.yml
srun python main.py --configs configs/train_ricord1a_unet_timm-res2net101_26w_4s_fold3.yml
srun python main.py --configs configs/train_ricord1a_unet_timm-res2net101_26w_4s_fold4.yml
srun python main.py --configs configs/train_ricord1a_fpn_timm-res2net101_26w_4s_fold0.yml
srun python main.py --configs configs/train_ricord1a_fpn_timm-res2net101_26w_4s_fold1.yml
srun python main.py --configs configs/train_ricord1a_fpn_timm-res2net101_26w_4s_fold2.yml
srun python main.py --configs configs/train_ricord1a_fpn_timm-res2net101_26w_4s_fold3.yml
srun python main.py --configs configs/train_ricord1a_fpn_timm-res2net101_26w_4s_fold4.yml
srun python main.py --configs configs/train_ricord1a_pspnet_timm-res2net101_26w_4s_fold0.yml
srun python main.py --configs configs/train_ricord1a_pspnet_timm-res2net101_26w_4s_fold1.yml
srun python main.py --configs configs/train_ricord1a_pspnet_timm-res2net101_26w_4s_fold2.yml
srun python main.py --configs configs/train_ricord1a_pspnet_timm-res2net101_26w_4s_fold3.yml
srun python main.py --configs configs/train_ricord1a_pspnet_timm-res2net101_26w_4s_fold4.yml
srun python main.py --configs configs/train_ricord1a_linknet_timm-res2net101_26w_4s_fold0.yml
srun python main.py --configs configs/train_ricord1a_linknet_timm-res2net101_26w_4s_fold1.yml
srun python main.py --configs configs/train_ricord1a_linknet_timm-res2net101_26w_4s_fold2.yml
srun python main.py --configs configs/train_ricord1a_linknet_timm-res2net101_26w_4s_fold3.yml
srun python main.py --configs configs/train_ricord1a_linknet_timm-res2net101_26w_4s_fold4.yml
srun python main.py --configs configs/train_ricord1a_manet_timm-res2net101_26w_4s_fold0.yml
srun python main.py --configs configs/train_ricord1a_manet_timm-res2net101_26w_4s_fold1.yml
srun python main.py --configs configs/train_ricord1a_manet_timm-res2net101_26w_4s_fold2.yml
srun python main.py --configs configs/train_ricord1a_manet_timm-res2net101_26w_4s_fold3.yml
srun python main.py --configs configs/train_ricord1a_manet_timm-res2net101_26w_4s_fold4.yml
