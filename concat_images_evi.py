import subprocess
import glob
import os

#movi la carpeta de enero de lugar y ahora corro este script.

tile = '0000000000-0000000000'
images_ndvi = sorted(glob.glob(
    './images/aoi/**/{tile}_evi.tif'.format(tile=tile)))
images_ndvi_otb = ' '.join(images_ndvi)
im_out_fname = './images/results/{tile}_evi_plus.tif'.format(
    tile=tile)
cmd = """bash -c 'source ~/OTB-7.2.0-Linux64/otbenv.profile;  otbcli_ConcatenateImages -il {im} -out {im_out}'""".format(
    im=images_ndvi_otb, im_out=im_out_fname)
print(cmd)
#subprocess.run(cmd, shell=True)



print("Ahora conectanamos la segunda midad del area")
tile = '0000000000-0000010496'
images_ndvi = sorted(glob.glob(
    './images/aoi/**/{tile}_evi.tif'.format(tile=tile)))
images_ndvi_otb = ' '.join(images_ndvi)
im_out_fname = './images/results/{tile}_evi_plus.tif'.format(
    tile=tile)
cmd = """bash -c 'source ~/OTB-7.2.0-Linux64/otbenv.profile;  otbcli_ConcatenateImages -il {im} -out {im_out}'""".format(
    im=images_ndvi_otb, im_out=im_out_fname)
print(cmd)
subprocess.run(cmd, shell=True)


#bash -c 'source ~/OTB-7.2.0-Linux64/otbenv.profile;  otbcli_ConcatenateImages -il ./images/aoi/2020-10-01/0000000000-0000000000_evi.tif ./images/aoi/2020-11-01/0000000000-0000000000_evi.tif ./images/aoi/2020-12-01/0000000000-0000000000_evi.tif ./images/aoi/2021-01-01/0000000000-0000000000_evi.tif ./images/aoi/2021-02-20/0000000000-0000000000_evi.tif ./images/aoi/2021-03-17/0000000000-0000000000_evi.tif -out ./images/aoi/results/0000000000-0000000000_evi.tif'
#bash -c 'source ~/OTB-7.2.0-Linux64/otbenv.profile;  otbcli_ConcatenateImages -il ./images/aoi/2020-10-01/0000000000-0000000000_evi.tif ./images/aoi/2020-11-01/0000000000-0000000000_evi.tif ./images/aoi/2020-12-01/0000000000-0000000000_evi.tif ./images/aoi/2021-02-20/0000000000-0000000000_evi.tif ./images/aoi/2021-03-17/0000000000-0000000000_evi.tif -out ./images/results/0000000000-0000000000_evi_plus.tif'
#Ahora conectanamos la segunda midad del area
#bash -c 'source ~/OTB-7.2.0-Linux64/otbenv.profile;  otbcli_ConcatenateImages -il ./images/aoi/2020-10-01/0000000000-0000010496_evi.tif ./images/aoi/2020-11-01/0000000000-0000010496_evi.tif ./images/aoi/2020-12-01/0000000000-0000010496_evi.tif ./images/aoi/2021-02-20/0000000000-0000010496_evi.tif ./images/aoi/2021-03-17/0000000000-0000010496_evi.tif -out ./images/results/0000000000-0000010496_evi_plus.tif'
#https://drive.google.com/file/d/1DRF2AjbkkY1YtxQH4wpx4xxZQ9qZ_xMx/view?usp=sharing
