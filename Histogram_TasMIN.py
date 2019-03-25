"""
Created on Thursday May 24th 2018

@author: s0899345
"""

import numpy as np
import iris
import iris.coord_categorisation as iriscc
import iris.analysis.cartography

#this file is split into parts as follows:
    #PART 1: Load and Format all Past Models
    #PART 2: Load and Format all Future Models
    #PART 3: Load Observed Data
    #PART 4: Format Data General
    #PART 5: Format Baseline and Observed Data
    #PART 6: Format for Time Periods
    #PART 7: print data

def main():
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT ALL PAST MODELS   
    CCCmaCanRCM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_b =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    
    #Load exactly one cube from given file
    CCCmaCanRCM_b =  iris.load_cube(CCCmaCanRCM_b)
    CCCmaSMHI_b =  iris.load_cube(CCCmaSMHI_b)
    CNRM_b =  iris.load_cube(CNRM_b)
    CNRMSMHI_b =  iris.load_cube(CNRMSMHI_b)
    CSIRO_b =  iris.load_cube(CSIRO_b)
    ICHECDMI_b =  iris.load_cube(ICHECDMI_b, 'air_temperature')
    ICHECCCLM_b =  iris.load_cube(ICHECCCLM_b)
    ICHECKNMI_b =  iris.load_cube(ICHECKNMI_b)
    ICHECMPI_b =  iris.load_cube(ICHECMPI_b)
    ICHECSMHI_b =  iris.load_cube(ICHECSMHI_b)
    IPSL_b =  iris.load_cube(IPSL_b)
    MIROC_b =  iris.load_cube(MIROC_b)
    MOHCCCLM_b =  iris.load_cube(MOHCCCLM_b)
    MOHCKNMI_b =  iris.load_cube(MOHCKNMI_b)
    MOHCSMHI_b =  iris.load_cube(MOHCSMHI_b)
    MPICCLM_b =  iris.load_cube(MPICCLM_b)
    MPIREMO_b =  iris.load_cube(MPIREMO_b)
    MPISMHI_b =  iris.load_cube(MPISMHI_b)
    NCCSMHI_b =  iris.load_cube(NCCSMHI_b)
    NOAA_b =  iris.load_cube(NOAA_b)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(CCCmaCanRCM_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM_b.remove_coord('latitude')
    CCCmaCanRCM_b.remove_coord('longitude')
    CCCmaCanRCM_b.remove_coord('grid_latitude')
    CCCmaCanRCM_b.remove_coord('grid_longitude')
    CCCmaCanRCM_b.add_dim_coord(lats, 1)
    CCCmaCanRCM_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI_b.remove_coord('latitude')
    CCCmaSMHI_b.remove_coord('longitude')
    CCCmaSMHI_b.remove_coord('grid_latitude')
    CCCmaSMHI_b.remove_coord('grid_longitude')
    CCCmaSMHI_b.add_dim_coord(lats, 1)
    CCCmaSMHI_b.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM_b.remove_coord('latitude')
    CNRM_b.remove_coord('longitude')
    CNRM_b.remove_coord('grid_latitude')
    CNRM_b.remove_coord('grid_longitude')
    CNRM_b.add_dim_coord(lats, 1)
    CNRM_b.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI_b.remove_coord('latitude')
    CNRMSMHI_b.remove_coord('longitude')
    CNRMSMHI_b.remove_coord('grid_latitude')
    CNRMSMHI_b.remove_coord('grid_longitude')
    CNRMSMHI_b.add_dim_coord(lats, 1)
    CNRMSMHI_b.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO_b.remove_coord('latitude')
    CSIRO_b.remove_coord('longitude')
    CSIRO_b.remove_coord('grid_latitude')
    CSIRO_b.remove_coord('grid_longitude')
    CSIRO_b.add_dim_coord(lats, 1)
    CSIRO_b.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI_b.remove_coord('latitude')
    ICHECDMI_b.remove_coord('longitude')
    ICHECDMI_b.remove_coord('grid_latitude')
    ICHECDMI_b.remove_coord('grid_longitude')
    ICHECDMI_b.add_dim_coord(lats, 1)
    ICHECDMI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM_b.remove_coord('latitude')
    ICHECCCLM_b.remove_coord('longitude')
    ICHECCCLM_b.remove_coord('grid_latitude')
    ICHECCCLM_b.remove_coord('grid_longitude')
    ICHECCCLM_b.add_dim_coord(lats, 1)
    ICHECCCLM_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI_b.remove_coord('latitude')
    ICHECKNMI_b.remove_coord('longitude')
    ICHECKNMI_b.remove_coord('grid_latitude')
    ICHECKNMI_b.remove_coord('grid_longitude')
    ICHECKNMI_b.add_dim_coord(lats, 1)
    ICHECKNMI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI_b.remove_coord('latitude')
    ICHECMPI_b.remove_coord('longitude')
    ICHECMPI_b.remove_coord('grid_latitude')
    ICHECMPI_b.remove_coord('grid_longitude')
    ICHECMPI_b.add_dim_coord(lats, 1)
    ICHECMPI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI_b.remove_coord('latitude')
    ICHECSMHI_b.remove_coord('longitude')
    ICHECSMHI_b.remove_coord('grid_latitude')
    ICHECSMHI_b.remove_coord('grid_longitude')
    ICHECSMHI_b.add_dim_coord(lats, 1)
    ICHECSMHI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL_b.remove_coord('latitude')
    IPSL_b.remove_coord('longitude')
    IPSL_b.remove_coord('grid_latitude')
    IPSL_b.remove_coord('grid_longitude')
    IPSL_b.add_dim_coord(lats, 1)
    IPSL_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC_b.remove_coord('latitude')
    MIROC_b.remove_coord('longitude')
    MIROC_b.remove_coord('grid_latitude')
    MIROC_b.remove_coord('grid_longitude')
    MIROC_b.add_dim_coord(lats, 1)
    MIROC_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM_b.remove_coord('latitude')
    MOHCCCLM_b.remove_coord('longitude')
    MOHCCCLM_b.remove_coord('grid_latitude')
    MOHCCCLM_b.remove_coord('grid_longitude')
    MOHCCCLM_b.add_dim_coord(lats, 1)
    MOHCCCLM_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI_b.remove_coord('latitude')
    MOHCKNMI_b.remove_coord('longitude')
    MOHCKNMI_b.remove_coord('grid_latitude')
    MOHCKNMI_b.remove_coord('grid_longitude')
    MOHCKNMI_b.add_dim_coord(lats, 1)
    MOHCKNMI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI_b.remove_coord('latitude')
    MOHCSMHI_b.remove_coord('longitude')
    MOHCSMHI_b.remove_coord('grid_latitude')
    MOHCSMHI_b.remove_coord('grid_longitude')
    MOHCSMHI_b.add_dim_coord(lats, 1)
    MOHCSMHI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM_b.remove_coord('latitude')
    MPICCLM_b.remove_coord('longitude')
    MPICCLM_b.remove_coord('grid_latitude')
    MPICCLM_b.remove_coord('grid_longitude')
    MPICCLM_b.add_dim_coord(lats, 1)
    MPICCLM_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO_b.remove_coord('latitude')
    MPIREMO_b.remove_coord('longitude')
    MPIREMO_b.remove_coord('grid_latitude')
    MPIREMO_b.remove_coord('grid_longitude')
    MPIREMO_b.add_dim_coord(lats, 1)
    MPIREMO_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI_b.remove_coord('latitude')
    MPISMHI_b.remove_coord('longitude')
    MPISMHI_b.remove_coord('grid_latitude')
    MPISMHI_b.remove_coord('grid_longitude')
    MPISMHI_b.add_dim_coord(lats, 1)
    MPISMHI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI_b.remove_coord('latitude')
    NCCSMHI_b.remove_coord('longitude')
    NCCSMHI_b.remove_coord('grid_latitude')
    NCCSMHI_b.remove_coord('grid_longitude')
    NCCSMHI_b.add_dim_coord(lats, 1)
    NCCSMHI_b.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA_b.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons= NOAA_b.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA_b.remove_coord('latitude')
    NOAA_b.remove_coord('longitude')
    NOAA_b.remove_coord('grid_latitude')
    NOAA_b.remove_coord('grid_longitude')
    NOAA_b.add_dim_coord(lats, 1)
    NOAA_b.add_dim_coord(lons, 2)
    
    #guess bounds    
    CCCmaCanRCM_b.coord('latitude').guess_bounds()
    CCCmaSMHI_b.coord('latitude').guess_bounds()
    CNRM_b.coord('latitude').guess_bounds()
    CNRMSMHI_b.coord('latitude').guess_bounds()
    CSIRO_b.coord('latitude').guess_bounds()
    ICHECDMI_b.coord('latitude').guess_bounds()
    ICHECCCLM_b.coord('latitude').guess_bounds()
    ICHECKNMI_b.coord('latitude').guess_bounds()
    ICHECMPI_b.coord('latitude').guess_bounds()
    ICHECSMHI_b.coord('latitude').guess_bounds()
    IPSL_b.coord('latitude').guess_bounds()
    MIROC_b.coord('latitude').guess_bounds()
    MOHCCCLM_b.coord('latitude').guess_bounds()
    MOHCKNMI_b.coord('latitude').guess_bounds() 
    MOHCSMHI_b.coord('latitude').guess_bounds()
    MPICCLM_b.coord('latitude').guess_bounds()
    MPIREMO_b.coord('latitude').guess_bounds()
    MPISMHI_b.coord('latitude').guess_bounds()
    NCCSMHI_b.coord('latitude').guess_bounds()
    NOAA_b.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_b.coord('longitude').guess_bounds()
    CCCmaSMHI_b.coord('longitude').guess_bounds()
    CNRM_b.coord('longitude').guess_bounds()
    CNRMSMHI_b.coord('longitude').guess_bounds()
    CSIRO_b.coord('longitude').guess_bounds()
    ICHECDMI_b.coord('longitude').guess_bounds()
    ICHECCCLM_b.coord('longitude').guess_bounds()
    ICHECKNMI_b.coord('longitude').guess_bounds()
    ICHECMPI_b.coord('longitude').guess_bounds()
    ICHECSMHI_b.coord('longitude').guess_bounds()
    IPSL_b.coord('longitude').guess_bounds()
    MIROC_b.coord('longitude').guess_bounds()
    MOHCCCLM_b.coord('longitude').guess_bounds()
    MOHCKNMI_b.coord('longitude').guess_bounds() 
    MOHCSMHI_b.coord('longitude').guess_bounds()
    MPICCLM_b.coord('longitude').guess_bounds()
    MPIREMO_b.coord('longitude').guess_bounds()
    MPISMHI_b.coord('longitude').guess_bounds()
    NCCSMHI_b.coord('longitude').guess_bounds()
    NOAA_b.coord('longitude').guess_bounds()
    
    #time constraint to make obsered data only from 1971-2000 for monthly comparison
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_b = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CCCmaCanRCM_b =  CCCmaCanRCM_b.extract(t_constraint_b)
    CCCmaSMHI_b =  CCCmaSMHI_b.extract(t_constraint_b)
    CNRM_b =  CNRM_b.extract(t_constraint_b)
    CNRMSMHI_b =  CNRMSMHI_b.extract(t_constraint_b)
    CSIRO_b =  CSIRO_b.extract(t_constraint_b)
    ICHECDMI_b =  ICHECDMI_b.extract(t_constraint_b)
    ICHECCCLM_b =  ICHECCCLM_b.extract(t_constraint_b)
    ICHECKNMI_b =  ICHECKNMI_b.extract(t_constraint_b)
    ICHECMPI_b =  ICHECMPI_b.extract(t_constraint_b)
    ICHECSMHI_b =  ICHECSMHI_b.extract(t_constraint_b)
    IPSL_b =  IPSL_b.extract(t_constraint_b)
    MIROC_b =  MIROC_b.extract(t_constraint_b)
    MOHCCCLM_b =  MOHCCCLM_b.extract(t_constraint_b)
    MOHCKNMI_b =  MOHCKNMI_b.extract(t_constraint_b)
    MOHCSMHI_b =  MOHCSMHI_b.extract(t_constraint_b)
    MPICCLM_b =  MPICCLM_b.extract(t_constraint_b)
    MPIREMO_b =  MPIREMO_b.extract(t_constraint_b)
    MPISMHI_b =  MPISMHI_b.extract(t_constraint_b)
    NCCSMHI_b =  NCCSMHI_b.extract(t_constraint_b)
    NOAA_b =  NOAA_b.extract(t_constraint_b)
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT ALL FUTURE MODELS   
    CCCmaCanRCM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/4.5/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'   
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmin/8.5/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'  
    
    #Load exactly one cube from given file
    CCCmaCanRCM = iris.load_cube(CCCmaCanRCM)
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRM = iris.load_cube(CNRM)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    ICHECDMI = iris.load_cube(ICHECDMI, 'air_temperature')
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
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'air_temperature')
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
    #PART 3: LOAD OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU= '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/Actual_Data/cru_ts4.01.1901.2016.tmn.dat.nc'
        
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'near-surface temperature minimum')  
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    
    #time constraint to make all observed data series the same
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_obs = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    CRU = CRU.extract(t_constraint_obs)
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA GENERAL
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -12)        
    
    CCCmaCanRCM_b = CCCmaCanRCM_b.extract(Central_Malawi)
    CCCmaSMHI_b = CCCmaSMHI_b.extract(Central_Malawi)
    CNRM_b = CNRM_b.extract(Central_Malawi)
    CNRMSMHI_b = CNRMSMHI_b.extract(Central_Malawi)
    CSIRO_b = CSIRO_b.extract(Central_Malawi)
    ICHECDMI_b = ICHECDMI_b.extract(Central_Malawi)
    ICHECCCLM_b = ICHECCCLM_b.extract(Central_Malawi)
    ICHECKNMI_b = ICHECKNMI_b.extract(Central_Malawi)
    ICHECMPI_b = ICHECMPI_b.extract(Central_Malawi)
    ICHECSMHI_b = ICHECSMHI_b.extract(Central_Malawi)
    IPSL_b = IPSL_b.extract(Central_Malawi)
    MIROC_b = MIROC_b.extract(Central_Malawi)
    MOHCCCLM_b = MOHCCCLM_b.extract(Central_Malawi)
    MOHCKNMI_b = MOHCKNMI_b.extract(Central_Malawi)
    MOHCSMHI_b = MOHCSMHI_b.extract(Central_Malawi)
    MPICCLM_b = MPICCLM_b.extract(Central_Malawi)
    MPIREMO_b = MPIREMO_b.extract(Central_Malawi)
    MPISMHI_b = MPISMHI_b.extract(Central_Malawi)
    NCCSMHI_b = NCCSMHI_b.extract(Central_Malawi)
    NOAA_b = NOAA_b.extract(Central_Malawi)
    
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
    
    CRU = CRU.extract(Central_Malawi)
    
    #Convert units to match, CORDEX data is in Kelvin but Observed data in Celsius, we would like to show all data in Celsius
    CCCmaCanRCM_b.convert_units('Celsius')
    CCCmaSMHI_b.convert_units('Celsius')
    CNRM_b.convert_units('Celsius')
    CNRMSMHI_b.convert_units('Celsius')
    CSIRO_b.convert_units('Celsius')
    ICHECDMI_b.convert_units('Celsius')
    ICHECCCLM_b.convert_units('Celsius') 
    ICHECKNMI_b.convert_units('Celsius')
    ICHECMPI_b.convert_units('Celsius')
    ICHECSMHI_b.convert_units('Celsius')
    IPSL_b.convert_units('Celsius')
    MIROC_b.convert_units('Celsius')
    MOHCCCLM_b.convert_units('Celsius')
    MOHCKNMI_b.convert_units('Celsius')
    MOHCSMHI_b.convert_units('Celsius')
    MPICCLM_b.convert_units('Celsius')
    MPIREMO_b.convert_units('Celsius')
    MPISMHI_b.convert_units('Celsius')
    NCCSMHI_b.convert_units('Celsius')
    NOAA_b.convert_units('Celsius')
    
    CCCmaCanRCM.convert_units('Celsius')
    CCCmaSMHI.convert_units('Celsius')
    CNRM.convert_units('Celsius')
    CNRMSMHI.convert_units('Celsius')
    CSIRO.convert_units('Celsius')
    ICHECDMI.convert_units('Celsius')
    ICHECCCLM.convert_units('Celsius') 
    ICHECKNMI.convert_units('Celsius')
    ICHECMPI.convert_units('Celsius')
    ICHECSMHI.convert_units('Celsius')
    IPSL.convert_units('Celsius')
    MIROC.convert_units('Celsius')
    MOHCCCLM.convert_units('Celsius')
    MOHCKNMI.convert_units('Celsius')
    MOHCSMHI.convert_units('Celsius')
    MPICCLM.convert_units('Celsius')
    MPIREMO.convert_units('Celsius')
    MPISMHI.convert_units('Celsius')
    NCCSMHI.convert_units('Celsius')
    NOAA.convert_units('Celsius')
    
    CCCmaCanRCM85.convert_units('Celsius')
    CCCmaSMHI85.convert_units('Celsius')
    CNRM85.convert_units('Celsius')
    CNRMSMHI85.convert_units('Celsius')
    CSIRO85.convert_units('Celsius')
    ICHECDMI85.convert_units('Celsius')
    ICHECCCLM85.convert_units('Celsius') 
    ICHECKNMI85.convert_units('Celsius')
    ICHECMPI85.convert_units('Celsius')
    ICHECSMHI85.convert_units('Celsius')
    IPSL85.convert_units('Celsius')
    MIROC85.convert_units('Celsius')
    MOHCCCLM85.convert_units('Celsius')
    MOHCKNMI85.convert_units('Celsius')
    MOHCSMHI85.convert_units('Celsius')
    MPICCLM85.convert_units('Celsius')
    MPIREMO85.convert_units('Celsius')
    MPISMHI85.convert_units('Celsius')
    NCCSMHI85.convert_units('Celsius')
    NOAA85.convert_units('Celsius')
    
    #add day of the year to all files
    iriscc.add_day_of_year(CCCmaCanRCM_b, 'time')
    iriscc.add_day_of_year(CCCmaSMHI_b, 'time')
    iriscc.add_day_of_year(CNRM_b, 'time')
    iriscc.add_day_of_year(CNRMSMHI_b, 'time')
    iriscc.add_day_of_year(CSIRO_b, 'time')
    iriscc.add_day_of_year(ICHECDMI_b, 'time')
    iriscc.add_day_of_year(ICHECCCLM_b, 'time')
    iriscc.add_day_of_year(ICHECKNMI_b, 'time')
    iriscc.add_day_of_year(ICHECMPI_b, 'time')
    iriscc.add_day_of_year(ICHECSMHI_b, 'time')
    iriscc.add_day_of_year(IPSL_b, 'time')
    iriscc.add_day_of_year(MIROC_b, 'time')
    iriscc.add_day_of_year(MOHCCCLM_b, 'time')
    iriscc.add_day_of_year(MOHCKNMI_b, 'time')
    iriscc.add_day_of_year(MOHCSMHI_b, 'time')
    iriscc.add_day_of_year(MPICCLM_b, 'time')
    iriscc.add_day_of_year(MPIREMO_b, 'time')
    iriscc.add_day_of_year(MPISMHI_b, 'time')
    iriscc.add_day_of_year(NCCSMHI_b, 'time')
    iriscc.add_day_of_year(NOAA_b, 'time')
    
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
    
    iriscc.add_day_of_year(CRU, 'time')
    
    #add year data to files
    iriscc.add_year(CCCmaCanRCM_b, 'time')
    iriscc.add_year(CCCmaSMHI_b, 'time')
    iriscc.add_year(CNRM_b, 'time')
    iriscc.add_year(CNRMSMHI_b, 'time')
    iriscc.add_year(CSIRO_b, 'time')
    iriscc.add_year(ICHECDMI_b, 'time')
    iriscc.add_year(ICHECCCLM_b, 'time')
    iriscc.add_year(ICHECKNMI_b, 'time')
    iriscc.add_year(ICHECMPI_b, 'time')
    iriscc.add_year(ICHECSMHI_b, 'time')
    iriscc.add_year(IPSL_b, 'time')
    iriscc.add_year(MIROC_b, 'time')
    iriscc.add_year(MOHCCCLM_b, 'time')
    iriscc.add_year(MOHCKNMI_b, 'time')
    iriscc.add_year(MOHCSMHI_b, 'time')
    iriscc.add_year(MPICCLM_b, 'time')
    iriscc.add_year(MPIREMO_b, 'time')
    iriscc.add_year(MPISMHI_b, 'time')
    iriscc.add_year(NCCSMHI_b, 'time')
    iriscc.add_year(NOAA_b, 'time')
    
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
    
    iriscc.add_year(CRU, 'time')

    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT BASELINE AND OBSERVED DATA
    #We are interested in plotting the data by year, so we need to take a mean of all the data by year
    CCCmaCanRCM_b = CCCmaCanRCM_b.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHI_b = CCCmaSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    CNRM_b = CNRM_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHI_b = CNRMSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    CSIRO_b = CSIRO_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMI_b = ICHECDMI_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLM_b = ICHECCCLM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMI_b = ICHECKNMI_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPI_b = ICHECMPI_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHI_b = ICHECSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    IPSL_b = IPSL_b.aggregated_by('year', iris.analysis.MEAN)
    MIROC_b = MIROC_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLM_b = MOHCCCLM_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMI_b = MOHCKNMI_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHI_b = MOHCSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    MPICCLM_b = MPICCLM_b.aggregated_by('year', iris.analysis.MEAN)
    MPIREMO_b = MPIREMO_b.aggregated_by('year', iris.analysis.MEAN)
    MPISMHI_b = MPISMHI_b.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHI_b = NCCSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    NOAA_b = NOAA_b.aggregated_by('year', iris.analysis.MEAN)
    
    CRU = CRU.aggregated_by('year', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCM_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_b)
    CCCmaSMHI_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_b)
    CNRM_b_grid_areas = iris.analysis.cartography.area_weights(CNRM_b)
    CNRMSMHI_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_b)
    CSIRO_b_grid_areas = iris.analysis.cartography.area_weights(CSIRO_b)
    ICHECDMI_b_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_b)
    ICHECCCLM_b_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_b)
    ICHECKNMI_b_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_b)
    ICHECMPI_b_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_b)
    ICHECSMHI_b_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_b)
    IPSL_b_grid_areas = iris.analysis.cartography.area_weights(IPSL_b)
    MIROC_b_grid_areas = iris.analysis.cartography.area_weights(MIROC_b)
    MOHCCCLM_b_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_b)
    MOHCKNMI_b_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_b)
    MOHCSMHI_b_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_b)
    MPICCLM_b_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_b)
    MPIREMO_b_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_b)
    MPISMHI_b_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_b)
    NCCSMHI_b_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_b)
    NOAA_b_grid_areas = iris.analysis.cartography.area_weights(NOAA_b)
    
    CRU_grid_areas = iris.analysis.cartography.area_weights(CRU)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons  
    CCCmaCanRCM_b_mean = CCCmaCanRCM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_b_grid_areas)   
    CCCmaSMHI_b_mean = CCCmaSMHI_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHI_b_grid_areas)
    CNRM_b_mean = CNRM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_b_grid_areas)
    CNRMSMHI_b_mean = CNRMSMHI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_b_grid_areas)  
    CSIRO_b_mean = CSIRO_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_b_grid_areas)
    ICHECDMI_b_mean = ICHECDMI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_b_grid_areas) 
    ICHECCCLM_b_mean = ICHECCCLM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_b_grid_areas)
    ICHECKNMI_b_mean = ICHECKNMI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_b_grid_areas)
    ICHECMPI_b_mean = ICHECMPI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_b_grid_areas)
    ICHECSMHI_b_mean = ICHECSMHI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_b_grid_areas)
    IPSL_b_mean = IPSL_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_b_grid_areas)
    MIROC_b_mean = MIROC_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_b_grid_areas)
    MOHCCCLM_b_mean = MOHCCCLM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_b_grid_areas)
    MOHCKNMI_b_mean = MOHCKNMI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_b_grid_areas)
    MOHCSMHI_b_mean = MOHCSMHI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_b_grid_areas)
    MPICCLM_b_mean = MPICCLM_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLM_b_grid_areas)  
    MPIREMO_b_mean = MPIREMO_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_b_grid_areas) 
    MPISMHI_b_mean = MPISMHI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_b_grid_areas)
    NCCSMHI_b_mean = NCCSMHI_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_b_grid_areas) 
    NOAA_b_mean = NOAA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_b_grid_areas)
    
    CRU_mean = CRU.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_grid_areas)
    
    #we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCM_b_mean = CCCmaCanRCM_b_mean.collapsed(['time'], iris.analysis.MEAN)   
    CCCmaSMHI_b_mean = CCCmaSMHI_b_mean.collapsed(['time'],iris.analysis.MEAN)
    CNRM_b_mean = CNRM_b_mean.collapsed(['time'], iris.analysis.MEAN)                                               
    CNRMSMHI_b_mean = CNRMSMHI_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    CSIRO_b_mean = CSIRO_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMI_b_mean = ICHECDMI_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECCCLM_b_mean = ICHECCCLM_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECKNMI_b_mean = ICHECKNMI_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECMPI_b_mean = ICHECMPI_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECSMHI_b_mean = ICHECSMHI_b_mean.collapsed(['time'], iris.analysis.MEAN)
    IPSL_b_mean = IPSL_b_mean.collapsed(['time'], iris.analysis.MEAN)
    MIROC_b_mean = MIROC_b_mean.collapsed(['time'], iris.analysis.MEAN)
    MOHCCCLM_b_mean = MOHCCCLM_b_mean.collapsed(['time'], iris.analysis.MEAN)
    MOHCKNMI_b_mean = MOHCKNMI_b_mean.collapsed(['time'], iris.analysis.MEAN)
    MOHCSMHI_b_mean = MOHCSMHI_b_mean.collapsed(['time'], iris.analysis.MEAN)
    MPICCLM_b_mean = MPICCLM_b_mean.collapsed(['time'],iris.analysis.MEAN)  
    MPIREMO_b_mean = MPIREMO_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPISMHI_b_mean = MPISMHI_b_mean.collapsed(['time'], iris.analysis.MEAN)
    NCCSMHI_b_mean = NCCSMHI_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    NOAA_b_mean = NOAA_b_mean.collapsed(['time'], iris.analysis.MEAN)
    
    CRU_mean = CRU_mean.collapsed(['time'], iris.analysis.MEAN)
    
    #Create Observed Average / Obs name
    Obs = CRU_mean
    
    
    #-------------------------------------------------------------------------
    #PART 6: FORMAT FOR TIME PERIODS
    #PART 6A: FORMAT FOR 2030
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
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_30_mean = (CCCmaCanRCM_30_mean.data - CCCmaCanRCM_b_mean.data + Obs.data)
    CCCmaSMHI_30_mean = (CCCmaSMHI_30_mean.data - CCCmaSMHI_b_mean.data + Obs.data)
    CNRM_30_mean = (CNRM_30_mean.data - CNRM_b_mean.data + Obs.data)
    CNRMSMHI_30_mean = (CNRMSMHI_30_mean.data - CNRMSMHI_b_mean.data + Obs.data)  
    CSIRO_30_mean = (CSIRO_30_mean.data - CSIRO_b_mean.data + Obs.data)
    ICHECDMI_30_mean = (ICHECDMI_30_mean.data - ICHECDMI_b_mean.data + Obs.data) 
    ICHECCCLM_30_mean = (ICHECCCLM_30_mean.data - ICHECCCLM_b_mean.data + Obs.data)
    ICHECKNMI_30_mean = (ICHECKNMI_30_mean.data - ICHECKNMI_b_mean.data + Obs.data)
    ICHECMPI_30_mean = (ICHECMPI_30_mean.data - ICHECMPI_b_mean.data + Obs.data)
    ICHECSMHI_30_mean = (ICHECSMHI_30_mean.data - ICHECSMHI_b_mean.data + Obs.data)
    IPSL_30_mean = (IPSL_30_mean.data - IPSL_b_mean.data + Obs.data)
    MIROC_30_mean = (MIROC_30_mean.data - MIROC_b_mean.data + Obs.data)
    MOHCCCLM_30_mean = (MOHCCCLM_30_mean.data - MOHCCCLM_b_mean.data + Obs.data)
    MOHCKNMI_30_mean = (MOHCKNMI_30_mean.data - MOHCKNMI_b_mean.data + Obs.data)
    MOHCSMHI_30_mean = (MOHCSMHI_30_mean.data - MOHCSMHI_b_mean.data + Obs.data)
    MPICCLM_30_mean = (MPICCLM_30_mean.data - MPICCLM_b_mean.data + Obs.data)      
    MPIREMO_30_mean = (MPIREMO_30_mean.data - MPIREMO_b_mean.data + Obs.data)                         
    MPISMHI_30_mean = (MPISMHI_30_mean.data - MPISMHI_b_mean.data + Obs.data)
    NCCSMHI_30_mean = (NCCSMHI_30_mean.data - NCCSMHI_b_mean.data + Obs.data) 
    NOAA_30_mean = (NOAA_30_mean.data - NOAA_b_mean.data + Obs.data)
    
    CCCmaCanRCM85_30_mean = (CCCmaCanRCM85_30_mean.data - CCCmaCanRCM_b_mean.data + Obs.data)
    CCCmaSMHI85_30_mean = (CCCmaSMHI85_30_mean.data - CCCmaSMHI_b_mean.data + Obs.data)
    CNRM85_30_mean = (CNRM85_30_mean.data - CNRM_b_mean.data + Obs.data)
    CNRMSMHI85_30_mean = (CNRMSMHI85_30_mean.data - CNRMSMHI_b_mean.data + Obs.data)  
    CSIRO85_30_mean = (CSIRO85_30_mean.data - CSIRO_b_mean.data + Obs.data)
    ICHECDMI85_30_mean = (ICHECDMI85_30_mean.data - ICHECDMI_b_mean.data + Obs.data) 
    ICHECCCLM85_30_mean = (ICHECCCLM85_30_mean.data - ICHECCCLM_b_mean.data + Obs.data)
    ICHECKNMI85_30_mean = (ICHECKNMI85_30_mean.data - ICHECKNMI_b_mean.data + Obs.data)
    ICHECMPI85_30_mean = (ICHECMPI85_30_mean.data - ICHECMPI_b_mean.data + Obs.data)
    ICHECSMHI85_30_mean = (ICHECSMHI85_30_mean.data - ICHECSMHI_b_mean.data + Obs.data)
    IPSL85_30_mean = (IPSL85_30_mean.data - IPSL_b_mean.data + Obs.data)
    MIROC85_30_mean = (MIROC85_30_mean.data - MIROC_b_mean.data + Obs.data)
    MOHCCCLM85_30_mean = (MOHCCCLM85_30_mean.data - MOHCCCLM_b_mean.data + Obs.data)
    MOHCKNMI85_30_mean = (MOHCKNMI85_30_mean.data - MOHCKNMI_b_mean.data + Obs.data)
    MOHCSMHI85_30_mean = (MOHCSMHI85_30_mean.data - MOHCSMHI_b_mean.data + Obs.data)
    MPICCLM85_30_mean = (MPICCLM85_30_mean.data - MPICCLM_b_mean.data + Obs.data)      
    MPIREMO85_30_mean = (MPIREMO85_30_mean.data - MPIREMO_b_mean.data + Obs.data)                         
    MPISMHI85_30_mean = (MPISMHI85_30_mean.data - MPISMHI_b_mean.data + Obs.data)
    NCCSMHI85_30_mean = (NCCSMHI85_30_mean.data - NCCSMHI_b_mean.data + Obs.data) 
    NOAA85_30_mean = (NOAA85_30_mean.data - NOAA_b_mean.data + Obs.data)
    
    #PART 6B: FORMAT FOR 2050
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
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_50_mean = (CCCmaCanRCM_50_mean.data - CCCmaCanRCM_b_mean.data + Obs.data)
    CCCmaSMHI_50_mean = (CCCmaSMHI_50_mean.data - CCCmaSMHI_b_mean.data + Obs.data)
    CNRM_50_mean = (CNRM_50_mean.data - CNRM_b_mean.data + Obs.data)
    CNRMSMHI_50_mean = (CNRMSMHI_50_mean.data - CNRMSMHI_b_mean.data + Obs.data)  
    CSIRO_50_mean = (CSIRO_50_mean.data - CSIRO_b_mean.data + Obs.data)
    ICHECDMI_50_mean = (ICHECDMI_50_mean.data - ICHECDMI_b_mean.data + Obs.data) 
    ICHECCCLM_50_mean = (ICHECCCLM_50_mean.data - ICHECCCLM_b_mean.data + Obs.data)
    ICHECKNMI_50_mean = (ICHECKNMI_50_mean.data - ICHECKNMI_b_mean.data + Obs.data)
    ICHECMPI_50_mean = (ICHECMPI_50_mean.data - ICHECMPI_b_mean.data + Obs.data)
    ICHECSMHI_50_mean = (ICHECSMHI_50_mean.data - ICHECSMHI_b_mean.data + Obs.data)
    IPSL_50_mean = (IPSL_50_mean.data - IPSL_b_mean.data + Obs.data)
    MIROC_50_mean = (MIROC_50_mean.data - MIROC_b_mean.data + Obs.data)
    MOHCCCLM_50_mean = (MOHCCCLM_50_mean.data - MOHCCCLM_b_mean.data + Obs.data)
    MOHCKNMI_50_mean = (MOHCKNMI_50_mean.data - MOHCKNMI_b_mean.data + Obs.data)
    MOHCSMHI_50_mean = (MOHCSMHI_50_mean.data - MOHCSMHI_b_mean.data + Obs.data)
    MPICCLM_50_mean = (MPICCLM_50_mean.data - MPICCLM_b_mean.data + Obs.data)      
    MPIREMO_50_mean = (MPIREMO_50_mean.data - MPIREMO_b_mean.data + Obs.data)                         
    MPISMHI_50_mean = (MPISMHI_50_mean.data - MPISMHI_b_mean.data + Obs.data)
    NCCSMHI_50_mean = (NCCSMHI_50_mean.data - NCCSMHI_b_mean.data + Obs.data) 
    NOAA_50_mean = (NOAA_50_mean.data - NOAA_b_mean.data + Obs.data)
    
    CCCmaCanRCM85_50_mean = (CCCmaCanRCM85_50_mean.data - CCCmaCanRCM_b_mean.data + Obs.data)
    CCCmaSMHI85_50_mean = (CCCmaSMHI85_50_mean.data - CCCmaSMHI_b_mean.data + Obs.data)
    CNRM85_50_mean = (CNRM85_50_mean.data - CNRM_b_mean.data + Obs.data)
    CNRMSMHI85_50_mean = (CNRMSMHI85_50_mean.data - CNRMSMHI_b_mean.data + Obs.data)  
    CSIRO85_50_mean = (CSIRO85_50_mean.data - CSIRO_b_mean.data + Obs.data)
    ICHECDMI85_50_mean = (ICHECDMI85_50_mean.data - ICHECDMI_b_mean.data + Obs.data) 
    ICHECCCLM85_50_mean = (ICHECCCLM85_50_mean.data - ICHECCCLM_b_mean.data + Obs.data)
    ICHECKNMI85_50_mean = (ICHECKNMI85_50_mean.data - ICHECKNMI_b_mean.data + Obs.data)
    ICHECMPI85_50_mean = (ICHECMPI85_50_mean.data - ICHECMPI_b_mean.data + Obs.data)
    ICHECSMHI85_50_mean = (ICHECSMHI85_50_mean.data - ICHECSMHI_b_mean.data + Obs.data)
    IPSL85_50_mean = (IPSL85_50_mean.data - IPSL_b_mean.data + Obs.data)
    MIROC85_50_mean = (MIROC85_50_mean.data - MIROC_b_mean.data + Obs.data)
    MOHCCCLM85_50_mean = (MOHCCCLM85_50_mean.data - MOHCCCLM_b_mean.data + Obs.data)
    MOHCKNMI85_50_mean = (MOHCKNMI85_50_mean.data - MOHCKNMI_b_mean.data + Obs.data)
    MOHCSMHI85_50_mean = (MOHCSMHI85_50_mean.data - MOHCSMHI_b_mean.data + Obs.data)
    MPICCLM85_50_mean = (MPICCLM85_50_mean.data - MPICCLM_b_mean.data + Obs.data)      
    MPIREMO85_50_mean = (MPIREMO85_50_mean.data - MPIREMO_b_mean.data + Obs.data)                         
    MPISMHI85_50_mean = (MPISMHI85_50_mean.data - MPISMHI_b_mean.data + Obs.data)
    NCCSMHI85_50_mean = (NCCSMHI85_50_mean.data - NCCSMHI_b_mean.data + Obs.data) 
    NOAA85_50_mean = (NOAA85_50_mean.data - NOAA_b_mean.data + Obs.data)
    
    
    #PART 3: PRINT DATA
    import csv
    with open('output_TasMINdata.csv', 'wb') as csvfile:
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
    
    