#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_resnet101_log.out
#SBATCH --job-name=mosmed_resnet101
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_resnet101_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_pan_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_pan_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_pan_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_pan_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_pan_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3_resnet101_4.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3plus_resnet101_0.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3plus_resnet101_1.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3plus_resnet101_2.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3plus_resnet101_3.yml
srun python main.py --configs configs/eval_mosmed_deeplabv3plus_resnet101_4.yml