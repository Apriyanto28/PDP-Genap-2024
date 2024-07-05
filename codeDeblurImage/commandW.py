import subprocess
import os

## Folder Location and filename image file
file_name = "ezgif-frame-050.jpg"

## Folder Result Location
res_loc = "hasil"
os.makedirs(res_loc)

## Filename Result
file_name_res = "result"

## Declare variabel
com = [""] * 4

## run the iteration
for i in range(2, 21):
    ## example command
    ## ./estimate-kernel 15 hollywood.jpg kernel.tif
    ## ./deconv hollywood.jpg kernel.tif deblurred.png
    
    ## Estimate Kernel
    com[0] = "./estimate-kernel" # command estimate kernel
    com[1] = str(i) # kernel size
    com[2] = file_name # filename to process
    com[3] = "kernel.tif" # kernel name

    # run the command
    subprocess.run(com)

    ## Estimate Kernel
    com[0] = "\\estimate-kernel" # command estimate kernel
    com[1] = str(i) # kernel size
    com[2] = file_name # filename to process
    com[3] = res_loc + "\\kernel.tif" # kernel name

    # run the command
    subprocess.run(com)