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
#datasets = ['ricord1a']

decoders = ['unetplusplus']

encoders = ['timm-regnetx_002']

das = ['Clahe/', 'CoarseDropout/', 'ElasticTransform/', 'Emboss/', 'Flip/', 
       'GaussianBlur/', 'GridDistortion/', 'GridDropout/', 'ImageCompression/', 'MedianBlur/',
       'OpticalDistortion/', 'PiecewiseAffine/', 'Posterize/', 'RandomBrightnessContrast/', 'RandomCrop/',
       'RandomGamma/', 'RandomSnow/', 'Rotate/', 'Sharpen/', 'ShiftScaleRotate/']

RUNS = ['RUNS/0p1_50elr3/','RUNS/0p2_50elr3/','RUNS/0p1_100elr3/','RUNS/0p2_100elr3/','RUNS/0p1_100elr4/','RUNS/0p2_100elr4/']
RUNS = ['RUNS/0p2_100elr4/']

for r in RUNS:
    print()
    print(r)
    print('--------------------------------------------------------------------------------')
    for dataset in datasets:
        print()
        print('Dataset: ' + dataset)

        runs_path = r + 'noda/' + dataset + '/' + decoders[0] + '/' + encoders[0]
        runs = glob.glob(runs_path + '/*')
        results_runs = []
        for run in runs:
            if 'graphics' not in run:
                individual_logs_path = run + '/individual_logs_last.json'
                with open(individual_logs_path) as f:
                    data = json.load(f)
                    data = data['fscores']
                    #data = [round(i*100) for i in data]
                    #print(data)
                    if len(data) == 0:
                        print('ERRO ERRO ERRO ERRO ERRO ERRO!!!!!!')
                results_runs.append(data)
        noda_result = [sum(x) / len(x) for x in zip(*results_runs)]
        noda_result = [round(i*100) for i in noda_result]

        da_results = []
        for da in das:
            #print(da)
            runs_path = r + da + dataset + '/' + decoders[0] + '/' + encoders[0]
            runs = glob.glob(runs_path + '/*')
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
            
            wilcoxon_result = stats.wilcoxon(noda_result, da_result,alternative='less')
            if wilcoxon_result.pvalue < 0.05:
                print(da)
                #print(wilcoxon_result)
            #print()

        #print(da_results[0])
        friedman = stats.f_oneway(da_results[0],da_results[1],da_results[2],da_results[3],da_results[4],
                                  da_results[5], da_results[6],da_results[7],da_results[8],da_results[9],
                                  da_results[10], da_results[11],da_results[12],da_results[13],da_results[14],
                                  da_results[15], da_results[16],da_results[17],da_results[18],da_results[19])
        print(friedman, format(friedman.pvalue, ".60f"))

'''
final_result = []
for decoder in decoders:
    print(decoder)
    decoder_list = []
    decoder_result = []

    for encoder in encoders:
        print(encoder)
        encoder_result = []

        for dataset in datasets:
            #print(dataset)
            
            runs_path = RUNS + dataset + '/' + decoder + '/' + encoder
            runs = glob.glob(runs_path + '/*')
            results_runs = []
            for run in runs:
                if 'graphics' not in run:
                    individual_logs_path = run + '/individual_logs_last.json'
                    with open(individual_logs_path) as f:
                        data = json.load(f)
                        data = data['fscores']
                        #data = [round(i, 3) for i in data]
                        #print(data)
                        if len(data) == 0:
                            print('ERRO ERRO ERRO ERRO ERRO ERRO!!!!!!')
                    results_runs.append(data)
            print(len(results_runs))
            dataset_result = [sum(x) / len(x) for x in zip(*results_runs)]
            print(len(dataset_result))
            dataset_result = [round(i, 2) for i in dataset_result]

            #print('Mean for dataset:')
            #print_list(dataset_result)

            encoder_result.extend(dataset_result)
        
        #print('Encoder result:')
        #print_list(encoder_result)
        #print('Size: ' + str(len(encoder_result)))

        shapiro_test = stats.shapiro(encoder_result)
        #print(shapiro_test)
        #print(shapiro_test, format(shapiro_test.pvalue, ".60f"))
        #print('\n\n')
        
        decoder_list.append(encoder_result)
        #print('Decoder list: ' + str(len(decoder_list)))
    
    #### Fazer comparação de encoders para decoder
    friedman = stats.f_oneway(decoder_list[0],decoder_list[1],decoder_list[2],decoder_list[3],decoder_list[4],
                                       decoder_list[5], decoder_list[6],decoder_list[7],decoder_list[8],decoder_list[9],
                                       decoder_list[10], decoder_list[11],decoder_list[12],decoder_list[13],decoder_list[14],
                                       decoder_list[15], decoder_list[16],decoder_list[17],decoder_list[18],decoder_list[19])
    #print(decoder_list[0])
    #print(decoder_list[1])
    #print(decoder_list[2])
    #print(decoder_list[3])
    #friedman = stats.f_oneway(decoder_list[0],decoder_list[1],decoder_list[2],decoder_list[3],decoder_list[4])

    print('----------------------------------------------')
    print('Decoder:' + decoder)
    print('Encoder comparison: ')                                   
    print(friedman, format(friedman.pvalue, ".60f"))
    print('----------------------------------------------')
    print('\n\n')

    #----------------
    for item in decoder_list:
        decoder_result.extend(item)
    final_result.append(decoder_result)
    #print('Final result: ' + str(len(final_result)))

#### Fazer comparação de decoders
friedman = stats.f_oneway(final_result[0],final_result[1],final_result[2],final_result[3],final_result[4], final_result[5])

print('----------------------------------------------')
print('Decoder comparison: ')
print(friedman)
print('----------------------------------------------')
print('\n\n')
'''
