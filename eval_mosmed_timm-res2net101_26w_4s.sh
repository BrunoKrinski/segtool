#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_timm-res2net101_26w_4s_log.out
#SBATCH --job-name=mosmed_timm-res2net101_26w_4s
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_timm-res2net101_26w_4s_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_mosmed_unetplusplus_timm-res2net101_26w_4s_0.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_timm-res2net101_26w_4s_1.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_timm-res2net101_26w_4s_2.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_timm-res2net101_26w_4s_3.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_timm-res2net101_26w_4s_4.yml
srun python main.py --configs configs/eval_mosmed_unet_timm-res2net101_26w_4s_0.yml
srun python main.py --configs configs/eval_mosmed_unet_timm-res2net101_26w_4s_1.yml
srun python main.py --configs configs/eval_mosmed_unet_timm-res2net101_26w_4s_2.yml
srun python main.py --configs configs/eval_mosmed_unet_timm-res2net101_26w_4s_3.yml
srun python main.py --configs configs/eval_mosmed_unet_timm-res2net101_26w_4s_4.yml
srun python main.py --configs configs/eval_mosmed_fpn_timm-res2net101_26w_4s_0.yml
srun python main.py --configs configs/eval_mosmed_fpn_timm-res2net101_26w_4s_1.yml
srun python main.py --configs configs/eval_mosmed_fpn_timm-res2net101_26w_4s_2.yml
srun python main.py --configs configs/eval_mosmed_fpn_timm-res2net101_26w_4s_3.yml
srun python main.py --configs configs/eval_mosmed_fpn_timm-res2net101_26w_4s_4.yml
srun python main.py --configs configs/eval_mosmed_pspnet_timm-res2net101_26w_4s_0.yml
srun python main.py --configs configs/eval_mosmed_pspnet_timm-res2net101_26w_4s_1.yml
srun python main.py --configs configs/eval_mosmed_pspnet_timm-res2net101_26w_4s_2.yml
srun python main.py --configs configs/eval_mosmed_pspnet_timm-res2net101_26w_4s_3.yml
srun python main.py --configs configs/eval_mosmed_pspnet_timm-res2net101_26w_4s_4.yml
srun python main.py --configs configs/eval_mosmed_linknet_timm-res2net101_26w_4s_0.yml
srun python main.py --configs configs/eval_mosmed_linknet_timm-res2net101_26w_4s_1.yml
srun python main.py --configs configs/eval_mosmed_linknet_timm-res2net101_26w_4s_2.yml
srun python main.py --configs configs/eval_mosmed_linknet_timm-res2net101_26w_4s_3.yml
srun python main.py --configs configs/eval_mosmed_linknet_timm-res2net101_26w_4s_4.yml
srun python main.py --configs configs/eval_mosmed_manet_timm-res2net101_26w_4s_0.yml
srun python main.py --configs configs/eval_mosmed_manet_timm-res2net101_26w_4s_1.yml
srun python main.py --configs configs/eval_mosmed_manet_timm-res2net101_26w_4s_2.yml
srun python main.py --configs configs/eval_mosmed_manet_timm-res2net101_26w_4s_3.yml
srun python main.py --configs configs/eval_mosmed_manet_timm-res2net101_26w_4s_4.yml
