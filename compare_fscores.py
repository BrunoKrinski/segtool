import json
import glob

probs = ['0p05/', '0p1/', '0p15/', '0p2/']
probs = ['0p15/']
das = ['Stargan/','StarganFlip/','Stylegan/','StyleganFlip/']
#das = ['Stargan/']

ids_path = 'datasets/ricord1a/valid/test_ids.txt'
ids_file = open(ids_path)
ids = ids_file.readlines()

for p in probs:
    print(p)
    noda_path = 'RUNS/das4/' + p + 'noda/ricord1a/unetplusplus/timm-regnetx_002/*' 

    runs_noda = glob.glob(noda_path)
    runs_noda.sort()

    for da in das:
        print(da)     
        gan_path = 'RUNS/das4/' + p + da + '/ricord1a/unetplusplus/timm-regnetx_002/*'
        runs_gan = glob.glob(gan_path)
        runs_gan.sort()

        for fold_n, fold_g in zip(runs_noda, runs_gan):
            #print(fold_n)
            #print(fold_g)
            noda_fscores_file_path = fold_n + '/individual_logs_last.json'
            gan_fscores_file_path = fold_g + '/individual_logs_last.json'

            noda_fscores_file = open(noda_fscores_file_path)
            noda_fscores = json.load(noda_fscores_file)
            noda_fscores = noda_fscores['fscores']
            
            gan_fscores_file = open(gan_fscores_file_path)
            gan_fscores = json.load(gan_fscores_file)
            gan_fscores = gan_fscores['fscores']

            differences = []
            indexes = []
            for i, (n_fscore, g_fscore) in enumerate(zip(noda_fscores, gan_fscores)):
                if g_fscore > n_fscore:
                    difference = g_fscore - n_fscore
                    if difference*100 > 10:
                        differences.append(difference)
                        indexes.append(ids[i])

            zipped_lists = zip(differences, indexes)
            sorted_pairs = sorted(zipped_lists)

            tuples = zip(*sorted_pairs)
            differences, indexes = [ list(tuple) for tuple in  tuples]
                        
            for d, i in zip(differences, indexes):
                if 'fold0' in fold_n and '007778.jpg' in i:
                    print(d, i)
            print('--------------------------------------------------------------')
        
                    
#005090.jpg fold1
#004431.jpg 0.15

