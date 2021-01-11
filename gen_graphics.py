import cv2
import glob
import json
import numpy as np
import matplotlib.pyplot as plt 

if __name__ == '__main__':

    experiments = ['baseline/']
    datasets = ['camvid/', 'cihp/', 'covid20cases/', 'gbn_caract_patched/', 'gbn_region_patched/']

    runs_path = 'RUNS/'

    for experiment in experiments:
        for dataset in datasets:
            runspath = runs_path + experiment + dataset
            runs = glob.glob(runspath + '*')

            for run in runs:
                train_logs_path = run + '/train_logs.json'

                with open(train_logs_path) as train_logs_file:
                    train_logs = json.load(train_logs_file)

                labels = []
                epoch_0 = train_logs[0]

                
                for i in range(num_classes):
                    x = []
                    fscore = []
                    label = ''
                    for epoch in train_logs['train']:
                        for key, value in epoch.items():
                            if key == 'fscore':
                                fscore.append(value)
                            elif key != 'epoch' and key != 'time':
                                label = key
                                x.append(value)
                    print(label)
                    print(x)
                        
                    