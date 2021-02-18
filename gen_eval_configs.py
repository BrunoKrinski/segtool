import os
import yaml
import glob

width = 512
height = 512
batch_size = 8
num_workers = 8

mode = 'eval'
type = 'best_fscore'
experiment = 'baseline'

encoders = ['resnet50']
nodes = ['vti1-ib', 'pti', 'vti2-ib']
decoders = ['unet','fpn','pspnet','linknet']
datasets = ['covid20cases', 'covid19china', 'mosmed', 'ricord1a']

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
            path = 'RUNS/' + experiment + '/' + dataset + '/' + decoder + '/' + encoder + '/'
            runs = glob.glob(path + '*')
            for run in runs:
                if 'graphics' not in run:
                    configs = {
                        "general": {"mode": mode, 
                                    "num_workers": num_workers,
                                    "path": run},
                        "model": {"encoder": encoder, 
                                "batch_size": batch_size,
                                "height": height, 
                                "width": width,
                                "type": type},
                        "dataset": {"test": "datasets/{}/valid/test_ids.txt".format(dataset),
                                    "labels": "datasets/{}/labels.txt".format(dataset)}
                    }
                    
                    configs_name = 'configs/eval_' + dataset + '_' + decoder + '_' + encoder + '.yml'
                    with open(configs_name, 'w') as config_file:
                        yaml.dump(configs, config_file)
                    py_cmds.append("python main.py --configs {}".format(configs_name))
                    sh_cmds.append("srun python main.py --configs {}".format(configs_name))
    
    for sh_cmd in sh_cmds:
        sh += sh_cmd + '\n'

    sh_file = 'eval_' + dataset + '.sh'
    with open(sh_file,'w') as shf:
        shf.write(sh)
    
    py = 'import os\n\nls=['
    for py_cmd in py_cmds:
        py += '"' + py_cmd + '",\n'
    py += ']\n\nfor l in ls:\n  os.system(l)'

    py_file = 'eval_' + dataset + '.py'
    with open(py_file,'w') as pyf:
        pyf.write(py)