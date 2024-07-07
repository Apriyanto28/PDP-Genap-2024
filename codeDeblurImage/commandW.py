import subprocess
import os

## Change directory to the directory file
os.system("pwd")

## Directory Location and filename image file
file_name = "codeDeblurImage/ezgif-frame-050.jpg"

## Directory Result Location
res_loc = "hasil-lambda"

# Making directory
#os.makedirs(res_loc)

## Filename Result
file_name_res = "result"

## Declare variabel
com = [""] * 6
com1 = [""] * 5

#com[0] = "/usr/bin/bash"
com[0] = "sudo"
com1[0] = "sudo"

## run the iteration
for i in range(1, 21):
    ## example command
    ## ./estimate-kernel 15 hollywood.jpg kernel.tif
    ## ./deconv hollywood.jpg kernel.tif deblurred.png
    
    print(f"Proses lambda-{i}")

    ## Estimate Kernel
    com[1] = "codeDeblurImage/estimate-kernel" # command estimate kernel
    com[2] = str(11) # kernel size
    com[3] = file_name # filename to process
    com[4] = res_loc + "/" + "kernel.tif" # kernel name and location directory
    com[5] = "--lambda-ratio=" + str(i * 10 ** (-3))
    

    # run the command
    subprocess.run(com)

    ## Deblurring Image
    com1[1] = "codeDeblurImage/deconv" # command deblurring image
    com1[2] = file_name # filename to process
    com1[3] = res_loc + "/" + "kernel.tif" # kernel name and location directory
    com1[4] = res_loc + "/" + file_name_res + "-" + str(i) + ".png" # result file

    # run the command
    subprocess.run(com1)