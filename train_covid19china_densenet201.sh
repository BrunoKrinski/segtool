#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid19china_densenet201_log.out
#SBATCH --job-name=covid19china_densenet201
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid19china_densenet201_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid19china_unetplusplus_densenet201_fold0.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_densenet201_fold1.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_densenet201_fold2.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_densenet201_fold3.yml
srun python main.py --configs configs/train_covid19china_unetplusplus_densenet201_fold4.yml
srun python main.py --configs configs/train_covid19china_unet_densenet201_fold0.yml
srun python main.py --configs configs/train_covid19china_unet_densenet201_fold1.yml
srun python main.py --configs configs/train_covid19china_unet_densenet201_fold2.yml
srun python main.py --configs configs/train_covid19china_unet_densenet201_fold3.yml
srun python main.py --configs configs/train_covid19china_unet_densenet201_fold4.yml
srun python main.py --configs configs/train_covid19china_fpn_densenet201_fold0.yml
srun python main.py --configs configs/train_covid19china_fpn_densenet201_fold1.yml
srun python main.py --configs configs/train_covid19china_fpn_densenet201_fold2.yml
srun python main.py --configs configs/train_covid19china_fpn_densenet201_fold3.yml
srun python main.py --configs configs/train_covid19china_fpn_densenet201_fold4.yml
srun python main.py --configs configs/train_covid19china_pspnet_densenet201_fold0.yml
srun python main.py --configs configs/train_covid19china_pspnet_densenet201_fold1.yml
srun python main.py --configs configs/train_covid19china_pspnet_densenet201_fold2.yml
srun python main.py --configs configs/train_covid19china_pspnet_densenet201_fold3.yml
srun python main.py --configs configs/train_covid19china_pspnet_densenet201_fold4.yml
srun python main.py --configs configs/train_covid19china_linknet_densenet201_fold0.yml
srun python main.py --configs configs/train_covid19china_linknet_densenet201_fold1.yml
srun python main.py --configs configs/train_covid19china_linknet_densenet201_fold2.yml
srun python main.py --configs configs/train_covid19china_linknet_densenet201_fold3.yml
srun python main.py --configs configs/train_covid19china_linknet_densenet201_fold4.yml
srun python main.py --configs configs/train_covid19china_manet_densenet201_fold0.yml
srun python main.py --configs configs/train_covid19china_manet_densenet201_fold1.yml
srun python main.py --configs configs/train_covid19china_manet_densenet201_fold2.yml
srun python main.py --configs configs/train_covid19china_manet_densenet201_fold3.yml
srun python main.py --configs configs/train_covid19china_manet_densenet201_fold4.yml
