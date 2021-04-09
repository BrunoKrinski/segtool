#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_densenet121_log.out
#SBATCH --job-name=mosmed_densenet121
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_densenet121_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_mosmed_unetplusplus_densenet121_fold0.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_densenet121_fold1.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_densenet121_fold2.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_densenet121_fold3.yml
srun python main.py --configs configs/train_mosmed_unetplusplus_densenet121_fold4.yml
srun python main.py --configs configs/train_mosmed_unet_densenet121_fold0.yml
srun python main.py --configs configs/train_mosmed_unet_densenet121_fold1.yml
srun python main.py --configs configs/train_mosmed_unet_densenet121_fold2.yml
srun python main.py --configs configs/train_mosmed_unet_densenet121_fold3.yml
srun python main.py --configs configs/train_mosmed_unet_densenet121_fold4.yml
srun python main.py --configs configs/train_mosmed_fpn_densenet121_fold0.yml
srun python main.py --configs configs/train_mosmed_fpn_densenet121_fold1.yml
srun python main.py --configs configs/train_mosmed_fpn_densenet121_fold2.yml
srun python main.py --configs configs/train_mosmed_fpn_densenet121_fold3.yml
srun python main.py --configs configs/train_mosmed_fpn_densenet121_fold4.yml
srun python main.py --configs configs/train_mosmed_pspnet_densenet121_fold0.yml
srun python main.py --configs configs/train_mosmed_pspnet_densenet121_fold1.yml
srun python main.py --configs configs/train_mosmed_pspnet_densenet121_fold2.yml
srun python main.py --configs configs/train_mosmed_pspnet_densenet121_fold3.yml
srun python main.py --configs configs/train_mosmed_pspnet_densenet121_fold4.yml
srun python main.py --configs configs/train_mosmed_linknet_densenet121_fold0.yml
srun python main.py --configs configs/train_mosmed_linknet_densenet121_fold1.yml
srun python main.py --configs configs/train_mosmed_linknet_densenet121_fold2.yml
srun python main.py --configs configs/train_mosmed_linknet_densenet121_fold3.yml
srun python main.py --configs configs/train_mosmed_linknet_densenet121_fold4.yml
srun python main.py --configs configs/train_mosmed_manet_densenet121_fold0.yml
srun python main.py --configs configs/train_mosmed_manet_densenet121_fold1.yml
srun python main.py --configs configs/train_mosmed_manet_densenet121_fold2.yml
srun python main.py --configs configs/train_mosmed_manet_densenet121_fold3.yml
srun python main.py --configs configs/train_mosmed_manet_densenet121_fold4.yml
