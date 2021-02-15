#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/logs/ricord1a_log.out
#SBATCH --job-name=segtool_train
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/logs/ricord1a_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/ricord1a_resnet50_unet_fold0.yml
srun python main.py --configs configs/ricord1a_resnet50_fpn_fold0.yml
srun python main.py --configs configs/ricord1a_resnet50_pspnet_fold0.yml
srun python main.py --configs configs/ricord1a_resnet50_linknet_fold0.yml
srun python main.py --configs configs/ricord1a_resnet50_unet_fold1.yml
srun python main.py --configs configs/ricord1a_resnet50_fpn_fold1.yml
srun python main.py --configs configs/ricord1a_resnet50_pspnet_fold1.yml
srun python main.py --configs configs/ricord1a_resnet50_linknet_fold1.yml
srun python main.py --configs configs/ricord1a_resnet50_unet_fold2.yml
srun python main.py --configs configs/ricord1a_resnet50_fpn_fold2.yml
srun python main.py --configs configs/ricord1a_resnet50_pspnet_fold2.yml
srun python main.py --configs configs/ricord1a_resnet50_linknet_fold2.yml
srun python main.py --configs configs/ricord1a_resnet50_unet_fold3.yml
srun python main.py --configs configs/ricord1a_resnet50_fpn_fold3.yml
srun python main.py --configs configs/ricord1a_resnet50_pspnet_fold3.yml
srun python main.py --configs configs/ricord1a_resnet50_linknet_fold3.yml
srun python main.py --configs configs/ricord1a_resnet50_unet_fold4.yml
srun python main.py --configs configs/ricord1a_resnet50_fpn_fold4.yml
srun python main.py --configs configs/ricord1a_resnet50_pspnet_fold4.yml
srun python main.py --configs configs/ricord1a_resnet50_linknet_fold4.yml
