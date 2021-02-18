#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/logs/covid19china_log.out
#SBATCH --job-name=covid19china
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/logs/covid19china_error.out

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
