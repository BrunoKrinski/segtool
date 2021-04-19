#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/medseg_densenet169_log.out
#SBATCH --job-name=medseg_densenet169
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_densenet169_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_medseg_unetplusplus_densenet169_0.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_densenet169_1.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_densenet169_2.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_densenet169_3.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_densenet169_4.yml
srun python main.py --configs configs/eval_medseg_unet_densenet169_0.yml
srun python main.py --configs configs/eval_medseg_unet_densenet169_1.yml
srun python main.py --configs configs/eval_medseg_unet_densenet169_2.yml
srun python main.py --configs configs/eval_medseg_unet_densenet169_3.yml
srun python main.py --configs configs/eval_medseg_unet_densenet169_4.yml
srun python main.py --configs configs/eval_medseg_fpn_densenet169_0.yml
srun python main.py --configs configs/eval_medseg_fpn_densenet169_1.yml
srun python main.py --configs configs/eval_medseg_fpn_densenet169_2.yml
srun python main.py --configs configs/eval_medseg_fpn_densenet169_3.yml
srun python main.py --configs configs/eval_medseg_fpn_densenet169_4.yml
srun python main.py --configs configs/eval_medseg_pspnet_densenet169_0.yml
srun python main.py --configs configs/eval_medseg_pspnet_densenet169_1.yml
srun python main.py --configs configs/eval_medseg_pspnet_densenet169_2.yml
srun python main.py --configs configs/eval_medseg_pspnet_densenet169_3.yml
srun python main.py --configs configs/eval_medseg_pspnet_densenet169_4.yml
srun python main.py --configs configs/eval_medseg_linknet_densenet169_0.yml
srun python main.py --configs configs/eval_medseg_linknet_densenet169_1.yml
srun python main.py --configs configs/eval_medseg_linknet_densenet169_2.yml
srun python main.py --configs configs/eval_medseg_linknet_densenet169_3.yml
srun python main.py --configs configs/eval_medseg_linknet_densenet169_4.yml
srun python main.py --configs configs/eval_medseg_manet_densenet169_0.yml
srun python main.py --configs configs/eval_medseg_manet_densenet169_1.yml
srun python main.py --configs configs/eval_medseg_manet_densenet169_2.yml
srun python main.py --configs configs/eval_medseg_manet_densenet169_3.yml
srun python main.py --configs configs/eval_medseg_manet_densenet169_4.yml
