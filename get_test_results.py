import os
import csv
import glob
import json

def init_results(test_results):
    
    results = {}
    for key, value in test_results.items():
        results[key] = value
    return results

if __name__ == '__main__':

    experiments = ['baseline/']
    
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

    encoders = ['resnet50','resnet101','resnext50_32x4d','resnext101_32x8d','vgg16']
    decoders = ['unetplusplus', 'unet','fpn','pspnet','linknet', 'pan', 'manet', 'deeplabv3', 'deeplabv3plus']
    datasets = ['medseg', 'covid20cases', 'covid19china', 'mosmed', 'ricord1a']
    runs_path = 'RUNS'

    test_files = ['test_logs_last.json','test_logs_best_iou.json','test_logs_best_fscore.json']

    for experiment in experiments:
        for test_file in test_files:
            result_table = []
                
            dts1 = [' ']
            dts2 = [' ']
            for dt in datasets:
                dts1.append(dt)
                dts2.append('Fscore / Iou')
            result_table.append(dts1)
            result_table.append(dts2)

            for decoder in decoders:
                for encoder in encoders:
                    line = [encoder.replace('_','\_') + ' ' + decoder]
                    for dataset in datasets:
                        runspath = runs_path + '/' + experiment + '/'  + dataset + '/'  + decoder + '/'  + encoder + '/' 
                        runs = glob.glob(runspath + '*')
                        mean_results = {}
                        init = True
                        cont = 0
                        for run in runs:
                            if 'graphics' not in run:
                                #print(run)
                                tf = run + '/' + test_file
                                if not os.path.isfile(tf):
                                    continue
                                cont += 1
                                with open(tf) as f:
                                    data = json.load(f)
                                    test_results = data['test'][0]
                                    #print(test_results)
                                    
                                    if init:
                                        mean_results = init_results(test_results)
                                        init = False
                                    else:
                                        for key, value in test_results.items():
                                            mean_results[key] += value

                        for key, value in mean_results.items():
                            mean_results[key] = mean_results[key] / cont
                        #line_i = [encoder + ' ' + decoder]

                        #print('--------------------------------------------')
                        #print('Experiment: ' + experiment)
                        #print('Dataset: ' + dataset)
                        #print('Decoder: ' + decoder)
                        #print('Encoder: ' + encoder)
                        #print('Test File: ' + test_file)
                        #for key, value in mean_results.items():
                        if len(mean_results) > 0:
                            line.append(str(mean_results['Fscore'])[:6] + ' / ' + str(mean_results['Iou'])[:6])
                        else:
                            line.append('--/--')
                        #elif key == 'IoU':
                        #    line.append(str(value))
                    result_table.append(line)
            with open(test_file.replace('.json','.csv'), 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(result_table)


                        
                    
                    
