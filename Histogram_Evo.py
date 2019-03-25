"""
Created on Thursday May 24th 2018

@author: s0899345
"""

import numpy as np
import iris
import iris.coord_categorisation as iriscc
import iris.analysis.cartography

#this file is split into parts as follows:
    #PART 1: Load and Format all Future Models
    #PART 2: Format Data General
    #PART 3: Format for Time Periods
    #PART 4: print data

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
    
    #Convert evaporation units from kg m-2 s-1 to mm day-1. Since kg m-2 of water to mm of water is 1 to 1, there are 60sec/min, 60min/hour, and 24hour/day the conversion is:
    Convert=60*60*24
    
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
    
    #add day of the year to all files
    iriscc.add_day_of_year(CCCmaCanRCM, 'time')
    iriscc.add_day_of_year(CCCmaSMHI, 'time')
    iriscc.add_day_of_year(CNRM, 'time')
    iriscc.add_day_of_year(CNRMSMHI, 'time')
    iriscc.add_day_of_year(CSIRO, 'time')
    iriscc.add_day_of_year(ICHECDMI, 'time')
    iriscc.add_day_of_year(ICHECCCLM, 'time')
    iriscc.add_day_of_year(ICHECKNMI, 'time')
    iriscc.add_day_of_year(ICHECMPI, 'time')
    iriscc.add_day_of_year(ICHECSMHI, 'time')
    iriscc.add_day_of_year(IPSL, 'time')
    iriscc.add_day_of_year(MIROC, 'time')
    iriscc.add_day_of_year(MOHCCCLM, 'time')
    iriscc.add_day_of_year(MOHCKNMI, 'time')
    iriscc.add_day_of_year(MOHCSMHI, 'time')
    iriscc.add_day_of_year(MPICCLM, 'time')
    iriscc.add_day_of_year(MPIREMO, 'time')
    iriscc.add_day_of_year(MPISMHI, 'time')
    iriscc.add_day_of_year(NCCSMHI, 'time')
    iriscc.add_day_of_year(NOAA, 'time')
    
    iriscc.add_day_of_year(CCCmaCanRCM85, 'time')
    iriscc.add_day_of_year(CCCmaSMHI85, 'time')
    iriscc.add_day_of_year(CNRM85, 'time')
    iriscc.add_day_of_year(CNRMSMHI85, 'time')
    iriscc.add_day_of_year(CSIRO85, 'time')
    iriscc.add_day_of_year(ICHECDMI85, 'time')
    iriscc.add_day_of_year(ICHECCCLM85, 'time')
    iriscc.add_day_of_year(ICHECKNMI85, 'time')
    iriscc.add_day_of_year(ICHECMPI85, 'time')
    iriscc.add_day_of_year(ICHECSMHI85, 'time')
    iriscc.add_day_of_year(IPSL85, 'time')
    iriscc.add_day_of_year(MIROC85, 'time')
    iriscc.add_day_of_year(MOHCCCLM85, 'time')
    iriscc.add_day_of_year(MOHCKNMI85, 'time')
    iriscc.add_day_of_year(MOHCSMHI85, 'time')
    iriscc.add_day_of_year(MPICCLM85, 'time')
    iriscc.add_day_of_year(MPIREMO85, 'time')
    iriscc.add_day_of_year(MPISMHI85, 'time')
    iriscc.add_day_of_year(NCCSMHI85, 'time')
    iriscc.add_day_of_year(NOAA85, 'time')
    
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
    
    
    #-------------------------------------------------------------------------
    #PART 3: FORMAT FOR TIME PERIODS
    #PART 3A: FORMAT FOR 2030
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_30 = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)
    
    CCCmaCanRCM_30 = CCCmaCanRCM.extract(t_constraint_30)
    CCCmaSMHI_30 = CCCmaSMHI.extract(t_constraint_30)
    CNRM_30 = CNRM.extract(t_constraint_30)
    CNRMSMHI_30 = CNRMSMHI.extract(t_constraint_30)
    CSIRO_30 = CSIRO.extract(t_constraint_30)
    ICHECDMI_30 = ICHECDMI.extract(t_constraint_30)
    ICHECCCLM_30 = ICHECCCLM.extract(t_constraint_30)
    ICHECKNMI_30 = ICHECKNMI.extract(t_constraint_30)
    ICHECMPI_30 = ICHECMPI.extract(t_constraint_30)
    ICHECSMHI_30 = ICHECSMHI.extract(t_constraint_30)
    IPSL_30 = IPSL.extract(t_constraint_30)
    MIROC_30 = MIROC.extract(t_constraint_30)
    MOHCCCLM_30 = MOHCCCLM.extract(t_constraint_30)
    MOHCKNMI_30 = MOHCKNMI.extract(t_constraint_30)
    MOHCSMHI_30 = MOHCSMHI.extract(t_constraint_30)
    MPICCLM_30 = MPICCLM.extract(t_constraint_30)
    MPIREMO_30 = MPIREMO.extract(t_constraint_30)
    MPISMHI_30 = MPISMHI.extract(t_constraint_30)
    NCCSMHI_30 = NCCSMHI.extract(t_constraint_30)
    NOAA_30 = NOAA.extract(t_constraint_30) 
    
    CCCmaCanRCM85_30 = CCCmaCanRCM85.extract(t_constraint_30)
    CCCmaSMHI85_30 = CCCmaSMHI85.extract(t_constraint_30)
    CNRM85_30 = CNRM85.extract(t_constraint_30)
    CNRMSMHI85_30 = CNRMSMHI85.extract(t_constraint_30)
    CSIRO85_30 = CSIRO85.extract(t_constraint_30)
    ICHECDMI85_30 = ICHECDMI85.extract(t_constraint_30)
    ICHECCCLM85_30 = ICHECCCLM85.extract(t_constraint_30)
    ICHECKNMI85_30 = ICHECKNMI85.extract(t_constraint_30)
    ICHECMPI85_30 = ICHECMPI85.extract(t_constraint_30)
    ICHECSMHI85_30 = ICHECSMHI85.extract(t_constraint_30)
    IPSL85_30 = IPSL85.extract(t_constraint_30)
    MIROC85_30 = MIROC85.extract(t_constraint_30)
    MOHCCCLM85_30 = MOHCCCLM85.extract(t_constraint_30)
    MOHCKNMI85_30 = MOHCKNMI85.extract(t_constraint_30)
    MOHCSMHI85_30 = MOHCSMHI85.extract(t_constraint_30)
    MPICCLM85_30 = MPICCLM85.extract(t_constraint_30)
    MPIREMO85_30 = MPIREMO85.extract(t_constraint_30)
    MPISMHI85_30 = MPISMHI85.extract(t_constraint_30)
    NCCSMHI85_30 = NCCSMHI85.extract(t_constraint_30)
    NOAA85_30 = NOAA85.extract(t_constraint_30) 
    
    #We are interested in plotting the data by days of the year, so we need to take a mean of all the data by day
    CCCmaCanRCM_30 = CCCmaCanRCM_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_30 = CCCmaSMHI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_30 = CNRM_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_30 = CNRMSMHI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_30 = CSIRO_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_30 = ICHECDMI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_30 = ICHECCCLM_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_30 = ICHECKNMI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_30 = ICHECMPI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_30 = ICHECSMHI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    IPSL_30 = IPSL_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_30 = MIROC_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_30 = MOHCCCLM_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_30 = MOHCKNMI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_30 = MOHCSMHI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_30 = MPICCLM_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_30 = MPIREMO_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_30 = MPISMHI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_30 = NCCSMHI_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_30 = NOAA_30.aggregated_by('day_of_year', iris.analysis.MEAN) 
    
    CCCmaCanRCM85_30 = CCCmaCanRCM85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_30 = CCCmaSMHI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_30 = CNRM85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_30 = CNRMSMHI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_30 = CSIRO85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_30 = ICHECDMI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_30 = ICHECCCLM85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_30 = ICHECKNMI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_30 = ICHECMPI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_30 = ICHECSMHI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    IPSL85_30 = IPSL85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_30 = MIROC85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_30 = MOHCCCLM85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_30 = MOHCKNMI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_30 = MOHCSMHI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_30 = MPICCLM85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_30 = MPIREMO85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_30 = MPISMHI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_30 = NCCSMHI85_30.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_30 = NOAA85_30.aggregated_by('day_of_year', iris.analysis.MEAN) 

    #Returns an array of area weights, with the same dimensions as the cube    
    CCCmaCanRCM_30_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_30)
    CCCmaSMHI_30_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_30)
    CNRM_30_grid_areas = iris.analysis.cartography.area_weights(CNRM_30)
    CNRMSMHI_30_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_30)
    CSIRO_30_grid_areas = iris.analysis.cartography.area_weights(CSIRO_30)
    ICHECDMI_30_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_30)
    ICHECCCLM_30_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_30)
    ICHECKNMI_30_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_30)
    ICHECMPI_30_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_30)
    ICHECSMHI_30_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_30)
    IPSL_30_grid_areas = iris.analysis.cartography.area_weights(IPSL_30)
    MIROC_30_grid_areas = iris.analysis.cartography.area_weights(MIROC_30)
    MOHCCCLM_30_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_30)
    MOHCKNMI_30_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_30)
    MOHCSMHI_30_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_30)
    MPICCLM_30_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_30)
    MPIREMO_30_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_30)
    MPISMHI_30_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_30)
    NCCSMHI_30_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_30)
    NOAA_30_grid_areas = iris.analysis.cartography.area_weights(NOAA_30)
    
    CCCmaCanRCM85_30_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_30)
    CCCmaSMHI85_30_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_30)
    CNRM85_30_grid_areas = iris.analysis.cartography.area_weights(CNRM85_30)
    CNRMSMHI85_30_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_30)
    CSIRO85_30_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_30)
    ICHECDMI85_30_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_30)
    ICHECCCLM85_30_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_30)
    ICHECKNMI85_30_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_30)
    ICHECMPI85_30_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_30)
    ICHECSMHI85_30_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_30)
    IPSL85_30_grid_areas = iris.analysis.cartography.area_weights(IPSL85_30)
    MIROC85_30_grid_areas = iris.analysis.cartography.area_weights(MIROC85_30)
    MOHCCCLM85_30_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_30)
    MOHCKNMI85_30_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_30)
    MOHCSMHI85_30_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_30)
    MPICCLM85_30_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_30)
    MPIREMO85_30_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_30)
    MPISMHI85_30_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_30)
    NCCSMHI85_30_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_30)
    NOAA85_30_grid_areas = iris.analysis.cartography.area_weights(NOAA85_30)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_30_mean = CCCmaCanRCM_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_30_grid_areas) 
    CCCmaSMHI_30_mean = CCCmaSMHI_30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_30_grid_areas)
    CNRM_30_mean = CNRM_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_30_grid_areas)                           
    CNRMSMHI_30_mean = CNRMSMHI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_30_grid_areas)  
    CSIRO_30_mean = CSIRO_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_30_grid_areas)
    ICHECDMI_30_mean = ICHECDMI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_30_grid_areas) 
    ICHECCCLM_30_mean = ICHECCCLM_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_30_grid_areas)
    ICHECKNMI_30_mean = ICHECKNMI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_30_grid_areas)
    ICHECMPI_30_mean = ICHECMPI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_30_grid_areas)
    ICHECSMHI_30_mean = ICHECSMHI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_30_grid_areas)
    IPSL_30_mean = IPSL_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_30_grid_areas)
    MIROC_30_mean = MIROC_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_30_grid_areas)
    MOHCCCLM_30_mean = MOHCCCLM_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_30_grid_areas)
    MOHCKNMI_30_mean = MOHCKNMI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_30_grid_areas)
    MOHCSMHI_30_mean = MOHCSMHI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_30_grid_areas)
    MPICCLM_30_mean = MPICCLM_30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_30_grid_areas)        
    MPIREMO_30_mean = MPIREMO_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_30_grid_areas)                         
    MPISMHI_30_mean = MPISMHI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_30_grid_areas)
    NCCSMHI_30_mean = NCCSMHI_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_30_grid_areas) 
    NOAA_30_mean = NOAA_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_30_grid_areas)
    
    CCCmaCanRCM85_30_mean = CCCmaCanRCM85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_30_grid_areas) 
    CCCmaSMHI85_30_mean = CCCmaSMHI85_30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_30_grid_areas)
    CNRM85_30_mean = CNRM85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_30_grid_areas)                           
    CNRMSMHI85_30_mean = CNRMSMHI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_30_grid_areas)  
    CSIRO85_30_mean = CSIRO85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_30_grid_areas)
    ICHECDMI85_30_mean = ICHECDMI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_30_grid_areas) 
    ICHECCCLM85_30_mean = ICHECCCLM85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_30_grid_areas)
    ICHECKNMI85_30_mean = ICHECKNMI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_30_grid_areas)
    ICHECMPI85_30_mean = ICHECMPI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_30_grid_areas)
    ICHECSMHI85_30_mean = ICHECSMHI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_30_grid_areas)
    IPSL85_30_mean = IPSL85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_30_grid_areas)
    MIROC85_30_mean = MIROC85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_30_grid_areas)
    MOHCCCLM85_30_mean = MOHCCCLM85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_30_grid_areas)
    MOHCKNMI85_30_mean = MOHCKNMI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_30_grid_areas)
    MOHCSMHI85_30_mean = MOHCSMHI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_30_grid_areas)
    MPICCLM85_30_mean = MPICCLM85_30.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_30_grid_areas)        
    MPIREMO85_30_mean = MPIREMO85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_30_grid_areas)                         
    MPISMHI85_30_mean = MPISMHI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_30_grid_areas)
    NCCSMHI85_30_mean = NCCSMHI85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_30_grid_areas) 
    NOAA85_30_mean = NOAA85_30.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_30_grid_areas)
    
    #PART 3B: FORMAT FOR 2050
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_50 = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)

    CCCmaCanRCM_50 = CCCmaCanRCM.extract(t_constraint_50)
    CCCmaSMHI_50 = CCCmaSMHI.extract(t_constraint_50)
    CNRM_50 = CNRM.extract(t_constraint_50)
    CNRMSMHI_50 = CNRMSMHI.extract(t_constraint_50)
    CSIRO_50 = CSIRO.extract(t_constraint_50)
    ICHECDMI_50 = ICHECDMI.extract(t_constraint_50)
    ICHECCCLM_50 = ICHECCCLM.extract(t_constraint_50)
    ICHECKNMI_50 = ICHECKNMI.extract(t_constraint_50)
    ICHECMPI_50 = ICHECMPI.extract(t_constraint_50)
    ICHECSMHI_50 = ICHECSMHI.extract(t_constraint_50)
    IPSL_50 = IPSL.extract(t_constraint_50)
    MIROC_50 = MIROC.extract(t_constraint_50)
    MOHCCCLM_50 = MOHCCCLM.extract(t_constraint_50)
    MOHCKNMI_50 = MOHCKNMI.extract(t_constraint_50)
    MOHCSMHI_50 = MOHCSMHI.extract(t_constraint_50)
    MPICCLM_50 = MPICCLM.extract(t_constraint_50)
    MPIREMO_50 = MPIREMO.extract(t_constraint_50)
    MPISMHI_50 = MPISMHI.extract(t_constraint_50)
    NCCSMHI_50 = NCCSMHI.extract(t_constraint_50)
    NOAA_50 = NOAA.extract(t_constraint_50) 
    
    CCCmaCanRCM85_50 = CCCmaCanRCM85.extract(t_constraint_50)
    CCCmaSMHI85_50 = CCCmaSMHI85.extract(t_constraint_50)
    CNRM85_50 = CNRM85.extract(t_constraint_50)
    CNRMSMHI85_50 = CNRMSMHI85.extract(t_constraint_50)
    CSIRO85_50 = CSIRO85.extract(t_constraint_50)
    ICHECDMI85_50 = ICHECDMI85.extract(t_constraint_50)
    ICHECCCLM85_50 = ICHECCCLM85.extract(t_constraint_50)
    ICHECKNMI85_50 = ICHECKNMI85.extract(t_constraint_50)
    ICHECMPI85_50 = ICHECMPI85.extract(t_constraint_50)
    ICHECSMHI85_50 = ICHECSMHI85.extract(t_constraint_50)
    IPSL85_50 = IPSL85.extract(t_constraint_50)
    MIROC85_50 = MIROC85.extract(t_constraint_50)
    MOHCCCLM85_50 = MOHCCCLM85.extract(t_constraint_50)
    MOHCKNMI85_50 = MOHCKNMI85.extract(t_constraint_50)
    MOHCSMHI85_50 = MOHCSMHI85.extract(t_constraint_50)
    MPICCLM85_50 = MPICCLM85.extract(t_constraint_50)
    MPIREMO85_50 = MPIREMO85.extract(t_constraint_50)
    MPISMHI85_50 = MPISMHI85.extract(t_constraint_50)
    NCCSMHI85_50 = NCCSMHI85.extract(t_constraint_50)
    NOAA85_50 = NOAA85.extract(t_constraint_50) 
    
    #We are interested in plotting the data by days of the year, so we need to take a mean of all the data by day
    CCCmaCanRCM_50 = CCCmaCanRCM_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI_50 = CCCmaSMHI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM_50 = CNRM_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI_50 = CNRMSMHI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO_50 = CSIRO_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI_50 = ICHECDMI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM_50 = ICHECCCLM_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI_50 = ICHECKNMI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI_50 = ICHECMPI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI_50 = ICHECSMHI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    IPSL_50 = IPSL_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC_50 = MIROC_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM_50 = MOHCCCLM_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI_50 = MOHCKNMI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI_50 = MOHCSMHI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM_50 = MPICCLM_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO_50 = MPIREMO_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI_50 = MPISMHI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI_50 = NCCSMHI_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA_50 = NOAA_50.aggregated_by('day_of_year', iris.analysis.MEAN) 
    
    CCCmaCanRCM85_50 = CCCmaCanRCM85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CCCmaSMHI85_50 = CCCmaSMHI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRM85_50 = CNRM85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CNRMSMHI85_50 = CNRMSMHI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    CSIRO85_50 = CSIRO85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECDMI85_50 = ICHECDMI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECCCLM85_50 = ICHECCCLM85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECKNMI85_50 = ICHECKNMI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECMPI85_50 = ICHECMPI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    ICHECSMHI85_50 = ICHECSMHI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    IPSL85_50 = IPSL85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MIROC85_50 = MIROC85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCCCLM85_50 = MOHCCCLM85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCKNMI85_50 = MOHCKNMI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MOHCSMHI85_50 = MOHCSMHI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPICCLM85_50 = MPICCLM85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPIREMO85_50 = MPIREMO85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    MPISMHI85_50 = MPISMHI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    NCCSMHI85_50 = NCCSMHI85_50.aggregated_by('day_of_year', iris.analysis.MEAN)
    NOAA85_50 = NOAA85_50.aggregated_by('day_of_year', iris.analysis.MEAN) 

    #Returns an array of area weights, with the same dimensions as the cube    
    CCCmaCanRCM_50_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_50)
    CCCmaSMHI_50_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_50)
    CNRM_50_grid_areas = iris.analysis.cartography.area_weights(CNRM_50)
    CNRMSMHI_50_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_50)
    CSIRO_50_grid_areas = iris.analysis.cartography.area_weights(CSIRO_50)
    ICHECDMI_50_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_50)
    ICHECCCLM_50_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_50)
    ICHECKNMI_50_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_50)
    ICHECMPI_50_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_50)
    ICHECSMHI_50_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_50)
    IPSL_50_grid_areas = iris.analysis.cartography.area_weights(IPSL_50)
    MIROC_50_grid_areas = iris.analysis.cartography.area_weights(MIROC_50)
    MOHCCCLM_50_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_50)
    MOHCKNMI_50_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_50)
    MOHCSMHI_50_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_50)
    MPICCLM_50_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_50)
    MPIREMO_50_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_50)
    MPISMHI_50_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_50)
    NCCSMHI_50_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_50)
    NOAA_50_grid_areas = iris.analysis.cartography.area_weights(NOAA_50)
    
    CCCmaCanRCM85_50_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM85_50)
    CCCmaSMHI85_50_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI85_50)
    CNRM85_50_grid_areas = iris.analysis.cartography.area_weights(CNRM85_50)
    CNRMSMHI85_50_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI85_50)
    CSIRO85_50_grid_areas = iris.analysis.cartography.area_weights(CSIRO85_50)
    ICHECDMI85_50_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI85_50)
    ICHECCCLM85_50_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM85_50)
    ICHECKNMI85_50_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI85_50)
    ICHECMPI85_50_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI85_50)
    ICHECSMHI85_50_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI85_50)
    IPSL85_50_grid_areas = iris.analysis.cartography.area_weights(IPSL85_50)
    MIROC85_50_grid_areas = iris.analysis.cartography.area_weights(MIROC85_50)
    MOHCCCLM85_50_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM85_50)
    MOHCKNMI85_50_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI85_50)
    MOHCSMHI85_50_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI85_50)
    MPICCLM85_50_grid_areas = iris.analysis.cartography.area_weights(MPICCLM85_50)
    MPIREMO85_50_grid_areas = iris.analysis.cartography.area_weights(MPIREMO85_50)
    MPISMHI85_50_grid_areas = iris.analysis.cartography.area_weights(MPISMHI85_50)
    NCCSMHI85_50_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI85_50)
    NOAA85_50_grid_areas = iris.analysis.cartography.area_weights(NOAA85_50)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_50_mean = CCCmaCanRCM_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_50_grid_areas) 
    CCCmaSMHI_50_mean = CCCmaSMHI_50.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_50_grid_areas)
    CNRM_50_mean = CNRM_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_50_grid_areas)                           
    CNRMSMHI_50_mean = CNRMSMHI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_50_grid_areas)  
    CSIRO_50_mean = CSIRO_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_50_grid_areas)
    ICHECDMI_50_mean = ICHECDMI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_50_grid_areas) 
    ICHECCCLM_50_mean = ICHECCCLM_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_50_grid_areas)
    ICHECKNMI_50_mean = ICHECKNMI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_50_grid_areas)
    ICHECMPI_50_mean = ICHECMPI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_50_grid_areas)
    ICHECSMHI_50_mean = ICHECSMHI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_50_grid_areas)
    IPSL_50_mean = IPSL_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_50_grid_areas)
    MIROC_50_mean = MIROC_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_50_grid_areas)
    MOHCCCLM_50_mean = MOHCCCLM_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_50_grid_areas)
    MOHCKNMI_50_mean = MOHCKNMI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_50_grid_areas)
    MOHCSMHI_50_mean = MOHCSMHI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_50_grid_areas)
    MPICCLM_50_mean = MPICCLM_50.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_50_grid_areas)        
    MPIREMO_50_mean = MPIREMO_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_50_grid_areas)                         
    MPISMHI_50_mean = MPISMHI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_50_grid_areas)
    NCCSMHI_50_mean = NCCSMHI_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_50_grid_areas) 
    NOAA_50_mean = NOAA_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_50_grid_areas)
    
    CCCmaCanRCM85_50_mean = CCCmaCanRCM85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM85_50_grid_areas) 
    CCCmaSMHI85_50_mean = CCCmaSMHI85_50.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI85_50_grid_areas)
    CNRM85_50_mean = CNRM85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM85_50_grid_areas)                           
    CNRMSMHI85_50_mean = CNRMSMHI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI85_50_grid_areas)  
    CSIRO85_50_mean = CSIRO85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO85_50_grid_areas)
    ICHECDMI85_50_mean = ICHECDMI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI85_50_grid_areas) 
    ICHECCCLM85_50_mean = ICHECCCLM85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM85_50_grid_areas)
    ICHECKNMI85_50_mean = ICHECKNMI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI85_50_grid_areas)
    ICHECMPI85_50_mean = ICHECMPI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI85_50_grid_areas)
    ICHECSMHI85_50_mean = ICHECSMHI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI85_50_grid_areas)
    IPSL85_50_mean = IPSL85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL85_50_grid_areas)
    MIROC85_50_mean = MIROC85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC85_50_grid_areas)
    MOHCCCLM85_50_mean = MOHCCCLM85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM85_50_grid_areas)
    MOHCKNMI85_50_mean = MOHCKNMI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI85_50_grid_areas)
    MOHCSMHI85_50_mean = MOHCSMHI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI85_50_grid_areas)
    MPICCLM85_50_mean = MPICCLM85_50.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM85_50_grid_areas)        
    MPIREMO85_50_mean = MPIREMO85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO85_50_grid_areas)                         
    MPISMHI85_50_mean = MPISMHI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI85_50_grid_areas)
    NCCSMHI85_50_mean = NCCSMHI85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI85_50_grid_areas) 
    NOAA85_50_mean = NOAA85_50.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA85_50_grid_areas)
    
   
    #-------------------------------------------------------------------------
    #PART 4: PRINT DATA
    import csv
    with open('output_EVOdata.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
     #PART 3A: WRITE RCP 4.5 DATA
        writer.writerow(["CCCmaCanRCM_30_mean"] + CCCmaCanRCM_30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_30_mean"] + CCCmaSMHI_30_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM_30_mean"] + CNRM_30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_30_mean"] +CNRMSMHI_30_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO_30_mean"] +CSIRO_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_30_mean"] +ICHECDMI_30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_30_mean"] +ICHECCCLM_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI_30_mean"] +ICHECKNMI_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI_30_mean"] +ICHECMPI_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_30_mean"] +ICHECSMHI_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL_30_mean"] +IPSL_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_30_mean"] +MIROC_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_30_mean"] +MOHCCCLM_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_30_mean"] +MOHCKNMI_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_30_mean"] +MOHCSMHI_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_30_mean"] +MPICCLM_30_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_30_mean"] +MPIREMO_30_mean.data.flatten().astype(np.str).tolist())                               
        writer.writerow(["MPISMHI_30_mean"] +MPISMHI_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_30_mean"] +NCCSMHI_30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_30_mean"] +NOAA_30_mean.data.flatten().astype(np.str).tolist())     
        
        writer.writerow(["CCCmaCanRCM_50_mean"] + CCCmaCanRCM_50_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_50_mean"] + CCCmaSMHI_50_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM_50_mean"] + CNRM_50_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_50_mean"] +CNRMSMHI_50_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO_50_mean"] +CSIRO_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_50_mean"] +ICHECDMI_50_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_50_mean"] +ICHECCCLM_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI_50_mean"] +ICHECKNMI_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI_50_mean"] +ICHECMPI_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_50_mean"] +ICHECSMHI_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL_50_mean"] +IPSL_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_50_mean"] +MIROC_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_50_mean"] +MOHCCCLM_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_50_mean"] +MOHCKNMI_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_50_mean"] +MOHCSMHI_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_50_mean"] +MPICCLM_50_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_50_mean"] +MPIREMO_50_mean.data.flatten().astype(np.str).tolist())                               
        writer.writerow(["MPISMHI_50_mean"] +MPISMHI_50_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["NCCSMHI_50_mean"] +NCCSMHI_50_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_50_mean"] +NOAA_50_mean.data.flatten().astype(np.str).tolist())     
        
    #PART 3B: WRITE RCP 8.5 DATA
        writer.writerow(["CCCmaCanRCM85_30_mean"] + CCCmaCanRCM85_30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_30_mean"] + CCCmaSMHI85_30_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_30_mean"] + CNRM85_30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_30_mean"] +CNRMSMHI85_30_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO85_30_mean"] +CSIRO85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_30_mean"] +ICHECDMI85_30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM85_30_mean"] +ICHECCCLM85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI85_30_mean"] +ICHECKNMI85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI85_30_mean"] +ICHECMPI85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI85_30_mean"] +ICHECSMHI85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL85_30_mean"] +IPSL85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_30_mean"] +MIROC85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_30_mean"] +MOHCCCLM85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_30_mean"] +MOHCKNMI85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI85_30_mean"] +MOHCSMHI85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM85_30_mean"] +MPICCLM85_30_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_30_mean"] +MPIREMO85_30_mean.data.flatten().astype(np.str).tolist())                               
        writer.writerow(["MPISMHI85_30_mean"] +MPISMHI85_30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI85_30_mean"] +NCCSMHI85_30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA85_30_mean"] +NOAA85_30_mean.data.flatten().astype(np.str).tolist())     

        writer.writerow(["CCCmaCanRCM85_50_mean"] + CCCmaCanRCM85_50_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_50_mean"] + CCCmaSMHI85_50_mean.data.flatten().astype(np.str).tolist())           
        writer.writerow(["CNRM85_50_mean"] + CNRM85_50_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_50_mean"] +CNRMSMHI85_50_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO85_50_mean"] +CSIRO85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_50_mean"] +ICHECDMI85_50_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM85_50_mean"] +ICHECCCLM85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI85_50_mean"] +ICHECKNMI85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI85_50_mean"] +ICHECMPI85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI85_50_mean"] +ICHECSMHI85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL85_50_mean"] +IPSL85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_50_mean"] +MIROC85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_50_mean"] +MOHCCCLM85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_50_mean"] +MOHCKNMI85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI85_50_mean"] +MOHCSMHI85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM85_50_mean"] +MPICCLM85_50_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_50_mean"] +MPIREMO85_50_mean.data.flatten().astype(np.str).tolist())                               
        writer.writerow(["MPISMHI85_50_mean"] +MPISMHI85_50_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI85_50_mean"] +NCCSMHI85_50_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA85_50_mean"] +NOAA85_50_mean.data.flatten().astype(np.str).tolist())     
    
if __name__ == '__main__':
    main()
    
    