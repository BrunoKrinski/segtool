import os
import cv2
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required='true')
    parser.add_argument('--run', type=str, required='true')
    args = parser.parse_args()

    run_path = 'RUNS/{}/'.format(args.run)
    run_images = run_path + 'segmented_images/'
    run_despatched = run_path + 'despatched/'

    if os.path.isdir(run_despatched):
        os.system('rm -rf {}'.format(run_despatched))

    os.mkdir(run_despatched)

    dataset_despatch_file = 'datasets/{}/valid/patched.txt'.format(args.dataset)

    with open(dataset_despatch_file, 'r') as despatch_file:
        despatch = despatch_file.read().splitlines()

    despatch_file_size = len(despatch)

    i = 0
    while i < len(despatch):
        if 'begin_image' in despatch[i]:
            i += 1
            full_image_name = despatch[i]
            print('Image name: ' + full_image_name)
            i += 1
            height, width = despatch[i].split(' ')
            print('Height, Width: {} {}'.format(height, width))
            i += 1
            #print(despatch[i])
            image_path, mask_path = despatch[i].split(' ')
            image_name = image_path.split('/')[-1]
            run_image = run_images + '/' + image_name
            image1 = cv2.imread(run_image)
            i += 1
            while despatch[i] != 'end_line':
                #print(despatch[i])
                image_path, mask_path = despatch[i].split(' ')
                image_name = image_path.split('/')[-1]
                run_image = run_images + '/' + image_name
                image2 = cv2.imread(run_image)
                image1 = cv2.hconcat([image1, image2])
                i += 1
            image_a = image1
            i += 1
            while despatch[i] != 'end_image':
                #print(despatch[i])
                image_path, mask_path = despatch[i].split(' ')
                image_name = image_path.split('/')[-1]
                run_image = run_images + '/' + image_name
                image1 = cv2.imread(run_image)
                i += 1
                while despatch[i] != 'end_line':
                    #print(despatch[i])
                    image_path, mask_path = despatch[i].split(' ')
                    image_name = image_path.split('/')[-1]
                    run_image = run_images + '/' + image_name
                    image2 = cv2.imread(run_image)
                    image1 = cv2.hconcat([image1, image2])
                    i += 1
                image_b = image1
                image_a = cv2.vconcat([image_a, image_b])
                i += 1
            image_despatched_path = run_despatched + '/' + full_image_name + '.jpg'
            cv2.imwrite(image_despatched_path, image_a)
            i += 1