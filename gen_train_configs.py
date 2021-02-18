import os
import yaml

width = 512
height = 512
num_folds = 5
batch_size = 8
num_epochs = 50
num_workers = 8
learning_rate = 0.001

mode = 'train'
experiment = 'baseline'

encoders = ['resnet50']
nodes = ['pti', 'vti1-ib', 'vti2-ib']
decoders = ['unet','fpn','pspnet','linknet']
datasets = ['ricord1a', 'covid20cases', 'covid19china', 'medseg', 'mosmed']

node_num = 0
node_count = 0
node_usage = 2

if node_usage * len(nodes) < len(datasets):
    print('Little node usage!')
    exit()

for dataset in datasets:

    sh_cmds = []
    py_cmds = []

    if node_count >= node_usage:
        node_num += 1
        node_count = 0
    
    node_count += 1
    print(nodes[node_num])

    sh = '#!/bin/sh\n#SBATCH -t 7-00:00:00\n#SBATCH -c 8\n#SBATCH -o /home/bakrinski/segtool/logs/{}_log.out\n\
#SBATCH --job-name={}\n#SBATCH -n 1 #NUM_DE_PROCESSOS\n#SBATCH -p 7d\n#SBATCH -N 1 #NUM_NODOS_NECESSARIOS\n\
#SBATCH --nodelist={}\n#SBATCH --gres=gpu:1\n#SBATCH -e /home/bakrinski/segtool/logs/{}_error.out\n\n\
export PATH="/home/bakrinski/anaconda3/bin:$PATH"\n\nmodule load libraries/cuda/10.1\n\n'.format(dataset, dataset, nodes[node_num], dataset)

    for decoder in decoders:
        for encoder in encoders:    
            for fold in range(num_folds):
                configs = {
                    "general": {"mode": mode, 
                                "num_workers": num_workers,
                                "experiment": experiment, 
                                "dataset": dataset},
                    
                    "model": {"encoder": encoder, 
                              "decoder": decoder, 
                              "batch_size": batch_size,
                              "num_epochs": num_epochs, 
                              "learning_rate": learning_rate,
                              "height": height, 
                              "width": width},

                    "dataset": {"train": "datasets/{}/train/train_ids{}.txt".format(dataset, fold),
                                "valid": "datasets/{}/train/valid_ids{}.txt".format(dataset, fold),
                                "labels": "datasets/{}/labels.txt".format(dataset)}
                }
                configs_name = 'configs/train_' + dataset + '_' + decoder + '_' + encoder + '_fold' + str(fold) + '.yml'
                with open(configs_name, 'w') as config_file:
                    yaml.dump(configs, config_file)

                py_cmds.append("python main.py --configs {}".format(configs_name))
                sh_cmds.append("srun python main.py --configs {}".format(configs_name))

    for sh_cmd in sh_cmds:
        sh += sh_cmd + '\n'

    sh_file = 'train_' + dataset + '.sh'
    with open(sh_file,'w') as shf:
        shf.write(sh)
    
    py = 'import os\n\nls=['
    for py_cmd in py_cmds:
        py += '"' + py_cmd + '",\n'
    py += ']\n\nfor l in ls:\n  os.system(l)'

    py_file = 'train_' + dataset + '.py'
    with open(py_file,'w') as pyf:
        pyf.write(py)
