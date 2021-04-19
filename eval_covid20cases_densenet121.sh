#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_densenet121_log.out
#SBATCH --job-name=covid20cases_densenet121
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_densenet121_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_covid20cases_unetplusplus_densenet121_0.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_densenet121_1.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_densenet121_2.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_densenet121_3.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_densenet121_4.yml
srun python main.py --configs configs/eval_covid20cases_unet_densenet121_0.yml
srun python main.py --configs configs/eval_covid20cases_unet_densenet121_1.yml
srun python main.py --configs configs/eval_covid20cases_unet_densenet121_2.yml
srun python main.py --configs configs/eval_covid20cases_unet_densenet121_3.yml
srun python main.py --configs configs/eval_covid20cases_unet_densenet121_4.yml
srun python main.py --configs configs/eval_covid20cases_fpn_densenet121_0.yml
srun python main.py --configs configs/eval_covid20cases_fpn_densenet121_1.yml
srun python main.py --configs configs/eval_covid20cases_fpn_densenet121_2.yml
srun python main.py --configs configs/eval_covid20cases_fpn_densenet121_3.yml
srun python main.py --configs configs/eval_covid20cases_fpn_densenet121_4.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_densenet121_0.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_densenet121_1.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_densenet121_2.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_densenet121_3.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_densenet121_4.yml
srun python main.py --configs configs/eval_covid20cases_linknet_densenet121_0.yml
srun python main.py --configs configs/eval_covid20cases_linknet_densenet121_1.yml
srun python main.py --configs configs/eval_covid20cases_linknet_densenet121_2.yml
srun python main.py --configs configs/eval_covid20cases_linknet_densenet121_3.yml
srun python main.py --configs configs/eval_covid20cases_linknet_densenet121_4.yml
srun python main.py --configs configs/eval_covid20cases_manet_densenet121_0.yml
srun python main.py --configs configs/eval_covid20cases_manet_densenet121_1.yml
srun python main.py --configs configs/eval_covid20cases_manet_densenet121_2.yml
srun python main.py --configs configs/eval_covid20cases_manet_densenet121_3.yml
srun python main.py --configs configs/eval_covid20cases_manet_densenet121_4.yml
