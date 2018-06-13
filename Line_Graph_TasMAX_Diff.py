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
    #PART 1: load and format all past models
    #PART 2: load and format all future models
    #PART 3: load observed data
    #PART 4: format files general
    #PART 5: format files to be plot specific for monthly plotting (A=Observed, B=RCM 2050, C=RCM 2030)
    #PART 6: plot monthly data
    #PART 7: format files to be plot specific for yearly plotting
    #PART 8: plot yearly data
    
    
def main():
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT ALL PAST MODELS   
    CCCmaCanRCM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_b =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_b = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    
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
    lons = NOAA_b.coord('longitude').points[0]
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
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD and FORMAT ALL FUTURE MODELS   
    CCCmaCanRCM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20501231.nc'
    CCCmaSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'   
    CNRM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc'
    CNRMSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20501231.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc'    
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20501231.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20501231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20501231.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc'     
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20501231.nc'    
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/4.5/tasmax_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'   
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20501231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'   
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20501231.nc'   
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20501231.nc'
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20501231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc' 
    MOHCCCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20501231.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    MPICCLM85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20501231.nc'     
    MPIREMO85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20501231.nc'    
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/AFR_44_tasmax/8.5/tasmax_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20501231.nc'  
    
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
    CRU= '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/Actual_Data/cru_ts4.01.1901.2016.tmx.dat.nc'
        
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'near-surface temperature maximum')  
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    
    
    #-------------------------------------------------------------------------
    #PART 4: FORMAT DATA GENERAL
    #we are only interested in the latitude and longitude relevant to Malawi 
    Malawi = iris.Constraint(longitude=lambda v: 32.0 <= v <= 36., latitude=lambda v: -17. <= v <= -8.)   
    
    CCCmaCanRCM_b = CCCmaCanRCM_b.extract(Malawi)
    CCCmaSMHI_b = CCCmaSMHI_b.extract(Malawi)
    CNRM_b = CNRM_b.extract(Malawi)
    CNRMSMHI_b = CNRMSMHI_b.extract(Malawi)
    CSIRO_b = CSIRO_b.extract(Malawi)
    ICHECDMI_b = ICHECDMI_b.extract(Malawi)
    ICHECCCLM_b = ICHECCCLM_b.extract(Malawi)
    ICHECKNMI_b = ICHECKNMI_b.extract(Malawi)
    ICHECMPI_b = ICHECMPI_b.extract(Malawi)
    ICHECSMHI_b = ICHECSMHI_b.extract(Malawi)
    IPSL_b = IPSL_b.extract(Malawi)
    MIROC_b = MIROC_b.extract(Malawi)
    MOHCCCLM_b = MOHCCCLM_b.extract(Malawi)
    MOHCKNMI_b = MOHCKNMI_b.extract(Malawi)
    MOHCSMHI_b = MOHCSMHI_b.extract(Malawi)
    MPICCLM_b = MPICCLM_b.extract(Malawi)
    MPIREMO_b = MPIREMO_b.extract(Malawi)
    MPISMHI_b = MPISMHI_b.extract(Malawi)
    NCCSMHI_b = NCCSMHI_b.extract(Malawi)
    NOAA_b = NOAA_b.extract(Malawi)
    
    CCCmaCanRCM = CCCmaCanRCM.extract(Malawi)
    CCCmaSMHI = CCCmaSMHI.extract(Malawi)
    CNRM =CNRM.extract(Malawi)
    CNRMSMHI =CNRMSMHI.extract(Malawi)
    CSIRO=CSIRO.extract(Malawi)
    ICHECDMI=ICHECDMI.extract(Malawi)
    ICHECCCLM=ICHECCCLM.extract(Malawi)
    ICHECKNMI=ICHECKNMI.extract(Malawi)
    ICHECMPI=ICHECMPI.extract(Malawi)
    ICHECSMHI=ICHECSMHI.extract(Malawi)
    IPSL=IPSL.extract(Malawi)
    MIROC=MIROC.extract(Malawi)
    MOHCCCLM=MOHCCCLM.extract(Malawi)
    MOHCKNMI=MOHCKNMI.extract(Malawi)
    MOHCSMHI=MOHCSMHI.extract(Malawi)
    MPICCLM=MPICCLM.extract(Malawi)
    MPIREMO=MPIREMO.extract(Malawi)
    MPISMHI=MPISMHI.extract(Malawi)
    NCCSMHI=NCCSMHI.extract(Malawi)
    NOAA=NOAA.extract(Malawi)
    
    CCCmaCanRCM85 = CCCmaCanRCM85.extract(Malawi)
    CCCmaSMHI85 = CCCmaSMHI85.extract(Malawi)
    CNRM85 = CNRM85.extract(Malawi)
    CNRMSMHI85 = CNRMSMHI85.extract(Malawi)
    CSIRO85 = CSIRO85.extract(Malawi)
    ICHECDMI85 = ICHECDMI85.extract(Malawi)
    ICHECCCLM85 = ICHECCCLM85.extract(Malawi)
    ICHECKNMI85 = ICHECKNMI85.extract(Malawi)
    ICHECMPI85 = ICHECMPI85.extract(Malawi)
    ICHECSMHI85 = ICHECSMHI85.extract(Malawi)
    IPSL85 = IPSL85.extract(Malawi)
    MIROC85 = MIROC85.extract(Malawi)
    MOHCCCLM85 = MOHCCCLM85.extract(Malawi)
    MOHCKNMI85 = MOHCKNMI85.extract(Malawi)
    MOHCSMHI85 = MOHCSMHI85.extract(Malawi)
    MPICCLM85 = MPICCLM85.extract(Malawi)
    MPIREMO85 = MPIREMO85.extract(Malawi)
    MPISMHI85 = MPISMHI85.extract(Malawi)
    NCCSMHI85 = NCCSMHI85.extract(Malawi)
    NOAA85 = NOAA85.extract(Malawi)
    
    CRU = CRU.extract(Malawi)
    
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
    
    #add month numbers to data
    iriscc.add_month_number(CCCmaCanRCM_b, 'time')
    iriscc.add_month_number(CCCmaSMHI_b, 'time')
    iriscc.add_month_number(CNRM_b, 'time')
    iriscc.add_month_number(CNRMSMHI_b, 'time')
    iriscc.add_month_number(CSIRO_b, 'time')
    iriscc.add_month_number(ICHECDMI_b, 'time')
    iriscc.add_month_number(ICHECCCLM_b, 'time')
    iriscc.add_month_number(ICHECKNMI_b, 'time')
    iriscc.add_month_number(ICHECMPI_b, 'time')
    iriscc.add_month_number(ICHECSMHI_b, 'time')
    iriscc.add_month_number(IPSL_b, 'time')
    iriscc.add_month_number(MIROC_b, 'time')
    iriscc.add_month_number(MOHCCCLM_b, 'time')
    iriscc.add_month_number(MOHCKNMI_b, 'time')
    iriscc.add_month_number(MOHCSMHI_b, 'time')
    iriscc.add_month_number(MPICCLM_b, 'time')
    iriscc.add_month_number(MPIREMO_b, 'time')
    iriscc.add_month_number(MPISMHI_b, 'time')
    iriscc.add_month_number(NCCSMHI_b, 'time')
    iriscc.add_month_number(NOAA_b, 'time')
    
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
    
    iriscc.add_month_number(CRU, 'time')
    
    #add time constraint for baseline data
    iris.FUTURE.cell_datetime_objects = True
    t_constraint = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CCCmaCanRCM_b = CCCmaCanRCM_b.extract(t_constraint)
    CCCmaSMHI_b = CCCmaSMHI_b.extract(t_constraint)
    CNRM_b = CNRM_b.extract(t_constraint)
    CNRMSMHI_b = CNRMSMHI_b.extract(t_constraint)
    CSIRO_b = CSIRO_b.extract(t_constraint)
    ICHECDMI_b = ICHECDMI_b.extract(t_constraint)
    ICHECCCLM_b = ICHECCCLM_b.extract(t_constraint)
    ICHECKNMI_b = ICHECKNMI_b.extract(t_constraint)
    ICHECMPI_b = ICHECMPI_b.extract(t_constraint)
    ICHECSMHI_b = ICHECSMHI_b.extract(t_constraint)
    IPSL_b = IPSL_b.extract(t_constraint)
    MIROC_b = MIROC_b.extract(t_constraint)
    MOHCCCLM_b = MOHCCCLM_b.extract(t_constraint)
    MOHCKNMI_b = MOHCKNMI_b.extract(t_constraint)
    MOHCSMHI_b = MOHCSMHI_b.extract(t_constraint)
    MPICCLM_b = MPICCLM_b.extract(t_constraint)
    MPIREMO_b = MPIREMO_b.extract(t_constraint)
    MPISMHI_b = MPISMHI_b.extract(t_constraint)
    NCCSMHI_b = NCCSMHI_b.extract(t_constraint)
    NOAA_b = NOAA_b.extract(t_constraint)
    
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT FILES TO BE PLOT SPECIFIC FOR MONTHLY PLOTTING
    #PART 5A: COMPLETE FORMATING FOR BASELINE MONTHLY DATA
    #Complete formatting of baseline data for use in 2030 and 2050 models
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month 
    CCCmaCanRCM_b_m = CCCmaCanRCM_b.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_b_m = CCCmaSMHI_b.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_b_m = CNRM_b.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_b_m = CNRMSMHI_b.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_b_m = CSIRO_b.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_b_m = ICHECDMI_b.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_b_m = ICHECCCLM_b.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_b_m = ICHECKNMI_b.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_b_m = ICHECMPI_b.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_b_m = ICHECSMHI_b.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_b_m = IPSL_b.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_b_m = MIROC_b.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_b_m = MOHCCCLM_b.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_b_m = MOHCKNMI_b.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_b_m = MOHCSMHI_b.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_b_m = MPICCLM_b.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_b_m = MPIREMO_b.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_b_m = MPISMHI_b.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_b_m = NCCSMHI_b.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_b_m = NOAA_b.aggregated_by('month_number', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube.
    CCCmaCanRCM_b_m_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_b_m)
    CCCmaSMHI_b_m_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_b_m)
    CNRM_b_m_grid_areas = iris.analysis.cartography.area_weights(CNRM_b_m)
    CNRMSMHI_b_m_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_b_m)
    CSIRO_b_m_grid_areas = iris.analysis.cartography.area_weights(CSIRO_b_m)
    ICHECDMI_b_m_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_b_m)
    ICHECCCLM_b_m_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_b_m)
    ICHECKNMI_b_m_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_b_m)
    ICHECMPI_b_m_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_b_m)
    ICHECSMHI_b_m_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_b_m)
    IPSL_b_m_grid_areas = iris.analysis.cartography.area_weights(IPSL_b_m)
    MIROC_b_m_grid_areas = iris.analysis.cartography.area_weights(MIROC_b_m)
    MOHCCCLM_b_m_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_b_m)
    MOHCKNMI_b_m_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_b_m)
    MOHCSMHI_b_m_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_b_m)
    MPICCLM_b_m_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_b_m)
    MPIREMO_b_m_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_b_m)
    MPISMHI_b_m_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_b_m)
    NCCSMHI_b_m_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_b_m)
    NOAA_b_m_grid_areas = iris.analysis.cartography.area_weights(NOAA_b_m)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_b_m_mean = CCCmaCanRCM_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_b_m_grid_areas)  
    CCCmaSMHI_b_m_mean = CCCmaSMHI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_b_m_grid_areas)  
    CNRM_b_m_mean = CNRM_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_b_m_grid_areas)
    CNRMSMHI_b_m_mean = CNRMSMHI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_b_m_grid_areas)  
    CSIRO_b_m_mean = CSIRO_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_b_m_grid_areas)  
    ICHECDMI_b_m_mean = ICHECDMI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_b_m_grid_areas)  
    ICHECCCLM_b_m_mean = ICHECCCLM_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_b_m_grid_areas)  
    ICHECKNMI_b_m_mean = ICHECKNMI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_b_m_grid_areas)  
    ICHECMPI_b_m_mean = ICHECMPI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_b_m_grid_areas)  
    ICHECSMHI_b_m_mean = ICHECSMHI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_b_m_grid_areas)  
    IPSL_b_m_mean = IPSL_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_b_m_grid_areas)
    MIROC_b_m_mean = MIROC_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_b_m_grid_areas)  
    MOHCCCLM_b_m_mean = MOHCCCLM_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_b_m_grid_areas)  
    MOHCKNMI_b_m_mean = MOHCKNMI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_b_m_grid_areas)  
    MOHCSMHI_b_m_mean = MOHCSMHI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_b_m_grid_areas)  
    MPICCLM_b_m_mean = MPICCLM_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_b_m_grid_areas)  
    MPIREMO_b_m_mean = MPIREMO_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_b_m_grid_areas)  
    MPISMHI_b_m_mean = MPISMHI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_b_m_grid_areas)  
    NCCSMHI_b_m_mean = NCCSMHI_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_b_m_grid_areas)  
    NOAA_b_m_mean = NOAA_b_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_b_m_grid_areas) 
    
    
    #-------------------------------------------------------------------------
    #PART 5B: OBSERVED DATA FORMATING
    
    #time constraint to make obsered data only from 1971-2000 for monthly comparison
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_obs = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CRU_b = CRU.extract(t_constraint_obs)
    
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month 
    CRU_m = CRU_b.aggregated_by('month_number', iris.analysis.MEAN) 
    
    #Returns an array of area weights, with the same dimensions as the cube.
    CRU_m_grid_areas = iris.analysis.cartography.area_weights(CRU_m)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons    
    CRU_m_mean = CRU_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_m_grid_areas) 
    
    #Create average
    ObsY_m = (CRU_m_mean.data)
    
    #-------------------------------------------------------------------------
    #PART 5C: 2050 FORMATING
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month    
    CCCmaCanRCM_m = CCCmaCanRCM.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_m = CCCmaSMHI.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_m = CNRM.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_m = CNRMSMHI.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_m = CSIRO.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_m = ICHECDMI.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_m = ICHECCCLM.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_m = ICHECKNMI.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_m = ICHECMPI.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_m = ICHECSMHI.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_m = IPSL.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_m = MIROC.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_m = MOHCCCLM.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_m = MOHCKNMI.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_m = MOHCSMHI.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_m = MPICCLM.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_m = MPIREMO.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_m = MPISMHI.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_m = NCCSMHI.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_m = NOAA.aggregated_by('month_number', iris.analysis.MEAN)
    
    CCCmaCanRCM85_m = CCCmaCanRCM85.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI85_m = CCCmaSMHI85.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM85_m = CNRM85.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI85_m = CNRMSMHI85.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO85_m = CSIRO85.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI85_m = ICHECDMI85.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM85_m = ICHECCCLM85.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI85_m = ICHECKNMI85.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI85_m = ICHECMPI85.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI85_m = ICHECSMHI85.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL85_m = IPSL85.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC85_m = MIROC85.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM85_m = MOHCCCLM85.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI85_m = MOHCKNMI85.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI85_m = MOHCSMHI85.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM85_m = MPICCLM85.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO85_m = MPIREMO85.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI85_m = MPISMHI85.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI85_m = NCCSMHI85.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA85_m = NOAA85.aggregated_by('month_number', iris.analysis.MEAN)
    
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
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_m_mean = (CCCmaCanRCM_m_mean.data - CCCmaCanRCM_b_m_mean.data + ObsY_m.data)
    CCCmaSMHI_m_mean = (CCCmaSMHI_m_mean.data - CCCmaSMHI_b_m_mean.data + ObsY_m.data)
    CNRM_m_mean = (CNRM_m_mean.data - CNRM_b_m_mean.data + ObsY_m.data)
    CNRMSMHI_m_mean = (CNRMSMHI_m_mean.data - CNRMSMHI_b_m_mean.data + ObsY_m.data)  
    CSIRO_m_mean = (CSIRO_m_mean.data - CSIRO_b_m_mean.data + ObsY_m.data)
    ICHECDMI_m_mean = (ICHECDMI_m_mean.data - ICHECDMI_b_m_mean.data + ObsY_m.data) 
    ICHECCCLM_m_mean = (ICHECCCLM_m_mean.data - ICHECCCLM_b_m_mean.data + ObsY_m.data)
    ICHECKNMI_m_mean = (ICHECKNMI_m_mean.data - ICHECKNMI_b_m_mean.data + ObsY_m.data)
    ICHECMPI_m_mean = (ICHECMPI_m_mean.data - ICHECMPI_b_m_mean.data + ObsY_m.data)
    ICHECSMHI_m_mean = (ICHECSMHI_m_mean.data - ICHECSMHI_b_m_mean.data + ObsY_m.data)
    IPSL_m_mean = (IPSL_m_mean.data - IPSL_b_m_mean.data + ObsY_m.data)
    MIROC_m_mean = (MIROC_m_mean.data - MIROC_b_m_mean.data + ObsY_m.data)
    MOHCCCLM_m_mean = (MOHCCCLM_m_mean.data - MOHCCCLM_b_m_mean.data + ObsY_m.data)
    MOHCKNMI_m_mean = (MOHCKNMI_m_mean.data - MOHCKNMI_b_m_mean.data + ObsY_m.data)
    MOHCSMHI_m_mean = (MOHCSMHI_m_mean.data - MOHCSMHI_b_m_mean.data + ObsY_m.data)
    MPICCLM_m_mean = (MPICCLM_m_mean.data - MPICCLM_b_m_mean.data + ObsY_m.data)      
    MPIREMO_m_mean = (MPIREMO_m_mean.data - MPIREMO_b_m_mean.data + ObsY_m.data)                         
    MPISMHI_m_mean = (MPISMHI_m_mean.data - MPISMHI_b_m_mean.data + ObsY_m.data)
    NCCSMHI_m_mean = (NCCSMHI_m_mean.data - NCCSMHI_b_m_mean.data + ObsY_m.data) 
    NOAA_m_mean = (NOAA_m_mean.data - NOAA_b_m_mean.data + ObsY_m.data)
    
    CCCmaCanRCM85_m_mean = (CCCmaCanRCM85_m_mean.data - CCCmaCanRCM_b_m_mean.data + ObsY_m.data)
    CCCmaSMHI85_m_mean = (CCCmaSMHI85_m_mean.data - CCCmaSMHI_b_m_mean.data + ObsY_m.data)
    CNRM85_m_mean = (CNRM85_m_mean.data - CNRM_b_m_mean.data + ObsY_m.data)
    CNRMSMHI85_m_mean = (CNRMSMHI85_m_mean.data - CNRMSMHI_b_m_mean.data + ObsY_m.data)  
    CSIRO85_m_mean = (CSIRO85_m_mean.data - CSIRO_b_m_mean.data + ObsY_m.data)
    ICHECDMI85_m_mean = (ICHECDMI85_m_mean.data - ICHECDMI_b_m_mean.data + ObsY_m.data) 
    ICHECCCLM85_m_mean = (ICHECCCLM85_m_mean.data - ICHECCCLM_b_m_mean.data + ObsY_m.data)
    ICHECKNMI85_m_mean = (ICHECKNMI85_m_mean.data - ICHECKNMI_b_m_mean.data + ObsY_m.data)
    ICHECMPI85_m_mean = (ICHECMPI85_m_mean.data - ICHECMPI_b_m_mean.data + ObsY_m.data)
    ICHECSMHI85_m_mean = (ICHECSMHI85_m_mean.data - ICHECSMHI_b_m_mean.data + ObsY_m.data)
    IPSL85_m_mean = (IPSL85_m_mean.data - IPSL_b_m_mean.data + ObsY_m.data)
    MIROC85_m_mean = (MIROC85_m_mean.data - MIROC_b_m_mean.data + ObsY_m.data)
    MOHCCCLM85_m_mean = (MOHCCCLM85_m_mean.data - MOHCCCLM_b_m_mean.data + ObsY_m.data)
    MOHCKNMI85_m_mean = (MOHCKNMI85_m_mean.data - MOHCKNMI_b_m_mean.data + ObsY_m.data)
    MOHCSMHI85_m_mean = (MOHCSMHI85_m_mean.data - MOHCSMHI_b_m_mean.data + ObsY_m.data)
    MPICCLM85_m_mean = (MPICCLM85_m_mean.data - MPICCLM_b_m_mean.data + ObsY_m.data)      
    MPIREMO85_m_mean = (MPIREMO85_m_mean.data - MPIREMO_b_m_mean.data + ObsY_m.data)                         
    MPISMHI85_m_mean = (MPISMHI85_m_mean.data - MPISMHI_b_m_mean.data + ObsY_m.data)
    NCCSMHI85_m_mean = (NCCSMHI85_m_mean.data - NCCSMHI_b_m_mean.data + ObsY_m.data) 
    NOAA85_m_mean = (NOAA85_m_mean.data - NOAA_b_m_mean.data + ObsY_m.data)
    
    #Create average      
    AverageRY_m = (CCCmaCanRCM_m_mean.data + CCCmaSMHI_m_mean.data + CNRM_m_mean.data + CNRMSMHI_m_mean.data + CSIRO_m_mean.data + ICHECDMI_m_mean.data + ICHECCCLM_m_mean.data + ICHECKNMI_m_mean.data + ICHECMPI_m_mean.data + ICHECSMHI_m_mean.data + IPSL_m_mean.data + MIROC_m_mean.data + MOHCCCLM_m_mean.data + MOHCKNMI_m_mean.data + MOHCSMHI_m_mean.data + MPICCLM_m_mean.data + MPIREMO_m_mean.data + MPISMHI_m_mean.data + NCCSMHI_m_mean.data + NOAA_m_mean.data)/20.
    
    AverageRY85_m = (CCCmaCanRCM85_m_mean.data + CCCmaSMHI85_m_mean.data + CNRM85_m_mean.data + CNRMSMHI85_m_mean.data + CSIRO85_m_mean.data + ICHECDMI85_m_mean.data + ICHECCCLM85_m_mean.data + ICHECKNMI85_m_mean.data + ICHECMPI85_m_mean.data + ICHECSMHI85_m_mean.data + IPSL85_m_mean.data + MIROC85_m_mean.data + MOHCCCLM85_m_mean.data + MOHCKNMI85_m_mean.data + MOHCSMHI85_m_mean.data + MPICCLM85_m_mean.data + MPIREMO85_m_mean.data + MPISMHI85_m_mean.data + NCCSMHI85_m_mean.data + NOAA85_m_mean.data)/20.
    
    #-------------------------------------------------------------------------
    #PART 5D: 2030 FORMATING

    #time constraint to make all series the same (1961-2050)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_m30 = iris.Constraint(time=lambda cell: 2006 <= cell.point.year <= 2030)

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
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_m30_mean = (CCCmaCanRCM_m30_mean.data - CCCmaCanRCM_b_m_mean.data + ObsY_m.data)
    CCCmaSMHI_m30_mean = (CCCmaSMHI_m30_mean.data - CCCmaSMHI_b_m_mean.data + ObsY_m.data)
    CNRM_m30_mean = (CNRM_m30_mean.data - CNRM_b_m_mean.data + ObsY_m.data)
    CNRMSMHI_m30_mean = (CNRMSMHI_m30_mean.data - CNRMSMHI_b_m_mean.data + ObsY_m.data)  
    CSIRO_m30_mean = (CSIRO_m30_mean.data - CSIRO_b_m_mean.data + ObsY_m.data)
    ICHECDMI_m30_mean = (ICHECDMI_m30_mean.data - ICHECDMI_b_m_mean.data + ObsY_m.data) 
    ICHECCCLM_m30_mean = (ICHECCCLM_m30_mean.data - ICHECCCLM_b_m_mean.data + ObsY_m.data)
    ICHECKNMI_m30_mean = (ICHECKNMI_m30_mean.data - ICHECKNMI_b_m_mean.data + ObsY_m.data)
    ICHECMPI_m30_mean = (ICHECMPI_m30_mean.data - ICHECMPI_b_m_mean.data + ObsY_m.data)
    ICHECSMHI_m30_mean = (ICHECSMHI_m30_mean.data - ICHECSMHI_b_m_mean.data + ObsY_m.data)
    IPSL_m30_mean = (IPSL_m30_mean.data - IPSL_b_m_mean.data + ObsY_m.data)
    MIROC_m30_mean = (MIROC_m30_mean.data - MIROC_b_m_mean.data + ObsY_m.data)
    MOHCCCLM_m30_mean = (MOHCCCLM_m30_mean.data - MOHCCCLM_b_m_mean.data + ObsY_m.data)
    MOHCKNMI_m30_mean = (MOHCKNMI_m30_mean.data - MOHCKNMI_b_m_mean.data + ObsY_m.data)
    MOHCSMHI_m30_mean = (MOHCSMHI_m30_mean.data - MOHCSMHI_b_m_mean.data + ObsY_m.data)
    MPICCLM_m30_mean = (MPICCLM_m30_mean.data - MPICCLM_b_m_mean.data + ObsY_m.data)      
    MPIREMO_m30_mean = (MPIREMO_m30_mean.data - MPIREMO_b_m_mean.data + ObsY_m.data)
    MPISMHI_m30_mean = (MPISMHI_m30_mean.data - MPISMHI_b_m_mean.data + ObsY_m.data)
    NCCSMHI_m30_mean = (NCCSMHI_m30_mean.data - NCCSMHI_b_m_mean.data + ObsY_m.data) 
    NOAA_m30_mean = (NOAA_m30_mean.data - NOAA_b_m_mean.data + ObsY_m.data)
    
    CCCmaCanRCM85_m30_mean = (CCCmaCanRCM85_m30_mean.data - CCCmaCanRCM_b_m_mean.data + ObsY_m.data)
    CCCmaSMHI85_m30_mean = (CCCmaSMHI85_m30_mean.data - CCCmaSMHI_b_m_mean.data + ObsY_m.data)
    CNRM85_m30_mean = (CNRM85_m30_mean.data - CNRM_b_m_mean.data + ObsY_m.data)
    CNRMSMHI85_m30_mean = (CNRMSMHI85_m30_mean.data - CNRMSMHI_b_m_mean.data + ObsY_m.data)  
    CSIRO85_m30_mean = (CSIRO85_m30_mean.data - CSIRO_b_m_mean.data + ObsY_m.data)
    ICHECDMI85_m30_mean = (ICHECDMI85_m30_mean.data - ICHECDMI_b_m_mean.data + ObsY_m.data) 
    ICHECCCLM85_m30_mean = (ICHECCCLM85_m30_mean.data - ICHECCCLM_b_m_mean.data + ObsY_m.data)
    ICHECKNMI85_m30_mean = (ICHECKNMI85_m30_mean.data - ICHECKNMI_b_m_mean.data + ObsY_m.data)
    ICHECMPI85_m30_mean = (ICHECMPI85_m30_mean.data - ICHECMPI_b_m_mean.data + ObsY_m.data)
    ICHECSMHI85_m30_mean = (ICHECSMHI85_m30_mean.data - ICHECSMHI_b_m_mean.data + ObsY_m.data)
    IPSL85_m30_mean = (IPSL85_m30_mean.data - IPSL_b_m_mean.data + ObsY_m.data)
    MIROC85_m30_mean = (MIROC85_m30_mean.data - MIROC_b_m_mean.data + ObsY_m.data)
    MOHCCCLM85_m30_mean = (MOHCCCLM85_m30_mean.data - MOHCCCLM_b_m_mean.data + ObsY_m.data)
    MOHCKNMI85_m30_mean = (MOHCKNMI85_m30_mean.data - MOHCKNMI_b_m_mean.data + ObsY_m.data)
    MOHCSMHI85_m30_mean = (MOHCSMHI85_m30_mean.data - MOHCSMHI_b_m_mean.data + ObsY_m.data)
    MPICCLM85_m30_mean = (MPICCLM85_m30_mean.data - MPICCLM_b_m_mean.data + ObsY_m.data)      
    MPIREMO85_m30_mean = (MPIREMO85_m30_mean.data - MPIREMO_b_m_mean.data + ObsY_m.data)
    MPISMHI85_m30_mean = (MPISMHI85_m30_mean.data - MPISMHI_b_m_mean.data + ObsY_m.data)
    NCCSMHI85_m30_mean = (NCCSMHI85_m30_mean.data - NCCSMHI_b_m_mean.data + ObsY_m.data) 
    NOAA85_m30_mean = (NOAA85_m30_mean.data - NOAA_b_m_mean.data + ObsY_m.data)
    
    #Create averages      
    AverageRY_m30 = (CCCmaCanRCM_m30_mean.data + CCCmaSMHI_m30_mean.data + CNRM_m30_mean.data + CNRMSMHI_m30_mean.data + CSIRO_m30_mean.data + ICHECDMI_m30_mean.data + ICHECCCLM_m30_mean.data + ICHECKNMI_m30_mean.data + ICHECMPI_m30_mean.data + ICHECSMHI_m30_mean.data + IPSL_m30_mean.data + MIROC_m30_mean.data + MOHCCCLM_m30_mean.data + MOHCKNMI_m30_mean.data + MOHCSMHI_m30_mean.data + MPICCLM_m30_mean.data + MPIREMO_m30_mean.data + MPISMHI_m30_mean.data + NCCSMHI_m30_mean.data + NOAA_m30_mean.data)/20.
    
    AverageRY85_m30 = (CCCmaCanRCM85_m30_mean.data + CCCmaSMHI85_m30_mean.data + CNRM85_m30_mean.data + CNRMSMHI85_m30_mean.data + CSIRO85_m30_mean.data + ICHECDMI85_m30_mean.data + ICHECCCLM85_m30_mean.data + ICHECKNMI85_m30_mean.data + ICHECMPI85_m30_mean.data + ICHECSMHI85_m30_mean.data + IPSL85_m30_mean.data + MIROC85_m30_mean.data + MOHCCCLM85_m30_mean.data + MOHCKNMI85_m30_mean.data + MOHCSMHI85_m30_mean.data + MPICCLM85_m30_mean.data + MPIREMO85_m30_mean.data + MPISMHI85_m30_mean.data + NCCSMHI85_m30_mean.data + NOAA85_m30_mean.data)/20.

    
    #-------------------------------------------------------------------------
    #PART 6: PLOT LINE MONTHLY GRAPH AND PRINT DATA
    X_m = np.arange(1,13,1) 
    
    #PART 5A: Regional Climate Models Line Graph 2050
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(20,36)
    
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
    plt.plot(X_m, AverageRY_m, label='Average RCM 2006-2050', lw=3, color='black', linestyle='--') 
    plt.plot(X_m, ObsY_m.data, label='Observed 1971-2000', lw=3, color='black') 
        
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Monthly_ALL4.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
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
    plt.plot(X_m, AverageRY85_m, label='Average RCM 2006-2050', lw=3, color='black', linestyle='--') 
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')   
        
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Monthly_ALL8.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    
    #PART 5B: Regional Climate Models Line Graph 2030
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(20,36)
    
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
    plt.plot(X_m, AverageRY_m30, label='Average RCM 2006-2030', lw=3, color='black', linestyle='--') 
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')
        
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Monthly_ALL4.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(20,36)
    
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
    plt.plot(X_m, AverageRY85_m30, label='Average RCM 2006-2030', lw=3, color='black', linestyle='--')   
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')
        
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Monthly_ALL8.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #PART 5C: Average RCM Line Graph 2050 and 2030
    #set x-axis ticks                                        
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #set y axis limits
    plt.ylim(20,36)
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m, AverageRY_m, label='Average RCM 2006-2050 RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X_m, AverageRY_m30, label='Average RCM 2006-2030 RCP 4.5', lw=1.5, color='cyan', linestyle=':')
    plt.plot(X_m, AverageRY85_m, label='Average RCM 2006-2050 RCP 8.5', lw=1.5, color='magenta')
    plt.plot(X_m, AverageRY85_m30, label='Average RCM 2006-2030 RCP 8.5', lw=1.5, color='magenta', linestyle=':')
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')
    
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('TasMax for Malawi by Month', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Monthly_AVE_2050.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    
    #-------------------------------------------------------------------------
    #PART 7: FORMAT DATA TO BE PLOT SPECIFIC FOR YEARLY PLOTTING
    
    #time constraint to make all observed data series the same
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_obs = iris.Constraint(time=lambda cell: 1961 <= cell.point.year <= 2006)
    CRU = CRU.extract(t_constraint_obs)
    
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
    iriscc.add_year(CRU_b, 'time')
    
    #limit to a season
    SON = iris.Constraint(season='son')
    DJF = iris.Constraint(season='djf')
    MAM = iris.Constraint(season='mam')
    JJA = iris.Constraint(season='jja')
    
    #add season data to files
    iriscc.add_season(CCCmaCanRCM_b, 'time')
    iriscc.add_season(CCCmaSMHI_b, 'time')
    iriscc.add_season(CNRM_b, 'time')
    iriscc.add_season(CNRMSMHI_b, 'time')
    iriscc.add_season(CSIRO_b, 'time')
    iriscc.add_season(ICHECDMI_b, 'time')
    iriscc.add_season(ICHECCCLM_b, 'time')
    iriscc.add_season(ICHECKNMI_b, 'time')
    iriscc.add_season(ICHECMPI_b, 'time')
    iriscc.add_season(ICHECSMHI_b, 'time')
    iriscc.add_season(IPSL_b, 'time')
    iriscc.add_season(MIROC_b, 'time')
    iriscc.add_season(MOHCCCLM_b, 'time')
    iriscc.add_season(MOHCKNMI_b, 'time')
    iriscc.add_season(MOHCSMHI_b, 'time')
    iriscc.add_season(MPICCLM_b, 'time')
    iriscc.add_season(MPIREMO_b, 'time')
    iriscc.add_season(MPISMHI_b, 'time')
    iriscc.add_season(NCCSMHI_b, 'time')
    iriscc.add_season(NOAA_b, 'time')
    
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
    
    iriscc.add_season(CRU, 'time')
    iriscc.add_season(CRU_b, 'time')
    
    #extract only the season we are interested in
    CCCmaCanRCMSON_b = CCCmaCanRCM_b.extract(SON) 
    CCCmaSMHISON_b = CCCmaSMHI_b.extract(SON) 
    CNRMSON_b = CNRM_b.extract(SON) 
    CNRMSMHISON_b = CNRMSMHI_b.extract(SON) 
    CSIROSON_b = CSIRO_b.extract(SON) 
    ICHECDMISON_b = ICHECDMI_b.extract(SON) 
    ICHECCCLMSON_b = ICHECCCLM_b.extract(SON) 
    ICHECKNMISON_b = ICHECKNMI_b.extract(SON) 
    ICHECMPISON_b = ICHECMPI_b.extract(SON) 
    ICHECSMHISON_b = ICHECSMHI_b.extract(SON) 
    IPSLSON_b = IPSL_b.extract(SON) 
    MIROCSON_b = MIROC_b.extract(SON) 
    MOHCCCLMSON_b = MOHCCCLM_b.extract(SON) 
    MOHCKNMISON_b = MOHCKNMI_b.extract(SON) 
    MOHCSMHISON_b = MOHCSMHI_b.extract(SON) 
    MPICCLMSON_b = MPICCLM_b.extract(SON) 
    MPIREMOSON_b = MPIREMO_b.extract(SON) 
    MPISMHISON_b = MPISMHI_b.extract(SON) 
    NCCSMHISON_b = NCCSMHI_b.extract(SON) 
    NOAASON_b = NOAA_b.extract(SON)
    
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
    
    CRUSON = CRU.extract(SON)
    CRUSON_b = CRU_b.extract(SON)
    
    CCCmaCanRCMDJF_b = CCCmaCanRCM_b.extract(DJF) 
    CCCmaSMHIDJF_b = CCCmaSMHI_b.extract(DJF) 
    CNRMDJF_b = CNRM_b.extract(DJF) 
    CNRMSMHIDJF_b = CNRMSMHI_b.extract(DJF) 
    CSIRODJF_b = CSIRO_b.extract(DJF) 
    ICHECDMIDJF_b = ICHECDMI_b.extract(DJF) 
    ICHECCCLMDJF_b = ICHECCCLM_b.extract(DJF) 
    ICHECKNMIDJF_b = ICHECKNMI_b.extract(DJF) 
    ICHECMPIDJF_b = ICHECMPI_b.extract(DJF) 
    ICHECSMHIDJF_b = ICHECSMHI_b.extract(DJF) 
    IPSLDJF_b = IPSL_b.extract(DJF) 
    MIROCDJF_b = MIROC_b.extract(DJF) 
    MOHCCCLMDJF_b = MOHCCCLM_b.extract(DJF) 
    MOHCKNMIDJF_b = MOHCKNMI_b.extract(DJF) 
    MOHCSMHIDJF_b = MOHCSMHI_b.extract(DJF) 
    MPICCLMDJF_b = MPICCLM_b.extract(DJF) 
    MPIREMODJF_b = MPIREMO_b.extract(DJF) 
    MPISMHIDJF_b = MPISMHI_b.extract(DJF)  
    NCCSMHIDJF_b = NCCSMHI_b.extract(DJF) 
    NOAADJF_b = NOAA_b.extract(DJF)
    
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
      
    CRUDJF = CRU.extract(DJF)
    CRUDJF_b = CRU_b.extract(DJF)
    
    CCCmaCanRCMMAM_b = CCCmaCanRCM_b.extract(MAM) 
    CCCmaSMHIMAM_b = CCCmaSMHI_b.extract(MAM) 
    CNRMMAM_b = CNRM_b.extract(MAM) 
    CNRMSMHIMAM_b = CNRMSMHI_b.extract(MAM) 
    CSIROMAM_b = CSIRO_b.extract(MAM) 
    ICHECDMIMAM_b = ICHECDMI_b.extract(MAM) 
    ICHECCCLMMAM_b = ICHECCCLM_b.extract(MAM) 
    ICHECKNMIMAM_b = ICHECKNMI_b.extract(MAM) 
    ICHECMPIMAM_b = ICHECMPI_b.extract(MAM) 
    ICHECSMHIMAM_b = ICHECSMHI_b.extract(MAM) 
    IPSLMAM_b = IPSL_b.extract(MAM) 
    MIROCMAM_b = MIROC_b.extract(MAM) 
    MOHCCCLMMAM_b = MOHCCCLM_b.extract(MAM) 
    MOHCKNMIMAM_b = MOHCKNMI_b.extract(MAM) 
    MOHCSMHIMAM_b = MOHCSMHI_b.extract(MAM) 
    MPICCLMMAM_b = MPICCLM_b.extract(MAM) 
    MPIREMOMAM_b = MPIREMO_b.extract(MAM) 
    MPISMHIMAM_b = MPISMHI_b.extract(MAM) 
    NCCSMHIMAM_b = NCCSMHI_b.extract(MAM) 
    NOAAMAM_b = NOAA_b.extract(MAM)
    
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
    
    CRUMAM = CRU.extract(MAM)
    CRUMAM_b = CRU_b.extract(MAM)
    
    CCCmaCanRCMJJA_b = CCCmaCanRCM_b.extract(JJA) 
    CCCmaSMHIJJA_b = CCCmaSMHI_b.extract(JJA) 
    CNRMJJA_b = CNRM_b.extract(JJA) 
    CNRMSMHIJJA_b = CNRMSMHI_b.extract(JJA) 
    CSIROJJA_b = CSIRO_b.extract(JJA) 
    ICHECDMIJJA_b = ICHECDMI_b.extract(JJA) 
    ICHECCCLMJJA_b = ICHECCCLM_b.extract(JJA) 
    ICHECKNMIJJA_b = ICHECKNMI_b.extract(JJA) 
    ICHECMPIJJA_b = ICHECMPI_b.extract(JJA) 
    ICHECSMHIJJA_b = ICHECSMHI_b.extract(JJA) 
    IPSLJJA_b = IPSL_b.extract(JJA) 
    MIROCJJA_b = MIROC_b.extract(JJA) 
    MOHCCCLMJJA_b = MOHCCCLM_b.extract(JJA) 
    MOHCKNMIJJA_b = MOHCKNMI_b.extract(JJA) 
    MOHCSMHIJJA_b = MOHCSMHI_b.extract(JJA) 
    MPICCLMJJA_b = MPICCLM_b.extract(JJA) 
    MPIREMOJJA_b = MPIREMO_b.extract(JJA) 
    MPISMHIJJA_b = MPISMHI_b.extract(JJA) 
    NCCSMHIJJA_b = NCCSMHI_b.extract(JJA) 
    NOAAJJA_b = NOAA_b.extract(JJA)
    
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
    
    CRUJJA = CRU.extract(JJA)
    CRUJJA_b = CRU_b.extract(JJA)
    
    #We are interested in plotting the data by year, so we need to take a mean of all the data by year
    CCCmaCanRCMSON_b = CCCmaCanRCMSON_b.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHISON_b = CCCmaSMHISON_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSON_b = CNRMSON_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHISON_b = CNRMSMHISON_b.aggregated_by('year', iris.analysis.MEAN)
    CSIROSON_b = CSIROSON_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMISON_b = ICHECDMISON_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMSON_b = ICHECCCLMSON_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMISON_b = ICHECKNMISON_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPISON_b = ICHECMPISON_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHISON_b = ICHECSMHISON_b.aggregated_by('year', iris.analysis.MEAN)
    IPSLSON_b = IPSLSON_b.aggregated_by('year', iris.analysis.MEAN)
    MIROCSON_b = MIROCSON_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMSON_b = MOHCCCLMSON_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMISON_b = MOHCKNMISON_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHISON_b = MOHCSMHISON_b.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMSON_b = MPICCLMSON_b.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOSON_b = MPIREMOSON_b.aggregated_by('year', iris.analysis.MEAN)
    MPISMHISON_b = MPISMHISON_b.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHISON_b = NCCSMHISON_b.aggregated_by('year', iris.analysis.MEAN)
    NOAASON_b = NOAASON_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    
    CRUSON = CRUSON.aggregated_by('year', iris.analysis.MEAN)  
    CRUSON_b = CRUSON_b.aggregated_by('year', iris.analysis.MEAN)  
    
    CCCmaCanRCMDJF_b = CCCmaCanRCMDJF_b.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIDJF_b = CCCmaSMHIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMDJF_b = CNRMDJF_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIDJF_b = CNRMSMHIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    CSIRODJF_b = CSIRODJF_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIDJF_b = ICHECDMIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMDJF_b = ICHECCCLMDJF_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIDJF_b = ICHECKNMIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIDJF_b = ICHECMPIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIDJF_b = ICHECSMHIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    IPSLDJF_b = IPSLDJF_b.aggregated_by('year', iris.analysis.MEAN)
    MIROCDJF_b = MIROCDJF_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMDJF_b = MOHCCCLMDJF_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIDJF_b = MOHCKNMIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIDJF_b = MOHCSMHIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMDJF_b = MPICCLMDJF_b.aggregated_by('year', iris.analysis.MEAN)
    MPIREMODJF_b = MPIREMODJF_b.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIDJF_b = MPISMHIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIDJF_b = NCCSMHIDJF_b.aggregated_by('year', iris.analysis.MEAN)
    NOAADJF_b = NOAADJF_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    
    CRUDJF = CRUDJF.aggregated_by('year', iris.analysis.MEAN)  
    CRUDJF_b = CRUDJF_b.aggregated_by('year', iris.analysis.MEAN)  
 
    CCCmaCanRCMMAM_b = CCCmaCanRCMMAM_b.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIMAM_b = CCCmaSMHIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMMAM_b = CNRMMAM_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIMAM_b = CNRMSMHIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    CSIROMAM_b = CSIROMAM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIMAM_b = ICHECDMIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMMAM_b = ICHECCCLMMAM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIMAM_b = ICHECKNMIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIMAM_b = ICHECMPIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIMAM_b = ICHECSMHIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    IPSLMAM_b = IPSLMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MIROCMAM_b = MIROCMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMMAM_b = MOHCCCLMMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIMAM_b = MOHCKNMIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIMAM_b = MOHCSMHIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMMAM_b = MPICCLMMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOMAM_b = MPIREMOMAM_b.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIMAM_b = MPISMHIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIMAM_b = NCCSMHIMAM_b.aggregated_by('year', iris.analysis.MEAN)
    NOAAMAM_b = NOAAMAM_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    
    CRUMAM = CRUMAM.aggregated_by('year', iris.analysis.MEAN)  
    CRUMAM_b = CRUMAM_b.aggregated_by('year', iris.analysis.MEAN)  
    
    CCCmaCanRCMJJA_b = CCCmaCanRCMJJA_b.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIJJA_b = CCCmaSMHIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMJJA_b = CNRMJJA_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIJJA_b = CNRMSMHIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    CSIROJJA_b = CSIROJJA_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIJJA_b = ICHECDMIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMJJA_b = ICHECCCLMJJA_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIJJA_b = ICHECKNMIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIJJA_b = ICHECMPIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIJJA_b = ICHECSMHIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    IPSLJJA_b = IPSLJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MIROCJJA_b = MIROCJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMJJA_b = MOHCCCLMJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIJJA_b = MOHCKNMIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIJJA_b = MOHCSMHIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMJJA_b = MPICCLMJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOJJA_b = MPIREMOJJA_b.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIJJA_b = MPISMHIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIJJA_b = NCCSMHIJJA_b.aggregated_by('year', iris.analysis.MEAN)
    NOAAJJA_b = NOAAJJA_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    
    CRUJJA = CRUJJA.aggregated_by('year', iris.analysis.MEAN)  
    CRUJJA_b = CRUJJA_b.aggregated_by('year', iris.analysis.MEAN)  
    
    CCCmaCanRCMYR_b = CCCmaCanRCM_b.aggregated_by('year', iris.analysis.MEAN)
    CCCmaSMHIYR_b = CCCmaSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMYR_b = CNRM_b.aggregated_by('year', iris.analysis.MEAN)
    CNRMSMHIYR_b = CNRMSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    CSIROYR_b = CSIRO_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECDMIYR_b = ICHECDMI_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECCCLMYR_b = ICHECCCLM_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECKNMIYR_b = ICHECKNMI_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECMPIYR_b = ICHECMPI_b.aggregated_by('year', iris.analysis.MEAN)
    ICHECSMHIYR_b = ICHECSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    IPSLYR_b = IPSL_b.aggregated_by('year', iris.analysis.MEAN)
    MIROCYR_b = MIROC_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCCCLMYR_b = MOHCCCLM_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCKNMIYR_b = MOHCKNMI_b.aggregated_by('year', iris.analysis.MEAN)
    MOHCSMHIYR_b = MOHCSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    MPICCLMYR_b = MPICCLM_b.aggregated_by('year', iris.analysis.MEAN)
    MPIREMOYR_b = MPIREMO_b.aggregated_by('year', iris.analysis.MEAN)
    MPISMHIYR_b = MPISMHI_b.aggregated_by('year', iris.analysis.MEAN)
    NCCSMHIYR_b = NCCSMHI_b.aggregated_by('year', iris.analysis.MEAN)
    NOAAYR_b = NOAA_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    
    CRUYR = CRU.aggregated_by('year', iris.analysis.MEAN) 
    CRUYR_b = CRU_b.aggregated_by('year', iris.analysis.MEAN)  
    
    #Returns an array of area weights, with the same dimensions as the cube
    CCCmaCanRCMSON_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMSON_b)
    CCCmaSMHISON_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHISON_b)
    CNRMSON_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSON_b)
    CNRMSMHISON_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHISON_b)
    CSIROSON_b_grid_areas = iris.analysis.cartography.area_weights(CSIROSON_b)
    ICHECDMISON_b_grid_areas = iris.analysis.cartography.area_weights(ICHECDMISON_b)
    ICHECCCLMSON_b_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMSON_b)
    ICHECKNMISON_b_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMISON_b)
    ICHECMPISON_b_grid_areas = iris.analysis.cartography.area_weights(ICHECMPISON_b)
    ICHECSMHISON_b_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHISON_b)
    IPSLSON_b_grid_areas = iris.analysis.cartography.area_weights(IPSLSON_b)
    MIROCSON_b_grid_areas = iris.analysis.cartography.area_weights(MIROCSON_b)
    MOHCCCLMSON_b_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMSON_b)
    MOHCKNMISON_b_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMISON_b)
    MOHCSMHISON_b_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHISON_b)
    MPICCLMSON_b_grid_areas = iris.analysis.cartography.area_weights(MPICCLMSON_b)
    MPIREMOSON_b_grid_areas = iris.analysis.cartography.area_weights(MPIREMOSON_b)
    MPISMHISON_b_grid_areas = iris.analysis.cartography.area_weights(MPISMHISON_b)
    NCCSMHISON_b_grid_areas = iris.analysis.cartography.area_weights(NCCSMHISON_b)
    NOAASON_b_grid_areas = iris.analysis.cartography.area_weights(NOAASON_b)
    
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
    
    CRUSON_grid_areas = iris.analysis.cartography.area_weights(CRUSON)
    CRUSON_b_grid_areas = iris.analysis.cartography.area_weights(CRUSON_b)
    
    CCCmaCanRCMDJF_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMDJF_b)
    CCCmaSMHIDJF_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIDJF_b)
    CNRMDJF_b_grid_areas = iris.analysis.cartography.area_weights(CNRMDJF_b)
    CNRMSMHIDJF_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIDJF_b)
    CSIRODJF_b_grid_areas = iris.analysis.cartography.area_weights(CSIRODJF_b)
    ICHECDMIDJF_b_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIDJF_b)
    ICHECCCLMDJF_b_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMDJF_b)
    ICHECKNMIDJF_b_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIDJF_b)
    ICHECMPIDJF_b_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIDJF_b)
    ICHECSMHIDJF_b_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIDJF_b)
    IPSLDJF_b_grid_areas = iris.analysis.cartography.area_weights(IPSLDJF_b)
    MIROCDJF_b_grid_areas = iris.analysis.cartography.area_weights(MIROCDJF_b)
    MOHCCCLMDJF_b_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMDJF_b)
    MOHCKNMIDJF_b_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIDJF_b)
    MOHCSMHIDJF_b_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIDJF_b)
    MPICCLMDJF_b_grid_areas = iris.analysis.cartography.area_weights(MPICCLMDJF_b)
    MPIREMODJF_b_grid_areas = iris.analysis.cartography.area_weights(MPIREMODJF_b)
    MPISMHIDJF_b_grid_areas = iris.analysis.cartography.area_weights(MPISMHIDJF_b)
    NCCSMHIDJF_b_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIDJF_b)
    NOAADJF_b_grid_areas = iris.analysis.cartography.area_weights(NOAADJF_b)
    
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
    
    CRUDJF_grid_areas = iris.analysis.cartography.area_weights(CRUDJF)
    CRUDJF_b_grid_areas = iris.analysis.cartography.area_weights(CRUDJF_b)
    
    CCCmaCanRCMMAM_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMMAM_b)
    CCCmaSMHIMAM_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIMAM_b)
    CNRMMAM_b_grid_areas = iris.analysis.cartography.area_weights(CNRMMAM_b)
    CNRMSMHIMAM_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIMAM_b)
    CSIROMAM_b_grid_areas = iris.analysis.cartography.area_weights(CSIROMAM_b)
    ICHECDMIMAM_b_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIMAM_b)
    ICHECCCLMMAM_b_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMMAM_b)
    ICHECKNMIMAM_b_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIMAM_b)
    ICHECMPIMAM_b_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIMAM_b)
    ICHECSMHIMAM_b_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIMAM_b)
    IPSLMAM_b_grid_areas = iris.analysis.cartography.area_weights(IPSLMAM_b)
    MIROCMAM_b_grid_areas = iris.analysis.cartography.area_weights(MIROCMAM_b)
    MOHCCCLMMAM_b_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMMAM_b)
    MOHCKNMIMAM_b_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIMAM_b)
    MOHCSMHIMAM_b_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIMAM_b)
    MPICCLMMAM_b_grid_areas = iris.analysis.cartography.area_weights(MPICCLMMAM_b)
    MPIREMOMAM_b_grid_areas = iris.analysis.cartography.area_weights(MPIREMOMAM_b)
    MPISMHIMAM_b_grid_areas = iris.analysis.cartography.area_weights(MPISMHIMAM_b)
    NCCSMHIMAM_b_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIMAM_b)
    NOAAMAM_b_grid_areas = iris.analysis.cartography.area_weights(NOAAMAM_b)
    
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
    
    CRUMAM_grid_areas = iris.analysis.cartography.area_weights(CRUMAM)
    CRUMAM_b_grid_areas = iris.analysis.cartography.area_weights(CRUMAM_b)
    
    CCCmaCanRCMJJA_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMJJA_b)
    CCCmaSMHIJJA_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIJJA_b)
    CNRMJJA_b_grid_areas = iris.analysis.cartography.area_weights(CNRMJJA_b)
    CNRMSMHIJJA_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIJJA_b)
    CSIROJJA_b_grid_areas = iris.analysis.cartography.area_weights(CSIROJJA_b)
    ICHECDMIJJA_b_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIJJA_b)
    ICHECCCLMJJA_b_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMJJA_b)
    ICHECKNMIJJA_b_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIJJA_b)
    ICHECMPIJJA_b_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIJJA_b)
    ICHECSMHIJJA_b_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIJJA_b)
    IPSLJJA_b_grid_areas = iris.analysis.cartography.area_weights(IPSLJJA_b)
    MIROCJJA_b_grid_areas = iris.analysis.cartography.area_weights(MIROCJJA_b)
    MOHCCCLMJJA_b_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMJJA_b)
    MOHCKNMIJJA_b_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIJJA_b)
    MOHCSMHIJJA_b_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIJJA_b)
    MPICCLMJJA_b_grid_areas = iris.analysis.cartography.area_weights(MPICCLMJJA_b)
    MPIREMOJJA_b_grid_areas = iris.analysis.cartography.area_weights(MPIREMOJJA_b)
    MPISMHIJJA_b_grid_areas = iris.analysis.cartography.area_weights(MPISMHIJJA_b)
    NCCSMHIJJA_b_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIJJA_b)
    NOAAJJA_b_grid_areas = iris.analysis.cartography.area_weights(NOAAJJA_b)
    
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
    
    CRUJJA_grid_areas = iris.analysis.cartography.area_weights(CRUJJA)
    CRUJJA_b_grid_areas = iris.analysis.cartography.area_weights(CRUJJA_b)
    
    CCCmaCanRCMYR_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCMYR_b)
    CCCmaSMHIYR_b_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHIYR_b)
    CNRMYR_b_grid_areas = iris.analysis.cartography.area_weights(CNRMYR_b)
    CNRMSMHIYR_b_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHIYR_b)
    CSIROYR_b_grid_areas = iris.analysis.cartography.area_weights(CSIROYR_b)
    ICHECDMIYR_b_grid_areas = iris.analysis.cartography.area_weights(ICHECDMIYR_b)
    ICHECCCLMYR_b_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLMYR_b)
    ICHECKNMIYR_b_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMIYR_b)
    ICHECMPIYR_b_grid_areas = iris.analysis.cartography.area_weights(ICHECMPIYR_b)
    ICHECSMHIYR_b_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHIYR_b)
    IPSLYR_b_grid_areas = iris.analysis.cartography.area_weights(IPSLYR_b)
    MIROCYR_b_grid_areas = iris.analysis.cartography.area_weights(MIROCYR_b)
    MOHCCCLMYR_b_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLMYR_b)
    MOHCKNMIYR_b_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMIYR_b)
    MOHCSMHIYR_b_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHIYR_b)
    MPICCLMYR_b_grid_areas = iris.analysis.cartography.area_weights(MPICCLMYR_b)
    MPIREMOYR_b_grid_areas = iris.analysis.cartography.area_weights(MPIREMOYR_b)
    MPISMHIYR_b_grid_areas = iris.analysis.cartography.area_weights(MPISMHIYR_b)
    NCCSMHIYR_b_grid_areas = iris.analysis.cartography.area_weights(NCCSMHIYR_b)
    NOAAYR_b_grid_areas = iris.analysis.cartography.area_weights(NOAAYR_b)
    
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
    
    CRUYR_grid_areas = iris.analysis.cartography.area_weights(CRUYR)
    CRUYR_b_grid_areas = iris.analysis.cartography.area_weights(CRUYR_b)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCMSON_b_mean = CCCmaCanRCMSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMSON_b_grid_areas) 
    CCCmaSMHISON_b_mean = CCCmaSMHISON_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHISON_b_grid_areas)
    CNRMSON_b_mean = CNRMSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSON_b_grid_areas)                           
    CNRMSMHISON_b_mean = CNRMSMHISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHISON_b_grid_areas)  
    CSIROSON_b_mean = CSIROSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROSON_b_grid_areas)
    ICHECDMISON_b_mean = ICHECDMISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMISON_b_grid_areas) 
    ICHECCCLMSON_b_mean = ICHECCCLMSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMSON_b_grid_areas)
    ICHECKNMISON_b_mean = ICHECKNMISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMISON_b_grid_areas)
    ICHECMPISON_b_mean = ICHECMPISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPISON_b_grid_areas)
    ICHECSMHISON_b_mean = ICHECSMHISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHISON_b_grid_areas)
    IPSLSON_b_mean = IPSLSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLSON_b_grid_areas)
    MIROCSON_b_mean = MIROCSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCSON_b_grid_areas)
    MOHCCCLMSON_b_mean = MOHCCCLMSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMSON_b_grid_areas)
    MOHCKNMISON_b_mean = MOHCKNMISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMISON_b_grid_areas)
    MOHCSMHISON_b_mean = MOHCSMHISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHISON_b_grid_areas)
    MPICCLMSON_b_mean = MPICCLMSON_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMSON_b_grid_areas)        
    MPIREMOSON_b_mean = MPIREMOSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOSON_b_grid_areas)          
    MPISMHISON_b_mean = MPISMHISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHISON_b_grid_areas)
    NCCSMHISON_b_mean = NCCSMHISON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHISON_b_grid_areas) 
    NOAASON_b_mean = NOAASON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAASON_b_grid_areas)
    
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
    
    CRUSON_mean = CRUSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUSON_grid_areas) 
    CRUSON_b_mean = CRUSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUSON_b_grid_areas) 
     
    CCCmaCanRCMDJF_b_mean = CCCmaCanRCMDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMDJF_b_grid_areas) 
    CCCmaSMHIDJF_b_mean = CCCmaSMHIDJF_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIDJF_b_grid_areas)
    CNRMDJF_b_mean = CNRMDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMDJF_b_grid_areas)                           
    CNRMSMHIDJF_b_mean = CNRMSMHIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIDJF_b_grid_areas)  
    CSIRODJF_b_mean = CSIRODJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRODJF_b_grid_areas)
    ICHECDMIDJF_b_mean = ICHECDMIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIDJF_b_grid_areas) 
    ICHECCCLMDJF_b_mean = ICHECCCLMDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMDJF_b_grid_areas)
    ICHECKNMIDJF_b_mean = ICHECKNMIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIDJF_b_grid_areas)
    ICHECMPIDJF_b_mean = ICHECMPIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIDJF_b_grid_areas)
    ICHECSMHIDJF_b_mean = ICHECSMHIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIDJF_b_grid_areas)
    IPSLDJF_b_mean = IPSLDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLDJF_b_grid_areas)
    MIROCDJF_b_mean = MIROCDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCDJF_b_grid_areas)
    MOHCCCLMDJF_b_mean = MOHCCCLMDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMDJF_b_grid_areas)
    MOHCKNMIDJF_b_mean = MOHCKNMIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIDJF_b_grid_areas)
    MOHCSMHIDJF_b_mean = MOHCSMHIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIDJF_b_grid_areas)
    MPICCLMDJF_b_mean = MPICCLMDJF_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMDJF_b_grid_areas)        
    MPIREMODJF_b_mean = MPIREMODJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMODJF_b_grid_areas)          
    MPISMHIDJF_b_mean = MPISMHIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIDJF_b_grid_areas)
    NCCSMHIDJF_b_mean = NCCSMHIDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIDJF_b_grid_areas) 
    NOAADJF_b_mean = NOAADJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAADJF_b_grid_areas)
    
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
    
    CRUDJF_mean = CRUDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUDJF_grid_areas) 
    CRUDJF_b_mean = CRUDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUDJF_b_grid_areas) 
    
    CCCmaCanRCMMAM_b_mean = CCCmaCanRCMMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMMAM_b_grid_areas) 
    CCCmaSMHIMAM_b_mean = CCCmaSMHIMAM_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIMAM_b_grid_areas)
    CNRMMAM_b_mean = CNRMMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMMAM_b_grid_areas)                           
    CNRMSMHIMAM_b_mean = CNRMSMHIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIMAM_b_grid_areas)  
    CSIROMAM_b_mean = CSIROMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROMAM_b_grid_areas)
    ICHECDMIMAM_b_mean = ICHECDMIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIMAM_b_grid_areas) 
    ICHECCCLMMAM_b_mean = ICHECCCLMMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMMAM_b_grid_areas)
    ICHECKNMIMAM_b_mean = ICHECKNMIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIMAM_b_grid_areas)
    ICHECMPIMAM_b_mean = ICHECMPIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIMAM_b_grid_areas)
    ICHECSMHIMAM_b_mean = ICHECSMHIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIMAM_b_grid_areas)
    IPSLMAM_b_mean = IPSLMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLMAM_b_grid_areas)
    MIROCMAM_b_mean = MIROCMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCMAM_b_grid_areas)
    MOHCCCLMMAM_b_mean = MOHCCCLMMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMMAM_b_grid_areas)
    MOHCKNMIMAM_b_mean = MOHCKNMIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIMAM_b_grid_areas)
    MOHCSMHIMAM_b_mean = MOHCSMHIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIMAM_b_grid_areas)
    MPICCLMMAM_b_mean = MPICCLMMAM_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMMAM_b_grid_areas)        
    MPIREMOMAM_b_mean = MPIREMOMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOMAM_b_grid_areas)          
    MPISMHIMAM_b_mean = MPISMHIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIMAM_b_grid_areas)
    NCCSMHIMAM_b_mean = NCCSMHIMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIMAM_b_grid_areas) 
    NOAAMAM_b_mean = NOAAMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAMAM_b_grid_areas)
    
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
    
    CRUMAM_mean = CRUMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUMAM_grid_areas) 
    CRUMAM_b_mean = CRUMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUMAM_b_grid_areas)
    
    CCCmaCanRCMJJA_b_mean = CCCmaCanRCMJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMJJA_b_grid_areas) 
    CCCmaSMHIJJA_b_mean = CCCmaSMHIJJA_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIJJA_b_grid_areas)
    CNRMJJA_b_mean = CNRMJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMJJA_b_grid_areas)                           
    CNRMSMHIJJA_b_mean = CNRMSMHIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIJJA_b_grid_areas)  
    CSIROJJA_b_mean = CSIROJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROJJA_b_grid_areas)
    ICHECDMIJJA_b_mean = ICHECDMIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIJJA_b_grid_areas) 
    ICHECCCLMJJA_b_mean = ICHECCCLMJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMJJA_b_grid_areas)
    ICHECKNMIJJA_b_mean = ICHECKNMIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIJJA_b_grid_areas)
    ICHECMPIJJA_b_mean = ICHECMPIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIJJA_b_grid_areas)
    ICHECSMHIJJA_b_mean = ICHECSMHIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIJJA_b_grid_areas)
    IPSLJJA_b_mean = IPSLJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLJJA_b_grid_areas)
    MIROCJJA_b_mean = MIROCJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCJJA_b_grid_areas)
    MOHCCCLMJJA_b_mean = MOHCCCLMJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMJJA_b_grid_areas)
    MOHCKNMIJJA_b_mean = MOHCKNMIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIJJA_b_grid_areas)
    MOHCSMHIJJA_b_mean = MOHCSMHIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIJJA_b_grid_areas)
    MPICCLMJJA_b_mean = MPICCLMJJA_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMJJA_b_grid_areas)        
    MPIREMOJJA_b_mean = MPIREMOJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOJJA_b_grid_areas)          
    MPISMHIJJA_b_mean = MPISMHIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIJJA_b_grid_areas)
    NCCSMHIJJA_b_mean = NCCSMHIJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIJJA_b_grid_areas) 
    NOAAJJA_b_mean = NOAAJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAJJA_b_grid_areas)
    
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
    
    CRUJJA_mean = CRUJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUJJA_grid_areas) 
    CRUJJA_b_mean = CRUJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUJJA_b_grid_areas) 
    
    CCCmaCanRCMYR_b_mean = CCCmaCanRCMYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCMYR_b_grid_areas) 
    CCCmaSMHIYR_b_mean = CCCmaSMHIYR_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=CCCmaSMHIYR_b_grid_areas)
    CNRMYR_b_mean = CNRMYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMYR_b_grid_areas)                           
    CNRMSMHIYR_b_mean = CNRMSMHIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHIYR_b_grid_areas)  
    CSIROYR_b_mean = CSIROYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIROYR_b_grid_areas)
    ICHECDMIYR_b_mean = ICHECDMIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMIYR_b_grid_areas) 
    ICHECCCLMYR_b_mean = ICHECCCLMYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLMYR_b_grid_areas)
    ICHECKNMIYR_b_mean = ICHECKNMIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMIYR_b_grid_areas)
    ICHECMPIYR_b_mean = ICHECMPIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPIYR_b_grid_areas)
    ICHECSMHIYR_b_mean = ICHECSMHIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHIYR_b_grid_areas)
    IPSLYR_b_mean = IPSLYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSLYR_b_grid_areas)
    MIROCYR_b_mean = MIROCYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROCYR_b_grid_areas)
    MOHCCCLMYR_b_mean = MOHCCCLMYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLMYR_b_grid_areas)
    MOHCKNMIYR_b_mean = MOHCKNMIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMIYR_b_grid_areas)
    MOHCSMHIYR_b_mean = MOHCSMHIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHIYR_b_grid_areas)
    MPICCLMYR_b_mean = MPICCLMYR_b.collapsed(['latitude', 'longitude'],iris.analysis.MEAN, weights=MPICCLMYR_b_grid_areas)        
    MPIREMOYR_b_mean = MPIREMOYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMOYR_b_grid_areas)          
    MPISMHIYR_b_mean = MPISMHIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHIYR_b_grid_areas)
    NCCSMHIYR_b_mean = NCCSMHIYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHIYR_b_grid_areas) 
    NOAAYR_b_mean = NOAAYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAAYR_b_grid_areas)
    
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
    
    CRUYR_mean = CRUYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUYR_grid_areas) 
    CRUYR_b_mean = CRUYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUYR_b_grid_areas) 
    
    #for the baseline we don't need to average for each year, but the average for the whole time period, so collapse by time
    CCCmaCanRCMSON_b_mean = CCCmaCanRCMSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHISON_b_mean = CCCmaSMHISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRMSON_b_mean = CNRMSON_b_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHISON_b_mean = CNRMSMHISON_b_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIROSON_b_mean = CSIROSON_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMISON_b_mean = ICHECDMISON_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLMSON_b_mean = ICHECCCLMSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMISON_b_mean = ICHECKNMISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPISON_b_mean = ICHECMPISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHISON_b_mean = ICHECSMHISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    IPSLSON_b_mean = IPSLSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROCSON_b_mean = MIROCSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLMSON_b_mean = MOHCCCLMSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMISON_b_mean = MOHCKNMISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHISON_b_mean = MOHCSMHISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLMSON_b_mean = MPICCLMSON_b_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMOSON_b_mean = MPIREMOSON_b_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHISON_b_mean = MPISMHISON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHISON_b_mean = NCCSMHISON_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAASON_b_mean = NOAASON_b_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRUSON_b_mean = CRUSON_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CCCmaCanRCMDJF_b_mean = CCCmaCanRCMDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHIDJF_b_mean = CCCmaSMHIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRMDJF_b_mean = CNRMDJF_b_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHIDJF_b_mean = CNRMSMHIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIRODJF_b_mean = CSIRODJF_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMIDJF_b_mean = ICHECDMIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLMDJF_b_mean = ICHECCCLMDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMIDJF_b_mean = ICHECKNMIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPIDJF_b_mean = ICHECMPIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHIDJF_b_mean = ICHECSMHIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    IPSLDJF_b_mean = IPSLDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROCDJF_b_mean = MIROCDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLMDJF_b_mean = MOHCCCLMDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMIDJF_b_mean = MOHCKNMIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHIDJF_b_mean = MOHCSMHIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLMDJF_b_mean = MPICCLMDJF_b_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMODJF_b_mean = MPIREMODJF_b_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHIDJF_b_mean = MPISMHIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHIDJF_b_mean = NCCSMHIDJF_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAADJF_b_mean = NOAADJF_b_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRUDJF_b_mean = CRUDJF_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CCCmaCanRCMMAM_b_mean = CCCmaCanRCMMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHIMAM_b_mean = CCCmaSMHIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRMMAM_b_mean = CNRMMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHIMAM_b_mean = CNRMSMHIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIROMAM_b_mean = CSIROMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMIMAM_b_mean = ICHECDMIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLMMAM_b_mean = ICHECCCLMMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMIMAM_b_mean = ICHECKNMIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPIMAM_b_mean = ICHECMPIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHIMAM_b_mean = ICHECSMHIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    IPSLMAM_b_mean = IPSLMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROCMAM_b_mean = MIROCMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLMMAM_b_mean = MOHCCCLMMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMIMAM_b_mean = MOHCKNMIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHIMAM_b_mean = MOHCSMHIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLMMAM_b_mean = MPICCLMMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMOMAM_b_mean = MPIREMOMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHIMAM_b_mean = MPISMHIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHIMAM_b_mean = NCCSMHIMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAAMAM_b_mean = NOAAMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRUMAM_b_mean = CRUMAM_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CCCmaCanRCMJJA_b_mean = CCCmaCanRCMJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHIJJA_b_mean = CCCmaSMHIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRMJJA_b_mean = CNRMJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHIJJA_b_mean = CNRMSMHIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIROJJA_b_mean = CSIROJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMIJJA_b_mean = ICHECDMIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLMJJA_b_mean = ICHECCCLMJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMIJJA_b_mean = ICHECKNMIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPIJJA_b_mean = ICHECMPIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHIJJA_b_mean = ICHECSMHIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    IPSLJJA_b_mean = IPSLJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROCJJA_b_mean = MIROCJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLMJJA_b_mean = MOHCCCLMJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMIJJA_b_mean = MOHCKNMIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHIJJA_b_mean = MOHCSMHIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLMJJA_b_mean = MPICCLMJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMOJJA_b_mean = MPIREMOJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHIJJA_b_mean = MPISMHIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    NCCSMHIJJA_b_mean = NCCSMHIJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAAJJA_b_mean = NOAAJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRUJJA_b_mean = CRUJJA_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    CCCmaCanRCMYR_b_mean = CCCmaCanRCMYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CCCmaSMHIYR_b_mean = CCCmaSMHIYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    CNRMYR_b_mean = CNRMYR_b_mean.collapsed(['time'], iris.analysis.MEAN)                      
    CNRMSMHIYR_b_mean = CNRMSMHIYR_b_mean.collapsed(['time'], iris.analysis.MEAN)   
    CSIROYR_b_mean = CSIROYR_b_mean.collapsed(['time'], iris.analysis.MEAN)
    ICHECDMIYR_b_mean = ICHECDMIYR_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    ICHECCCLMYR_b_mean = ICHECCCLMYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECKNMIYR_b_mean = ICHECKNMIYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECMPIYR_b_mean = ICHECMPIYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    ICHECSMHIYR_b_mean = ICHECSMHIYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    IPSLYR_b_mean = IPSLYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MIROCYR_b_mean = MIROCYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCCCLMYR_b_mean = MOHCCCLMYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCKNMIYR_b_mean = MOHCKNMIYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MOHCSMHIYR_b_mean = MOHCSMHIYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    MPICCLMYR_b_mean = MPICCLMYR_b_mean.collapsed(['time'], iris.analysis.MEAN)        
    MPIREMOYR_b_mean = MPIREMOYR_b_mean.collapsed(['time'], iris.analysis.MEAN)           
    MPISMHIYR_b_mean = MPISMHIYR_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    NCCSMHIYR_b_mean = NCCSMHIYR_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    NOAAYR_b_mean = NOAAYR_b_mean.collapsed(['time'], iris.analysis.MEAN)     
    
    CRUYR_b_mean = CRUYR_b_mean.collapsed(['time'], iris.analysis.MEAN)  
    
    #We want to see the change in temperature from the baseline for Observed
    CRUSON_mean = CRUSON_mean.data - CRUSON_b_mean.data
    CRUDJF_mean = CRUDJF_mean.data - CRUDJF_b_mean.data
    CRUMAM_mean = CRUMAM_mean.data - CRUMAM_b_mean.data
    CRUJJA_mean = CRUJJA_mean.data - CRUJJA_b_mean.data
    CRUYR_mean = CRUYR_mean.data - CRUYR_b_mean.data
    
    #We want to see the change in temperature from the baseline for models
    CCCmaCanRCMSON_mean = (CCCmaCanRCMSON_mean.data - CCCmaCanRCMSON_b_mean.data)
    CCCmaSMHISON_mean = (CCCmaSMHISON_mean.data -  CCCmaSMHISON_b_mean.data) 
    CNRMSON_mean = (CNRMSON_mean.data -  CNRMSON_b_mean.data)                      
    CNRMSMHISON_mean = (CNRMSMHISON_mean.data -  CNRMSMHISON_b_mean.data)   
    CSIROSON_mean = (CSIROSON_mean.data -  CSIROSON_b_mean.data)
    ICHECDMISON_mean = (ICHECDMISON_mean.data -  ICHECDMISON_b_mean.data)  
    ICHECCCLMSON_mean = (ICHECCCLMSON_mean.data -  ICHECCCLMSON_b_mean.data) 
    ICHECKNMISON_mean = (ICHECKNMISON_mean.data -  ICHECKNMISON_b_mean.data) 
    ICHECMPISON_mean = (ICHECMPISON_mean.data -  ICHECMPISON_b_mean.data) 
    ICHECSMHISON_mean = (ICHECSMHISON_mean.data -  ICHECSMHISON_b_mean.data) 
    IPSLSON_mean = (IPSLSON_mean.data -  IPSLSON_b_mean.data) 
    MIROCSON_mean = (MIROCSON_mean.data -  MIROCSON_b_mean.data) 
    MOHCCCLMSON_mean = (MOHCCCLMSON_mean.data -  MOHCCCLMSON_b_mean.data) 
    MOHCKNMISON_mean = (MOHCKNMISON_mean.data -  MOHCKNMISON_b_mean.data) 
    MOHCSMHISON_mean = (MOHCSMHISON_mean.data -  MOHCSMHISON_b_mean.data) 
    MPICCLMSON_mean = (MPICCLMSON_mean.data -  MPICCLMSON_b_mean.data)        
    MPIREMOSON_mean = (MPIREMOSON_mean.data -  MPIREMOSON_b_mean.data)           
    MPISMHISON_mean = (MPISMHISON_mean.data -  MPISMHISON_b_mean.data) 
    NCCSMHISON_mean = (NCCSMHISON_mean.data -  NCCSMHISON_b_mean.data)  
    NOAASON_mean = (NOAASON_mean.data -  NOAASON_b_mean.data) 
    
    CCCmaCanRCMDJF_mean = (CCCmaCanRCMDJF_mean.data - CCCmaCanRCMDJF_b_mean.data)
    CCCmaSMHIDJF_mean = (CCCmaSMHIDJF_mean.data -  CCCmaSMHIDJF_b_mean.data) 
    CNRMDJF_mean = (CNRMDJF_mean.data -  CNRMDJF_b_mean.data)                      
    CNRMSMHIDJF_mean = (CNRMSMHIDJF_mean.data -  CNRMSMHIDJF_b_mean.data)   
    CSIRODJF_mean = (CSIRODJF_mean.data -  CSIRODJF_b_mean.data)
    ICHECDMIDJF_mean = (ICHECDMIDJF_mean.data -  ICHECDMIDJF_b_mean.data)  
    ICHECCCLMDJF_mean = (ICHECCCLMDJF_mean.data -  ICHECCCLMDJF_b_mean.data) 
    ICHECKNMIDJF_mean = (ICHECKNMIDJF_mean.data -  ICHECKNMIDJF_b_mean.data) 
    ICHECMPIDJF_mean = (ICHECMPIDJF_mean.data -  ICHECMPIDJF_b_mean.data) 
    ICHECSMHIDJF_mean = (ICHECSMHIDJF_mean.data -  ICHECSMHIDJF_b_mean.data) 
    IPSLDJF_mean = (IPSLDJF_mean.data -  IPSLDJF_b_mean.data) 
    MIROCDJF_mean = (MIROCDJF_mean.data -  MIROCDJF_b_mean.data) 
    MOHCCCLMDJF_mean = (MOHCCCLMDJF_mean.data -  MOHCCCLMDJF_b_mean.data) 
    MOHCKNMIDJF_mean = (MOHCKNMIDJF_mean.data -  MOHCKNMIDJF_b_mean.data) 
    MOHCSMHIDJF_mean = (MOHCSMHIDJF_mean.data -  MOHCSMHIDJF_b_mean.data) 
    MPICCLMDJF_mean = (MPICCLMDJF_mean.data -  MPICCLMDJF_b_mean.data)        
    MPIREMODJF_mean = (MPIREMODJF_mean.data -  MPIREMODJF_b_mean.data)           
    MPISMHIDJF_mean = (MPISMHIDJF_mean.data -  MPISMHIDJF_b_mean.data) 
    NCCSMHIDJF_mean = (NCCSMHIDJF_mean.data -  NCCSMHIDJF_b_mean.data)  
    NOAADJF_mean = (NOAADJF_mean.data -  NOAADJF_b_mean.data) 
    
    CCCmaCanRCMMAM_mean = (CCCmaCanRCMMAM_mean.data - CCCmaCanRCMMAM_b_mean.data)
    CCCmaSMHIMAM_mean = (CCCmaSMHIMAM_mean.data -  CCCmaSMHIMAM_b_mean.data) 
    CNRMMAM_mean = (CNRMMAM_mean.data -  CNRMMAM_b_mean.data)                      
    CNRMSMHIMAM_mean = (CNRMSMHIMAM_mean.data -  CNRMSMHIMAM_b_mean.data)   
    CSIROMAM_mean = (CSIROMAM_mean.data -  CSIROMAM_b_mean.data)
    ICHECDMIMAM_mean = (ICHECDMIMAM_mean.data -  ICHECDMIMAM_b_mean.data)  
    ICHECCCLMMAM_mean = (ICHECCCLMMAM_mean.data -  ICHECCCLMMAM_b_mean.data) 
    ICHECKNMIMAM_mean = (ICHECKNMIMAM_mean.data -  ICHECKNMIMAM_b_mean.data) 
    ICHECMPIMAM_mean = (ICHECMPIMAM_mean.data -  ICHECMPIMAM_b_mean.data) 
    ICHECSMHIMAM_mean = (ICHECSMHIMAM_mean.data -  ICHECSMHIMAM_b_mean.data) 
    IPSLMAM_mean = (IPSLMAM_mean.data -  IPSLMAM_b_mean.data) 
    MIROCMAM_mean = (MIROCMAM_mean.data -  MIROCMAM_b_mean.data) 
    MOHCCCLMMAM_mean = (MOHCCCLMMAM_mean.data -  MOHCCCLMMAM_b_mean.data) 
    MOHCKNMIMAM_mean = (MOHCKNMIMAM_mean.data -  MOHCKNMIMAM_b_mean.data) 
    MOHCSMHIMAM_mean = (MOHCSMHIMAM_mean.data -  MOHCSMHIMAM_b_mean.data) 
    MPICCLMMAM_mean = (MPICCLMMAM_mean.data -  MPICCLMMAM_b_mean.data)        
    MPIREMOMAM_mean = (MPIREMOMAM_mean.data -  MPIREMOMAM_b_mean.data)           
    MPISMHIMAM_mean = (MPISMHIMAM_mean.data -  MPISMHIMAM_b_mean.data) 
    NCCSMHIMAM_mean = (NCCSMHIMAM_mean.data -  NCCSMHIMAM_b_mean.data)  
    NOAAMAM_mean = (NOAAMAM_mean.data -  NOAAMAM_b_mean.data) 
    
    CCCmaCanRCMJJA_mean = (CCCmaCanRCMJJA_mean.data - CCCmaCanRCMJJA_b_mean.data)
    CCCmaSMHIJJA_mean = (CCCmaSMHIJJA_mean.data -  CCCmaSMHIJJA_b_mean.data) 
    CNRMJJA_mean = (CNRMJJA_mean.data -  CNRMJJA_b_mean.data)                      
    CNRMSMHIJJA_mean = (CNRMSMHIJJA_mean.data -  CNRMSMHIJJA_b_mean.data)   
    CSIROJJA_mean = (CSIROJJA_mean.data -  CSIROJJA_b_mean.data)
    ICHECDMIJJA_mean = (ICHECDMIJJA_mean.data -  ICHECDMIJJA_b_mean.data)  
    ICHECCCLMJJA_mean = (ICHECCCLMJJA_mean.data -  ICHECCCLMJJA_b_mean.data) 
    ICHECKNMIJJA_mean = (ICHECKNMIJJA_mean.data -  ICHECKNMIJJA_b_mean.data) 
    ICHECMPIJJA_mean = (ICHECMPIJJA_mean.data -  ICHECMPIJJA_b_mean.data) 
    ICHECSMHIJJA_mean = (ICHECSMHIJJA_mean.data -  ICHECSMHIJJA_b_mean.data) 
    IPSLJJA_mean = (IPSLJJA_mean.data -  IPSLJJA_b_mean.data) 
    MIROCJJA_mean = (MIROCJJA_mean.data -  MIROCJJA_b_mean.data) 
    MOHCCCLMJJA_mean = (MOHCCCLMJJA_mean.data -  MOHCCCLMJJA_b_mean.data) 
    MOHCKNMIJJA_mean = (MOHCKNMIJJA_mean.data -  MOHCKNMIJJA_b_mean.data) 
    MOHCSMHIJJA_mean = (MOHCSMHIJJA_mean.data -  MOHCSMHIJJA_b_mean.data) 
    MPICCLMJJA_mean = (MPICCLMJJA_mean.data -  MPICCLMJJA_b_mean.data)        
    MPIREMOJJA_mean = (MPIREMOJJA_mean.data -  MPIREMOJJA_b_mean.data)           
    MPISMHIJJA_mean = (MPISMHIJJA_mean.data -  MPISMHIJJA_b_mean.data) 
    NCCSMHIJJA_mean = (NCCSMHIJJA_mean.data -  NCCSMHIJJA_b_mean.data)  
    NOAAJJA_mean = (NOAAJJA_mean.data -  NOAAJJA_b_mean.data) 
    
    CCCmaCanRCMYR_mean = (CCCmaCanRCMYR_mean.data - CCCmaCanRCMYR_b_mean.data)
    CCCmaSMHIYR_mean = (CCCmaSMHIYR_mean.data -  CCCmaSMHIYR_b_mean.data) 
    CNRMYR_mean = (CNRMYR_mean.data -  CNRMYR_b_mean.data)                      
    CNRMSMHIYR_mean = (CNRMSMHIYR_mean.data -  CNRMSMHIYR_b_mean.data)   
    CSIROYR_mean = (CSIROYR_mean.data -  CSIROYR_b_mean.data)
    ICHECDMIYR_mean = (ICHECDMIYR_mean.data -  ICHECDMIYR_b_mean.data)  
    ICHECCCLMYR_mean = (ICHECCCLMYR_mean.data -  ICHECCCLMYR_b_mean.data) 
    ICHECKNMIYR_mean = (ICHECKNMIYR_mean.data -  ICHECKNMIYR_b_mean.data) 
    ICHECMPIYR_mean = (ICHECMPIYR_mean.data -  ICHECMPIYR_b_mean.data) 
    ICHECSMHIYR_mean = (ICHECSMHIYR_mean.data -  ICHECSMHIYR_b_mean.data) 
    IPSLYR_mean = (IPSLYR_mean.data -  IPSLYR_b_mean.data) 
    MIROCYR_mean = (MIROCYR_mean.data -  MIROCYR_b_mean.data) 
    MOHCCCLMYR_mean = (MOHCCCLMYR_mean.data -  MOHCCCLMYR_b_mean.data) 
    MOHCKNMIYR_mean = (MOHCKNMIYR_mean.data -  MOHCKNMIYR_b_mean.data) 
    MOHCSMHIYR_mean = (MOHCSMHIYR_mean.data -  MOHCSMHIYR_b_mean.data) 
    MPICCLMYR_mean = (MPICCLMYR_mean.data -  MPICCLMYR_b_mean.data)        
    MPIREMOYR_mean = (MPIREMOYR_mean.data -  MPIREMOYR_b_mean.data)           
    MPISMHIYR_mean = (MPISMHIYR_mean.data -  MPISMHIYR_b_mean.data)  
    NCCSMHIYR_mean = (NCCSMHIYR_mean.data -  NCCSMHIYR_b_mean.data)  
    NOAAYR_mean = (NOAAYR_mean.data -  NOAAYR_b_mean.data) 
    
    CCCmaCanRCMSON85_mean = (CCCmaCanRCMSON85_mean.data - CCCmaCanRCMSON_b_mean.data)
    CCCmaSMHISON85_mean = (CCCmaSMHISON85_mean.data -  CCCmaSMHISON_b_mean.data) 
    CNRMSON85_mean = (CNRMSON85_mean.data -  CNRMSON_b_mean.data)                      
    CNRMSMHISON85_mean = (CNRMSMHISON85_mean.data -  CNRMSMHISON_b_mean.data)   
    CSIROSON85_mean = (CSIROSON85_mean.data -  CSIROSON_b_mean.data)
    ICHECDMISON85_mean = (ICHECDMISON85_mean.data -  ICHECDMISON_b_mean.data)  
    ICHECCCLMSON85_mean = (ICHECCCLMSON85_mean.data -  ICHECCCLMSON_b_mean.data) 
    ICHECKNMISON85_mean = (ICHECKNMISON85_mean.data -  ICHECKNMISON_b_mean.data) 
    ICHECMPISON85_mean = (ICHECMPISON85_mean.data -  ICHECMPISON_b_mean.data) 
    ICHECSMHISON85_mean = (ICHECSMHISON85_mean.data -  ICHECSMHISON_b_mean.data) 
    IPSLSON85_mean = (IPSLSON85_mean.data -  IPSLSON_b_mean.data) 
    MIROCSON85_mean = (MIROCSON85_mean.data -  MIROCSON_b_mean.data) 
    MOHCCCLMSON85_mean = (MOHCCCLMSON85_mean.data -  MOHCCCLMSON_b_mean.data) 
    MOHCKNMISON85_mean = (MOHCKNMISON85_mean.data -  MOHCKNMISON_b_mean.data) 
    MOHCSMHISON85_mean = (MOHCSMHISON85_mean.data -  MOHCSMHISON_b_mean.data) 
    MPICCLMSON85_mean = (MPICCLMSON85_mean.data -  MPICCLMSON_b_mean.data)        
    MPIREMOSON85_mean = (MPIREMOSON85_mean.data -  MPIREMOSON_b_mean.data)           
    MPISMHISON85_mean = (MPISMHISON85_mean.data -  MPISMHISON_b_mean.data) 
    NCCSMHISON85_mean = (NCCSMHISON85_mean.data -  NCCSMHISON_b_mean.data)  
    NOAASON85_mean = (NOAASON85_mean.data -  NOAASON_b_mean.data) 
    
    CCCmaCanRCMDJF85_mean = (CCCmaCanRCMDJF85_mean.data - CCCmaCanRCMDJF_b_mean.data)
    CCCmaSMHIDJF85_mean = (CCCmaSMHIDJF85_mean.data -  CCCmaSMHIDJF_b_mean.data) 
    CNRMDJF85_mean = (CNRMDJF85_mean.data -  CNRMDJF_b_mean.data)                      
    CNRMSMHIDJF85_mean = (CNRMSMHIDJF85_mean.data -  CNRMSMHIDJF_b_mean.data)   
    CSIRODJF85_mean = (CSIRODJF85_mean.data -  CSIRODJF_b_mean.data)
    ICHECDMIDJF85_mean = (ICHECDMIDJF85_mean.data -  ICHECDMIDJF_b_mean.data)  
    ICHECCCLMDJF85_mean = (ICHECCCLMDJF85_mean.data -  ICHECCCLMDJF_b_mean.data) 
    ICHECKNMIDJF85_mean = (ICHECKNMIDJF85_mean.data -  ICHECKNMIDJF_b_mean.data) 
    ICHECMPIDJF85_mean = (ICHECMPIDJF85_mean.data -  ICHECMPIDJF_b_mean.data) 
    ICHECSMHIDJF85_mean = (ICHECSMHIDJF85_mean.data -  ICHECSMHIDJF_b_mean.data) 
    IPSLDJF85_mean = (IPSLDJF85_mean.data -  IPSLDJF_b_mean.data) 
    MIROCDJF85_mean = (MIROCDJF85_mean.data -  MIROCDJF_b_mean.data) 
    MOHCCCLMDJF85_mean = (MOHCCCLMDJF85_mean.data -  MOHCCCLMDJF_b_mean.data) 
    MOHCKNMIDJF85_mean = (MOHCKNMIDJF85_mean.data -  MOHCKNMIDJF_b_mean.data) 
    MOHCSMHIDJF85_mean = (MOHCSMHIDJF85_mean.data -  MOHCSMHIDJF_b_mean.data) 
    MPICCLMDJF85_mean = (MPICCLMDJF85_mean.data -  MPICCLMDJF_b_mean.data)        
    MPIREMODJF85_mean = (MPIREMODJF85_mean.data -  MPIREMODJF_b_mean.data)           
    MPISMHIDJF85_mean = (MPISMHIDJF85_mean.data -  MPISMHIDJF_b_mean.data) 
    NCCSMHIDJF85_mean = (NCCSMHIDJF85_mean.data -  NCCSMHIDJF_b_mean.data)  
    NOAADJF85_mean = (NOAADJF85_mean.data -  NOAADJF_b_mean.data) 
    
    CCCmaCanRCMMAM85_mean = (CCCmaCanRCMMAM85_mean.data - CCCmaCanRCMMAM_b_mean.data)
    CCCmaSMHIMAM85_mean = (CCCmaSMHIMAM85_mean.data -  CCCmaSMHIMAM_b_mean.data) 
    CNRMMAM85_mean = (CNRMMAM85_mean.data -  CNRMMAM_b_mean.data)                      
    CNRMSMHIMAM85_mean = (CNRMSMHIMAM85_mean.data -  CNRMSMHIMAM_b_mean.data)   
    CSIROMAM85_mean = (CSIROMAM85_mean.data -  CSIROMAM_b_mean.data)
    ICHECDMIMAM85_mean = (ICHECDMIMAM85_mean.data -  ICHECDMIMAM_b_mean.data)  
    ICHECCCLMMAM85_mean = (ICHECCCLMMAM85_mean.data -  ICHECCCLMMAM_b_mean.data) 
    ICHECKNMIMAM85_mean = (ICHECKNMIMAM85_mean.data -  ICHECKNMIMAM_b_mean.data) 
    ICHECMPIMAM85_mean = (ICHECMPIMAM85_mean.data -  ICHECMPIMAM_b_mean.data) 
    ICHECSMHIMAM85_mean = (ICHECSMHIMAM85_mean.data -  ICHECSMHIMAM_b_mean.data) 
    IPSLMAM85_mean = (IPSLMAM85_mean.data -  IPSLMAM_b_mean.data) 
    MIROCMAM85_mean = (MIROCMAM85_mean.data -  MIROCMAM_b_mean.data) 
    MOHCCCLMMAM85_mean = (MOHCCCLMMAM85_mean.data -  MOHCCCLMMAM_b_mean.data) 
    MOHCKNMIMAM85_mean = (MOHCKNMIMAM85_mean.data -  MOHCKNMIMAM_b_mean.data) 
    MOHCSMHIMAM85_mean = (MOHCSMHIMAM85_mean.data -  MOHCSMHIMAM_b_mean.data) 
    MPICCLMMAM85_mean = (MPICCLMMAM85_mean.data -  MPICCLMMAM_b_mean.data)        
    MPIREMOMAM85_mean = (MPIREMOMAM85_mean.data -  MPIREMOMAM_b_mean.data)           
    MPISMHIMAM85_mean = (MPISMHIMAM85_mean.data -  MPISMHIMAM_b_mean.data)  
    NCCSMHIMAM85_mean = (NCCSMHIMAM85_mean.data -  NCCSMHIMAM_b_mean.data)  
    NOAAMAM85_mean = (NOAAMAM85_mean.data -  NOAAMAM_b_mean.data) 
    
    CCCmaCanRCMJJA85_mean = (CCCmaCanRCMJJA85_mean.data - CCCmaCanRCMJJA_b_mean.data)
    CCCmaSMHIJJA85_mean = (CCCmaSMHIJJA85_mean.data -  CCCmaSMHIJJA_b_mean.data) 
    CNRMJJA85_mean = (CNRMJJA85_mean.data -  CNRMJJA_b_mean.data)                      
    CNRMSMHIJJA85_mean = (CNRMSMHIJJA85_mean.data -  CNRMSMHIJJA_b_mean.data)   
    CSIROJJA85_mean = (CSIROJJA85_mean.data -  CSIROJJA_b_mean.data)
    ICHECDMIJJA85_mean = (ICHECDMIJJA85_mean.data -  ICHECDMIJJA_b_mean.data)  
    ICHECCCLMJJA85_mean = (ICHECCCLMJJA85_mean.data -  ICHECCCLMJJA_b_mean.data) 
    ICHECKNMIJJA85_mean = (ICHECKNMIJJA85_mean.data -  ICHECKNMIJJA_b_mean.data) 
    ICHECMPIJJA85_mean = (ICHECMPIJJA85_mean.data -  ICHECMPIJJA_b_mean.data) 
    ICHECSMHIJJA85_mean = (ICHECSMHIJJA85_mean.data -  ICHECSMHIJJA_b_mean.data) 
    IPSLJJA85_mean = (IPSLJJA85_mean.data -  IPSLJJA_b_mean.data) 
    MIROCJJA85_mean = (MIROCJJA85_mean.data -  MIROCJJA_b_mean.data) 
    MOHCCCLMJJA85_mean = (MOHCCCLMJJA85_mean.data -  MOHCCCLMJJA_b_mean.data) 
    MOHCKNMIJJA85_mean = (MOHCKNMIJJA85_mean.data -  MOHCKNMIJJA_b_mean.data) 
    MOHCSMHIJJA85_mean = (MOHCSMHIJJA85_mean.data -  MOHCSMHIJJA_b_mean.data) 
    MPICCLMJJA85_mean = (MPICCLMJJA85_mean.data -  MPICCLMJJA_b_mean.data)        
    MPIREMOJJA85_mean = (MPIREMOJJA85_mean.data -  MPIREMOJJA_b_mean.data)           
    MPISMHIJJA85_mean = (MPISMHIJJA85_mean.data -  MPISMHIJJA_b_mean.data) 
    NCCSMHIJJA85_mean = (NCCSMHIJJA85_mean.data -  NCCSMHIJJA_b_mean.data)  
    NOAAJJA85_mean = (NOAAJJA85_mean.data -  NOAAJJA_b_mean.data) 
    
    CCCmaCanRCMYR85_mean = (CCCmaCanRCMYR85_mean.data - CCCmaCanRCMYR_b_mean.data)
    CCCmaSMHIYR85_mean = (CCCmaSMHIYR85_mean.data -  CCCmaSMHIYR_b_mean.data) 
    CNRMYR85_mean = (CNRMYR85_mean.data -  CNRMYR_b_mean.data)                      
    CNRMSMHIYR85_mean = (CNRMSMHIYR85_mean.data -  CNRMSMHIYR_b_mean.data)   
    CSIROYR85_mean = (CSIROYR85_mean.data -  CSIROYR_b_mean.data)
    ICHECDMIYR85_mean = (ICHECDMIYR85_mean.data -  ICHECDMIYR_b_mean.data)  
    ICHECCCLMYR85_mean = (ICHECCCLMYR85_mean.data -  ICHECCCLMYR_b_mean.data) 
    ICHECKNMIYR85_mean = (ICHECKNMIYR85_mean.data -  ICHECKNMIYR_b_mean.data) 
    ICHECMPIYR85_mean = (ICHECMPIYR85_mean.data -  ICHECMPIYR_b_mean.data) 
    ICHECSMHIYR85_mean = (ICHECSMHIYR85_mean.data -  ICHECSMHIYR_b_mean.data) 
    IPSLYR85_mean = (IPSLYR85_mean.data -  IPSLYR_b_mean.data) 
    MIROCYR85_mean = (MIROCYR85_mean.data -  MIROCYR_b_mean.data) 
    MOHCCCLMYR85_mean = (MOHCCCLMYR85_mean.data -  MOHCCCLMYR_b_mean.data) 
    MOHCKNMIYR85_mean = (MOHCKNMIYR85_mean.data -  MOHCKNMIYR_b_mean.data) 
    MOHCSMHIYR85_mean = (MOHCSMHIYR85_mean.data -  MOHCSMHIYR_b_mean.data) 
    MPICCLMYR85_mean = (MPICCLMYR85_mean.data -  MPICCLMYR_b_mean.data)        
    MPIREMOYR85_mean = (MPIREMOYR85_mean.data -  MPIREMOYR_b_mean.data)           
    MPISMHIYR85_mean = (MPISMHIYR85_mean.data -  MPISMHIYR_b_mean.data) 
    NCCSMHIYR85_mean = (NCCSMHIYR85_mean.data -  NCCSMHIYR_b_mean.data)  
    NOAAYR85_mean = (NOAAYR85_mean.data -  NOAAYR_b_mean.data) 
    
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
    
    ObsSONY = (CRUSON_mean.data)
    ObsDJFY = (CRUDJF_mean.data)
    ObsMAMY = (CRUMAM_mean.data)
    ObsJJAY = (CRUJJA_mean.data)
    ObsY = (CRUYR_mean.data)
    
    X = np.array([1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006]) 
    X2 = np.array ([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050])
    
    
    #-------------------------------------------------------------------------
    #PART 8: PLOT LINE GRAPH
    print "Observed"
    print ObsY
    print "Average RCM RCP 4.5"
    print AverageRY
    print "Average RCM RCP 8.5"
    print AverageRY85
    
    print "Observed SON"
    print ObsSONY
    print "Average RCM RCP 4.5 SON"
    print AverageSONRY
    print "Average RCM RCP 8.5 SON"
    print AverageSONRY85

    print "Observed DJF"
    print ObsDJFY
    print "Average RCM RCP 4.5 DJF"
    print AverageDJFRY
    print "Average RCM RCP 8.5 DJF"
    print AverageDJFRY85

    print "Observed MAM"
    print ObsMAMY
    print "Average RCM RCP 4.5 MAM"
    print AverageMAMRY
    print "Average RCM RCP 8.5 MAM"
    print AverageMAMRY85

    print "Observed JJA"
    print ObsJJAY
    print "Average RCM RCP 4.5 JJA"
    print AverageJJARY
    print "Average RCM RCP 8.5 JJA"
    print AverageJJARY85 
    

    #PART 8A: Regional Climate Models Line Graph
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsSONY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageSONRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi SON 1961-2050 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_SON_ALL4.5_V2.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsDJFY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageDJFRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi DJF 1961-2050 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_DJF_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsMAMY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageMAMRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi MAM 1961-2050 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_MAM_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsJJAY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageJJARY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi JJA 1961-2050 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_JJA_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageRY, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi 1961-2050 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Annual_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsSONY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageSONRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi SON 1961-2050 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_SON_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2050))
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsDJFY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageDJFRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi DJF 1961-2050 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_DJF_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsMAMY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageMAMRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi MAM 1961-2050 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_MAM_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsJJAY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageJJARY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi JJA 1961-2050 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_JJA_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2050))
    
    #set y axis limits
    plt.ylim(-2,6)
    
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
    plt.plot(X, ObsY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageRY85, label='Average RCM', lw=3, color='black', linestyle='--')   
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('TasMax for Malawi 1961-2050 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Annual_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #PART 8B: Average Line Graph
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,3)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X, ObsSONY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageSONRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageSONRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('TasMax for Malawi SON 1961-2050', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_SON_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,3)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X, ObsDJFY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageDJFRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageDJFRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('TasMax for Malawi DJF 1961-2050', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_DJF_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2050))
    
    #set y axis limits
    plt.ylim(-2,3)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X, ObsMAMY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageMAMRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageMAMRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('TasMax for Malawi MAM 1961-2050', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_MAM_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,3)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X, ObsJJAY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageJJARY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageJJARY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('TasMax for Malawi JJA 1961-2050', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_JJA_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2050)) 
    
    #set y axis limits
    plt.ylim(-2,3)
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X, ObsY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Near-Surface Temperature (degrees Celsius)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('TasMax for Malawi 1961-2050', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Tasmax_LineGraph_Annual_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
if __name__ == '__main__':
    main()