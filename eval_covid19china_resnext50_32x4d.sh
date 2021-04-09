#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid19china_resnext50_32x4d_log.out
#SBATCH --job-name=covid19china_resnext50_32x4d
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid19china_resnext50_32x4d_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_covid19china_unetplusplus_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_unet_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_unet_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_unet_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_unet_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_unet_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_fpn_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_fpn_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_fpn_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_fpn_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_fpn_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_pspnet_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_pspnet_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_pspnet_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_pspnet_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_pspnet_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_linknet_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_linknet_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_linknet_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_linknet_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_linknet_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_pan_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_pan_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_pan_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_pan_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_pan_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_manet_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_manet_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_manet_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_manet_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_manet_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3_resnext50_32x4d_4.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3plus_resnext50_32x4d_0.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3plus_resnext50_32x4d_1.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3plus_resnext50_32x4d_2.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3plus_resnext50_32x4d_3.yml
srun python main.py --configs configs/eval_covid19china_deeplabv3plus_resnext50_32x4d_4.yml