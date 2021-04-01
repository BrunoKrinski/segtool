#!/bin/sh
#SBATCH -t 7-00:00:00
#SBATCH -c 4
#SBATCH -o /home/bakrinski/segtool/logs/medseg_vgg16_log.out
#SBATCH --job-name=medseg_vgg16
#SBATCH -n 1 #NUM_DE_PROCESSOS
#SBATCH -p 7d
#SBATCH -N 1 #NUM_NODOS_NECESSARIOS
#SBATCH --nodelist=vti1-ib
#SBATCH --gres=gpu:2
#SBATCH -e /home/bakrinski/segtool/logs/medseg_vgg16_error.out

export PATH="/home/bakrinski/anaconda3/bin:$PATH"

module load libraries/cuda/10.1

srun python main.py --configs configs/eval_medseg_unetplusplus_vgg16_0.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_vgg16_1.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_vgg16_2.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_vgg16_3.yml
srun python main.py --configs configs/eval_medseg_unetplusplus_vgg16_4.yml
srun python main.py --configs configs/eval_medseg_unet_vgg16_0.yml
srun python main.py --configs configs/eval_medseg_unet_vgg16_1.yml
srun python main.py --configs configs/eval_medseg_unet_vgg16_2.yml
srun python main.py --configs configs/eval_medseg_unet_vgg16_3.yml
srun python main.py --configs configs/eval_medseg_unet_vgg16_4.yml
srun python main.py --configs configs/eval_medseg_fpn_vgg16_0.yml
srun python main.py --configs configs/eval_medseg_fpn_vgg16_1.yml
srun python main.py --configs configs/eval_medseg_fpn_vgg16_2.yml
srun python main.py --configs configs/eval_medseg_fpn_vgg16_3.yml
srun python main.py --configs configs/eval_medseg_fpn_vgg16_4.yml
srun python main.py --configs configs/eval_medseg_pspnet_vgg16_0.yml
srun python main.py --configs configs/eval_medseg_pspnet_vgg16_1.yml
srun python main.py --configs configs/eval_medseg_pspnet_vgg16_2.yml
srun python main.py --configs configs/eval_medseg_pspnet_vgg16_3.yml
srun python main.py --configs configs/eval_medseg_pspnet_vgg16_4.yml
srun python main.py --configs configs/eval_medseg_linknet_vgg16_0.yml
srun python main.py --configs configs/eval_medseg_linknet_vgg16_1.yml
srun python main.py --configs configs/eval_medseg_linknet_vgg16_2.yml
srun python main.py --configs configs/eval_medseg_linknet_vgg16_3.yml
srun python main.py --configs configs/eval_medseg_linknet_vgg16_4.yml
srun python main.py --configs configs/eval_medseg_manet_vgg16_0.yml
srun python main.py --configs configs/eval_medseg_manet_vgg16_1.yml
srun python main.py --configs configs/eval_medseg_manet_vgg16_2.yml
srun python main.py --configs configs/eval_medseg_manet_vgg16_3.yml
srun python main.py --configs configs/eval_medseg_manet_vgg16_4.yml
