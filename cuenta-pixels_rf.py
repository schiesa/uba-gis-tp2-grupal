import rasterio as rio
file = './images/results/rf_results_merge_mask_soja_rsp.tif'
raster = rio.open(file).read()
raster_crop = raster[raster==1]
sum_pixels = raster_crop.sum()
print("ROQUE SAENZ PEÑA")
#print("Soja")
#print(sum_pixels, " pixels")
#print(sum_pixels*0.04," Hectareas")
print("Soja ",sum_pixels, " pixels ",sum_pixels*0.04," Hectareas")


file = './images/results/rf_results_merge_mask_maiz_rsp.tif'
raster = rio.open(file).read()
raster_crop = raster[raster==1]
sum_pixels = raster_crop.sum()
#print("Maiz")
#print(sum_pixels," pixels")
#print(sum_pixels*0.04," Hectareas")
print("Maiz ",sum_pixels, " pixels ",sum_pixels*0.04," Hectareas")



print("")
file = './images/results/rf_results_merge_mask_soja_villegas.tif'
raster = rio.open(file).read()
raster_crop = raster[raster==1]
sum_pixels = raster_crop.sum()
print("GENERAL VILLEGAS")
print("Soja ",sum_pixels, " pixels ",sum_pixels*0.04," Hectareas")
#print("Soja")
#print(sum_pixels, " pixels")
#print(sum_pixels*0.04,"Hectareas")

file = './images/results/rf_results_merge_mask_maiz_villegas.tif'
raster = rio.open(file).read()
raster_crop = raster[raster==1]
sum_pixels = raster_crop.sum()
print("Maiz ",sum_pixels, " pixels ",sum_pixels*0.04," Hectareas")
#print(sum_pixels, " pixels")
#print(sum_pixels*0.04," Hectareas")

print("")
file = './images/results/rf_results_merge_mask_soja_roca.tif'
raster = rio.open(file).read()
raster_crop = raster[raster==1]
sum_pixels = raster_crop.sum()
print("GENERAL ROCA")
#print("Soja")
#print(sum_pixels, " pixels")
#print(sum_pixels*0.04," Hectareas")
print("Soja ",sum_pixels, " pixels ",sum_pixels*0.04," Hectareas")


file = './images/results/rf_results_merge_mask_maiz_roca.tif'
raster = rio.open(file).read()
raster_crop = raster[raster==1]
sum_pixels = raster_crop.sum()
#print("Maiz")
#print(sum_pixels)
#print(sum_pixels*0.04,"Hectareas")
print("Maiz ",sum_pixels, " pixels ",sum_pixels*0.04," Hectareas")
