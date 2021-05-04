#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_timm-regnetx_006_log.out
#SBATCH --job-name=covid20cases_timm-regnetx_006
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_timm-regnetx_006_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_006_fold0.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_006_fold1.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_006_fold2.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_006_fold3.yml
srun python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_006_fold4.yml
srun python main.py --configs configs/train_covid20cases_unet_timm-regnetx_006_fold0.yml
srun python main.py --configs configs/train_covid20cases_unet_timm-regnetx_006_fold1.yml
srun python main.py --configs configs/train_covid20cases_unet_timm-regnetx_006_fold2.yml
srun python main.py --configs configs/train_covid20cases_unet_timm-regnetx_006_fold3.yml
srun python main.py --configs configs/train_covid20cases_unet_timm-regnetx_006_fold4.yml
srun python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_006_fold0.yml
srun python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_006_fold1.yml
srun python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_006_fold2.yml
srun python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_006_fold3.yml
srun python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_006_fold4.yml
srun python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_006_fold0.yml
srun python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_006_fold1.yml
srun python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_006_fold2.yml
srun python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_006_fold3.yml
srun python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_006_fold4.yml
srun python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_006_fold0.yml
srun python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_006_fold1.yml
srun python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_006_fold2.yml
srun python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_006_fold3.yml
srun python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_006_fold4.yml
srun python main.py --configs configs/train_covid20cases_manet_timm-regnetx_006_fold0.yml
srun python main.py --configs configs/train_covid20cases_manet_timm-regnetx_006_fold1.yml
srun python main.py --configs configs/train_covid20cases_manet_timm-regnetx_006_fold2.yml
srun python main.py --configs configs/train_covid20cases_manet_timm-regnetx_006_fold3.yml
srun python main.py --configs configs/train_covid20cases_manet_timm-regnetx_006_fold4.yml
