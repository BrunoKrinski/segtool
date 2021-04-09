#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/covid20cases_vgg16_log.out
#SBATCH --job-name=covid20cases_vgg16
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/covid20cases_vgg16_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_covid20cases_unetplusplus_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_unetplusplus_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_unet_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_unet_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_unet_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_unet_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_unet_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_fpn_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_fpn_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_fpn_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_fpn_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_fpn_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_pspnet_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_linknet_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_linknet_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_linknet_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_linknet_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_linknet_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_pan_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_pan_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_pan_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_pan_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_pan_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_manet_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_manet_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_manet_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_manet_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_manet_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3_vgg16_4.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3plus_vgg16_0.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3plus_vgg16_1.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3plus_vgg16_2.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3plus_vgg16_3.yml
srun python main.py --configs configs/eval_covid20cases_deeplabv3plus_vgg16_4.yml
