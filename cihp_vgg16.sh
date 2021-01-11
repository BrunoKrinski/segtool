#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/cihp_vgg16unet_log.out
#SBATCH --job-name=segtool_train
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/cihp_vgg16unet_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/vgg16_unet_cihp_fold0.yml
srun python main.py --configs configs/vgg16_unet_cihp_fold1.yml
srun python main.py --configs configs/vgg16_unet_cihp_fold2.yml
srun python main.py --configs configs/vgg16_unet_cihp_fold3.yml
srun python main.py --configs configs/vgg16_unet_cihp_fold4.yml