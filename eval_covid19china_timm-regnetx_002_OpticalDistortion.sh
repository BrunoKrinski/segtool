#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid19china_timm-regnetx_002_log.out
    #SBATCH --job-name=covid19china_timm-regnetx_002
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
    #SBATCH --nodelist=vti2-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid19china_timm-regnetx_002_error.out

    export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_OpticalDistortion.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_OpticalDistortion.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_OpticalDistortion.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_OpticalDistortion.yml
srun python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_OpticalDistortion.yml
