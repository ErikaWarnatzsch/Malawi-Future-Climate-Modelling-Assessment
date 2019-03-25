"""
Created on Monday 21 May 2018

@author: s0899345
"""

import matplotlib.pyplot as plt
import iris
import iris.coord_categorisation as iriscc
import iris.plot as iplt
import iris.analysis.cartography
import numpy as np
import calendar

#this file is split into parts as follows:
    #PART 1: load and format all future models
    #PART 2: format files general
    #PART 3: format files to be plot specific for monthly plotting 
    #PART 4: plot monthly data
    #PART 5: format files to be plot specific for yearly plotting
    #PART 6: plot yearly data
    
    
def main():
  
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT ALL FUTURE MODELS   
    CCCmaCanRCM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc' 
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MPIREMO85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc' 
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_Evo/evspsbl_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'  
    
    #Load exactly one cube from given file
    CCCmaCanRCM = iris.load_cube(CCCmaCanRCM)
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRM = iris.load_cube(CNRM)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    ICHECDMI = iris.load_cube(ICHECDMI, 'water_evaporation_flux')
    ICHECCCLM = iris.load_cube(ICHECCCLM)
    ICHECKNMI = iris.load_cube(ICHECKNMI)
    ICHECMPI = iris.load_cube(ICHECMPI)
    ICHECSMHI = iris.load_cube(ICHECSMHI)
    IPSL = iris.load_cube(IPSL)
    MIROC = iris.load_cube(MIROC)
    MOHCCCLM = iris.load_cube(MOHCCCLM)
    MOHCKNMI = iris.load_cube(MOHCKNMI)
    MOHCSMHI = iris.load_cube(MOHCSMHI)
    MPICCLM = iris.load_cube(MPICCLM)
    MPIREMO = iris.load_cube(MPIREMO)
    MPISMHI = iris.load_cube(MPISMHI)
    NCCSMHI = iris.load_cube(NCCSMHI)
    NOAA = iris.load_cube(NOAA)
    
    CCCmaCanRCM85 = iris.load_cube(CCCmaCanRCM85)
    CCCmaSMHI85 = iris.load_cube(CCCmaSMHI85)
    CNRM85 = iris.load_cube(CNRM85)
    CNRMSMHI85 = iris.load_cube(CNRMSMHI85)
    CSIRO85 = iris.load_cube(CSIRO85)
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'water_evaporation_flux')
    ICHECCCLM85 = iris.load_cube(ICHECCCLM85)
    ICHECKNMI85 = iris.load_cube(ICHECKNMI85)
    ICHECMPI85 = iris.load_cube(ICHECMPI85)
    ICHECSMHI85 = iris.load_cube(ICHECSMHI85)
    IPSL85 = iris.load_cube(IPSL85)
    MIROC85 = iris.load_cube(MIROC85)
    MOHCCCLM85 = iris.load_cube(MOHCCCLM85)
    MOHCKNMI85 = iris.load_cube(MOHCKNMI85)
    MOHCSMHI85 = iris.load_cube(MOHCSMHI85)
    MPICCLM85 = iris.load_cube(MPICCLM85)
    MPIREMO85 = iris.load_cube(MPIREMO85)
    MPISMHI85 = iris.load_cube(MPISMHI85)
    NCCSMHI85 = iris.load_cube(NCCSMHI85)
    NOAA85 = iris.load_cube(NOAA85)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(CCCmaCanRCM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM.remove_coord('latitude')
    CCCmaCanRCM.remove_coord('longitude')
    CCCmaCanRCM.remove_coord('grid_latitude')
    CCCmaCanRCM.remove_coord('grid_longitude')
    CCCmaCanRCM.add_dim_coord(lats, 1)
    CCCmaCanRCM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI.remove_coord('latitude')
    CCCmaSMHI.remove_coord('longitude')
    CCCmaSMHI.remove_coord('grid_latitude')
    CCCmaSMHI.remove_coord('grid_longitude')
    CCCmaSMHI.add_dim_coord(lats, 1)
    CCCmaSMHI.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM.remove_coord('latitude')
    CNRM.remove_coord('longitude')
    CNRM.remove_coord('grid_latitude')
    CNRM.remove_coord('grid_longitude')
    CNRM.add_dim_coord(lats, 1)
    CNRM.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI.remove_coord('latitude')
    CNRMSMHI.remove_coord('longitude')
    CNRMSMHI.remove_coord('grid_latitude')
    CNRMSMHI.remove_coord('grid_longitude')
    CNRMSMHI.add_dim_coord(lats, 1)
    CNRMSMHI.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO.remove_coord('latitude')
    CSIRO.remove_coord('longitude')
    CSIRO.remove_coord('grid_latitude')
    CSIRO.remove_coord('grid_longitude')
    CSIRO.add_dim_coord(lats, 1)
    CSIRO.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI.remove_coord('latitude')
    ICHECDMI.remove_coord('longitude')
    ICHECDMI.remove_coord('grid_latitude')
    ICHECDMI.remove_coord('grid_longitude')
    ICHECDMI.add_dim_coord(lats, 1)
    ICHECDMI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM.remove_coord('latitude')
    ICHECCCLM.remove_coord('longitude')
    ICHECCCLM.remove_coord('grid_latitude')
    ICHECCCLM.remove_coord('grid_longitude')
    ICHECCCLM.add_dim_coord(lats, 1)
    ICHECCCLM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI.remove_coord('latitude')
    ICHECKNMI.remove_coord('longitude')
    ICHECKNMI.remove_coord('grid_latitude')
    ICHECKNMI.remove_coord('grid_longitude')
    ICHECKNMI.add_dim_coord(lats, 1)
    ICHECKNMI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI.remove_coord('latitude')
    ICHECMPI.remove_coord('longitude')
    ICHECMPI.remove_coord('grid_latitude')
    ICHECMPI.remove_coord('grid_longitude')
    ICHECMPI.add_dim_coord(lats, 1)
    ICHECMPI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI.remove_coord('latitude')
    ICHECSMHI.remove_coord('longitude')
    ICHECSMHI.remove_coord('grid_latitude')
    ICHECSMHI.remove_coord('grid_longitude')
    ICHECSMHI.add_dim_coord(lats, 1)
    ICHECSMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL.remove_coord('latitude')
    IPSL.remove_coord('longitude')
    IPSL.remove_coord('grid_latitude')
    IPSL.remove_coord('grid_longitude')
    IPSL.add_dim_coord(lats, 1)
    IPSL.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC.remove_coord('latitude')
    MIROC.remove_coord('longitude')
    MIROC.remove_coord('grid_latitude')
    MIROC.remove_coord('grid_longitude')
    MIROC.add_dim_coord(lats, 1)
    MIROC.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM.remove_coord('latitude')
    MOHCCCLM.remove_coord('longitude')
    MOHCCCLM.remove_coord('grid_latitude')
    MOHCCCLM.remove_coord('grid_longitude')
    MOHCCCLM.add_dim_coord(lats, 1)
    MOHCCCLM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI.remove_coord('latitude')
    MOHCKNMI.remove_coord('longitude')
    MOHCKNMI.remove_coord('grid_latitude')
    MOHCKNMI.remove_coord('grid_longitude')
    MOHCKNMI.add_dim_coord(lats, 1)
    MOHCKNMI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI.remove_coord('latitude')
    MOHCSMHI.remove_coord('longitude')
    MOHCSMHI.remove_coord('grid_latitude')
    MOHCSMHI.remove_coord('grid_longitude')
    MOHCSMHI.add_dim_coord(lats, 1)
    MOHCSMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM.remove_coord('latitude')
    MPICCLM.remove_coord('longitude')
    MPICCLM.remove_coord('grid_latitude')
    MPICCLM.remove_coord('grid_longitude')
    MPICCLM.add_dim_coord(lats, 1)
    MPICCLM.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO.remove_coord('latitude')
    MPIREMO.remove_coord('longitude')
    MPIREMO.remove_coord('grid_latitude')
    MPIREMO.remove_coord('grid_longitude')
    MPIREMO.add_dim_coord(lats, 1)
    MPIREMO.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI.remove_coord('latitude')
    MPISMHI.remove_coord('longitude')
    MPISMHI.remove_coord('grid_latitude')
    MPISMHI.remove_coord('grid_longitude')
    MPISMHI.add_dim_coord(lats, 1)
    MPISMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI.remove_coord('latitude')
    NCCSMHI.remove_coord('longitude')
    NCCSMHI.remove_coord('grid_latitude')
    NCCSMHI.remove_coord('grid_longitude')
    NCCSMHI.add_dim_coord(lats, 1)
    NCCSMHI.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NOAA.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA.remove_coord('latitude')
    NOAA.remove_coord('longitude')
    NOAA.remove_coord('grid_latitude')
    NOAA.remove_coord('grid_longitude')
    NOAA.add_dim_coord(lats, 1)
    NOAA.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaCanRCM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM85.remove_coord('latitude')
    CCCmaCanRCM85.remove_coord('longitude')
    CCCmaCanRCM85.remove_coord('grid_latitude')
    CCCmaCanRCM85.remove_coord('grid_longitude')
    CCCmaCanRCM85.add_dim_coord(lats, 1)
    CCCmaCanRCM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI85.remove_coord('latitude')
    CCCmaSMHI85.remove_coord('longitude')
    CCCmaSMHI85.remove_coord('grid_latitude')
    CCCmaSMHI85.remove_coord('grid_longitude')
    CCCmaSMHI85.add_dim_coord(lats, 1)
    CCCmaSMHI85.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM85.remove_coord('latitude')
    CNRM85.remove_coord('longitude')
    CNRM85.remove_coord('grid_latitude')
    CNRM85.remove_coord('grid_longitude')
    CNRM85.add_dim_coord(lats, 1)
    CNRM85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI85.remove_coord('latitude')
    CNRMSMHI85.remove_coord('longitude')
    CNRMSMHI85.remove_coord('grid_latitude')
    CNRMSMHI85.remove_coord('grid_longitude')
    CNRMSMHI85.add_dim_coord(lats, 1)
    CNRMSMHI85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO85.remove_coord('latitude')
    CSIRO85.remove_coord('longitude')
    CSIRO85.remove_coord('grid_latitude')
    CSIRO85.remove_coord('grid_longitude')
    CSIRO85.add_dim_coord(lats, 1)
    CSIRO85.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI85.remove_coord('latitude')
    ICHECDMI85.remove_coord('longitude')
    ICHECDMI85.remove_coord('grid_latitude')
    ICHECDMI85.remove_coord('grid_longitude')
    ICHECDMI85.add_dim_coord(lats, 1)
    ICHECDMI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM85.remove_coord('latitude')
    ICHECCCLM85.remove_coord('longitude')
    ICHECCCLM85.remove_coord('grid_latitude')
    ICHECCCLM85.remove_coord('grid_longitude')
    ICHECCCLM85.add_dim_coord(lats, 1)
    ICHECCCLM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI85.remove_coord('latitude')
    ICHECKNMI85.remove_coord('longitude')
    ICHECKNMI85.remove_coord('grid_latitude')
    ICHECKNMI85.remove_coord('grid_longitude')
    ICHECKNMI85.add_dim_coord(lats, 1)
    ICHECKNMI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI85.remove_coord('latitude')
    ICHECMPI85.remove_coord('longitude')
    ICHECMPI85.remove_coord('grid_latitude')
    ICHECMPI85.remove_coord('grid_longitude')
    ICHECMPI85.add_dim_coord(lats, 1)
    ICHECMPI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI85.remove_coord('latitude')
    ICHECSMHI85.remove_coord('longitude')
    ICHECSMHI85.remove_coord('grid_latitude')
    ICHECSMHI85.remove_coord('grid_longitude')
    ICHECSMHI85.add_dim_coord(lats, 1)
    ICHECSMHI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL85.remove_coord('latitude')
    IPSL85.remove_coord('longitude')
    IPSL85.remove_coord('grid_latitude')
    IPSL85.remove_coord('grid_longitude')
    IPSL85.add_dim_coord(lats, 1)
    IPSL85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC85.remove_coord('latitude')
    MIROC85.remove_coord('longitude')
    MIROC85.remove_coord('grid_latitude')
    MIROC85.remove_coord('grid_longitude')
    MIROC85.add_dim_coord(lats, 1)
    MIROC85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM85.remove_coord('latitude')
    MOHCCCLM85.remove_coord('longitude')
    MOHCCCLM85.remove_coord('grid_latitude')
    MOHCCCLM85.remove_coord('grid_longitude')
    MOHCCCLM85.add_dim_coord(lats, 1)
    MOHCCCLM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI85.remove_coord('latitude')
    MOHCKNMI85.remove_coord('longitude')
    MOHCKNMI85.remove_coord('grid_latitude')
    MOHCKNMI85.remove_coord('grid_longitude')
    MOHCKNMI85.add_dim_coord(lats, 1)
    MOHCKNMI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI85.remove_coord('latitude')
    MOHCSMHI85.remove_coord('longitude')
    MOHCSMHI85.remove_coord('grid_latitude')
    MOHCSMHI85.remove_coord('grid_longitude')
    MOHCSMHI85.add_dim_coord(lats, 1)
    MOHCSMHI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM85.remove_coord('latitude')
    MPICCLM85.remove_coord('longitude')
    MPICCLM85.remove_coord('grid_latitude')
    MPICCLM85.remove_coord('grid_longitude')
    MPICCLM85.add_dim_coord(lats, 1)
    MPICCLM85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO85.remove_coord('latitude')
    MPIREMO85.remove_coord('longitude')
    MPIREMO85.remove_coord('grid_latitude')
    MPIREMO85.remove_coord('grid_longitude')
    MPIREMO85.add_dim_coord(lats, 1)
    MPIREMO85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI85.remove_coord('latitude')
    MPISMHI85.remove_coord('longitude')
    MPISMHI85.remove_coord('grid_latitude')
    MPISMHI85.remove_coord('grid_longitude')
    MPISMHI85.add_dim_coord(lats, 1)
    MPISMHI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI85.remove_coord('latitude')
    NCCSMHI85.remove_coord('longitude')
    NCCSMHI85.remove_coord('grid_latitude')
    NCCSMHI85.remove_coord('grid_longitude')
    NCCSMHI85.add_dim_coord(lats, 1)
    NCCSMHI85.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA85.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NOAA85.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA85.remove_coord('latitude')
    NOAA85.remove_coord('longitude')
    NOAA85.remove_coord('grid_latitude')
    NOAA85.remove_coord('grid_longitude')
    NOAA85.add_dim_coord(lats, 1)
    NOAA85.add_dim_coord(lons, 2)
    
    #guess bounds    
    CCCmaCanRCM.coord('latitude').guess_bounds()
    CCCmaSMHI.coord('latitude').guess_bounds()
    CNRM.coord('latitude').guess_bounds()
    CNRMSMHI.coord('latitude').guess_bounds()
    CSIRO.coord('latitude').guess_bounds()
    ICHECDMI.coord('latitude').guess_bounds()
    ICHECCCLM.coord('latitude').guess_bounds()
    ICHECKNMI.coord('latitude').guess_bounds()
    ICHECMPI.coord('latitude').guess_bounds()
    ICHECSMHI.coord('latitude').guess_bounds()
    IPSL.coord('latitude').guess_bounds()
    MIROC.coord('latitude').guess_bounds()
    MOHCCCLM.coord('latitude').guess_bounds()
    MOHCKNMI.coord('latitude').guess_bounds() 
    MOHCSMHI.coord('latitude').guess_bounds()
    MPICCLM.coord('latitude').guess_bounds()
    MPIREMO.coord('latitude').guess_bounds()
    MPISMHI.coord('latitude').guess_bounds()
    NCCSMHI.coord('latitude').guess_bounds()
    NOAA.coord('latitude').guess_bounds()
    
    CCCmaCanRCM85.coord('latitude').guess_bounds()
    CCCmaSMHI85.coord('latitude').guess_bounds()
    CNRM85.coord('latitude').guess_bounds()
    CNRMSMHI85.coord('latitude').guess_bounds()
    CSIRO85.coord('latitude').guess_bounds()
    ICHECDMI85.coord('latitude').guess_bounds()
    ICHECCCLM85.coord('latitude').guess_bounds()
    ICHECKNMI85.coord('latitude').guess_bounds()
    ICHECMPI85.coord('latitude').guess_bounds()
    ICHECSMHI85.coord('latitude').guess_bounds()
    IPSL85.coord('latitude').guess_bounds()
    MIROC85.coord('latitude').guess_bounds()
    MOHCCCLM85.coord('latitude').guess_bounds()
    MOHCKNMI85.coord('latitude').guess_bounds() 
    MOHCSMHI85.coord('latitude').guess_bounds()
    MPICCLM85.coord('latitude').guess_bounds()
    MPIREMO85.coord('latitude').guess_bounds()
    MPISMHI85.coord('latitude').guess_bounds()
    NCCSMHI85.coord('latitude').guess_bounds()
    NOAA85.coord('latitude').guess_bounds()
    
    CCCmaCanRCM.coord('longitude').guess_bounds()
    CCCmaSMHI.coord('longitude').guess_bounds()
    CNRM.coord('longitude').guess_bounds()
    CNRMSMHI.coord('longitude').guess_bounds()
    CSIRO.coord('longitude').guess_bounds()
    ICHECDMI.coord('longitude').guess_bounds()
    ICHECCCLM.coord('longitude').guess_bounds()
    ICHECKNMI.coord('longitude').guess_bounds()
    ICHECMPI.coord('longitude').guess_bounds()
    ICHECSMHI.coord('longitude').guess_bounds()
    IPSL.coord('longitude').guess_bounds()
    MIROC.coord('longitude').guess_bounds()
    MOHCCCLM.coord('longitude').guess_bounds()
    MOHCKNMI.coord('longitude').guess_bounds() 
    MOHCSMHI.coord('longitude').guess_bounds()
    MPICCLM.coord('longitude').guess_bounds()
    MPIREMO.coord('longitude').guess_bounds()
    MPISMHI.coord('longitude').guess_bounds()
    NCCSMHI.coord('longitude').guess_bounds()
    NOAA.coord('longitude').guess_bounds()
    
    CCCmaCanRCM85.coord('longitude').guess_bounds()
    CCCmaSMHI85.coord('longitude').guess_bounds()
    CNRM85.coord('longitude').guess_bounds()
    CNRMSMHI85.coord('longitude').guess_bounds()
    CSIRO85.coord('longitude').guess_bounds()
    ICHECDMI85.coord('longitude').guess_bounds()
    ICHECCCLM85.coord('longitude').guess_bounds()
    ICHECKNMI85.coord('longitude').guess_bounds()
    ICHECMPI85.coord('longitude').guess_bounds()
    ICHECSMHI85.coord('longitude').guess_bounds()
    IPSL85.coord('longitude').guess_bounds()
    MIROC85.coord('longitude').guess_bounds()
    MOHCCCLM85.coord('longitude').guess_bounds()
    MOHCKNMI85.coord('longitude').guess_bounds() 
    MOHCSMHI85.coord('longitude').guess_bounds()
    MPICCLM85.coord('longitude').guess_bounds()
    MPIREMO85.coord('longitude').guess_bounds()
    MPISMHI85.coord('longitude').guess_bounds()
    NCCSMHI85.coord('longitude').guess_bounds()
    NOAA85.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 2: FORMAT DATA GENERAL
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -12)         
    
    CCCmaCanRCM = CCCmaCanRCM.extract(Central_Malawi)
    CCCmaSMHI = CCCmaSMHI.extract(Central_Malawi)
    CNRM =CNRM.extract(Central_Malawi)
    CNRMSMHI =CNRMSMHI.extract(Central_Malawi)
    CSIRO=CSIRO.extract(Central_Malawi)
    ICHECDMI=ICHECDMI.extract(Central_Malawi)
    ICHECCCLM=ICHECCCLM.extract(Central_Malawi)
    ICHECKNMI=ICHECKNMI.extract(Central_Malawi)
    ICHECMPI=ICHECMPI.extract(Central_Malawi)
    ICHECSMHI=ICHECSMHI.extract(Central_Malawi)
    IPSL=IPSL.extract(Central_Malawi)
    MIROC=MIROC.extract(Central_Malawi)
    MOHCCCLM=MOHCCCLM.extract(Central_Malawi)
    MOHCKNMI=MOHCKNMI.extract(Central_Malawi)
    MOHCSMHI=MOHCSMHI.extract(Central_Malawi)
    MPICCLM=MPICCLM.extract(Central_Malawi)
    MPIREMO=MPIREMO.extract(Central_Malawi)
    MPISMHI=MPISMHI.extract(Central_Malawi)
    NCCSMHI=NCCSMHI.extract(Central_Malawi)
    NOAA=NOAA.extract(Central_Malawi)
    
    CCCmaCanRCM85 = CCCmaCanRCM85.extract(Central_Malawi)
    CCCmaSMHI85 = CCCmaSMHI85.extract(Central_Malawi)
    CNRM85 = CNRM85.extract(Central_Malawi)
    CNRMSMHI85 = CNRMSMHI85.extract(Central_Malawi)
    CSIRO85 = CSIRO85.extract(Central_Malawi)
    ICHECDMI85 = ICHECDMI85.extract(Central_Malawi)
    ICHECCCLM85 = ICHECCCLM85.extract(Central_Malawi)
    ICHECKNMI85 = ICHECKNMI85.extract(Central_Malawi)
    ICHECMPI85 = ICHECMPI85.extract(Central_Malawi)
    ICHECSMHI85 = ICHECSMHI85.extract(Central_Malawi)
    IPSL85 = IPSL85.extract(Central_Malawi)
    MIROC85 = MIROC85.extract(Central_Malawi)
    MOHCCCLM85 = MOHCCCLM85.extract(Central_Malawi)
    MOHCKNMI85 = MOHCKNMI85.extract(Central_Malawi)
    MOHCSMHI85 = MOHCSMHI85.extract(Central_Malawi)
    MPICCLM85 = MPICCLM85.extract(Central_Malawi)
    MPIREMO85 = MPIREMO85.extract(Central_Malawi)
    MPISMHI85 = MPISMHI85.extract(Central_Malawi)
    NCCSMHI85 = NCCSMHI85.extract(Central_Malawi)
    NOAA85 = NOAA85.extract(Central_Malawi)
   
    #Convert units, CORDEX Data is in kg m-2 s-1 but we want data in mm day-1
    #Conversion from kg m-2 of water to mm of water is 1 to 1, and from second to day is 86400 therefore the conversion is:
    Convert=86400
    
    CCCmaCanRCM = CCCmaCanRCM*Convert
    CCCmaSMHI = CCCmaSMHI*Convert
    CNRM = CNRM*Convert
    CNRMSMHI = CNRMSMHI*Convert 
    CSIRO = CSIRO*Convert
    ICHECDMI = ICHECDMI*Convert
    ICHECCCLM = ICHECCCLM*Convert
    ICHECKNMI = ICHECKNMI*Convert
    ICHECMPI = ICHECMPI*Convert
    ICHECSMHI = ICHECSMHI*Convert
    IPSL = IPSL*Convert
    MIROC = MIROC*Convert
    MOHCCCLM = MOHCCCLM*Convert
    MOHCKNMI = MOHCKNMI*Convert
    MOHCSMHI = MOHCSMHI*Convert
    MPICCLM = MPICCLM*Convert
    MPIREMO = MPIREMO*Convert
    MPISMHI = MPISMHI*Convert
    NCCSMHI = NCCSMHI*Convert
    NOAA = NOAA*Convert
    
    CCCmaCanRCM85 = CCCmaCanRCM85*Convert
    CCCmaSMHI85 = CCCmaSMHI85*Convert
    CNRM85 = CNRM85*Convert
    CNRMSMHI85 = CNRMSMHI85*Convert 
    CSIRO85 = CSIRO85*Convert
    ICHECDMI85 = ICHECDMI85*Convert
    ICHECCCLM85 = ICHECCCLM85*Convert
    ICHECKNMI85 = ICHECKNMI85*Convert
    ICHECMPI85 = ICHECMPI85*Convert
    ICHECSMHI85 = ICHECSMHI85*Convert
    IPSL85 = IPSL85*Convert
    MIROC85 = MIROC85*Convert
    MOHCCCLM85 = MOHCCCLM85*Convert
    MOHCKNMI85 = MOHCKNMI85*Convert
    MOHCSMHI85 = MOHCSMHI85*Convert
    MPICCLM85 = MPICCLM85*Convert
    MPIREMO85 = MPIREMO85*Convert
    MPISMHI85 = MPISMHI85*Convert
    NCCSMHI85 = NCCSMHI85*Convert
    NOAA85 = NOAA85*Convert
    
    #add month numbers to data
    iriscc.add_month_number(CCCmaCanRCM, 'time')
    iriscc.add_month_number(CCCmaSMHI, 'time')
    iriscc.add_month_number(CNRM, 'time')
    iriscc.add_month_number(CNRMSMHI, 'time')
    iriscc.add_month_number(CSIRO, 'time')
    iriscc.add_month_number(ICHECDMI, 'time')
    iriscc.add_month_number(ICHECCCLM, 'time')
    iriscc.add_month_number(ICHECKNMI, 'time')
    iriscc.add_month_number(ICHECMPI, 'time')
    iriscc.add_month_number(ICHECSMHI, 'time')
    iriscc.add_month_number(IPSL, 'time')
    iriscc.add_month_number(MIROC, 'time')
    iriscc.add_month_number(MOHCCCLM, 'time')
    iriscc.add_month_number(MOHCKNMI, 'time')
    iriscc.add_month_number(MOHCSMHI, 'time')
    iriscc.add_month_number(MPICCLM, 'time')
    iriscc.add_month_number(MPIREMO, 'time')
    iriscc.add_month_number(MPISMHI, 'time')
    iriscc.add_month_number(NCCSMHI, 'time')
    iriscc.add_month_number(NOAA, 'time')
    
    iriscc.add_month_number(CCCmaCanRCM85, 'time')
    iriscc.add_month_number(CCCmaSMHI85, 'time')
    iriscc.add_month_number(CNRM85, 'time')
    iriscc.add_month_number(CNRMSMHI85, 'time')
    iriscc.add_month_number(CSIRO85, 'time')
    iriscc.add_month_number(ICHECDMI85, 'time')
    iriscc.add_month_number(ICHECCCLM85, 'time')
    iriscc.add_month_number(ICHECKNMI85, 'time')
    iriscc.add_month_number(ICHECMPI85, 'time')
    iriscc.add_month_number(ICHECSMHI85, 'time')
    iriscc.add_month_number(IPSL85, 'time')
    iriscc.add_month_number(MIROC85, 'time')
    iriscc.add_month_number(MOHCCCLM85, 'time')
    iriscc.add_month_number(MOHCKNMI85, 'time')
    iriscc.add_month_number(MOHCSMHI85, 'time')
    iriscc.add_month_number(MPICCLM85, 'time')
    iriscc.add_month_number(MPIREMO85, 'time')
    iriscc.add_month_number(MPISMHI85, 'time')
    iriscc.add_month_number(NCCSMHI85, 'time')
    iriscc.add_month_number(NOAA85, 'time')
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT FILES TO BE PLOT SPECIFIC FOR MONTHLY PLOTTING
    #-------------------------------------------------------------------------
    #PART 5A: 2050 FORMATING
    #time constraint to make all series the same (1940-2069)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_m50 = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)

    CCCmaCanRCM_m = CCCmaCanRCM.extract(t_constraint_m50)
    CCCmaSMHI_m = CCCmaSMHI.extract(t_constraint_m50)
    CNRM_m =CNRM.extract(t_constraint_m50)
    CNRMSMHI_m =CNRMSMHI.extract(t_constraint_m50)
    CSIRO_m = CSIRO.extract(t_constraint_m50)
    ICHECDMI_m = ICHECDMI.extract(t_constraint_m50)
    ICHECCCLM_m = ICHECCCLM.extract(t_constraint_m50)
    ICHECKNMI_m = ICHECKNMI.extract(t_constraint_m50)
    ICHECMPI_m = ICHECMPI.extract(t_constraint_m50)
    ICHECSMHI_m = ICHECSMHI.extract(t_constraint_m50)
    IPSL_m = IPSL.extract(t_constraint_m50)
    MIROC_m = MIROC.extract(t_constraint_m50)
    MOHCCCLM_m = MOHCCCLM.extract(t_constraint_m50)
    MOHCKNMI_m = MOHCKNMI.extract(t_constraint_m50)
    MOHCSMHI_m = MOHCSMHI.extract(t_constraint_m50)
    MPICCLM_m = MPICCLM.extract(t_constraint_m50)
    MPIREMO_m = MPIREMO.extract(t_constraint_m50)
    MPISMHI_m = MPISMHI.extract(t_constraint_m50)
    NCCSMHI_m = NCCSMHI.extract(t_constraint_m50)
    NOAA_m = NOAA.extract(t_constraint_m50) 
    
    CCCmaCanRCM85_m =  CCCmaCanRCM85.extract(t_constraint_m50)
    CCCmaSMHI85_m =  CCCmaSMHI85.extract(t_constraint_m50)
    CNRM85_m = CNRM85.extract(t_constraint_m50)
    CNRMSMHI85_m = CNRMSMHI85.extract(t_constraint_m50)
    CSIRO85_m = CSIRO85.extract(t_constraint_m50)
    ICHECDMI85_m = ICHECDMI85.extract(t_constraint_m50)
    ICHECCCLM85_m = ICHECCCLM85.extract(t_constraint_m50)
    ICHECKNMI85_m = ICHECKNMI85.extract(t_constraint_m50)
    ICHECMPI85_m = ICHECMPI85.extract(t_constraint_m50)
    ICHECSMHI85_m = ICHECSMHI85.extract(t_constraint_m50)
    IPSL85_m = IPSL85.extract(t_constraint_m50)
    MIROC85_m = MIROC85.extract(t_constraint_m50)
    MOHCCCLM85_m = MOHCCCLM85.extract(t_constraint_m50)
    MOHCKNMI85_m = MOHCKNMI85.extract(t_constraint_m50)
    MOHCSMHI85_m = MOHCSMHI85.extract(t_constraint_m50)
    MPICCLM85_m = MPICCLM85.extract(t_constraint_m50)
    MPIREMO85_m = MPIREMO85.extract(t_constraint_m50)
    MPISMHI85_m = MPISMHI85.extract(t_constraint_m50)
    NCCSMHI85_m = NCCSMHI85.extract(t_constraint_m50)
    NOAA85_m =NOAA85.extract(t_constraint_m50) 
    
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month    
    CCCmaCanRCM_m = CCCmaCanRCM_m.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_m = CCCmaSMHI_m.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_m = CNRM_m.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_m = CNRMSMHI_m.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_m = CSIRO_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_m = ICHECDMI_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_m = ICHECCCLM_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_m = ICHECKNMI_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_m = ICHECMPI_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_m = ICHECSMHI_m.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_m = IPSL_m.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_m = MIROC_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_m = MOHCCCLM_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_m = MOHCKNMI_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_m = MOHCSMHI_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_m = MPICCLM_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_m = MPIREMO_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_m = MPISMHI_m.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_m = NCCSMHI_m.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_m = NOAA_m.aggregated_by('month_number', iris.analysis.MEAN)
    
    CCCmaCanRCM85_m = CCCmaCanRCM85_m.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI85_m = CCCmaSMHI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM85_m = CNRM85_m.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI85_m = CNRMSMHI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO85_m = CSIRO85_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI85_m = ICHECDMI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM85_m = ICHECCCLM85_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI85_m = ICHECKNMI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI85_m = ICHECMPI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI85_m = ICHECSMHI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL85_m = IPSL85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC85_m = MIROC85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM85_m = MOHCCCLM85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI85_m = MOHCKNMI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI85_m = MOHCSMHI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM85_m = MPICCLM85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO85_m = MPIREMO85_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI85_m = MPISMHI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI85_m = NCCSMHI85_m.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA85_m = NOAA85_m.aggregated_by('month_number', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube.
    CCCmaCanRCM_m_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_m)
    CCCmaSMHI_m_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_m)
    CNRM_m_grid_areas = iris.analysis.cartography.area_weights(CNRM_m)
    CNRMSMHI_m_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_m)
    CSIRO_m_grid_areas = iris.analysis.cartography.area_weights(CSIRO_m)
    ICHECDMI_m_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_m)
    ICHECCCLM_m_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_m)
    ICHECKNMI_m_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_m)
    ICHECMPI_m_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_m)
    ICHECSMHI_m_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_m)
    IPSL_m_grid_areas = iris.analysis.cartography.area_weights(IPSL_m)
    MIROC_m_grid_areas = iris.analysis.cartography.area_weights(MIROC_m)
    MOHCCCLM_m_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_m)
    MOHCKNMI_m_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_m)
    MOHCSMHI_m_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_m)
    MPICCLM_m_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_m)
    MPIREMO_m_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_m)
    MPISMHI_m_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_m)
    NCCSMHI_m_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_m)
    NOAA_m_grid_areas = iris.analysis.cartography.area_weights(NOAA_m)
    
    CCCmaCanRCM85_m_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_m)
    CCCmaSMHI85_m_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_m)
    CNRM85_m_grid_areas = iris.analysis.cartography.area_weights(CNRM85_m)
    CNRMSMHI85_m_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_m)
    CSIRO85_m_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_m)
    ICHECDMI85_m_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_m)
    ICHECCCLM85_m_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_m)
    ICHECKNMI85_m_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_m)
    ICHECMPI85_m_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_m)
    ICHECSMHI85_m_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_m)
    IPSL85_m_grid_areas = iris.analysis.cartography.area_weights(IPSL85_m)
    MIROC85_m_grid_areas = iris.analysis.cartography.area_weights(MIROC85_m)
    MOHCCCLM85_m_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_m)
    MOHCKNMI85_m_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_m)
    MOHCSMHI85_m_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_m)
    MPICCLM85_m_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_m)
    MPIREMO85_m_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_m)
    MPISMHI85_m_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_m)
    NCCSMHI85_m_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_m)
    NOAA85_m_grid_areas = iris.analysis.cartography.area_weights(NOAA85_m)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_m_mean = CCCmaCanRCM_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_m_grid_areas)      
    CCCmaSMHI_m_mean = CCCmaSMHI_m.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_m_grid_areas)
    CNRM_m_mean = CNRM_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_m_grid_areas)
    CNRMSMHI_m_mean = CNRMSMHI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_m_grid_areas)  
    CSIRO_m_mean = CSIRO_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_m_grid_areas)
    ICHECDMI_m_mean = ICHECDMI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_m_grid_areas) 
    ICHECCCLM_m_mean = ICHECCCLM_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_m_grid_areas)
    ICHECKNMI_m_mean = ICHECKNMI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_m_grid_areas)
    ICHECMPI_m_mean = ICHECMPI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_m_grid_areas)
    ICHECSMHI_m_mean = ICHECSMHI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_m_grid_areas)
    IPSL_m_mean = IPSL_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_m_grid_areas)
    MIROC_m_mean = MIROC_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_m_grid_areas)
    MOHCCCLM_m_mean = MOHCCCLM_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_m_grid_areas)
    MOHCKNMI_m_mean = MOHCKNMI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_m_grid_areas)
    MOHCSMHI_m_mean = MOHCSMHI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_m_grid_areas)
    MPICCLM_m_mean = MPICCLM_m.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_m_grid_areas)      
    MPIREMO_m_mean = MPIREMO_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_m_grid_areas)                         
    MPISMHI_m_mean = MPISMHI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_m_grid_areas)
    NCCSMHI_m_mean = NCCSMHI_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_m_grid_areas) 
    NOAA_m_mean = NOAA_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_m_grid_areas)
    
    CCCmaCanRCM85_m_mean = CCCmaCanRCM85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_m_grid_areas)      
    CCCmaSMHI85_m_mean = CCCmaSMHI85_m.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_m_grid_areas)
    CNRM85_m_mean = CNRM85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_m_grid_areas)
    CNRMSMHI85_m_mean = CNRMSMHI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_m_grid_areas)  
    CSIRO85_m_mean = CSIRO85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_m_grid_areas)
    ICHECDMI85_m_mean = ICHECDMI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_m_grid_areas) 
    ICHECCCLM85_m_mean = ICHECCCLM85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_m_grid_areas)
    ICHECKNMI85_m_mean = ICHECKNMI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_m_grid_areas)
    ICHECMPI85_m_mean = ICHECMPI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_m_grid_areas)
    ICHECSMHI85_m_mean = ICHECSMHI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_m_grid_areas)
    IPSL85_m_mean = IPSL85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_m_grid_areas)
    MIROC85_m_mean = MIROC85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_m_grid_areas)
    MOHCCCLM85_m_mean = MOHCCCLM85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_m_grid_areas)
    MOHCKNMI85_m_mean = MOHCKNMI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_m_grid_areas)
    MOHCSMHI85_m_mean = MOHCSMHI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_m_grid_areas)
    MPICCLM85_m_mean = MPICCLM85_m.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_m_grid_areas)      
    MPIREMO85_m_mean = MPIREMO85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_m_grid_areas)                         
    MPISMHI85_m_mean = MPISMHI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_m_grid_areas)
    NCCSMHI85_m_mean = NCCSMHI85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_m_grid_areas) 
    NOAA85_m_mean = NOAA85_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_m_grid_areas)
    
    #Create average      
    AverageRY_m = (CCCmaCanRCM_m_mean.data + CCCmaSMHI_m_mean.data + CNRM_m_mean.data + CNRMSMHI_m_mean.data + CSIRO_m_mean.data + ICHECDMI_m_mean.data + ICHECCCLM_m_mean.data + ICHECKNMI_m_mean.data + ICHECMPI_m_mean.data + ICHECSMHI_m_mean.data + IPSL_m_mean.data + MIROC_m_mean.data + MOHCCCLM_m_mean.data + MOHCKNMI_m_mean.data + MOHCSMHI_m_mean.data + MPICCLM_m_mean.data + MPIREMO_m_mean.data + MPISMHI_m_mean.data + NCCSMHI_m_mean.data + NOAA_m_mean.data)/20.
    
    AverageRY85_m = (CCCmaCanRCM85_m_mean.data + CCCmaSMHI85_m_mean.data + CNRM85_m_mean.data + CNRMSMHI85_m_mean.data + CSIRO85_m_mean.data + ICHECDMI85_m_mean.data + ICHECCCLM85_m_mean.data + ICHECKNMI85_m_mean.data + ICHECMPI85_m_mean.data + ICHECSMHI85_m_mean.data + IPSL85_m_mean.data + MIROC85_m_mean.data + MOHCCCLM85_m_mean.data + MOHCKNMI85_m_mean.data + MOHCSMHI85_m_mean.data + MPICCLM85_m_mean.data + MPIREMO85_m_mean.data + MPISMHI85_m_mean.data + NCCSMHI85_m_mean.data + NOAA85_m_mean.data)/20.
    
    #-------------------------------------------------------------------------
    #PART 5B: 2030 FORMATING

    #time constraint to make all series the same (2020-2049)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_m30 = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)

    CCCmaCanRCM_m30 = CCCmaCanRCM.extract(t_constraint_m30)
    CCCmaSMHI_m30 = CCCmaSMHI.extract(t_constraint_m30)
    CNRM_m30 =CNRM.extract(t_constraint_m30)
    CNRMSMHI_m30 =CNRMSMHI.extract(t_constraint_m30)
    CSIRO_m30=CSIRO.extract(t_constraint_m30)
    ICHECDMI_m30=ICHECDMI.extract(t_constraint_m30)
    ICHECCCLM_m30=ICHECCCLM.extract(t_constraint_m30)
    ICHECKNMI_m30=ICHECKNMI.extract(t_constraint_m30)
    ICHECMPI_m30=ICHECMPI.extract(t_constraint_m30)
    ICHECSMHI_m30=ICHECSMHI.extract(t_constraint_m30)
    IPSL_m30=IPSL.extract(t_constraint_m30)
    MIROC_m30=MIROC.extract(t_constraint_m30)
    MOHCCCLM_m30=MOHCCCLM.extract(t_constraint_m30)
    MOHCKNMI_m30=MOHCKNMI.extract(t_constraint_m30)
    MOHCSMHI_m30=MOHCSMHI.extract(t_constraint_m30)
    MPICCLM_m30=MPICCLM.extract(t_constraint_m30)
    MPIREMO_m30=MPIREMO.extract(t_constraint_m30)
    MPISMHI_m30=MPISMHI.extract(t_constraint_m30)
    NCCSMHI_m30=NCCSMHI.extract(t_constraint_m30)
    NOAA_m30=NOAA.extract(t_constraint_m30) 
    
    CCCmaCanRCM85_m30= CCCmaCanRCM85.extract(t_constraint_m30)
    CCCmaSMHI85_m30 =  CCCmaSMHI85.extract(t_constraint_m30)
    CNRM85_m30 = CNRM85.extract(t_constraint_m30)
    CNRMSMHI85_m30 = CNRMSMHI85.extract(t_constraint_m30)
    CSIRO85_m30 = CSIRO85.extract(t_constraint_m30)
    ICHECDMI85_m30 = ICHECDMI85.extract(t_constraint_m30)
    ICHECCCLM85_m30 = ICHECCCLM85.extract(t_constraint_m30)
    ICHECKNMI85_m30 = ICHECKNMI85.extract(t_constraint_m30)
    ICHECMPI85_m30 = ICHECMPI85.extract(t_constraint_m30)
    ICHECSMHI85_m30 = ICHECSMHI85.extract(t_constraint_m30)
    IPSL85_m30 = IPSL85.extract(t_constraint_m30)
    MIROC85_m30 = MIROC85.extract(t_constraint_m30)
    MOHCCCLM85_m30 = MOHCCCLM85.extract(t_constraint_m30)
    MOHCKNMI85_m30 = MOHCKNMI85.extract(t_constraint_m30)
    MOHCSMHI85_m30 = MOHCSMHI85.extract(t_constraint_m30)
    MPICCLM85_m30 = MPICCLM85.extract(t_constraint_m30)
    MPIREMO85_m30 = MPIREMO85.extract(t_constraint_m30)
    MPISMHI85_m30 = MPISMHI85.extract(t_constraint_m30)
    NCCSMHI85_m30 = NCCSMHI85.extract(t_constraint_m30)
    NOAA85_m30 =NOAA85.extract(t_constraint_m30) 
     
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month    
    CCCmaCanRCM_m30= CCCmaCanRCM_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_m30= CCCmaSMHI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_m30= CNRM_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_m30= CNRMSMHI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_m30= CSIRO_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_m30= ICHECDMI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_m30= ICHECCCLM_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_m30= ICHECKNMI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_m30= ICHECMPI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_m30= ICHECSMHI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_m30= IPSL_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_m30= MIROC_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_m30= MOHCCCLM_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_m30= MOHCKNMI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_m30= MOHCSMHI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_m30= MPICCLM_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_m30= MPIREMO_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_m30= MPISMHI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_m30= NCCSMHI_m30.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_m30= NOAA_m30.aggregated_by('month_number', iris.analysis.MEAN)
    
    CCCmaCanRCM85_m30 = CCCmaCanRCM85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI85_m30= CCCmaSMHI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM85_m30= CNRM85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI85_m30= CNRMSMHI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO85_m30= CSIRO85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI85_m30= ICHECDMI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM85_m30= ICHECCCLM85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI85_m30= ICHECKNMI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI85_m30= ICHECMPI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI85_m30= ICHECSMHI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL85_m30= IPSL85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC85_m30= MIROC85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM85_m30= MOHCCCLM85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI85_m30= MOHCKNMI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI85_m30= MOHCSMHI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM85_m30= MPICCLM85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO85_m30= MPIREMO85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI85_m30= MPISMHI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI85_m30= NCCSMHI85_m30.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA85_m30= NOAA85_m30.aggregated_by('month_number', iris.analysis.MEAN)
   
    #Returns an array of area weights, with the same dimensions as the cube.
    CCCmaCanRCM_m30_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_m30)
    CCCmaSMHI_m30_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_m30)
    CNRM_m30_grid_areas = iris.analysis.cartography.area_weights(CNRM_m30)
    CNRMSMHI_m30_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_m30)
    CSIRO_m30_grid_areas = iris.analysis.cartography.area_weights(CSIRO_m30)
    ICHECDMI_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_m30)
    ICHECCCLM_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_m30)
    ICHECKNMI_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_m30)
    ICHECMPI_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_m30)
    ICHECSMHI_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_m30)
    IPSL_m30_grid_areas = iris.analysis.cartography.area_weights(IPSL_m30)
    MIROC_m30_grid_areas = iris.analysis.cartography.area_weights(MIROC_m30)
    MOHCCCLM_m30_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_m30)
    MOHCKNMI_m30_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_m30)
    MOHCSMHI_m30_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_m30)
    MPICCLM_m30_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_m30)
    MPIREMO_m30_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_m30)
    MPISMHI_m30_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_m30)
    NCCSMHI_m30_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_m30)
    NOAA_m30_grid_areas = iris.analysis.cartography.area_weights(NOAA_m30)
    
    CCCmaCanRCM85_m30_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_m30)
    CCCmaSMHI85_m30_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_m30)
    CNRM85_m30_grid_areas = iris.analysis.cartography.area_weights(CNRM85_m30)
    CNRMSMHI85_m30_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_m30)
    CSIRO85_m30_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_m30)
    ICHECDMI85_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_m30)
    ICHECCCLM85_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_m30)
    ICHECKNMI85_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_m30)
    ICHECMPI85_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_m30)
    ICHECSMHI85_m30_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_m30)
    IPSL85_m30_grid_areas = iris.analysis.cartography.area_weights(IPSL85_m30)
    MIROC85_m30_grid_areas = iris.analysis.cartography.area_weights(MIROC85_m30)
    MOHCCCLM85_m30_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_m30)
    MOHCKNMI85_m30_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_m30)
    MOHCSMHI85_m30_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_m30)
    MPICCLM85_m30_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_m30)
    MPIREMO85_m30_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_m30)
    MPISMHI85_m30_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_m30)
    NCCSMHI85_m30_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_m30)
    NOAA85_m30_grid_areas = iris.analysis.cartography.area_weights(NOAA85_m30)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_m30_mean = CCCmaCanRCM_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_m30_grid_areas)      
    CCCmaSMHI_m30_mean = CCCmaSMHI_m30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_m30_grid_areas)
    CNRM_m30_mean = CNRM_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_m30_grid_areas)
    CNRMSMHI_m30_mean = CNRMSMHI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_m30_grid_areas)  
    CSIRO_m30_mean = CSIRO_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_m30_grid_areas)
    ICHECDMI_m30_mean = ICHECDMI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_m30_grid_areas) 
    ICHECCCLM_m30_mean = ICHECCCLM_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_m30_grid_areas)
    ICHECKNMI_m30_mean = ICHECKNMI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_m30_grid_areas)
    ICHECMPI_m30_mean = ICHECMPI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_m30_grid_areas)
    ICHECSMHI_m30_mean = ICHECSMHI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_m30_grid_areas)
    IPSL_m30_mean = IPSL_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_m30_grid_areas)
    MIROC_m30_mean = MIROC_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_m30_grid_areas)
    MOHCCCLM_m30_mean = MOHCCCLM_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_m30_grid_areas)
    MOHCKNMI_m30_mean = MOHCKNMI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_m30_grid_areas)
    MOHCSMHI_m30_mean = MOHCSMHI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_m30_grid_areas)
    MPICCLM_m30_mean = MPICCLM_m30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_m30_grid_areas)      
    MPIREMO_m30_mean = MPIREMO_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_m30_grid_areas)                         
    MPISMHI_m30_mean = MPISMHI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_m30_grid_areas)
    NCCSMHI_m30_mean = NCCSMHI_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_m30_grid_areas) 
    NOAA_m30_mean = NOAA_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_m30_grid_areas)
    
    CCCmaCanRCM85_m30_mean = CCCmaCanRCM85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_m30_grid_areas)
    CCCmaSMHI85_m30_mean = CCCmaSMHI85_m30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_m30_grid_areas)
    CNRM85_m30_mean = CNRM85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_m30_grid_areas)
    CNRMSMHI85_m30_mean = CNRMSMHI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_m30_grid_areas)  
    CSIRO85_m30_mean = CSIRO85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_m30_grid_areas)
    ICHECDMI85_m30_mean = ICHECDMI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_m30_grid_areas) 
    ICHECCCLM85_m30_mean = ICHECCCLM85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_m30_grid_areas)
    ICHECKNMI85_m30_mean = ICHECKNMI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_m30_grid_areas)
    ICHECMPI85_m30_mean = ICHECMPI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_m30_grid_areas)
    ICHECSMHI85_m30_mean = ICHECSMHI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_m30_grid_areas)
    IPSL85_m30_mean = IPSL85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_m30_grid_areas)
    MIROC85_m30_mean = MIROC85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_m30_grid_areas)
    MOHCCCLM85_m30_mean = MOHCCCLM85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_m30_grid_areas)
    MOHCKNMI85_m30_mean = MOHCKNMI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_m30_grid_areas)
    MOHCSMHI85_m30_mean = MOHCSMHI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_m30_grid_areas)
    MPICCLM85_m30_mean = MPICCLM85_m30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_m30_grid_areas)      
    MPIREMO85_m30_mean = MPIREMO85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_m30_grid_areas)   
    MPISMHI85_m30_mean = MPISMHI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_m30_grid_areas)
    NCCSMHI85_m30_mean = NCCSMHI85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_m30_grid_areas) 
    NOAA85_m30_mean = NOAA85_m30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_m30_grid_areas)
    
    #Create averages      
    AverageRY_m30 = (CCCmaCanRCM_m30_mean.data + CCCmaSMHI_m30_mean.data + CNRM_m30_mean.data + CNRMSMHI_m30_mean.data + CSIRO_m30_mean.data + ICHECDMI_m30_mean.data + ICHECCCLM_m30_mean.data + ICHECKNMI_m30_mean.data + ICHECMPI_m30_mean.data + ICHECSMHI_m30_mean.data + IPSL_m30_mean.data + MIROC_m30_mean.data + MOHCCCLM_m30_mean.data + MOHCKNMI_m30_mean.data + MOHCSMHI_m30_mean.data + MPICCLM_m30_mean.data + MPIREMO_m30_mean.data + MPISMHI_m30_mean.data + NCCSMHI_m30_mean.data + NOAA_m30_mean.data)/20.
    
    AverageRY85_m30 = (CCCmaCanRCM85_m30_mean.data + CCCmaSMHI85_m30_mean.data + CNRM85_m30_mean.data + CNRMSMHI85_m30_mean.data + CSIRO85_m30_mean.data + ICHECDMI85_m30_mean.data + ICHECCCLM85_m30_mean.data + ICHECKNMI85_m30_mean.data + ICHECMPI85_m30_mean.data + ICHECSMHI85_m30_mean.data + IPSL85_m30_mean.data + MIROC85_m30_mean.data + MOHCCCLM85_m30_mean.data + MOHCKNMI85_m30_mean.data + MOHCSMHI85_m30_mean.data + MPICCLM85_m30_mean.data + MPIREMO85_m30_mean.data + MPISMHI85_m30_mean.data + NCCSMHI85_m30_mean.data + NOAA85_m30_mean.data)/20.

    
    #-------------------------------------------------------------------------
    #PART 3: PLOT LINE MONTHLY GRAPH 
    X_m = np.arange(1,13,1) 
    
    #PART 5A: Regional Climate Models Line Graph 2050
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m, CCCmaCanRCM_m_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X_m, CCCmaSMHI_m_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X_m, CNRM_m_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X_m, CNRMSMHI_m_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X_m, CSIRO_m_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X_m, ICHECDMI_m_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X_m, ICHECCCLM_m_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X_m, ICHECKNMI_m_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X_m, ICHECMPI_m_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X_m, ICHECSMHI_m_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X_m, IPSL_m_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X_m, MIROC_m_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X_m, MOHCCCLM_m_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X_m, MOHCKNMI_m_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X_m, MOHCSMHI_m_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X_m, MPICCLM_m_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X_m, MPIREMO_m_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X_m, MPISMHI_m_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X_m, NCCSMHI_m_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X_m, NOAA_m_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X_m, AverageRY_m, label='Average RCM 2040-2069', lw=3, color='black', linestyle='--') 
        
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Monthly_ALL4.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m, CCCmaCanRCM85_m_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X_m, CCCmaSMHI85_m_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X_m, CNRM85_m_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X_m, CNRMSMHI85_m_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X_m, CSIRO85_m_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X_m, ICHECDMI85_m_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X_m, ICHECCCLM85_m_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X_m, ICHECKNMI85_m_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X_m, ICHECMPI85_m_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X_m, ICHECSMHI85_m_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X_m, IPSL85_m_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X_m, MIROC85_m_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X_m, MOHCCCLM85_m_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X_m, MOHCKNMI85_m_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X_m, MOHCSMHI85_m_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X_m, MPICCLM85_m_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X_m, MPIREMO85_m_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X_m, MPISMHI85_m_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X_m, NCCSMHI85_m_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X_m, NOAA85_m_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X_m, AverageRY85_m, label='Average RCM 2040-2069', lw=3, color='black', linestyle='--') 
        
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Monthly_ALL8.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    
    #PART 5B: Regional Climate Models Line Graph 2030
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'month' rather than 'time' 
    plt.plot(X_m, CCCmaCanRCM_m30_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X_m, CCCmaSMHI_m30_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X_m, CNRM_m30_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X_m, CNRMSMHI_m30_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X_m, CSIRO_m30_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X_m, ICHECDMI_m30_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X_m, ICHECCCLM_m30_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X_m, ICHECKNMI_m30_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X_m, ICHECMPI_m30_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X_m, ICHECSMHI_m30_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X_m, IPSL_m30_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X_m, MIROC_m30_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X_m, MOHCCCLM_m30_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X_m, MOHCKNMI_m30_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X_m, MOHCSMHI_m30_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X_m, MPICCLM_m30_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X_m, MPIREMO_m30_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X_m, MPISMHI_m30_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X_m, NCCSMHI_m30_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X_m, NOAA_m30_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X_m, AverageRY_m30, label='Average RCM 2020-2049', lw=3, color='black', linestyle='--') 
        
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Monthly_ALL4.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'month' rather than 'time' 
    plt.plot(X_m, CCCmaCanRCM85_m30_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X_m, CCCmaSMHI85_m30_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X_m, CNRM85_m30_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X_m, CNRMSMHI85_m30_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X_m, CSIRO85_m30_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X_m, ICHECDMI85_m30_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X_m, ICHECCCLM85_m30_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X_m, ICHECKNMI85_m30_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X_m, ICHECMPI85_m30_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X_m, ICHECSMHI85_m30_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X_m, IPSL85_m30_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X_m, MIROC85_m30_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X_m, MOHCCCLM85_m30_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X_m, MOHCKNMI85_m30_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X_m, MOHCSMHI85_m30_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X_m, MPICCLM85_m30_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X_m, MPIREMO85_m30_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X_m, MPISMHI85_m30_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X_m, NCCSMHI85_m30_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X_m, NOAA85_m30_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X_m, AverageRY85_m30, label='Average RCM 2020-2049', lw=3, color='black', linestyle='--')   
        
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Monthly_ALL8.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #PART 5C: Average RCM Line Graph 2050 and 2030
    #set x-axis ticks                                        
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m, AverageRY_m, label='Average RCM 2040-2069 RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X_m, AverageRY_m30, label='Average RCM 2020-2049 RCP 4.5', lw=1.5, color='cyan', linestyle=':')
    plt.plot(X_m, AverageRY85_m, label='Average RCM 2040-2069 RCP 8.5', lw=1.5, color='magenta')
    plt.plot(X_m, AverageRY85_m30, label='Average RCM 2020-2049 RCP 8.5', lw=1.5, color='magenta', linestyle=':')
    
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('ETo for Central Malawi by Month', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Monthly_AVE_2050.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA TO BE PLOT SPECIFIC FOR YEARLY PLOTTING
    
    #add year data to files
    iriscc.add_year(CCCmaCanRCM, 'time')
    iriscc.add_year(CCCmaSMHI, 'time')
    iriscc.add_year(CNRM, 'time')
    iriscc.add_year(CNRMSMHI, 'time')
    iriscc.add_year(CSIRO, 'time')
    iriscc.add_year(ICHECDMI, 'time')
    iriscc.add_year(ICHECCCLM, 'time')
    iriscc.add_year(ICHECKNMI, 'time')
    iriscc.add_year(ICHECMPI, 'time')
    iriscc.add_year(ICHECSMHI, 'time')
    iriscc.add_year(IPSL, 'time')
    iriscc.add_year(MIROC, 'time')
    iriscc.add_year(MOHCCCLM, 'time')
    iriscc.add_year(MOHCKNMI, 'time')
    iriscc.add_year(MOHCSMHI, 'time')
    iriscc.add_year(MPICCLM, 'time')
    iriscc.add_year(MPIREMO, 'time')
    iriscc.add_year(MPISMHI, 'time')
    iriscc.add_year(NCCSMHI, 'time')
    iriscc.add_year(NOAA, 'time')
    
    iriscc.add_year(CCCmaCanRCM85, 'time')
    iriscc.add_year(CCCmaSMHI85, 'time')
    iriscc.add_year(CNRM85, 'time')
    iriscc.add_year(CNRMSMHI85, 'time')
    iriscc.add_year(CSIRO85, 'time')
    iriscc.add_year(ICHECDMI85, 'time')
    iriscc.add_year(ICHECCCLM85, 'time')
    iriscc.add_year(ICHECKNMI85, 'time')
    iriscc.add_year(ICHECMPI85, 'time')
    iriscc.add_year(ICHECSMHI85, 'time')
    iriscc.add_year(IPSL85, 'time')
    iriscc.add_year(MIROC85, 'time')
    iriscc.add_year(MOHCCCLM85, 'time')
    iriscc.add_year(MOHCKNMI85, 'time')
    iriscc.add_year(MOHCSMHI85, 'time')
    iriscc.add_year(MPICCLM85, 'time')
    iriscc.add_year(MPIREMO85, 'time')
    iriscc.add_year(MPISMHI85, 'time')
    iriscc.add_year(NCCSMHI85, 'time')
    iriscc.add_year(NOAA85, 'time')
    
    #limit to a season
    SON = iris.Constraint(season='son')
    DJF = iris.Constraint(season='djf')
    MAM = iris.Constraint(season='mam')
    JJA = iris.Constraint(season='jja')
    
    #add season data to files
    iriscc.add_season(CCCmaCanRCM, 'time')
    iriscc.add_season(CCCmaSMHI, 'time')
    iriscc.add_season(CNRM, 'time')
    iriscc.add_season(CNRMSMHI, 'time')
    iriscc.add_season(CSIRO, 'time')
    iriscc.add_season(ICHECDMI, 'time')
    iriscc.add_season(ICHECCCLM, 'time')
    iriscc.add_season(ICHECKNMI, 'time')
    iriscc.add_season(ICHECMPI, 'time')
    iriscc.add_season(ICHECSMHI, 'time')
    iriscc.add_season(IPSL, 'time')
    iriscc.add_season(MIROC, 'time')
    iriscc.add_season(MOHCCCLM, 'time')
    iriscc.add_season(MOHCKNMI, 'time')
    iriscc.add_season(MOHCSMHI, 'time')
    iriscc.add_season(MPICCLM, 'time')
    iriscc.add_season(MPIREMO, 'time')
    iriscc.add_season(MPISMHI, 'time')
    iriscc.add_season(NCCSMHI, 'time')
    iriscc.add_season(NOAA, 'time')
    
    iriscc.add_season(CCCmaCanRCM85, 'time')
    iriscc.add_season(CCCmaSMHI85, 'time')
    iriscc.add_season(CNRM85, 'time')
    iriscc.add_season(CNRMSMHI85, 'time')
    iriscc.add_season(CSIRO85, 'time')
    iriscc.add_season(ICHECDMI85, 'time')
    iriscc.add_season(ICHECCCLM85, 'time')
    iriscc.add_season(ICHECKNMI85, 'time')
    iriscc.add_season(ICHECMPI85, 'time')
    iriscc.add_season(ICHECSMHI85, 'time')
    iriscc.add_season(IPSL85, 'time')
    iriscc.add_season(MIROC85, 'time')
    iriscc.add_season(MOHCCCLM85, 'time')
    iriscc.add_season(MOHCKNMI85, 'time')
    iriscc.add_season(MOHCSMHI85, 'time')
    iriscc.add_season(MPICCLM85, 'time')
    iriscc.add_season(MPIREMO85, 'time')
    iriscc.add_season(MPISMHI85, 'time')
    iriscc.add_season(NCCSMHI85, 'time')
    iriscc.add_season(NOAA85, 'time')
    
    #extract only the season we are interested in
    CCCmaCanRCMSON = CCCmaCanRCM.extract(SON) 
    CCCmaSMHISON = CCCmaSMHI.extract(SON) 
    CNRMSON = CNRM.extract(SON) 
    CNRMSMHISON = CNRMSMHI.extract(SON) 
    CSIROSON = CSIRO.extract(SON) 
    ICHECDMISON = ICHECDMI.extract(SON) 
    ICHECCCLMSON = ICHECCCLM.extract(SON) 
    ICHECKNMISON = ICHECKNMI.extract(SON) 
    ICHECMPISON = ICHECMPI.extract(SON) 
    ICHECSMHISON = ICHECSMHI.extract(SON) 
    IPSLSON = IPSL.extract(SON) 
    MIROCSON = MIROC.extract(SON) 
    MOHCCCLMSON = MOHCCCLM.extract(SON) 
    MOHCKNMISON = MOHCKNMI.extract(SON) 
    MOHCSMHISON = MOHCSMHI.extract(SON) 
    MPICCLMSON = MPICCLM.extract(SON) 
    MPIREMOSON = MPIREMO.extract(SON) 
    MPISMHISON = MPISMHI.extract(SON) 
    NCCSMHISON = NCCSMHI.extract(SON) 
    NOAASON = NOAA.extract(SON) 
    
    CCCmaCanRCMSON85 = CCCmaCanRCM85.extract(SON) 
    CCCmaSMHISON85 = CCCmaSMHI85.extract(SON) 
    CNRMSON85 = CNRM85.extract(SON) 
    CNRMSMHISON85 = CNRMSMHI85.extract(SON) 
    CSIROSON85 = CSIRO85.extract(SON) 
    ICHECDMISON85 = ICHECDMI85.extract(SON) 
    ICHECCCLMSON85 = ICHECCCLM85.extract(SON) 
    ICHECKNMISON85 = ICHECKNMI85.extract(SON) 
    ICHECMPISON85 = ICHECMPI85.extract(SON) 
    ICHECSMHISON85 = ICHECSMHI85.extract(SON) 
    IPSLSON85 = IPSL85.extract(SON) 
    MIROCSON85 = MIROC85.extract(SON) 
    MOHCCCLMSON85 = MOHCCCLM85.extract(SON) 
    MOHCKNMISON85 = MOHCKNMI85.extract(SON) 
    MOHCSMHISON85 = MOHCSMHI85.extract(SON) 
    MPICCLMSON85 = MPICCLM85.extract(SON) 
    MPIREMOSON85 = MPIREMO85.extract(SON) 
    MPISMHISON85 = MPISMHI85.extract(SON) 
    NCCSMHISON85 = NCCSMHI85.extract(SON) 
    NOAASON85 = NOAA85.extract(SON)
    
    CCCmaCanRCMDJF = CCCmaCanRCM.extract(DJF) 
    CCCmaSMHIDJF = CCCmaSMHI.extract(DJF) 
    CNRMDJF = CNRM.extract(DJF) 
    CNRMSMHIDJF = CNRMSMHI.extract(DJF) 
    CSIRODJF = CSIRO.extract(DJF) 
    ICHECDMIDJF = ICHECDMI.extract(DJF) 
    ICHECCCLMDJF = ICHECCCLM.extract(DJF) 
    ICHECKNMIDJF = ICHECKNMI.extract(DJF) 
    ICHECMPIDJF = ICHECMPI.extract(DJF) 
    ICHECSMHIDJF = ICHECSMHI.extract(DJF) 
    IPSLDJF = IPSL.extract(DJF) 
    MIROCDJF = MIROC.extract(DJF) 
    MOHCCCLMDJF = MOHCCCLM.extract(DJF) 
    MOHCKNMIDJF = MOHCKNMI.extract(DJF) 
    MOHCSMHIDJF = MOHCSMHI.extract(DJF) 
    MPICCLMDJF = MPICCLM.extract(DJF) 
    MPIREMODJF = MPIREMO.extract(DJF) 
    MPISMHIDJF = MPISMHI.extract(DJF) 
    NCCSMHIDJF = NCCSMHI.extract(DJF) 
    NOAADJF = NOAA.extract(DJF) 
    
    CCCmaCanRCMDJF85 = CCCmaCanRCM85.extract(DJF) 
    CCCmaSMHIDJF85 = CCCmaSMHI85.extract(DJF) 
    CNRMDJF85 = CNRM85.extract(DJF) 
    CNRMSMHIDJF85 = CNRMSMHI85.extract(DJF) 
    CSIRODJF85 = CSIRO85.extract(DJF) 
    ICHECDMIDJF85 = ICHECDMI85.extract(DJF) 
    ICHECCCLMDJF85 = ICHECCCLM85.extract(DJF) 
    ICHECKNMIDJF85 = ICHECKNMI85.extract(DJF) 
    ICHECMPIDJF85 = ICHECMPI85.extract(DJF) 
    ICHECSMHIDJF85 = ICHECSMHI85.extract(DJF) 
    IPSLDJF85 = IPSL85.extract(DJF) 
    MIROCDJF85 = MIROC85.extract(DJF) 
    MOHCCCLMDJF85 = MOHCCCLM85.extract(DJF) 
    MOHCKNMIDJF85 = MOHCKNMI85.extract(DJF) 
    MOHCSMHIDJF85 = MOHCSMHI85.extract(DJF) 
    MPICCLMDJF85 = MPICCLM85.extract(DJF) 
    MPIREMODJF85 = MPIREMO85.extract(DJF) 
    MPISMHIDJF85 = MPISMHI85.extract(DJF) 
    NCCSMHIDJF85 = NCCSMHI85.extract(DJF) 
    NOAADJF85 = NOAA85.extract(DJF)
      
    CCCmaCanRCMMAM = CCCmaCanRCM.extract(MAM) 
    CCCmaSMHIMAM = CCCmaSMHI.extract(MAM) 
    CNRMMAM = CNRM.extract(MAM) 
    CNRMSMHIMAM = CNRMSMHI.extract(MAM) 
    CSIROMAM = CSIRO.extract(MAM) 
    ICHECDMIMAM = ICHECDMI.extract(MAM) 
    ICHECCCLMMAM = ICHECCCLM.extract(MAM) 
    ICHECKNMIMAM = ICHECKNMI.extract(MAM) 
    ICHECMPIMAM = ICHECMPI.extract(MAM) 
    ICHECSMHIMAM = ICHECSMHI.extract(MAM) 
    IPSLMAM = IPSL.extract(MAM) 
    MIROCMAM = MIROC.extract(MAM) 
    MOHCCCLMMAM = MOHCCCLM.extract(MAM) 
    MOHCKNMIMAM = MOHCKNMI.extract(MAM) 
    MOHCSMHIMAM = MOHCSMHI.extract(MAM) 
    MPICCLMMAM = MPICCLM.extract(MAM) 
    MPIREMOMAM = MPIREMO.extract(MAM) 
    MPISMHIMAM = MPISMHI.extract(MAM) 
    NCCSMHIMAM = NCCSMHI.extract(MAM) 
    NOAAMAM = NOAA.extract(MAM) 
    
    CCCmaCanRCMMAM85 = CCCmaCanRCM85.extract(MAM) 
    CCCmaSMHIMAM85 = CCCmaSMHI85.extract(MAM) 
    CNRMMAM85 = CNRM85.extract(MAM) 
    CNRMSMHIMAM85 = CNRMSMHI85.extract(MAM) 
    CSIROMAM85 = CSIRO85.extract(MAM) 
    ICHECDMIMAM85 = ICHECDMI85.extract(MAM) 
    ICHECCCLMMAM85 = ICHECCCLM85.extract(MAM) 
    ICHECKNMIMAM85 = ICHECKNMI85.extract(MAM) 
    ICHECMPIMAM85 = ICHECMPI85.extract(MAM) 
    ICHECSMHIMAM85 = ICHECSMHI85.extract(MAM) 
    IPSLMAM85 = IPSL85.extract(MAM) 
    MIROCMAM85 = MIROC85.extract(MAM) 
    MOHCCCLMMAM85 = MOHCCCLM85.extract(MAM) 
    MOHCKNMIMAM85 = MOHCKNMI85.extract(MAM) 
    MOHCSMHIMAM85 = MOHCSMHI85.extract(MAM) 
    MPICCLMMAM85 = MPICCLM85.extract(MAM) 
    MPIREMOMAM85 = MPIREMO85.extract(MAM) 
    MPISMHIMAM85 = MPISMHI85.extract(MAM) 
    NCCSMHIMAM85 = NCCSMHI85.extract(MAM) 
    NOAAMAM85 = NOAA85.extract(MAM)
    
    CCCmaCanRCMJJA = CCCmaCanRCM.extract(JJA) 
    CCCmaSMHIJJA = CCCmaSMHI.extract(JJA) 
    CNRMJJA = CNRM.extract(JJA) 
    CNRMSMHIJJA = CNRMSMHI.extract(JJA) 
    CSIROJJA = CSIRO.extract(JJA) 
    ICHECDMIJJA = ICHECDMI.extract(JJA) 
    ICHECCCLMJJA = ICHECCCLM.extract(JJA) 
    ICHECKNMIJJA = ICHECKNMI.extract(JJA) 
    ICHECMPIJJA = ICHECMPI.extract(JJA) 
    ICHECSMHIJJA = ICHECSMHI.extract(JJA) 
    IPSLJJA = IPSL.extract(JJA) 
    MIROCJJA = MIROC.extract(JJA) 
    MOHCCCLMJJA = MOHCCCLM.extract(JJA) 
    MOHCKNMIJJA = MOHCKNMI.extract(JJA) 
    MOHCSMHIJJA = MOHCSMHI.extract(JJA) 
    MPICCLMJJA = MPICCLM.extract(JJA) 
    MPIREMOJJA = MPIREMO.extract(JJA) 
    MPISMHIJJA = MPISMHI.extract(JJA) 
    NCCSMHIJJA = NCCSMHI.extract(JJA) 
    NOAAJJA = NOAA.extract(JJA) 
    
    CCCmaCanRCMJJA85 = CCCmaCanRCM85.extract(JJA) 
    CCCmaSMHIJJA85 = CCCmaSMHI85.extract(JJA) 
    CNRMJJA85 = CNRM85.extract(JJA) 
    CNRMSMHIJJA85 = CNRMSMHI85.extract(JJA) 
    CSIROJJA85 = CSIRO85.extract(JJA) 
    ICHECDMIJJA85 = ICHECDMI85.extract(JJA) 
    ICHECCCLMJJA85 = ICHECCCLM85.extract(JJA) 
    ICHECKNMIJJA85 = ICHECKNMI85.extract(JJA) 
    ICHECMPIJJA85 = ICHECMPI85.extract(JJA) 
    ICHECSMHIJJA85 = ICHECSMHI85.extract(JJA) 
    IPSLJJA85 = IPSL85.extract(JJA) 
    MIROCJJA85 = MIROC85.extract(JJA) 
    MOHCCCLMJJA85 = MOHCCCLM85.extract(JJA) 
    MOHCKNMIJJA85 = MOHCKNMI85.extract(JJA) 
    MOHCSMHIJJA85 = MOHCSMHI85.extract(JJA) 
    MPICCLMJJA85 = MPICCLM85.extract(JJA) 
    MPIREMOJJA85 = MPIREMO85.extract(JJA) 
    MPISMHIJJA85 = MPISMHI85.extract(JJA) 
    NCCSMHIJJA85 = NCCSMHI85.extract(JJA) 
    NOAAJJA85 = NOAA85.extract(JJA) 
    
    #We are interested in plotting the data by year, so we need to take a mean of all the data by year
    CCCmaCanRCMSON = CCCmaCanRCMSON.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHISON = CCCmaSMHISON.aggregated_by('year', iris.analysis.MEAN)
    CNRMSON = CNRMSON.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHISON = CNRMSMHISON.aggregated_by('year', iris.analysis.MEAN)
    CSIROSON = CSIROSON.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMISON = ICHECDMISON.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMSON = ICHECCCLMSON.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMISON = ICHECKNMISON.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPISON = ICHECMPISON.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHISON = ICHECSMHISON.aggregated_by('year', iris.analysis.MEAN)
    IPSLSON = IPSLSON.aggregated_by('year', iris.analysis.MEAN)
    MIROCSON = MIROCSON.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMSON = MOHCCCLMSON.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMISON = MOHCKNMISON.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHISON = MOHCSMHISON.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMSON = MPICCLMSON.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOSON = MPIREMOSON.aggregated_by('year', iris.analysis.MEAN)
    MPISMHISON = MPISMHISON.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHISON = NCCSMHISON.aggregated_by('year', iris.analysis.MEAN)
    NOAASON = NOAASON.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMSON85 = CCCmaCanRCMSON85.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHISON85 = CCCmaSMHISON85.aggregated_by('year', iris.analysis.MEAN)
    CNRMSON85 = CNRMSON85.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHISON85 = CNRMSMHISON85.aggregated_by('year', iris.analysis.MEAN)
    CSIROSON85 = CSIROSON85.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMISON85 = ICHECDMISON85.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMSON85 = ICHECCCLMSON85.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMISON85 = ICHECKNMISON85.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPISON85 = ICHECMPISON85.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHISON85 = ICHECSMHISON85.aggregated_by('year', iris.analysis.MEAN)
    IPSLSON85 = IPSLSON85.aggregated_by('year', iris.analysis.MEAN)
    MIROCSON85 = MIROCSON85.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMSON85 = MOHCCCLMSON85.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMISON85 = MOHCKNMISON85.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHISON85 = MOHCSMHISON85.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMSON85 = MPICCLMSON85.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOSON85 = MPIREMOSON85.aggregated_by('year', iris.analysis.MEAN)
    MPISMHISON85 = MPISMHISON85.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHISON85 = NCCSMHISON85.aggregated_by('year', iris.analysis.MEAN)
    NOAASON85 = NOAASON85.aggregated_by('year', iris.analysis.MEAN)
  
    CCCmaCanRCMDJF = CCCmaCanRCMDJF.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIDJF = CCCmaSMHIDJF.aggregated_by('year', iris.analysis.MEAN)
    CNRMDJF = CNRMDJF.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIDJF = CNRMSMHIDJF.aggregated_by('year', iris.analysis.MEAN)
    CSIRODJF = CSIRODJF.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIDJF = ICHECDMIDJF.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMDJF = ICHECCCLMDJF.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIDJF = ICHECKNMIDJF.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIDJF = ICHECMPIDJF.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIDJF = ICHECSMHIDJF.aggregated_by('year', iris.analysis.MEAN)
    IPSLDJF = IPSLDJF.aggregated_by('year', iris.analysis.MEAN)
    MIROCDJF = MIROCDJF.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMDJF = MOHCCCLMDJF.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIDJF = MOHCKNMIDJF.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIDJF = MOHCSMHIDJF.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMDJF = MPICCLMDJF.aggregated_by('year', iris.analysis.MEAN)
    MPIREMODJF = MPIREMODJF.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIDJF = MPISMHIDJF.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIDJF = NCCSMHIDJF.aggregated_by('year', iris.analysis.MEAN)
    NOAADJF = NOAADJF.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMDJF85 = CCCmaCanRCMDJF85.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIDJF85 = CCCmaSMHIDJF85.aggregated_by('year', iris.analysis.MEAN)
    CNRMDJF85 = CNRMDJF85.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIDJF85 = CNRMSMHIDJF85.aggregated_by('year', iris.analysis.MEAN)
    CSIRODJF85 = CSIRODJF85.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIDJF85 = ICHECDMIDJF85.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMDJF85 = ICHECCCLMDJF85.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIDJF85 = ICHECKNMIDJF85.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIDJF85 = ICHECMPIDJF85.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIDJF85 = ICHECSMHIDJF85.aggregated_by('year', iris.analysis.MEAN)
    IPSLDJF85 = IPSLDJF85.aggregated_by('year', iris.analysis.MEAN)
    MIROCDJF85 = MIROCDJF85.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMDJF85 = MOHCCCLMDJF85.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIDJF85 = MOHCKNMIDJF85.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIDJF85 = MOHCSMHIDJF85.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMDJF85 = MPICCLMDJF85.aggregated_by('year', iris.analysis.MEAN)
    MPIREMODJF85 = MPIREMODJF85.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIDJF85 = MPISMHIDJF85.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIDJF85 = NCCSMHIDJF85.aggregated_by('year', iris.analysis.MEAN)
    NOAADJF85 = NOAADJF85.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMMAM = CCCmaCanRCMMAM.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIMAM = CCCmaSMHIMAM.aggregated_by('year', iris.analysis.MEAN)
    CNRMMAM = CNRMMAM.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIMAM = CNRMSMHIMAM.aggregated_by('year', iris.analysis.MEAN)
    CSIROMAM = CSIROMAM.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIMAM = ICHECDMIMAM.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMMAM = ICHECCCLMMAM.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIMAM = ICHECKNMIMAM.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIMAM = ICHECMPIMAM.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIMAM = ICHECSMHIMAM.aggregated_by('year', iris.analysis.MEAN)
    IPSLMAM = IPSLMAM.aggregated_by('year', iris.analysis.MEAN)
    MIROCMAM = MIROCMAM.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMMAM = MOHCCCLMMAM.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIMAM = MOHCKNMIMAM.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIMAM = MOHCSMHIMAM.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMMAM = MPICCLMMAM.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOMAM = MPIREMOMAM.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIMAM = MPISMHIMAM.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIMAM = NCCSMHIMAM.aggregated_by('year', iris.analysis.MEAN)
    NOAAMAM = NOAAMAM.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMMAM85 = CCCmaCanRCMMAM85.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIMAM85 = CCCmaSMHIMAM85.aggregated_by('year', iris.analysis.MEAN)
    CNRMMAM85 = CNRMMAM85.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIMAM85 = CNRMSMHIMAM85.aggregated_by('year', iris.analysis.MEAN)
    CSIROMAM85 = CSIROMAM85.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIMAM85 = ICHECDMIMAM85.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMMAM85 = ICHECCCLMMAM85.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIMAM85 = ICHECKNMIMAM85.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIMAM85 = ICHECMPIMAM85.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIMAM85 = ICHECSMHIMAM85.aggregated_by('year', iris.analysis.MEAN)
    IPSLMAM85 = IPSLMAM85.aggregated_by('year', iris.analysis.MEAN)
    MIROCMAM85 = MIROCMAM85.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMMAM85 = MOHCCCLMMAM85.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIMAM85 = MOHCKNMIMAM85.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIMAM85 = MOHCSMHIMAM85.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMMAM85 = MPICCLMMAM85.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOMAM85 = MPIREMOMAM85.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIMAM85 = MPISMHIMAM85.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIMAM85 = NCCSMHIMAM85.aggregated_by('year', iris.analysis.MEAN)
    NOAAMAM85 = NOAAMAM85.aggregated_by('year', iris.analysis.MEAN)
   
    CCCmaCanRCMJJA = CCCmaCanRCMJJA.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIJJA = CCCmaSMHIJJA.aggregated_by('year', iris.analysis.MEAN)
    CNRMJJA = CNRMJJA.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIJJA = CNRMSMHIJJA.aggregated_by('year', iris.analysis.MEAN)
    CSIROJJA = CSIROJJA.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIJJA = ICHECDMIJJA.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMJJA = ICHECCCLMJJA.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIJJA = ICHECKNMIJJA.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIJJA = ICHECMPIJJA.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIJJA = ICHECSMHIJJA.aggregated_by('year', iris.analysis.MEAN)
    IPSLJJA = IPSLJJA.aggregated_by('year', iris.analysis.MEAN)
    MIROCJJA = MIROCJJA.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMJJA = MOHCCCLMJJA.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIJJA = MOHCKNMIJJA.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIJJA = MOHCSMHIJJA.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMJJA = MPICCLMJJA.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOJJA = MPIREMOJJA.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIJJA = MPISMHIJJA.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIJJA = NCCSMHIJJA.aggregated_by('year', iris.analysis.MEAN)
    NOAAJJA = NOAAJJA.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMJJA85 = CCCmaCanRCMJJA85.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIJJA85 = CCCmaSMHIJJA85.aggregated_by('year', iris.analysis.MEAN)
    CNRMJJA85 = CNRMJJA85.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIJJA85 = CNRMSMHIJJA85.aggregated_by('year', iris.analysis.MEAN)
    CSIROJJA85 = CSIROJJA85.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIJJA85 = ICHECDMIJJA85.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMJJA85 = ICHECCCLMJJA85.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIJJA85 = ICHECKNMIJJA85.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIJJA85 = ICHECMPIJJA85.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIJJA85 = ICHECSMHIJJA85.aggregated_by('year', iris.analysis.MEAN)
    IPSLJJA85 = IPSLJJA85.aggregated_by('year', iris.analysis.MEAN)
    MIROCJJA85 = MIROCJJA85.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMJJA85 = MOHCCCLMJJA85.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIJJA85 = MOHCKNMIJJA85.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIJJA85 = MOHCSMHIJJA85.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMJJA85 = MPICCLMJJA85.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOJJA85 = MPIREMOJJA85.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIJJA85 = MPISMHIJJA85.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIJJA85 = NCCSMHIJJA85.aggregated_by('year', iris.analysis.MEAN)
    NOAAJJA85 = NOAAJJA85.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMYR = CCCmaCanRCM.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIYR = CCCmaSMHI.aggregated_by('year', iris.analysis.MEAN)
    CNRMYR = CNRM.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIYR = CNRMSMHI.aggregated_by('year', iris.analysis.MEAN)
    CSIROYR = CSIRO.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIYR = ICHECDMI.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMYR = ICHECCCLM.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIYR = ICHECKNMI.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIYR = ICHECMPI.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIYR = ICHECSMHI.aggregated_by('year', iris.analysis.MEAN)
    IPSLYR = IPSL.aggregated_by('year', iris.analysis.MEAN)
    MIROCYR = MIROC.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMYR = MOHCCCLM.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIYR = MOHCKNMI.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIYR = MOHCSMHI.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMYR = MPICCLM.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOYR = MPIREMO.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIYR = MPISMHI.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIYR = NCCSMHI.aggregated_by('year', iris.analysis.MEAN)
    NOAAYR = NOAA.aggregated_by('year', iris.analysis.MEAN)
    
    CCCmaCanRCMYR85 = CCCmaCanRCM85.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIYR85 = CCCmaSMHI85.aggregated_by('year', iris.analysis.MEAN)
    CNRMYR85 = CNRM85.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIYR85 = CNRMSMHI85.aggregated_by('year', iris.analysis.MEAN)
    CSIROYR85 = CSIRO85.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIYR85 = ICHECDMI85.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMYR85 = ICHECCCLM85.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIYR85 = ICHECKNMI85.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIYR85 = ICHECMPI85.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIYR85 = ICHECSMHI85.aggregated_by('year', iris.analysis.MEAN)
    IPSLYR85 = IPSL85.aggregated_by('year', iris.analysis.MEAN)
    MIROCYR85 = MIROC85.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMYR85 = MOHCCCLM85.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIYR85 = MOHCKNMI85.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIYR85 = MOHCSMHI85.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMYR85 = MPICCLM85.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOYR85 = MPIREMO85.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIYR85 = MPISMHI85.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIYR85 = NCCSMHI85.aggregated_by('year', iris.analysis.MEAN)
    NOAAYR85 = NOAA85.aggregated_by('year', iris.analysis.MEAN)
   
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCMSON_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMSON)
    CCCmaSMHISON_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHISON)
    CNRMSON_grid_areas = iris.analysis.cartography.area_weights(CNRMSON)
    CNRMSMHISON_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHISON)
    CSIROSON_grid_areas = iris.analysis.cartography.area_weights(CSIROSON)
    ICHECDMISON_grid_areas = iris.analysis.cartography.area_weights(ICHECDMISON)
    ICHECCCLMSON_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMSON)
    ICHECKNMISON_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMISON)
    ICHECMPISON_grid_areas = iris.analysis.cartography.area_weights(ICHECMPISON)
    ICHECSMHISON_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHISON)
    IPSLSON_grid_areas = iris.analysis.cartography.area_weights(IPSLSON)
    MIROCSON_grid_areas = iris.analysis.cartography.area_weights(MIROCSON)
    MOHCCCLMSON_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMSON)
    MOHCKNMISON_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMISON)
    MOHCSMHISON_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHISON)
    MPICCLMSON_grid_areas = iris.analysis.cartography.area_weights(MPICCLMSON)
    MPIREMOSON_grid_areas = iris.analysis.cartography.area_weights(MPIREMOSON)
    MPISMHISON_grid_areas = iris.analysis.cartography.area_weights(MPISMHISON)
    NCCSMHISON_grid_areas = iris.analysis.cartography.area_weights(NCCSMHISON)
    NOAASON_grid_areas = iris.analysis.cartography.area_weights(NOAASON)
    
    CCCmaCanRCMSON85_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMSON85)
    CCCmaSMHISON85_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHISON85)
    CNRMSON85_grid_areas = iris.analysis.cartography.area_weights(CNRMSON85)
    CNRMSMHISON85_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHISON85)
    CSIROSON85_grid_areas = iris.analysis.cartography.area_weights(CSIROSON85)
    ICHECDMISON85_grid_areas = iris.analysis.cartography.area_weights(ICHECDMISON85)
    ICHECCCLMSON85_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMSON85)
    ICHECKNMISON85_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMISON85)
    ICHECMPISON85_grid_areas = iris.analysis.cartography.area_weights(ICHECMPISON85)
    ICHECSMHISON85_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHISON85)
    IPSLSON85_grid_areas = iris.analysis.cartography.area_weights(IPSLSON85)
    MIROCSON85_grid_areas = iris.analysis.cartography.area_weights(MIROCSON85)
    MOHCCCLMSON85_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMSON85)
    MOHCKNMISON85_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMISON85)
    MOHCSMHISON85_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHISON85)
    MPICCLMSON85_grid_areas = iris.analysis.cartography.area_weights(MPICCLMSON85)
    MPIREMOSON85_grid_areas = iris.analysis.cartography.area_weights(MPIREMOSON85)
    MPISMHISON85_grid_areas = iris.analysis.cartography.area_weights(MPISMHISON85)
    NCCSMHISON85_grid_areas = iris.analysis.cartography.area_weights(NCCSMHISON85)
    NOAASON85_grid_areas = iris.analysis.cartography.area_weights(NOAASON85)
    
    CCCmaCanRCMDJF_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMDJF)
    CCCmaSMHIDJF_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIDJF)
    CNRMDJF_grid_areas = iris.analysis.cartography.area_weights(CNRMDJF)
    CNRMSMHIDJF_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIDJF)
    CSIRODJF_grid_areas = iris.analysis.cartography.area_weights(CSIRODJF)
    ICHECDMIDJF_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIDJF)
    ICHECCCLMDJF_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMDJF)
    ICHECKNMIDJF_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIDJF)
    ICHECMPIDJF_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIDJF)
    ICHECSMHIDJF_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIDJF)
    IPSLDJF_grid_areas = iris.analysis.cartography.area_weights(IPSLDJF)
    MIROCDJF_grid_areas = iris.analysis.cartography.area_weights(MIROCDJF)
    MOHCCCLMDJF_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMDJF)
    MOHCKNMIDJF_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIDJF)
    MOHCSMHIDJF_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIDJF)
    MPICCLMDJF_grid_areas = iris.analysis.cartography.area_weights(MPICCLMDJF)
    MPIREMODJF_grid_areas = iris.analysis.cartography.area_weights(MPIREMODJF)
    MPISMHIDJF_grid_areas = iris.analysis.cartography.area_weights(MPISMHIDJF)
    NCCSMHIDJF_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIDJF)
    NOAADJF_grid_areas = iris.analysis.cartography.area_weights(NOAADJF)
    
    CCCmaCanRCMDJF85_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMDJF85)
    CCCmaSMHIDJF85_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIDJF85)
    CNRMDJF85_grid_areas = iris.analysis.cartography.area_weights(CNRMDJF85)
    CNRMSMHIDJF85_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIDJF85)
    CSIRODJF85_grid_areas = iris.analysis.cartography.area_weights(CSIRODJF85)
    ICHECDMIDJF85_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIDJF85)
    ICHECCCLMDJF85_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMDJF85)
    ICHECKNMIDJF85_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIDJF85)
    ICHECMPIDJF85_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIDJF85)
    ICHECSMHIDJF85_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIDJF85)
    IPSLDJF85_grid_areas = iris.analysis.cartography.area_weights(IPSLDJF85)
    MIROCDJF85_grid_areas = iris.analysis.cartography.area_weights(MIROCDJF85)
    MOHCCCLMDJF85_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMDJF85)
    MOHCKNMIDJF85_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIDJF85)
    MOHCSMHIDJF85_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIDJF85)
    MPICCLMDJF85_grid_areas = iris.analysis.cartography.area_weights(MPICCLMDJF85)
    MPIREMODJF85_grid_areas = iris.analysis.cartography.area_weights(MPIREMODJF85)
    MPISMHIDJF85_grid_areas = iris.analysis.cartography.area_weights(MPISMHIDJF85)
    NCCSMHIDJF85_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIDJF85)
    NOAADJF85_grid_areas = iris.analysis.cartography.area_weights(NOAADJF85)
    
    CCCmaCanRCMMAM_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMMAM)
    CCCmaSMHIMAM_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIMAM)
    CNRMMAM_grid_areas = iris.analysis.cartography.area_weights(CNRMMAM)
    CNRMSMHIMAM_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIMAM)
    CSIROMAM_grid_areas = iris.analysis.cartography.area_weights(CSIROMAM)
    ICHECDMIMAM_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIMAM)
    ICHECCCLMMAM_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMMAM)
    ICHECKNMIMAM_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIMAM)
    ICHECMPIMAM_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIMAM)
    ICHECSMHIMAM_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIMAM)
    IPSLMAM_grid_areas = iris.analysis.cartography.area_weights(IPSLMAM)
    MIROCMAM_grid_areas = iris.analysis.cartography.area_weights(MIROCMAM)
    MOHCCCLMMAM_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMMAM)
    MOHCKNMIMAM_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIMAM)
    MOHCSMHIMAM_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIMAM)
    MPICCLMMAM_grid_areas = iris.analysis.cartography.area_weights(MPICCLMMAM)
    MPIREMOMAM_grid_areas = iris.analysis.cartography.area_weights(MPIREMOMAM)
    MPISMHIMAM_grid_areas = iris.analysis.cartography.area_weights(MPISMHIMAM)
    NCCSMHIMAM_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIMAM)
    NOAAMAM_grid_areas = iris.analysis.cartography.area_weights(NOAAMAM)
    
    CCCmaCanRCMMAM85_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMMAM85)
    CCCmaSMHIMAM85_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIMAM85)
    CNRMMAM85_grid_areas = iris.analysis.cartography.area_weights(CNRMMAM85)
    CNRMSMHIMAM85_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIMAM85)
    CSIROMAM85_grid_areas = iris.analysis.cartography.area_weights(CSIROMAM85)
    ICHECDMIMAM85_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIMAM85)
    ICHECCCLMMAM85_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMMAM85)
    ICHECKNMIMAM85_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIMAM85)
    ICHECMPIMAM85_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIMAM85)
    ICHECSMHIMAM85_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIMAM85)
    IPSLMAM85_grid_areas = iris.analysis.cartography.area_weights(IPSLMAM85)
    MIROCMAM85_grid_areas = iris.analysis.cartography.area_weights(MIROCMAM85)
    MOHCCCLMMAM85_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMMAM85)
    MOHCKNMIMAM85_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIMAM85)
    MOHCSMHIMAM85_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIMAM85)
    MPICCLMMAM85_grid_areas = iris.analysis.cartography.area_weights(MPICCLMMAM85)
    MPIREMOMAM85_grid_areas = iris.analysis.cartography.area_weights(MPIREMOMAM85)
    MPISMHIMAM85_grid_areas = iris.analysis.cartography.area_weights(MPISMHIMAM85)
    NCCSMHIMAM85_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIMAM85)
    NOAAMAM85_grid_areas = iris.analysis.cartography.area_weights(NOAAMAM85)
    
    CCCmaCanRCMJJA_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMJJA)
    CCCmaSMHIJJA_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIJJA)
    CNRMJJA_grid_areas = iris.analysis.cartography.area_weights(CNRMJJA)
    CNRMSMHIJJA_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIJJA)
    CSIROJJA_grid_areas = iris.analysis.cartography.area_weights(CSIROJJA)
    ICHECDMIJJA_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIJJA)
    ICHECCCLMJJA_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMJJA)
    ICHECKNMIJJA_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIJJA)
    ICHECMPIJJA_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIJJA)
    ICHECSMHIJJA_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIJJA)
    IPSLJJA_grid_areas = iris.analysis.cartography.area_weights(IPSLJJA)
    MIROCJJA_grid_areas = iris.analysis.cartography.area_weights(MIROCJJA)
    MOHCCCLMJJA_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMJJA)
    MOHCKNMIJJA_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIJJA)
    MOHCSMHIJJA_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIJJA)
    MPICCLMJJA_grid_areas = iris.analysis.cartography.area_weights(MPICCLMJJA)
    MPIREMOJJA_grid_areas = iris.analysis.cartography.area_weights(MPIREMOJJA)
    MPISMHIJJA_grid_areas = iris.analysis.cartography.area_weights(MPISMHIJJA)
    NCCSMHIJJA_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIJJA)
    NOAAJJA_grid_areas = iris.analysis.cartography.area_weights(NOAAJJA)
    
    CCCmaCanRCMJJA85_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMJJA85)
    CCCmaSMHIJJA85_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIJJA85)
    CNRMJJA85_grid_areas = iris.analysis.cartography.area_weights(CNRMJJA85)
    CNRMSMHIJJA85_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIJJA85)
    CSIROJJA85_grid_areas = iris.analysis.cartography.area_weights(CSIROJJA85)
    ICHECDMIJJA85_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIJJA85)
    ICHECCCLMJJA85_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMJJA85)
    ICHECKNMIJJA85_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIJJA85)
    ICHECMPIJJA85_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIJJA85)
    ICHECSMHIJJA85_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIJJA85)
    IPSLJJA85_grid_areas = iris.analysis.cartography.area_weights(IPSLJJA85)
    MIROCJJA85_grid_areas = iris.analysis.cartography.area_weights(MIROCJJA85)
    MOHCCCLMJJA85_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMJJA85)
    MOHCKNMIJJA85_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIJJA85)
    MOHCSMHIJJA85_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIJJA85)
    MPICCLMJJA85_grid_areas = iris.analysis.cartography.area_weights(MPICCLMJJA85)
    MPIREMOJJA85_grid_areas = iris.analysis.cartography.area_weights(MPIREMOJJA85)
    MPISMHIJJA85_grid_areas = iris.analysis.cartography.area_weights(MPISMHIJJA85)
    NCCSMHIJJA85_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIJJA85)
    NOAAJJA85_grid_areas = iris.analysis.cartography.area_weights(NOAAJJA85)
    
    CCCmaCanRCMYR_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMYR)
    CCCmaSMHIYR_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIYR)
    CNRMYR_grid_areas = iris.analysis.cartography.area_weights(CNRMYR)
    CNRMSMHIYR_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIYR)
    CSIROYR_grid_areas = iris.analysis.cartography.area_weights(CSIROYR)
    ICHECDMIYR_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIYR)
    ICHECCCLMYR_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMYR)
    ICHECKNMIYR_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIYR)
    ICHECMPIYR_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIYR)
    ICHECSMHIYR_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIYR)
    IPSLYR_grid_areas = iris.analysis.cartography.area_weights(IPSLYR)
    MIROCYR_grid_areas = iris.analysis.cartography.area_weights(MIROCYR)
    MOHCCCLMYR_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMYR)
    MOHCKNMIYR_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIYR)
    MOHCSMHIYR_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIYR)
    MPICCLMYR_grid_areas = iris.analysis.cartography.area_weights(MPICCLMYR)
    MPIREMOYR_grid_areas = iris.analysis.cartography.area_weights(MPIREMOYR)
    MPISMHIYR_grid_areas = iris.analysis.cartography.area_weights(MPISMHIYR)
    NCCSMHIYR_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIYR)
    NOAAYR_grid_areas = iris.analysis.cartography.area_weights(NOAAYR)
    
    CCCmaCanRCMYR85_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMYR85)
    CCCmaSMHIYR85_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIYR85)
    CNRMYR85_grid_areas = iris.analysis.cartography.area_weights(CNRMYR85)
    CNRMSMHIYR85_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIYR85)
    CSIROYR85_grid_areas = iris.analysis.cartography.area_weights(CSIROYR85)
    ICHECDMIYR85_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIYR85)
    ICHECCCLMYR85_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMYR85)
    ICHECKNMIYR85_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIYR85)
    ICHECMPIYR85_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIYR85)
    ICHECSMHIYR85_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIYR85)
    IPSLYR85_grid_areas = iris.analysis.cartography.area_weights(IPSLYR85)
    MIROCYR85_grid_areas = iris.analysis.cartography.area_weights(MIROCYR85)
    MOHCCCLMYR85_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMYR85)
    MOHCKNMIYR85_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIYR85)
    MOHCSMHIYR85_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIYR85)
    MPICCLMYR85_grid_areas = iris.analysis.cartography.area_weights(MPICCLMYR85)
    MPIREMOYR85_grid_areas = iris.analysis.cartography.area_weights(MPIREMOYR85)
    MPISMHIYR85_grid_areas = iris.analysis.cartography.area_weights(MPISMHIYR85)
    NCCSMHIYR85_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIYR85)
    NOAAYR85_grid_areas = iris.analysis.cartography.area_weights(NOAAYR85)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCMSON_mean = CCCmaCanRCMSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMSON_grid_areas) 
    CCCmaSMHISON_mean = CCCmaSMHISON.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHISON_grid_areas)
    CNRMSON_mean = CNRMSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSON_grid_areas) 
    CNRMSMHISON_mean = CNRMSMHISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHISON_grid_areas)  
    CSIROSON_mean = CSIROSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROSON_grid_areas)
    ICHECDMISON_mean = ICHECDMISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMISON_grid_areas) 
    ICHECCCLMSON_mean = ICHECCCLMSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMSON_grid_areas)
    ICHECKNMISON_mean = ICHECKNMISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMISON_grid_areas)
    ICHECMPISON_mean = ICHECMPISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPISON_grid_areas)
    ICHECSMHISON_mean = ICHECSMHISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHISON_grid_areas)
    IPSLSON_mean = IPSLSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLSON_grid_areas)
    MIROCSON_mean = MIROCSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCSON_grid_areas)
    MOHCCCLMSON_mean = MOHCCCLMSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMSON_grid_areas)
    MOHCKNMISON_mean = MOHCKNMISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMISON_grid_areas)
    MOHCSMHISON_mean = MOHCSMHISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHISON_grid_areas)
    MPICCLMSON_mean = MPICCLMSON.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMSON_grid_areas)        
    MPIREMOSON_mean = MPIREMOSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOSON_grid_areas)                         
    MPISMHISON_mean = MPISMHISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHISON_grid_areas)
    NCCSMHISON_mean = NCCSMHISON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHISON_grid_areas) 
    NOAASON_mean = NOAASON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAASON_grid_areas)
    
    CCCmaCanRCMSON85_mean = CCCmaCanRCMSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMSON85_grid_areas) 
    CCCmaSMHISON85_mean = CCCmaSMHISON85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHISON85_grid_areas)
    CNRMSON85_mean = CNRMSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSON85_grid_areas)                           
    CNRMSMHISON85_mean = CNRMSMHISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHISON85_grid_areas)  
    CSIROSON85_mean = CSIROSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROSON85_grid_areas)
    ICHECDMISON85_mean = ICHECDMISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMISON85_grid_areas) 
    ICHECCCLMSON85_mean = ICHECCCLMSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMSON85_grid_areas)
    ICHECKNMISON85_mean = ICHECKNMISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMISON85_grid_areas)
    ICHECMPISON85_mean = ICHECMPISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPISON85_grid_areas)
    ICHECSMHISON85_mean = ICHECSMHISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHISON85_grid_areas)
    IPSLSON85_mean = IPSLSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLSON85_grid_areas)
    MIROCSON85_mean = MIROCSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCSON85_grid_areas)
    MOHCCCLMSON85_mean = MOHCCCLMSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMSON85_grid_areas)
    MOHCKNMISON85_mean = MOHCKNMISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMISON85_grid_areas)
    MOHCSMHISON85_mean = MOHCSMHISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHISON85_grid_areas)
    MPICCLMSON85_mean = MPICCLMSON85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMSON85_grid_areas)        
    MPIREMOSON85_mean = MPIREMOSON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOSON85_grid_areas)          
    MPISMHISON85_mean = MPISMHISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHISON85_grid_areas)
    NCCSMHISON85_mean = NCCSMHISON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHISON85_grid_areas) 
    NOAASON85_mean = NOAASON85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAASON85_grid_areas)
    
    CCCmaCanRCMDJF_mean = CCCmaCanRCMDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMDJF_grid_areas)  
    CCCmaSMHIDJF_mean = CCCmaSMHIDJF.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIDJF_grid_areas)
    CNRMDJF_mean = CNRMDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMDJF_grid_areas) 
    CNRMSMHIDJF_mean = CNRMSMHIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIDJF_grid_areas)  
    CSIRODJF_mean = CSIRODJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRODJF_grid_areas)
    ICHECDMIDJF_mean = ICHECDMIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIDJF_grid_areas) 
    ICHECCCLMDJF_mean = ICHECCCLMDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMDJF_grid_areas)
    ICHECKNMIDJF_mean = ICHECKNMIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIDJF_grid_areas)
    ICHECMPIDJF_mean = ICHECMPIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIDJF_grid_areas)
    ICHECSMHIDJF_mean = ICHECSMHIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIDJF_grid_areas)
    IPSLDJF_mean = IPSLDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLDJF_grid_areas)
    MIROCDJF_mean = MIROCDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCDJF_grid_areas)
    MOHCCCLMDJF_mean = MOHCCCLMDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMDJF_grid_areas)
    MOHCKNMIDJF_mean = MOHCKNMIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIDJF_grid_areas)
    MOHCSMHIDJF_mean = MOHCSMHIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIDJF_grid_areas)
    MPICCLMDJF_mean = MPICCLMDJF.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMDJF_grid_areas)   
    MPIREMODJF_mean = MPIREMODJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMODJF_grid_areas)                     
    MPISMHIDJF_mean = MPISMHIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIDJF_grid_areas)
    NCCSMHIDJF_mean = NCCSMHIDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIDJF_grid_areas) 
    NOAADJF_mean = NOAADJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAADJF_grid_areas)
    
    CCCmaCanRCMDJF85_mean = CCCmaCanRCMDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMDJF85_grid_areas)  
    CCCmaSMHIDJF85_mean = CCCmaSMHIDJF85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIDJF85_grid_areas)
    CNRMDJF85_mean = CNRMDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMDJF85_grid_areas)              
    CNRMSMHIDJF85_mean = CNRMSMHIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIDJF85_grid_areas)  
    CSIRODJF85_mean = CSIRODJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRODJF85_grid_areas)
    ICHECDMIDJF85_mean = ICHECDMIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIDJF85_grid_areas) 
    ICHECCCLMDJF85_mean = ICHECCCLMDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMDJF85_grid_areas)
    ICHECKNMIDJF85_mean = ICHECKNMIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIDJF85_grid_areas)
    ICHECMPIDJF85_mean = ICHECMPIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIDJF85_grid_areas)
    ICHECSMHIDJF85_mean = ICHECSMHIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIDJF85_grid_areas)
    IPSLDJF85_mean = IPSLDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLDJF85_grid_areas)
    MIROCDJF85_mean = MIROCDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCDJF85_grid_areas)
    MOHCCCLMDJF85_mean = MOHCCCLMDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMDJF85_grid_areas)
    MOHCKNMIDJF85_mean = MOHCKNMIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIDJF85_grid_areas)
    MOHCSMHIDJF85_mean = MOHCSMHIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIDJF85_grid_areas)
    MPICCLMDJF85_mean = MPICCLMDJF85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMDJF85_grid_areas)   
    MPIREMODJF85_mean = MPIREMODJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMODJF85_grid_areas)                     
    MPISMHIDJF85_mean = MPISMHIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIDJF85_grid_areas)
    NCCSMHIDJF85_mean = NCCSMHIDJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIDJF85_grid_areas) 
    NOAADJF85_mean = NOAADJF85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAADJF85_grid_areas)
    
    CCCmaCanRCMMAM_mean = CCCmaCanRCMMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMMAM_grid_areas)     
    CCCmaSMHIMAM_mean = CCCmaSMHIMAM.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIMAM_grid_areas)
    CNRMMAM_mean = CNRMMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMMAM_grid_areas) 
    CNRMSMHIMAM_mean = CNRMSMHIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIMAM_grid_areas)  
    CSIROMAM_mean = CSIROMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROMAM_grid_areas)
    ICHECDMIMAM_mean = ICHECDMIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIMAM_grid_areas) 
    ICHECCCLMMAM_mean = ICHECCCLMMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMMAM_grid_areas)
    ICHECKNMIMAM_mean = ICHECKNMIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIMAM_grid_areas)
    ICHECMPIMAM_mean = ICHECMPIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIMAM_grid_areas)
    ICHECSMHIMAM_mean = ICHECSMHIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIMAM_grid_areas)
    IPSLMAM_mean = IPSLMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLMAM_grid_areas)
    MIROCMAM_mean = MIROCMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCMAM_grid_areas)
    MOHCCCLMMAM_mean = MOHCCCLMMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMMAM_grid_areas)
    MOHCKNMIMAM_mean = MOHCKNMIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIMAM_grid_areas)
    MOHCSMHIMAM_mean = MOHCSMHIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIMAM_grid_areas)
    MPICCLMMAM_mean = MPICCLMMAM.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMMAM_grid_areas)       
    MPIREMOMAM_mean = MPIREMOMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOMAM_grid_areas)                       
    MPISMHIMAM_mean = MPISMHIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIMAM_grid_areas)
    NCCSMHIMAM_mean = NCCSMHIMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIMAM_grid_areas) 
    NOAAMAM_mean = NOAAMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAMAM_grid_areas)

    CCCmaCanRCMMAM85_mean = CCCmaCanRCMMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMMAM85_grid_areas)     
    CCCmaSMHIMAM85_mean = CCCmaSMHIMAM85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIMAM85_grid_areas)
    CNRMMAM85_mean = CNRMMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMMAM85_grid_areas)                         
    CNRMSMHIMAM85_mean = CNRMSMHIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIMAM85_grid_areas)  
    CSIROMAM85_mean = CSIROMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROMAM85_grid_areas)
    ICHECDMIMAM85_mean = ICHECDMIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIMAM85_grid_areas) 
    ICHECCCLMMAM85_mean = ICHECCCLMMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMMAM85_grid_areas)
    ICHECKNMIMAM85_mean = ICHECKNMIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIMAM85_grid_areas)
    ICHECMPIMAM85_mean = ICHECMPIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIMAM85_grid_areas)
    ICHECSMHIMAM85_mean = ICHECSMHIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIMAM85_grid_areas)
    IPSLMAM85_mean = IPSLMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLMAM85_grid_areas)
    MIROCMAM85_mean = MIROCMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCMAM85_grid_areas)
    MOHCCCLMMAM85_mean = MOHCCCLMMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMMAM85_grid_areas)
    MOHCKNMIMAM85_mean = MOHCKNMIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIMAM85_grid_areas)
    MOHCSMHIMAM85_mean = MOHCSMHIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIMAM85_grid_areas)
    MPICCLMMAM85_mean = MPICCLMMAM85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMMAM85_grid_areas)       
    MPIREMOMAM85_mean = MPIREMOMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOMAM85_grid_areas)                     
    MPISMHIMAM85_mean = MPISMHIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIMAM85_grid_areas)
    NCCSMHIMAM85_mean = NCCSMHIMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIMAM85_grid_areas) 
    NOAAMAM85_mean = NOAAMAM85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAMAM85_grid_areas)
   
    CCCmaCanRCMJJA_mean = CCCmaCanRCMJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMJJA_grid_areas)   
    CCCmaSMHIJJA_mean = CCCmaSMHIJJA.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIJJA_grid_areas)
    CNRMJJA_mean = CNRMJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMJJA_grid_areas) 
    CNRMSMHIJJA_mean = CNRMSMHIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIJJA_grid_areas)  
    CSIROJJA_mean = CSIROJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROJJA_grid_areas)
    ICHECDMIJJA_mean = ICHECDMIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIJJA_grid_areas) 
    ICHECCCLMJJA_mean = ICHECCCLMJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMJJA_grid_areas)
    ICHECKNMIJJA_mean = ICHECKNMIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIJJA_grid_areas)
    ICHECMPIJJA_mean = ICHECMPIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIJJA_grid_areas)
    ICHECSMHIJJA_mean = ICHECSMHIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIJJA_grid_areas)
    IPSLJJA_mean = IPSLJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLJJA_grid_areas)
    MIROCJJA_mean = MIROCJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCJJA_grid_areas)
    MOHCCCLMJJA_mean = MOHCCCLMJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMJJA_grid_areas)
    MOHCKNMIJJA_mean = MOHCKNMIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIJJA_grid_areas)
    MOHCSMHIJJA_mean = MOHCSMHIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIJJA_grid_areas)
    MPICCLMJJA_mean = MPICCLMJJA.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMJJA_grid_areas)  
    MPIREMOJJA_mean = MPIREMOJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOJJA_grid_areas)                  
    MPISMHIJJA_mean = MPISMHIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIJJA_grid_areas)
    NCCSMHIJJA_mean = NCCSMHIJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIJJA_grid_areas) 
    NOAAJJA_mean = NOAAJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAJJA_grid_areas)
    
    CCCmaCanRCMJJA85_mean = CCCmaCanRCMJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMJJA85_grid_areas)   
    CCCmaSMHIJJA85_mean = CCCmaSMHIJJA85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIJJA85_grid_areas)
    CNRMJJA85_mean = CNRMJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMJJA85_grid_areas)                      
    CNRMSMHIJJA85_mean = CNRMSMHIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIJJA85_grid_areas)  
    CSIROJJA85_mean = CSIROJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROJJA85_grid_areas)
    ICHECDMIJJA85_mean = ICHECDMIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIJJA85_grid_areas) 
    ICHECCCLMJJA85_mean = ICHECCCLMJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMJJA85_grid_areas)
    ICHECKNMIJJA85_mean = ICHECKNMIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIJJA85_grid_areas)
    ICHECMPIJJA85_mean = ICHECMPIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIJJA85_grid_areas)
    ICHECSMHIJJA85_mean = ICHECSMHIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIJJA85_grid_areas)
    IPSLJJA85_mean = IPSLJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLJJA85_grid_areas)
    MIROCJJA85_mean = MIROCJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCJJA85_grid_areas)
    MOHCCCLMJJA85_mean = MOHCCCLMJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMJJA85_grid_areas)
    MOHCKNMIJJA85_mean = MOHCKNMIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIJJA85_grid_areas)
    MOHCSMHIJJA85_mean = MOHCSMHIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIJJA85_grid_areas)
    MPICCLMJJA85_mean = MPICCLMJJA85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMJJA85_grid_areas)  
    MPIREMOJJA85_mean = MPIREMOJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOJJA85_grid_areas)                  
    MPISMHIJJA85_mean = MPISMHIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIJJA85_grid_areas)
    NCCSMHIJJA85_mean = NCCSMHIJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIJJA85_grid_areas) 
    NOAAJJA85_mean = NOAAJJA85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAJJA85_grid_areas)
    
    CCCmaCanRCMYR_mean = CCCmaCanRCMYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMYR_grid_areas)   
    CCCmaSMHIYR_mean = CCCmaSMHIYR.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIYR_grid_areas)
    CNRMYR_mean = CNRMYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMYR_grid_areas)  
    CNRMSMHIYR_mean = CNRMSMHIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIYR_grid_areas)  
    CSIROYR_mean = CSIROYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROYR_grid_areas)
    ICHECDMIYR_mean = ICHECDMIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIYR_grid_areas) 
    ICHECCCLMYR_mean = ICHECCCLMYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMYR_grid_areas)
    ICHECKNMIYR_mean = ICHECKNMIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIYR_grid_areas)
    ICHECMPIYR_mean = ICHECMPIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIYR_grid_areas)
    ICHECSMHIYR_mean = ICHECSMHIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIYR_grid_areas)
    IPSLYR_mean = IPSLYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLYR_grid_areas)
    MIROCYR_mean = MIROCYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCYR_grid_areas)
    MOHCCCLMYR_mean = MOHCCCLMYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMYR_grid_areas)
    MOHCKNMIYR_mean = MOHCKNMIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIYR_grid_areas)
    MOHCSMHIYR_mean = MOHCSMHIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIYR_grid_areas)
    MPICCLMYR_mean = MPICCLMYR.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMYR_grid_areas)    
    MPIREMOYR_mean = MPIREMOYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOYR_grid_areas)                  
    MPISMHIYR_mean = MPISMHIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIYR_grid_areas)
    NCCSMHIYR_mean = NCCSMHIYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIYR_grid_areas) 
    NOAAYR_mean = NOAAYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAYR_grid_areas)
    
    CCCmaCanRCMYR85_mean = CCCmaCanRCMYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMYR85_grid_areas)   
    CCCmaSMHIYR85_mean = CCCmaSMHIYR85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIYR85_grid_areas)
    CNRMYR85_mean = CNRMYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMYR85_grid_areas)
    CNRMSMHIYR85_mean = CNRMSMHIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIYR85_grid_areas)  
    CSIROYR85_mean = CSIROYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROYR85_grid_areas)
    ICHECDMIYR85_mean = ICHECDMIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIYR85_grid_areas) 
    ICHECCCLMYR85_mean = ICHECCCLMYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMYR85_grid_areas)
    ICHECKNMIYR85_mean = ICHECKNMIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIYR85_grid_areas)
    ICHECMPIYR85_mean = ICHECMPIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIYR85_grid_areas)
    ICHECSMHIYR85_mean = ICHECSMHIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIYR85_grid_areas)
    IPSLYR85_mean = IPSLYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLYR85_grid_areas)
    MIROCYR85_mean = MIROCYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCYR85_grid_areas)
    MOHCCCLMYR85_mean = MOHCCCLMYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMYR85_grid_areas)
    MOHCKNMIYR85_mean = MOHCKNMIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIYR85_grid_areas)
    MOHCSMHIYR85_mean = MOHCSMHIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIYR85_grid_areas)
    MPICCLMYR85_mean = MPICCLMYR85.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMYR85_grid_areas)    
    MPIREMOYR85_mean = MPIREMOYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOYR85_grid_areas)                  
    MPISMHIYR85_mean = MPISMHIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIYR85_grid_areas)
    NCCSMHIYR85_mean = NCCSMHIYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIYR85_grid_areas) 
    NOAAYR85_mean = NOAAYR85.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAYR85_grid_areas)
   
    #create averages
    AverageSONRY = (CCCmaCanRCMSON_mean.data + CCCmaSMHISON_mean.data + CNRMSON_mean.data + CNRMSMHISON_mean.data + CSIROSON_mean.data + ICHECDMISON_mean.data + ICHECCCLMSON_mean.data + ICHECKNMISON_mean.data + ICHECMPISON_mean.data + ICHECSMHISON_mean.data + IPSLSON_mean.data + MIROCSON_mean.data + MOHCCCLMSON_mean.data + MOHCKNMISON_mean.data + MOHCSMHISON_mean.data + MPICCLMSON_mean.data + MPIREMOSON_mean.data + MPISMHISON_mean.data + NCCSMHISON_mean.data + NOAASON_mean.data)/20.
    AverageDJFRY = (CCCmaCanRCMDJF_mean.data + CCCmaSMHIDJF_mean.data + CNRMDJF_mean.data + CNRMSMHIDJF_mean.data + CSIRODJF_mean.data + ICHECDMIDJF_mean.data + ICHECCCLMDJF_mean.data + ICHECKNMIDJF_mean.data + ICHECMPIDJF_mean.data + ICHECSMHIDJF_mean.data + IPSLDJF_mean.data + MIROCDJF_mean.data + MOHCCCLMDJF_mean.data + MOHCKNMIDJF_mean.data + MOHCSMHIDJF_mean.data + MPICCLMDJF_mean.data + MPIREMODJF_mean.data + MPISMHIDJF_mean.data + NCCSMHIDJF_mean.data + NOAADJF_mean.data)/20.
    AverageMAMRY = (CCCmaCanRCMMAM_mean.data + CCCmaSMHIMAM_mean.data + CNRMMAM_mean.data + CNRMSMHIMAM_mean.data + CSIROMAM_mean.data + ICHECDMIMAM_mean.data + ICHECCCLMMAM_mean.data + ICHECKNMIMAM_mean.data + ICHECMPIMAM_mean.data + ICHECSMHIMAM_mean.data + IPSLMAM_mean.data + MIROCMAM_mean.data + MOHCCCLMMAM_mean.data + MOHCKNMIMAM_mean.data + MOHCSMHIMAM_mean.data + MPICCLMMAM_mean.data + MPIREMOMAM_mean.data + MPISMHIMAM_mean.data + NCCSMHIMAM_mean.data + NOAAMAM_mean.data)/20.
    AverageJJARY = (CCCmaCanRCMJJA_mean.data + CCCmaSMHIJJA_mean.data + CNRMJJA_mean.data + CNRMSMHIJJA_mean.data + CSIROJJA_mean.data + ICHECDMIJJA_mean.data + ICHECCCLMJJA_mean.data + ICHECKNMIJJA_mean.data + ICHECMPIJJA_mean.data + ICHECSMHIJJA_mean.data + IPSLJJA_mean.data + MIROCJJA_mean.data + MOHCCCLMJJA_mean.data + MOHCKNMIJJA_mean.data + MOHCSMHIJJA_mean.data + MPICCLMJJA_mean.data + MPIREMOJJA_mean.data + MPISMHIJJA_mean.data + NCCSMHIJJA_mean.data + NOAAJJA_mean.data)/20.
    AverageRY = (CCCmaCanRCMYR_mean.data + CCCmaSMHIYR_mean.data + CNRMYR_mean.data + CNRMSMHIYR_mean.data + CSIROYR_mean.data + ICHECDMIYR_mean.data + ICHECCCLMYR_mean.data + ICHECKNMIYR_mean.data + ICHECMPIYR_mean.data + ICHECSMHIYR_mean.data + IPSLYR_mean.data + MIROCYR_mean.data + MOHCCCLMYR_mean.data + MOHCKNMIYR_mean.data + MOHCSMHIYR_mean.data + MPICCLMYR_mean.data + MPIREMOYR_mean.data + MPISMHIYR_mean.data + NCCSMHIYR_mean.data + NOAAYR_mean.data)/20.

    AverageSONRY85 = (CCCmaCanRCMSON85_mean.data + CCCmaSMHISON85_mean.data + CNRMSON85_mean.data + CNRMSMHISON85_mean.data + CSIROSON85_mean.data + ICHECDMISON85_mean.data + ICHECCCLMSON85_mean.data + ICHECKNMISON85_mean.data + ICHECMPISON85_mean.data + ICHECSMHISON85_mean.data + IPSLSON85_mean.data + MIROCSON85_mean.data + MOHCCCLMSON85_mean.data + MOHCKNMISON85_mean.data + MOHCSMHISON85_mean.data + MPICCLMSON85_mean.data + MPIREMOSON85_mean.data + MPISMHISON85_mean.data + NCCSMHISON85_mean.data + NOAASON85_mean.data)/20.
    AverageDJFRY85 = (CCCmaCanRCMDJF85_mean.data + CCCmaSMHIDJF85_mean.data + CNRMDJF85_mean.data + CNRMSMHIDJF85_mean.data + CSIRODJF85_mean.data + ICHECDMIDJF85_mean.data + ICHECCCLMDJF85_mean.data + ICHECKNMIDJF85_mean.data + ICHECMPIDJF85_mean.data + ICHECSMHIDJF85_mean.data + IPSLDJF85_mean.data + MIROCDJF85_mean.data + MOHCCCLMDJF85_mean.data + MOHCKNMIDJF85_mean.data + MOHCSMHIDJF85_mean.data + MPICCLMDJF85_mean.data + MPIREMODJF85_mean.data + MPISMHIDJF85_mean.data + NCCSMHIDJF85_mean.data + NOAADJF85_mean.data)/20.
    AverageMAMRY85 = (CCCmaCanRCMMAM85_mean.data + CCCmaSMHIMAM85_mean.data + CNRMMAM85_mean.data + CNRMSMHIMAM85_mean.data + CSIROMAM85_mean.data + ICHECDMIMAM85_mean.data + ICHECCCLMMAM85_mean.data + ICHECKNMIMAM85_mean.data + ICHECMPIMAM85_mean.data + ICHECSMHIMAM85_mean.data + IPSLMAM85_mean.data + MIROCMAM85_mean.data + MOHCCCLMMAM85_mean.data + MOHCKNMIMAM85_mean.data + MOHCSMHIMAM85_mean.data + MPICCLMMAM85_mean.data + MPIREMOMAM85_mean.data + MPISMHIMAM85_mean.data + NCCSMHIMAM85_mean.data + NOAAMAM85_mean.data)/20.
    AverageJJARY85 = (CCCmaCanRCMJJA85_mean.data + CCCmaSMHIJJA85_mean.data + CNRMJJA85_mean.data + CNRMSMHIJJA85_mean.data + CSIROJJA85_mean.data + ICHECDMIJJA85_mean.data + ICHECCCLMJJA85_mean.data + ICHECKNMIJJA85_mean.data + ICHECMPIJJA85_mean.data + ICHECSMHIJJA85_mean.data + IPSLJJA85_mean.data + MIROCJJA85_mean.data + MOHCCCLMJJA85_mean.data + MOHCKNMIJJA85_mean.data + MOHCSMHIJJA85_mean.data + MPICCLMJJA85_mean.data + MPIREMOJJA85_mean.data + MPISMHIJJA85_mean.data + NCCSMHIJJA85_mean.data + NOAAJJA85_mean.data)/20.
    AverageRY85 = (CCCmaCanRCMYR85_mean.data + CCCmaSMHIYR85_mean.data + CNRMYR85_mean.data + CNRMSMHIYR85_mean.data + CSIROYR85_mean.data + ICHECDMIYR85_mean.data + ICHECCCLMYR85_mean.data + ICHECKNMIYR85_mean.data + ICHECMPIYR85_mean.data + ICHECSMHIYR85_mean.data + IPSLYR85_mean.data + MIROCYR85_mean.data + MOHCCCLMYR85_mean.data + MOHCKNMIYR85_mean.data + MOHCSMHIYR85_mean.data + MPICCLMYR85_mean.data + MPIREMOYR85_mean.data + MPISMHIYR85_mean.data + NCCSMHIYR85_mean.data + NOAAYR85_mean.data)/20.
    
    X2 = np.array ([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070])
    
    
    #-------------------------------------------------------------------------
    #PART 8: PLOT LINE GRAPH
    print "Average RCM RCP 4.5"
    print AverageRY
    print "Average RCM RCP 8.5"
    print AverageRY85
    
    print "Average RCM RCP 4.5 SON"
    print AverageSONRY
    print "Average RCM RCP 8.5 SON"
    print AverageSONRY85

    print "Average RCM RCP 4.5 DJF"
    print AverageDJFRY
    print "Average RCM RCP 8.5 DJF"
    print AverageDJFRY85

    print "Average RCM RCP 4.5 MAM"
    print AverageMAMRY
    print "Average RCM RCP 8.5 MAM"
    print AverageMAMRY85

    print "Average RCM RCP 4.5 JJA"
    print AverageJJARY
    print "Average RCM RCP 8.5 JJA"
    print AverageJJARY85 
    
    
    #PART 8A: Regional Climate Models Line Graph
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMSON_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHISON_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMSON_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHISON_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROSON_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMISON_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMSON_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMISON_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPISON_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHISON_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLSON_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCSON_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMSON_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMISON_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHISON_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMSON_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOSON_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHISON_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHISON_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAASON_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageSONRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi SON 2006-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_SON_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMDJF_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIDJF_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMDJF_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIDJF_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIRODJF_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIDJF_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMDJF_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIDJF_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIDJF_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIDJF_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLDJF_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCDJF_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMDJF_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIDJF_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIDJF_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMDJF_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMODJF_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIDJF_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIDJF_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAADJF_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageDJFRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi DJF 2006-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_DJF_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMMAM_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIMAM_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMMAM_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIMAM_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROMAM_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIMAM_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMMAM_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIMAM_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIMAM_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIMAM_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLMAM_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCMAM_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMMAM_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIMAM_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIMAM_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMMAM_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOMAM_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIMAM_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIMAM_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAAMAM_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageMAMRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi MAM 2006-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_MAM_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMJJA_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIJJA_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMJJA_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIJJA_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROJJA_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIJJA_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMJJA_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIJJA_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIJJA_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIJJA_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLJJA_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCJJA_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMJJA_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIJJA_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIJJA_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMJJA_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOJJA_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIJJA_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIJJA_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAAJJA_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageJJARY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi JJA 2006-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_JJA_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMYR_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIYR_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMYR_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIYR_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROYR_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIYR_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMYR_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIYR_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIYR_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIYR_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLYR_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCYR_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMYR_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIYR_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIYR_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMYR_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOYR_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIYR_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIYR_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAAYR_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi 2006-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Annual_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMSON85_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHISON85_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMSON85_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHISON85_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROSON85_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMISON85_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMSON85_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMISON85_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPISON85_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHISON85_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLSON85_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCSON85_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMSON85_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMISON85_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHISON85_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMSON85_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOSON85_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHISON85_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHISON85_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAASON85_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageSONRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi SON 2006-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_SON_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMDJF85_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIDJF85_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMDJF85_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIDJF85_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIRODJF85_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIDJF85_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMDJF85_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIDJF85_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIDJF85_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIDJF85_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLDJF85_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCDJF85_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMDJF85_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIDJF85_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIDJF85_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMDJF85_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMODJF85_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIDJF85_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIDJF85_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAADJF85_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageDJFRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi DJF 2006-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_DJF_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMMAM85_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIMAM85_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMMAM85_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIMAM85_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROMAM85_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIMAM85_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMMAM85_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIMAM85_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIMAM85_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIMAM85_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLMAM85_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCMAM85_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMMAM85_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIMAM85_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIMAM85_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMMAM85_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOMAM85_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIMAM85_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIMAM85_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAAMAM85_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageMAMRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi MAM 2006-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_MAM_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMJJA85_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIJJA85_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMJJA85_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIJJA85_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROJJA85_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIJJA85_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMJJA85_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIJJA85_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIJJA85_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIJJA85_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLJJA85_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCJJA85_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMJJA85_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIJJA85_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIJJA85_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMJJA85_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOJJA85_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIJJA85_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIJJA85_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAAJJA85_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageJJARY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi JJA 2006-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_JJA_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, CCCmaCanRCMYR85_mean.data, label='CanRCM4_CanESM2', lw=1.5, color='blue')
    plt.plot(X2, CCCmaSMHIYR85_mean.data, label='RCA4_CanESM2', lw=1.5, color='green')
    plt.plot(X2, CNRMYR85_mean.data, label='CCLM4-8-17_CNRM-CM5', lw=1.5, color='red')
    plt.plot(X2, CNRMSMHIYR85_mean.data, label='RCA4_CNRM-CM5', lw=1.5, color='cyan')
    plt.plot(X2, CSIROYR85_mean.data, label='RCA4_CSIRO-MK3', lw=1.5, color='magenta')
    plt.plot(X2, ICHECDMIYR85_mean.data, label='HIRHAM5_EC-EARTH', lw=1.5, color='yellow')
    plt.plot(X2, ICHECCCLMYR85_mean.data, label='CCLM4-8-17_EC-EARTH ', lw=1.5, color='blue', linestyle='--')
    plt.plot(X2, ICHECKNMIYR85_mean.data, label='RACMO22T_EC-EARTH', lw=1.5, color='green', linestyle='--')
    plt.plot(X2, ICHECMPIYR85_mean.data, label='REMO2009_EC-EARTH ', lw=1.5, color='red', linestyle='--') 
    plt.plot(X2, ICHECSMHIYR85_mean.data, label='RCA4_EC-EARTH', lw=1.5, color='cyan', linestyle='--') 
    plt.plot(X2, IPSLYR85_mean.data, label='RCA4_IPSL-CM5A-MR', lw=1.5, color='magenta', linestyle='--') 
    plt.plot(X2, MIROCYR85_mean.data, label='RCA4_MIROC5', lw=1.5, color='yellow', linestyle='--')
    plt.plot(X2, MOHCCCLMYR85_mean.data, label='CCLM4-8-17_HadGEM2-ES', lw=1.5, color='blue', linestyle='-.')
    plt.plot(X2, MOHCKNMIYR85_mean.data, label='RACMO22T_HadGEM2-ES', lw=1.5, color='green', linestyle='-.')
    plt.plot(X2, MOHCSMHIYR85_mean.data, label='RCA4_HadGEM2-ES', lw=1.5, color='red', linestyle='-.')
    plt.plot(X2, MPICCLMYR85_mean.data, label='CCLM4-8-17_MPI-ESM-LR', lw=1.5, color='cyan', linestyle='-.')
    plt.plot(X2, MPIREMOYR85_mean.data, label='REMO2009_MPI-ESM-LR ', lw=1.5, color='magenta', linestyle='-.')
    plt.plot(X2, MPISMHIYR85_mean.data, label='RCA4_MPI-ESM-LR ', lw=1.5, color='yellow', linestyle='-.')
    plt.plot(X2, NCCSMHIYR85_mean.data, label='RCA4_NorESM1-M', lw=1.5, color='blue', linestyle=':')
    plt.plot(X2, NOAAYR85_mean.data, label='RCA4_GFDL-ESM2M', lw=1.5, color='green', linestyle=':') 
    plt.plot(X2, AverageRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('ETo for Central Malawi 2006-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Annual_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #PART 8B: Average Line Graph
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, AverageSONRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageSONRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('ETo for Central Malawi SON 2006-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_SON_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, AverageDJFRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageDJFRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('ETo for Central Malawi DJF 2006-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_DJF_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, AverageMAMRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageMAMRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('ETo for Central Malawi MAM 2006-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_MAM_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, AverageJJARY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageJJARY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('ETo for Central Malawi JJA 2006-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_JJA_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((2006,2070)) 
    
    #set y axis limits
    plt.ylim(0,5)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X2, AverageRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Water Evaporation Flux (mm per day)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('ETo for Central Malawi 2006-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('ETo_LineGraph_Annual_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
if __name__ == '__main__':
    main()