#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/mosmed_resnet50_log.out
#SBATCH --job-name=mosmed_resnet50
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=pti
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/mosmed_resnet50_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet50_0.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet50_1.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet50_2.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet50_3.yml
srun python main.py --configs configs/eval_mosmed_unetplusplus_resnet50_4.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet50_0.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet50_1.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet50_2.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet50_3.yml
srun python main.py --configs configs/eval_mosmed_unet_resnet50_4.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet50_0.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet50_1.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet50_2.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet50_3.yml
srun python main.py --configs configs/eval_mosmed_fpn_resnet50_4.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet50_0.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet50_1.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet50_2.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet50_3.yml
srun python main.py --configs configs/eval_mosmed_pspnet_resnet50_4.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet50_0.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet50_1.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet50_2.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet50_3.yml
srun python main.py --configs configs/eval_mosmed_linknet_resnet50_4.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet50_0.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet50_1.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet50_2.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet50_3.yml
srun python main.py --configs configs/eval_mosmed_manet_resnet50_4.yml
