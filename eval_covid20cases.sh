#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 8
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_log.out
#SBATCH --job-name=covid20cases
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:1
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_covid20cases_resnet50_unet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_unet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_unet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_unet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_unet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_fpn.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_fpn.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_fpn.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_fpn.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_fpn.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_pspnet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_pspnet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_pspnet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_pspnet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_pspnet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_linknet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_linknet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_linknet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_linknet.yml
srun python main.py --configs configs/eval_covid20cases_resnet50_linknet.yml
