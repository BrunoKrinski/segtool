import os
import cv2
import glob
import json
import numpy as np
import matplotlib.pyplot as plt

def getminmax(x1, x2):
    aux1 = sorted(x1)
    aux2 = sorted(x2)

    if aux1[0] > aux2[0]:
        p = aux1[0]
    else:
        p = aux2[0]
    
    p = p * 10
    
    if p < 0:
        p = 0
    if aux1[len(aux1)-1] > aux2[len(aux2)-1]:
        e = aux1[len(aux1)-1]
    else:
        e = aux2[len(aux2)-1]
    
    e = e * 10 + 1
    if e > 10:
        e = 10

    return int(p)*10, int(e)*10+1

if __name__ == '__main__':

    experiments = ['baseline_resnet50unet/', 'cdropout_resnet50unet/']
    datasets = ['camvid/', 'cihp/', 'covid20cases/', 'gbn_caract_patched/', 'gbn_region_patched/']
    datasets = ['camvid/']
    runs_path = 'RUNS/'

    for experiment in experiments:
        for dataset in datasets:
            runspath = runs_path + experiment + dataset
            
            mean_results_path = runspath + '/graphics'
            if os.path.isdir(mean_results_path):
                os.system('rm -rf {}'.format(mean_results_path))

            runs = glob.glob(runspath + '*')

            all_train = []
            all_valid = []
            num_classes = 0
            labels = []

            for run in runs:
                print(run)
                results_path = run + '/graphics'
                if os.path.isdir(results_path):
                    os.system('rm -rf {}'.format(results_path))

                os.mkdir(results_path)

                train_logs_path = run + '/train_logs.json'

                with open(train_logs_path) as train_logs_file:
                    train_logs = json.load(train_logs_file)
                
                if len(labels) == 0:
                    epoch_0 = train_logs['train'][0]
                    for key, value in epoch_0.items():
                        labels.append(key)
                    num_classes = len(labels) - 3

                train_results = train_logs['train']
                valid_results = train_logs['valid']
                #print(labels)
                for label in labels:
                    if label != 'Time' and label != 'Epoch' and label != 'Jaccard_loss':
                        print(label)
                        x1 = []
                        x2 = []
                        for train_epoch, valid_epoch in zip(train_results, valid_results):
                            x1.append(train_epoch[label])
                            x2.append(valid_epoch[label])

                        #if label == 'fscore':
                        #    print(x1)
                        
                        all_train.append(x1)
                        all_valid.append(x2)
                        
                        y = list(range(len(x1)))
                        
                        p, e = getminmax(x1, x2)
                        #print(int(p)*10)
                        #print(int(e)*10+1)
                        yticks = [p/100 for p in range(p, e, 1)]
                        xticks = [p for p in range(0, len(x1)+5, 5)]
                        plt.plot(y, x1, label='train')
                        plt.plot(y, x2, label='valid')
                        plt.xticks(xticks)
                        plt.yticks(yticks)
                        plt.title(label)
                        plt.legend()
                        plt.grid(True)
                        plt.savefig(results_path + '/' + label.lower() + '.png')
                        plt.clf()
            print("--------------------------------------------------")
            os.mkdir(mean_results_path)
            
            for i in range(num_classes):
                mean_train = []
                mean_valid = []
                print(labels[i+1])
                for j in range(0+i, len(all_train), num_classes):
                    mean_train.append(all_train[j])
                    mean_valid.append(all_valid[j])

                mean_train = list(map(lambda x: sum(x)/len(x), zip(*mean_train)))
                mean_valid = list(map(lambda x: sum(x)/len(x), zip(*mean_valid)))

                p, e = getminmax(mean_train, mean_valid)

                y = list(range(len(mean_train)))
                yticks = [p/100 for p in range(p, e, 1)]
                xticks = [p for p in range(0, len(mean_train)+5, 5)]
                plt.plot(y, mean_train, label='train')
                plt.plot(y, mean_valid, label='valid')
                plt.xticks(xticks)
                plt.yticks(yticks)
                plt.title(dataset + experiment.split('_')[0] + '/' + labels[i+1])
                plt.legend()
                plt.grid(True)
                plt.savefig(mean_results_path + '/' + labels[i+1].lower() + '.png')
                plt.clf()
