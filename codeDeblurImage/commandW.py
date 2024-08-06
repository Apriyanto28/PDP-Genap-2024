import subprocess
import os
import glob

## Directory Location and filename image file
#file_name = "codeDeblurImage/ezgif-frame-050.jpg"

## Directory Name [source]
dir_name = "/home/apriyanto/Documents/DatasetBaru/train/images"

## Directory Result Location
res_loc = "/home/apriyanto/Documents/DatasetBaru/train-res-deconv"

# Making directory
if(not(os.path.exists(res_loc))):
    os.makedirs(res_loc)

## Filename Result
file_name_res = "result"

## Declare variabel
com = [""] * 6
com1 = [""] * 6

#com[0] = "/usr/bin/bash"
com[0] = "sudo"
com1[0] = "sudo"

i = 0
for image_file in os.listdir(dir_name):
    if(image_file.endswith(".jpg")):
        
        print(f"Proses Citra ke-{i} = {image_file}")
        
        #Estimate the kernel
        file_name = dir_name + "/" + image_file
        com[1] = "codeDeblurImage/estimate-kernel" # command estimate kernel
        com[2] = str(7) # kernel size
        com[3] = file_name # filename to process
        com[4] = res_loc + "/" + "kernel-" + str(i) + ".tif" # kernel name and location directory
        com[5] = "--no-multiscale"
        subprocess.run(com)

        ## Deblurring Image
        com1[1] = "codeDeblurImage/deconv" # command deblurring image
        com1[2] = file_name # filename to process
        com1[3] = res_loc + "/" + "kernel-" + str(i) + ".tif" # kernel name and location directory
        com1[4] = res_loc + "/" + file_name_res + "-" + str(i) + ".png" # result file
        com1[5] = "--alpha=" + str(9)
        subprocess.run(com1)
        
        i = i + 1

## Untuk pengujian
'''
## run the iteration
for i in range(1, 51, 2):
    ## example command
    ## ./estimate-kernel 15 hollywood.jpg kernel.tif
    ## ./deconv hollywood.jpg kernel.tif deblurred.png
    
    print(f"Proses lambda-{i}")

    ## Estimate Kernel
    com[1] = "codeDeblurImage/estimate-kernel" # command estimate kernel
    com[2] = str(7) # kernel size
    com[3] = file_name # filename to process
    com[4] = res_loc + "/" + "kernel.tif" # kernel name and location directory
    com[5] = "--no-multiscale"
    

    # run the command
    subprocess.run(com)

    ## Deblurring Image
    com1[1] = "codeDeblurImage/deconv" # command deblurring image
    com1[2] = file_name # filename to process
    com1[3] = res_loc + "/" + "kernel.tif" # kernel name and location directory
    com1[4] = res_loc + "/" + file_name_res + "-" + str(i) + ".png" # result file
    com1[5] = "--alpha=" + str(i)

    # run the command
    subprocess.run(com1)
'''