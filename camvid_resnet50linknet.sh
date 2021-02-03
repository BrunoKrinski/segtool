#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/logs/camvid_resnet50linknet_log.out
#SBATCH --job-name=segtool_train
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/logs/camvid_resnet50linknet_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/resnet50_linknet_camvid_fold0.yml
srun python main.py --configs configs/resnet50_linknet_camvid_fold1.yml
srun python main.py --configs configs/resnet50_linknet_camvid_fold2.yml
srun python main.py --configs configs/resnet50_linknet_camvid_fold3.yml
srun python main.py --configs configs/resnet50_linknet_camvid_fold4.yml