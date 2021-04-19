#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/medseg_resnext101_32x8d_log.out
#SBATCH --job-name=medseg_resnext101_32x8d
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_resnext101_32x8d_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_medseg_unetplusplus_resnext101_32x8d_0.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_resnext101_32x8d_1.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_resnext101_32x8d_2.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_resnext101_32x8d_3.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_resnext101_32x8d_4.yml
srun python main.py --configs configs/eval_medseg_unet_resnext101_32x8d_0.yml
srun python main.py --configs configs/eval_medseg_unet_resnext101_32x8d_1.yml
srun python main.py --configs configs/eval_medseg_unet_resnext101_32x8d_2.yml
srun python main.py --configs configs/eval_medseg_unet_resnext101_32x8d_3.yml
srun python main.py --configs configs/eval_medseg_unet_resnext101_32x8d_4.yml
srun python main.py --configs configs/eval_medseg_fpn_resnext101_32x8d_0.yml
srun python main.py --configs configs/eval_medseg_fpn_resnext101_32x8d_1.yml
srun python main.py --configs configs/eval_medseg_fpn_resnext101_32x8d_2.yml
srun python main.py --configs configs/eval_medseg_fpn_resnext101_32x8d_3.yml
srun python main.py --configs configs/eval_medseg_fpn_resnext101_32x8d_4.yml
srun python main.py --configs configs/eval_medseg_pspnet_resnext101_32x8d_0.yml
srun python main.py --configs configs/eval_medseg_pspnet_resnext101_32x8d_1.yml
srun python main.py --configs configs/eval_medseg_pspnet_resnext101_32x8d_2.yml
srun python main.py --configs configs/eval_medseg_pspnet_resnext101_32x8d_3.yml
srun python main.py --configs configs/eval_medseg_pspnet_resnext101_32x8d_4.yml
srun python main.py --configs configs/eval_medseg_linknet_resnext101_32x8d_0.yml
srun python main.py --configs configs/eval_medseg_linknet_resnext101_32x8d_1.yml
srun python main.py --configs configs/eval_medseg_linknet_resnext101_32x8d_2.yml
srun python main.py --configs configs/eval_medseg_linknet_resnext101_32x8d_3.yml
srun python main.py --configs configs/eval_medseg_linknet_resnext101_32x8d_4.yml
srun python main.py --configs configs/eval_medseg_manet_resnext101_32x8d_0.yml
srun python main.py --configs configs/eval_medseg_manet_resnext101_32x8d_1.yml
srun python main.py --configs configs/eval_medseg_manet_resnext101_32x8d_2.yml
srun python main.py --configs configs/eval_medseg_manet_resnext101_32x8d_3.yml
srun python main.py --configs configs/eval_medseg_manet_resnext101_32x8d_4.yml
