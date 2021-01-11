#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/covid20cases_vgg16unet_log.out
#SBATCH --job-name=segtool_train
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/covid20cases_vgg16unet_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/vgg16_unet_covid20cases_fold0.yml
srun python main.py --configs configs/vgg16_unet_covid20cases_fold1.yml
srun python main.py --configs configs/vgg16_unet_covid20cases_fold2.yml
srun python main.py --configs configs/vgg16_unet_covid20cases_fold3.yml
srun python main.py --configs configs/vgg16_unet_covid20cases_fold4.yml