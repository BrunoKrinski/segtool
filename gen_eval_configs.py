import os
import yaml
import glob

width = 512
height = 512
batch_size = 8
num_workers = 8

mode = 'eval'
#type = 'last'
#type = 'best_iou'
type = 'best_fscore'
experiment = 'baseline'

encoders = ['resnet18', 
            'resnet34', 
            'resnet50', 
            'resnet101', 
            'resnet152', 
            'resnext50_32x4d', 
            'resnext101_32x8d',
            'timm-resnest14d', 
            'timm-resnest26d',
            'timm-resnest50d', 
            'timm-resnest101e',
            'timm-resnest200e', 
            'timm-resnest269e',
            'timm-resnest50d_4s2x40d', 
            'timm-resnest50d_4s2x40d',
            'timm-res2net50_26w_4s', 
            'timm-res2net101_26w_4s',
            'timm-res2net101_26w_4s', 
            'timm-res2net50_26w_8s',
            'timm-res2net50_48w_2s', 
            'timm-res2net50_14w_8s',
            'timm-res2next50',
            'timm-regnetx_002',
            'timm-regnetx_004', 
            'timm-regnetx_006',
            'timm-regnetx_008', 
            'timm-regnetx_016',
            'timm-regnetx_032', 
            'timm-regnetx_040',
            'timm-regnetx_064', 
            'timm-regnetx_080',
            'timm-regnetx_120', 
            'timm-regnetx_160',
            'timm-regnetx_320',
            'timm-regnety_002',
            'timm-regnety_004', 
            'timm-regnety_006',
            'timm-regnety_008', 
            'timm-regnety_016',
            'timm-regnety_032', 
            'timm-regnety_040',
            'timm-regnety_064', 
            'timm-regnety_080',
            'timm-regnety_120', 
            'timm-regnety_160',
            'timm-regnety_320',
            'senet154',
            'se_resnet50', 
            'se_resnet101',
            'se_resnet152', 
            'se_resnext50_32x4d',
            'se_resnext101_32x4d', 
            'timm-skresnet18',
            'timm-skresnet34', 
            'timm-skresnext50_32x4d',
            'densenet121', 
            'densenet169',
            'densenet201', 
            'densenet161',
            'inceptionresnetv2', 
            'inceptionv4',
            'xception', 
            'efficientnet-b0',
            'efficientnet-b1', 
            'efficientnet-b2',
            'efficientnet-b3', 
            'efficientnet-b4',
            'efficientnet-b5', 
            'efficientnet-b6',
            'efficientnet-b7', 
            'timm-efficientnet-b0',
            'timm-efficientnet-b1', 
            'timm-efficientnet-b2',
            'timm-efficientnet-b3', 
            'timm-efficientnet-b4',
            'timm-efficientnet-b5', 
            'timm-efficientnet-b6',
            'timm-efficientnet-b7', 
            'timm-efficientnet-b8',
            'timm-efficientnet-l2', 
            'timm-efficientnet-lite0',
            'timm-efficientnet-lite1', 
            'timm-efficientnet-lite2',
            'timm-efficientnet-lite3',
            'timm-efficientnet-lite4', 
            'mobilenet_v2',
            'dpn68', 
            'dpn68b',
            'dpn92', 
            'dpn98',
            'dpn107', 
            'dpn131',
            'vgg11', 
            'vgg11_bn',
            'vgg13', 
            'vgg13_bn',
            'vgg16', 
            'vgg16_bn',
            'vgg19', 
            'vgg19_bn']

encoders = ['resnet50']
nodes = ['vti1-ib', 'pti', 'vti2-ib']
decoders = ['unetplusplus','unet','fpn','pspnet','linknet', 'pan', 'manet', 'deeplabv3', 'deeplabv3plus']
#datasets = ['ricord1a', 'medseg', 'covid20cases', 'mosmed', 'covid19china']
datasets = ['medseg', 'mosmed', 'covid19china']

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
            r = 0
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
                    
                    configs_name = 'configs/eval_' + dataset + '_' + decoder + '_' + encoder + '_' + str(r) + '.yml'
                    r += 1
                    with open(configs_name, 'w') as config_file:
                        yaml.dump(configs, config_file)
                    py_cmds.append("python main.py --configs {}".format(configs_name))
                    sh_cmds.append("srun python main.py --configs {}".format(configs_name))
    
    for sh_cmd in sh_cmds:
        sh += sh_cmd + '\n'

    sh_file = 'eval_' + dataset + '_' + encoders[0] + '.sh'
    with open(sh_file,'w') as shf:
        shf.write(sh)
    
    py = 'import os\n\nls=['
    for py_cmd in py_cmds:
        py += '"' + py_cmd + '",\n'
    py += ']\n\nfor l in ls:\n  os.system(l)'

    py_file = 'eval_' + dataset + '_' + encoders[0] + '.py'
    with open(py_file,'w') as pyf:
        pyf.write(py)
