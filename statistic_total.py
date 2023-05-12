import json
import glob
from pprint import pprint
from scipy import stats

def list_diff(a, b):
    d = []
    for x, y in zip(a,b):
        #print(x,y)
        diff = x - y
        if diff == 0:
            continue
        elif diff < 0:
            diff = diff * (-1)
            d.append(diff)
        else:
            d.append(diff)
    return d

def print_list(my_list):
    size = len(my_list)
    list_str = '['
    for i in range(2):
        list_str += str(my_list[i]) + ', '
    list_str += str(my_list[2]) + ' ... '
    for i in range(2):
        list_str += str(my_list[size - 3 + i]) + ','
    list_str += str(my_list[size-1]) + ']'
    print(list_str)

datasets = ['covid19china', 'medseg', 'mosmed', 'ricord1a', 'covid20cases']
#datasets = ['mosmed']

decoders = ['unetplusplus']

encoders = ['timm-regnetx_002']

das = ['Clahe/', 'CoarseDropout/', 'ElasticTransform/', 'Emboss/', 'Flip/', 
       'GaussianBlur/', 'GridDistortion/', 'GridDropout/', 'ImageCompression/', 'MedianBlur/',
       'OpticalDistortion/', 'PiecewiseAffine/', 'Posterize/', 'RandomBrightnessContrast/', 'RandomCrop/',
       'RandomGamma/', 'RandomSnow/', 'Rotate/', 'Sharpen/', 'ShiftScaleRotate/','noda/']#, 'Stargan/', 'StarganFlip/','Stylegan/','StyleganFlip/']
#das = ['StarganNoFlip/','StyleganNoFlip/']

RUN4 = ['RUNS/das4/0p45/', 'RUNS/das4/0p5/']#, 'RUNS/das4/0p15/', 'RUNS/das4/0p2/']
RUN5 = ['RUNS/das5/0p45/', 'RUNS/das5/0p5/']#, 'RUNS/das5/0p15/', 'RUNS/das5/0p2/']

for run4, run5 in zip(RUN4, RUN5):
    print('-------------------------------------------------------------------')
    print(run4)
    print(run5)
    print('-------------------------------------------------------------------')
    for dataset in datasets:
        print('-------------------------------------------------------------------')
        print(dataset)
        print('-------------------------------------------------------------------')
        for da_i, da in enumerate(das):
            #print(da)
            runs_path4 = run4 + da + dataset + '/' + decoders[0] + '/' + encoders[0]
            runs_path5 = run5 + da + dataset + '/' + decoders[0] + '/' + encoders[0]

            runs4 = glob.glob(runs_path4 + '/*')
            runs5 = glob.glob(runs_path5 + '/*')
            
            results_runs4 = []
            for run in runs4:
                if 'graphics' not in run:
                    individual_logs_path = run + '/individual_logs_last.json'
                    #print(individual_logs_path)
                    with open(individual_logs_path) as f:
                        data = json.load(f)
                        data = data['fscores']
                        #data = [round(i*100) for i in data]
                        if len(data) == 0:
                            print('ERRO ERRO ERRO ERRO ERRO ERRO!!!!!!')
                    results_runs4.append(data)
            da_result4 = [sum(x) / len(x) for x in zip(*results_runs4)]
            da_result4 = [round(i*100) for i in da_result4]

            results_runs5 = []
            for run in runs5:
                if 'graphics' not in run:
                    individual_logs_path = run + '/individual_logs_last.json'
                    #print(individual_logs_path)
                    with open(individual_logs_path) as f:
                        data = json.load(f)
                        data = data['fscores']
                        #data = [round(i*100) for i in data]
                        if len(data) == 0:
                            print('ERRO ERRO ERRO ERRO ERRO ERRO!!!!!!')
                    results_runs5.append(data)
            da_result5 = [sum(x) / len(x) for x in zip(*results_runs5)]
            da_result5 = [round(i*100) for i in da_result5]

            wilcoxon_result = stats.wilcoxon(da_result4, da_result5,alternative='less')
            if wilcoxon_result.pvalue < 0.05:
                print(da_i+1, da)


'''
for r in RUNS:
    print()
    print(r)
    print('--------------------------------------------------------------------------------')
    for dataset in datasets:
        print()
        print('Dataset: ' + dataset)

        runs_path = r + 'noda/' + dataset + '/' + decoders[0] + '/' + encoders[0]
        #print(runs_path)
        runs = glob.glob(runs_path + '/*')
        results_runs = []
        for run in runs:
            #print(run)
            if 'graphics' not in run:
                individual_logs_path = run + '/individual_logs_last.json'
                with open(individual_logs_path) as f:
                    data = json.load(f)
                    data = data['fscores']
                    #data = [round(i*100) for i in data]
                    #print(len(data))
                    if len(data) == 0:
                        print('ERRO ERRO ERRO ERRO ERRO ERRO!!!!!!')
                results_runs.append(data)
        noda_result = [sum(x) / len(x) for x in zip(*results_runs)]
        noda_result = [round(i*100) for i in noda_result]

        da_results = []
        for da_i, da in enumerate(das):
            #print(da)
            runs_path = r + da + dataset + '/' + decoders[0] + '/' + encoders[0]
            runs = glob.glob(runs_path + '/*')
            #print(runs)
            results_runs = []
            for run in runs:
                if 'graphics' not in run:
                    individual_logs_path = run + '/individual_logs_last.json'
                    #print(individual_logs_path)
                    with open(individual_logs_path) as f:
                        data = json.load(f)
                        data = data['fscores']
                        #data = [round(i*100) for i in data]
                        if len(data) == 0:
                            print('ERRO ERRO ERRO ERRO ERRO ERRO!!!!!!')
                    results_runs.append(data)
            #print(results_runs)
            da_result = [sum(x) / len(x) for x in zip(*results_runs)]
            #print(da_result)
            da_result = [round(i*100) for i in da_result]
            #print(da_result[0:10])
            da_results.append(da_result)
            #print(len(da_results))

            #shapiro_test = stats.shapiro(da_result)
            #print(shapiro_test)
            #print(shapiro_test, format(shapiro_test.pvalue, ".60f"))
            #print('\n\n')
            #print(da)
            #diff = list_diff(noda_result, da_result)
            #print(len(diff))
            #diff = set(diff)
            #print(len(diff))
            #print(len(noda_result))
            #print(len(da_result))
            wilcoxon_result = stats.wilcoxon(noda_result, da_result,alternative='less')
            if wilcoxon_result.pvalue < 0.05:
                print(da_i + 1, da)
                #print(wilcoxon_result)
            #print()

        #print(da_results[0])
        #friedman = stats.f_oneway(da_results[0],da_results[1],da_results[2],da_results[3],da_results[4],
        #                          da_results[5], da_results[6],da_results[7],da_results[8],da_results[9],
        #                          da_results[10], da_results[11],da_results[12],da_results[13],da_results[14],
        #                          da_results[15], da_results[16],da_results[17],da_results[18],da_results[19])
        #print(friedman, format(friedman.pvalue, ".60f"))
'''
