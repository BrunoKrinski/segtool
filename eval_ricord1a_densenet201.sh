#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/ricord1a_densenet201_log.out
#SBATCH --job-name=ricord1a_densenet201
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/ricord1a_densenet201_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_0.yml
srun python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_1.yml
srun python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_2.yml
srun python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_3.yml
srun python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_4.yml
srun python main.py --configs configs/eval_ricord1a_unet_densenet201_0.yml
srun python main.py --configs configs/eval_ricord1a_unet_densenet201_1.yml
srun python main.py --configs configs/eval_ricord1a_unet_densenet201_2.yml
srun python main.py --configs configs/eval_ricord1a_unet_densenet201_3.yml
srun python main.py --configs configs/eval_ricord1a_unet_densenet201_4.yml
srun python main.py --configs configs/eval_ricord1a_fpn_densenet201_0.yml
srun python main.py --configs configs/eval_ricord1a_fpn_densenet201_1.yml
srun python main.py --configs configs/eval_ricord1a_fpn_densenet201_2.yml
srun python main.py --configs configs/eval_ricord1a_fpn_densenet201_3.yml
srun python main.py --configs configs/eval_ricord1a_fpn_densenet201_4.yml
