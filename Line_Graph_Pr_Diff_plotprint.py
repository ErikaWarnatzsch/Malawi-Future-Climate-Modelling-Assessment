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
    #PART 1: LOAD and FORMAT ALL PAST MODELS   
    CCCmaCanRCM_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_b =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_b = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    
    #Load exactly one cube from given file
    CCCmaCanRCM_b =  iris.load_cube(CCCmaCanRCM_b)
    CCCmaSMHI_b =  iris.load_cube(CCCmaSMHI_b)
    CNRM_b =  iris.load_cube(CNRM_b)
    CNRMSMHI_b =  iris.load_cube(CNRMSMHI_b)
    CSIRO_b =  iris.load_cube(CSIRO_b)
    ICHECDMI_b =  iris.load_cube(ICHECDMI_b, 'precipitation_flux')
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
    CCCmaCanRCM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CCCma-CanESM2_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CNRM= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI= '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'   
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_ICHEC-EC-EARTH_rcp45_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_IPSL-IPSL-CM5A-MR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MIROC-MIROC5_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_NCC-NorESM1-M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_4.5/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'     
    
    CCCmaCanRCM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_CCCma-CanRCM4_r2_day_20060101-20701231.nc'
    CCCmaSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CCCma-CanESM2_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CNRM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'
    CNRMSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    CSIRO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    ICHECDMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r3i1p1_DMI-HIRHAM5_v2_day_20060101-20701231.nc'
    ICHECCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'    
    ICHECKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r1i1p1_KNMI-RACMO22T_v1_day_20060101-20701231.nc'   
    ICHECMPI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'
    ICHECSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_ICHEC-EC-EARTH_rcp85_r12i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    IPSL85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MIROC85 =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MIROC-MIROC5_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc' 
    MOHCCCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc' 
    MOHCKNMI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_20060101-20701231.nc'
    MOHCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    MPICCLM85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_CLMcom-CCLM4-8-17_v1_day_20060101-20701231.nc'     
    MPIREMO85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_MPI-CSC-REMO2009_v1_day_20060101-20701231.nc'    
    MPISMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'
    NCCSMHI85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_NCC-NorESM1-M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'   
    NOAA85 = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/RCP_8.5/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v1_day_20060101-20701231.nc'     
    
    #Load exactly one cube from given file    
    CCCmaCanRCM = iris.load_cube(CCCmaCanRCM)
    CCCmaSMHI = iris.load_cube(CCCmaSMHI)
    CNRM = iris.load_cube(CNRM)
    CNRMSMHI = iris.load_cube(CNRMSMHI)
    CSIRO = iris.load_cube(CSIRO)
    ICHECDMI = iris.load_cube(ICHECDMI, 'precipitation_flux')
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
    ICHECDMI85 = iris.load_cube(ICHECDMI85, 'precipitation_flux')
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
    CRU= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.pre.dat.nc'
    UDel= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_precip.mon.total.v401.nc'
    GPCC= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/ESRL_PSD_GPCC_precip.mon.combined.total.v7.nc'
    
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'precipitation')
    UDel = iris.load_cube(UDel)
    GPCC = iris.load_cube(GPCC)
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    UDel.coord('latitude').guess_bounds()
    GPCC.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    UDel.coord('longitude').guess_bounds()
    GPCC.coord('longitude').guess_bounds()
    
    
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
    UDel = UDel.extract(Central_Malawi)
    GPCC = GPCC.extract(Central_Malawi)
    
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
    
    CRU_b = CRU.extract(t_constraint)
    UDel_b = UDel.extract(t_constraint)
    GPCC_b = GPCC.extract(t_constraint)
    
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT FILES TO BE PLOT SPECIFIC FOR MONTHLY PLOTTING
    
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
    iriscc.add_month_number(UDel, 'time')
    iriscc.add_month_number(GPCC, 'time')
    iriscc.add_month_number(CRU_b, 'time')
    iriscc.add_month_number(UDel_b, 'time')
    iriscc.add_month_number(GPCC_b, 'time')
    
    #PART 5A: COMPLETE FORMATING FOR BASELINE MONTHLY DATA
    #Convert units to match, CORDEX data in precipitation_flux (kg m-2 s-1) but want all data in precipitation rate (mm month-1).
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year and 12 months in the year, the conversion is:
    Convert=31557600/12
       
    CCCmaCanRCM_b_m = CCCmaCanRCM_b*Convert
    CCCmaSMHI_b_m = CCCmaSMHI_b*Convert
    CNRM_b_m = CNRM_b*Convert
    CNRMSMHI_b_m = CNRMSMHI_b*Convert 
    CSIRO_b_m = CSIRO_b*Convert
    ICHECDMI_b_m = ICHECDMI_b*Convert
    ICHECCCLM_b_m = ICHECCCLM_b*Convert
    ICHECKNMI_b_m = ICHECKNMI_b*Convert
    ICHECMPI_b_m = ICHECMPI_b*Convert
    ICHECSMHI_b_m = ICHECSMHI_b*Convert
    IPSL_b_m = IPSL_b*Convert
    MIROC_b_m = MIROC_b*Convert
    MOHCCCLM_b_m = MOHCCCLM_b*Convert
    MOHCKNMI_b_m = MOHCKNMI_b*Convert
    MOHCSMHI_b_m = MOHCSMHI_b*Convert
    MPICCLM_b_m = MPICCLM_b*Convert
    MPIREMO_b_m = MPIREMO_b*Convert
    MPISMHI_b_m = MPISMHI_b*Convert
    NCCSMHI_b_m = NCCSMHI_b*Convert
    NOAA_b_m = NOAA_b*Convert
    
    #Complete formatting of baseline data for use in 2030 and 2050 models
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month 
    CCCmaCanRCM_b_m = CCCmaCanRCM_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_b_m = CCCmaSMHI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_b_m = CNRM_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_b_m = CNRMSMHI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_b_m = CSIRO_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_b_m = ICHECDMI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_b_m = ICHECCCLM_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_b_m = ICHECKNMI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_b_m = ICHECMPI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_b_m = ICHECSMHI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_b_m = IPSL_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_b_m = MIROC_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_b_m = MOHCCCLM_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_b_m = MOHCKNMI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_b_m = MOHCSMHI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_b_m = MPICCLM_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_b_m = MPIREMO_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_b_m = MPISMHI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_b_m = NCCSMHI_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_b_m = NOAA_b_m.aggregated_by('month_number', iris.analysis.MEAN)
    
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

    #Convert units to match, UDel data in cm per month but want precipitation rate in mm per month.
    #Since there are 10mm in a cm, the conversion is:
    Convert=10
    UDel_m = UDel_b*Convert
 
    #CRU and GPCC already in mm/month
    CRU_m = CRU_b
    GPCC_m = GPCC_b
    
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month 
    CRU_m = CRU_m.aggregated_by('month_number', iris.analysis.MEAN) 
    UDel_m = UDel_m.aggregated_by('month_number', iris.analysis.MEAN) 
    GPCC_m = GPCC_m.aggregated_by('month_number', iris.analysis.MEAN) 
    
    #Returns an array of area weights, with the same dimensions as the cube.
    CRU_m_grid_areas = iris.analysis.cartography.area_weights(CRU_m)
    UDel_m_grid_areas = iris.analysis.cartography.area_weights(UDel_m)
    GPCC_m_grid_areas = iris.analysis.cartography.area_weights(GPCC_m)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons    
    CRU_m_mean = CRU_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_m_grid_areas) 
    UDel_m_mean = UDel_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_m_grid_areas)
    GPCC_m_mean = GPCC_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCC_m_grid_areas)
    
    #Create average
    ObsY_m = (CRU_m_mean.data + UDel_m_mean.data + GPCC_m_mean.data)/3.
    
    #-------------------------------------------------------------------------
    #PART 5C: MODEL FORMATTING
    #Convert units to match, CORDEX data in precipitation_flux (kg m-2 s-1) but want all data in precipitation rate (mm month-1).
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year and 12 months in the year, the conversion is:
    Convert=31557600/12
       
    CCCmaCanRCM_m = CCCmaCanRCM*Convert
    CCCmaSMHI_m = CCCmaSMHI*Convert
    CNRM_m = CNRM*Convert
    CNRMSMHI_m = CNRMSMHI*Convert 
    CSIRO_m = CSIRO*Convert
    ICHECDMI_m = ICHECDMI*Convert
    ICHECCCLM_m = ICHECCCLM*Convert
    ICHECKNMI_m = ICHECKNMI*Convert
    ICHECMPI_m = ICHECMPI*Convert
    ICHECSMHI_m = ICHECSMHI*Convert
    IPSL_m = IPSL*Convert
    MIROC_m = MIROC*Convert
    MOHCCCLM_m = MOHCCCLM*Convert
    MOHCKNMI_m = MOHCKNMI*Convert
    MOHCSMHI_m = MOHCSMHI*Convert
    MPICCLM_m = MPICCLM*Convert
    MPIREMO_m = MPIREMO*Convert
    MPISMHI_m = MPISMHI*Convert
    NCCSMHI_m = NCCSMHI*Convert
    NOAA_m = NOAA*Convert
    
    CCCmaCanRCM85_m = CCCmaCanRCM85*Convert
    CCCmaSMHI85_m = CCCmaSMHI85*Convert
    CNRM85_m = CNRM85*Convert
    CNRMSMHI85_m = CNRMSMHI85*Convert 
    CSIRO85_m = CSIRO85*Convert
    ICHECDMI85_m = ICHECDMI85*Convert
    ICHECCCLM85_m = ICHECCCLM85*Convert
    ICHECKNMI85_m = ICHECKNMI85*Convert
    ICHECMPI85_m = ICHECMPI85*Convert
    ICHECSMHI85_m = ICHECSMHI85*Convert
    IPSL85_m = IPSL85*Convert
    MIROC85_m = MIROC85*Convert
    MOHCCCLM85_m = MOHCCCLM85*Convert
    MOHCKNMI85_m = MOHCKNMI85*Convert
    MOHCSMHI85_m = MOHCSMHI85*Convert
    MPICCLM85_m = MPICCLM85*Convert
    MPIREMO85_m = MPIREMO85*Convert
    MPISMHI85_m = MPISMHI85*Convert
    NCCSMHI85_m = NCCSMHI85*Convert
    NOAA85_m = NOAA85*Convert

    
    #-------------------------------------------------------------------------
    #PART 5D: 2030 FORMATING

    #time constraint to make all series the same (2020-2049)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_m30 = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)

    CCCmaCanRCM_m30 = CCCmaCanRCM_m.extract(t_constraint_m30)
    CCCmaSMHI_m30 = CCCmaSMHI_m.extract(t_constraint_m30)
    CNRM_m30 =CNRM_m.extract(t_constraint_m30)
    CNRMSMHI_m30 =CNRMSMHI_m.extract(t_constraint_m30)
    CSIRO_m30=CSIRO_m.extract(t_constraint_m30)
    ICHECDMI_m30=ICHECDMI_m.extract(t_constraint_m30)
    ICHECCCLM_m30=ICHECCCLM_m.extract(t_constraint_m30)
    ICHECKNMI_m30=ICHECKNMI_m.extract(t_constraint_m30)
    ICHECMPI_m30=ICHECMPI_m.extract(t_constraint_m30)
    ICHECSMHI_m30=ICHECSMHI_m.extract(t_constraint_m30)
    IPSL_m30=IPSL_m.extract(t_constraint_m30)
    MIROC_m30=MIROC_m.extract(t_constraint_m30)
    MOHCCCLM_m30=MOHCCCLM_m.extract(t_constraint_m30)
    MOHCKNMI_m30=MOHCKNMI_m.extract(t_constraint_m30)
    MOHCSMHI_m30=MOHCSMHI_m.extract(t_constraint_m30)
    MPICCLM_m30=MPICCLM_m.extract(t_constraint_m30)
    MPIREMO_m30=MPIREMO_m.extract(t_constraint_m30)
    MPISMHI_m30=MPISMHI_m.extract(t_constraint_m30)
    NCCSMHI_m30=NCCSMHI_m.extract(t_constraint_m30)
    NOAA_m30=NOAA_m.extract(t_constraint_m30) 
    
    CCCmaCanRCM85_m30= CCCmaCanRCM85_m.extract(t_constraint_m30)
    CCCmaSMHI85_m30 =  CCCmaSMHI85_m.extract(t_constraint_m30)
    CNRM85_m30 = CNRM85_m.extract(t_constraint_m30)
    CNRMSMHI85_m30 = CNRMSMHI85_m.extract(t_constraint_m30)
    CSIRO85_m30 = CSIRO85_m.extract(t_constraint_m30)
    ICHECDMI85_m30 = ICHECDMI85_m.extract(t_constraint_m30)
    ICHECCCLM85_m30 = ICHECCCLM85_m.extract(t_constraint_m30)
    ICHECKNMI85_m30 = ICHECKNMI85_m.extract(t_constraint_m30)
    ICHECMPI85_m30 = ICHECMPI85_m.extract(t_constraint_m30)
    ICHECSMHI85_m30 = ICHECSMHI85_m.extract(t_constraint_m30)
    IPSL85_m30 = IPSL85_m.extract(t_constraint_m30)
    MIROC85_m30 = MIROC85_m.extract(t_constraint_m30)
    MOHCCCLM85_m30 = MOHCCCLM85_m.extract(t_constraint_m30)
    MOHCKNMI85_m30 = MOHCKNMI85_m.extract(t_constraint_m30)
    MOHCSMHI85_m30 = MOHCSMHI85_m.extract(t_constraint_m30)
    MPICCLM85_m30 = MPICCLM85_m.extract(t_constraint_m30)
    MPIREMO85_m30 = MPIREMO85_m.extract(t_constraint_m30)
    MPISMHI85_m30 = MPISMHI85_m.extract(t_constraint_m30)
    NCCSMHI85_m30 = NCCSMHI85_m.extract(t_constraint_m30)
    NOAA85_m30 =NOAA85_m.extract(t_constraint_m30)
     
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
    #PART 5E: 2050 FORMATING
    #time constraint to make all series the same (2040-2069)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_m50 = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)

    CCCmaCanRCM_m = CCCmaCanRCM_m.extract(t_constraint_m50)
    CCCmaSMHI_m = CCCmaSMHI_m.extract(t_constraint_m50)
    CNRM_m =CNRM_m.extract(t_constraint_m50)
    CNRMSMHI_m =CNRMSMHI_m.extract(t_constraint_m50)
    CSIRO_m = CSIRO_m.extract(t_constraint_m50)
    ICHECDMI_m = ICHECDMI_m.extract(t_constraint_m50)
    ICHECCCLM_m = ICHECCCLM_m.extract(t_constraint_m50)
    ICHECKNMI_m = ICHECKNMI_m.extract(t_constraint_m50)
    ICHECMPI_m = ICHECMPI_m.extract(t_constraint_m50)
    ICHECSMHI_m = ICHECSMHI_m.extract(t_constraint_m50)
    IPSL_m = IPSL_m.extract(t_constraint_m50)
    MIROC_m = MIROC_m.extract(t_constraint_m50)
    MOHCCCLM_m = MOHCCCLM_m.extract(t_constraint_m50)
    MOHCKNMI_m = MOHCKNMI_m.extract(t_constraint_m50)
    MOHCSMHI_m = MOHCSMHI_m.extract(t_constraint_m50)
    MPICCLM_m = MPICCLM_m.extract(t_constraint_m50)
    MPIREMO_m = MPIREMO_m.extract(t_constraint_m50)
    MPISMHI_m = MPISMHI_m.extract(t_constraint_m50)
    NCCSMHI_m = NCCSMHI_m.extract(t_constraint_m50)
    NOAA_m = NOAA_m.extract(t_constraint_m50) 
    
    CCCmaCanRCM85_m =  CCCmaCanRCM85_m.extract(t_constraint_m50)
    CCCmaSMHI85_m =  CCCmaSMHI85_m.extract(t_constraint_m50)
    CNRM85_m = CNRM85_m.extract(t_constraint_m50)
    CNRMSMHI85_m = CNRMSMHI85_m.extract(t_constraint_m50)
    CSIRO85_m = CSIRO85_m.extract(t_constraint_m50)
    ICHECDMI85_m = ICHECDMI85_m.extract(t_constraint_m50)
    ICHECCCLM85_m = ICHECCCLM85_m.extract(t_constraint_m50)
    ICHECKNMI85_m = ICHECKNMI85_m.extract(t_constraint_m50)
    ICHECMPI85_m = ICHECMPI85_m.extract(t_constraint_m50)
    ICHECSMHI85_m = ICHECSMHI85_m.extract(t_constraint_m50)
    IPSL85_m = IPSL85_m.extract(t_constraint_m50)
    MIROC85_m = MIROC85_m.extract(t_constraint_m50)
    MOHCCCLM85_m = MOHCCCLM85_m.extract(t_constraint_m50)
    MOHCKNMI85_m = MOHCKNMI85_m.extract(t_constraint_m50)
    MOHCSMHI85_m = MOHCSMHI85_m.extract(t_constraint_m50)
    MPICCLM85_m = MPICCLM85_m.extract(t_constraint_m50)
    MPIREMO85_m = MPIREMO85_m.extract(t_constraint_m50)
    MPISMHI85_m = MPISMHI85_m.extract(t_constraint_m50)
    NCCSMHI85_m = NCCSMHI85_m.extract(t_constraint_m50)
    NOAA85_m =NOAA85_m.extract(t_constraint_m50) 
    
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

    #import minimum and maximum numbers (from the output_Pr_Mean_Monthly.csv file, negative numbers considered zero (0)
    Max_m_2030_45 = (278.85, 255.10, 232.27, 97.61, 26.37, 7.67, 7.12, 3.79, 3.95,19.37, 96.12,248.92)
    Max_m_2030_85= (291.22,260.32,218.37,107.30,22.71,7.91,7.44,3.70,5.89,22.17,89.84,255.96)
    Max_m_2050_45= (293.35,254.26,264.97,94.82,22.49,8.48,7.69,3.93,4.16,17.74,95.30,239.48)
    Max_m_2050_85= (307.52,290.02,245.44,119.51,22.38,6.79,6.53,3.58,4.07,17.88,97.03,254.81)
    Min_m_2030_45= (224.86,170.15,168.29,65.32,8.25,1.77,1.21,0,0,0,40.35,162.36)
    Min_m_2030_85= (196.86,157.99,166.73,60.26,11.48,0.29,0.54,0,0,1.30,33.28,132.99)
    Min_m_2050_45= (207.80,166.69,168.30,55.42,2.96,1.58,0.42,0.00,0,0,41.64,157.46)
    Min_m_2050_85= (195.24,163.65,169.55,60.09,8.84,0,0,0,0,0,17.06,151.36)


                          
    #-------------------------------------------------------------------------
    #PART 6: PRINT AND PLOT LINE MONTHLY GRAPH 
    import csv
    with open('output_Pr_Mean_Monthly.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Parameter', 'Means'])
   
        writer.writerow(["CCCmaCanRCM_m_mean"] + CCCmaCanRCM_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_m_mean"] + CCCmaSMHI_m_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["CNRM_m_mean"] + CNRM_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_m_mean"] + CNRMSMHI_m_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO_m_mean"] + CSIRO_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_m_mean"] + ICHECDMI_m_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_m_mean"] + ICHECCCLM_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI_m_mean"] + ICHECKNMI_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI_m_mean"] + ICHECMPI_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_m_mean"] + ICHECSMHI_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL_m_mean"] + IPSL_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_m_mean"] + MIROC_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_m_mean"] + MOHCCCLM_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_m_mean"] + MOHCKNMI_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_m_mean"] + MOHCSMHI_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_m_mean"] + MPICCLM_m_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_m_mean"] + MPIREMO_m_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MPISMHI_m_mean"] + MPISMHI_m_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHI_m_mean"] + NCCSMHI_m_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_m_mean"] + NOAA_m_mean.data.flatten().astype(np.str).tolist())  

        writer.writerow(["CCCmaCanRCM85_m_mean"] + CCCmaCanRCM85_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_m_mean"] + CCCmaSMHI85_m_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["CNRM85_m_mean"] + CNRM85_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_m_mean"] + CNRMSMHI85_m_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO85_m_mean"] + CSIRO85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_m_mean"] + ICHECDMI85_m_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM85_m_mean"] + ICHECCCLM85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI85_m_mean"] + ICHECKNMI85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI85_m_mean"] + ICHECMPI85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI85_m_mean"] + ICHECSMHI85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL85_m_mean"] + IPSL85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_m_mean"] + MIROC85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_m_mean"] + MOHCCCLM85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI85_m_mean"] + MOHCKNMI85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI85_m_mean"] + MOHCSMHI85_m_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM85_m_mean"] + MPICCLM85_m_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_m_mean"] + MPIREMO85_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_m_mean"] + MPISMHI85_m_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHI85_m_mean"] + NCCSMHI85_m_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA85_m_mean"] + NOAA85_m_mean.data.flatten().astype(np.str).tolist())  
        
        writer.writerow(["CCCmaCanRCM_m30_mean"] + CCCmaCanRCM_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_m30_mean"] + CCCmaSMHI_m30_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["CNRM_m30_mean"] + CNRM_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_m30_mean"] + CNRMSMHI_m30_mean.data.flatten().astype(np.str).tolist())        
        writer.writerow(["CSIRO_m30_mean"] + CSIRO_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_m30_mean"] + ICHECDMI_m30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_m30_mean"] + ICHECCCLM_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECKNMI_m30_mean"] + ICHECKNMI_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECMPI_m30_mean"] + ICHECMPI_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_m30_mean"] + ICHECSMHI_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["IPSL_m30_mean"] + IPSL_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_m30_mean"] + MIROC_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_m30_mean"] + MOHCCCLM_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_m30_mean"] + MOHCKNMI_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_m30_mean"] + MOHCSMHI_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_m30_mean"] + MPICCLM_m30_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_m30_mean"] + MPIREMO_m30_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MPISMHI_m30_mean"] + MPISMHI_m30_mean.data.flatten().astype(np.str).tolist())         
        writer.writerow(["NCCSMHI_m30_mean"] + NCCSMHI_m30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_m30_mean"] + NOAA_m30_mean.data.flatten().astype(np.str).tolist())  
        
        writer.writerow(["CCCmaCanRCM85_m30_mean"] + CCCmaCanRCM85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI85_m30_mean"] + CCCmaSMHI85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM85_m30_mean"] + CNRM85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI85_m30_mean"] + CNRMSMHI85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CSIRO85_m30_mean"] + CSIRO85_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI85_m30_mean"] + ICHECDMI85_m30_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLM85_m30_mean"] + ICHECCCLM85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMI85_m30_mean"] + ICHECKNMI85_m30_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI85_m30_mean"] + ICHECMPI85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECSMHI85_m30_mean"] + ICHECSMHI85_m30_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["IPSL85_m30_mean"] + IPSL85_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC85_m30_mean"] + MIROC85_m30_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM85_m30_mean"] + MOHCCCLM85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMI85_m30_mean"] + MOHCKNMI85_m30_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCSMHI85_m30_mean"] + MOHCSMHI85_m30_mean.data.flatten().astype(np.str).tolist())  
        writer.writerow(["MPICCLM85_m30_mean"] + MPICCLM85_m30_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO85_m30_mean"] + MPIREMO85_m30_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHI85_m30_mean"] + MPISMHI85_m30_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["NCCSMHI85_m30_mean"] + NCCSMHI85_m30_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA85_m30_mean"] + NOAA85_m30_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CRU_m"] + CRU_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDEL_m"] + UDel_m_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCC_m"] + GPCC_m_mean.data.flatten().astype(np.str).tolist())
        
    #set x-axis for all graphs
    X_m = np.arange(1,13,1) 

    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
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
    plt.plot(X_m, ObsY_m.data, label='Observed 1971-2000', lw=3, color='black') 
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_ALL4.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
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
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')     
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_ALL8.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time' 
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
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
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')  
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_ALL4.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time' 
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
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
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_ALL8.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                        
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.plot(X_m, AverageRY_m, label='Average RCM 2040-2069 RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X_m, AverageRY_m30, label='Average RCM 2020-2049 RCP 4.5', lw=1.5, color='cyan', linestyle=':')
    plt.plot(X_m, AverageRY85_m, label='Average RCM 2040-2069 RCP 8.5', lw=1.5, color='magenta')
    plt.plot(X_m, AverageRY85_m30, label='Average RCM 2020-2049 RCP 8.5', lw=1.5, color='magenta', linestyle=':')
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('Pr for Central Malawi by Month', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_AVE_2050.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #set x-axis for all graphs
    X_m = np.arange(1,13,1) 

    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.plot(X_m, CCCmaCanRCM_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CCCmaSMHI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRM_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRMSMHI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CSIRO_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECDMI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECCCLM_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECKNMI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECMPI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECSMHI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, IPSL_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MIROC_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCCCLM_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCKNMI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCSMHI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPICCLM_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPIREMO_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPISMHI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NCCSMHI_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NOAA_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, AverageRY_m, label='Average RCM 2040-2069', lw=3, color='cyan')
    plt.plot(X_m, Min_m_2050_45, label = 'Minimum RCM 2040-2069', lw=3, color='magenta')
    plt.plot(X_m, Max_m_2050_45, label = 'Maximum RCM 2040-2069', lw=3, color='blue')
    plt.plot(X_m, ObsY_m.data, label='Observed 1971-2000', lw=3, color='black') 
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_MMA4.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time'       
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.plot(X_m, CCCmaSMHI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRM85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRMSMHI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CSIRO85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECDMI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECCCLM85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECKNMI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECMPI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECSMHI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, IPSL85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MIROC85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCCCLM85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCKNMI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCSMHI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPICCLM85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPIREMO85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPISMHI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NCCSMHI85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NOAA85_m_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, AverageRY85_m, label='Average RCM 2040-2069', lw=3, color='cyan')
    plt.plot(X_m, Min_m_2050_85, label = 'Minimum RCM 2040-2069', lw=3, color='magenta')
    plt.plot(X_m, Max_m_2050_85, label = 'Maximum RCM 2040-2069', lw=3, color='blue')
    plt.plot(X_m, ObsY_m.data, label='Observed 1971-2000', lw=3, color='black') 
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_MMA8.5_2050.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time' 
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.plot(X_m, CCCmaCanRCM_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CCCmaSMHI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRM_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRMSMHI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CSIRO_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECDMI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECCCLM_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECKNMI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECMPI_m30_mean.data, lw=1, color='grey', linestyle='--') 
    plt.plot(X_m, ICHECSMHI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, IPSL_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MIROC_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCCCLM_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCKNMI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCSMHI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPICCLM_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPIREMO_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPISMHI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NCCSMHI_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NOAA_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, AverageRY_m30, label='Average RCM 2020-2049', lw=3, color='cyan')
    plt.plot(X_m, Min_m_2030_45, label = 'Minimum RCM 2020-2049', lw=3, color='magenta')
    plt.plot(X_m, Max_m_2030_45, label = 'Maximum RCM 2020-2049', lw=3, color='blue')
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')  
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_MMA4.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    #set x-axis ticks                                   
    plt.xticks(range(12), calendar.month_abbr[0:12])
    
    #assign the line colours and set x axis to 'month' rather than 'time' 
    plt.plot(X_m,CRU_m_mean.data, lw=1, color='grey')   
    plt.plot(X_m,UDel_m_mean.data, lw=1, color='grey')
    plt.plot(X_m,GPCC_m_mean.data, lw=1, color='grey')
    plt.fill_between(X_m,CRU_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,CRU_m_mean.data,GPCC_m_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X_m,GPCC_m_mean.data,UDel_m_mean.data, color='grey', alpha='0.5')
    plt.plot(X_m, CCCmaCanRCM85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CCCmaSMHI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRM85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CNRMSMHI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, CSIRO85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECDMI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECCCLM85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECKNMI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECMPI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, ICHECSMHI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, IPSL85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MIROC85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCCCLM85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCKNMI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MOHCSMHI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPICCLM85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPIREMO85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, MPISMHI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NCCSMHI85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, NOAA85_m30_mean.data, lw=1, color='grey', linestyle='--')
    plt.plot(X_m, AverageRY85_m30, label='Average RCM 2020-2049', lw=3, color='cyan')
    plt.plot(X_m, Min_m_2030_85, label = 'Minimum RCM 2020-2049', lw=3, color='magenta')
    plt.plot(X_m, Max_m_2030_85, label = 'Maximum RCM 2020-2049', lw=3, color='blue') 
    plt.plot(X_m, ObsY_m.data, label='Observed 2071-2000', lw=3, color='black')
        
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per month)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi by Month RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Monthly_MMA8.5_2030.png', bbox_inches='tight')
    
    #show the graph in the console
    iplt.show()
    
    
    #-------------------------------------------------------------------------
    #PART 7: FORMAT DATA TO BE PLOT SPECIFIC FOR YEARLY PLOTTING
    
    #time constraint to make all observed data series the same
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_obs = iris.Constraint(time=lambda cell: 1961 <= cell.point.year <= 2006)
    CRU = CRU.extract(t_constraint_obs)
    UDel = UDel.extract(t_constraint_obs)
    GPCC = GPCC.extract(t_constraint_obs)
    
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
    iriscc.add_year(UDel, 'time')
    iriscc.add_year(GPCC, 'time')
    iriscc.add_year(CRU_b, 'time')
    iriscc.add_year(UDel_b, 'time')
    iriscc.add_year(GPCC_b, 'time')
    
    #Convert units to match, CORDEX data in precipitation_flux (kg m-2 s-1) but want all data in precipitation rate (mm year-1).
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year, the conversion is: 
    Convert=31557600
    CCCmaCanRCM_b = CCCmaCanRCM_b*Convert
    CCCmaSMHI_b = CCCmaSMHI_b*Convert
    CNRM_b = CNRM_b*Convert
    CNRMSMHI_b = CNRMSMHI_b*Convert 
    CSIRO_b = CSIRO_b*Convert
    ICHECDMI_b = ICHECDMI_b*Convert
    ICHECCCLM_b = ICHECCCLM_b*Convert
    ICHECKNMI_b = ICHECKNMI_b*Convert
    ICHECMPI_b = ICHECMPI_b*Convert
    ICHECSMHI_b = ICHECSMHI_b*Convert
    IPSL_b = IPSL_b*Convert
    MIROC_b = MIROC_b*Convert
    MOHCCCLM_b = MOHCCCLM_b*Convert
    MOHCKNMI_b = MOHCKNMI_b*Convert
    MOHCSMHI_b = MOHCSMHI_b*Convert
    MPICCLM_b = MPICCLM_b*Convert
    MPIREMO_b = MPIREMO_b*Convert
    MPISMHI_b = MPISMHI_b*Convert
    NCCSMHI_b = NCCSMHI_b*Convert
    NOAA_b = NOAA_b*Convert
    
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
    
    #Convert units to match, CRU and GPCC data is in mm per month but want precipitation rate in mm per year.
    #Since there are 12 months in the year, the conversion is:
    Convert=12
    CRU = CRU*Convert
    GPCC = GPCC*Convert
    
    CRU_b = CRU_b*Convert
    GPCC_b = GPCC_b*Convert
           
    #Convert units to match, UDel data in cm per month but want precipitation rate in mm per year.
    #Since there are 12 months in the year and 10mm in a cm, the conversion is:
    Convert=12*10
    UDel = UDel*Convert
    UDel_b = UDel_b*Convert
    
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
    iriscc.add_season(UDel, 'time')
    iriscc.add_season(GPCC, 'time')
    iriscc.add_season(CRU_b, 'time')
    iriscc.add_season(UDel_b, 'time')
    iriscc.add_season(GPCC_b, 'time')
        
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
    UDelSON = UDel.extract(SON)
    GPCCSON = GPCC.extract(SON)
    CRUSON_b = CRU_b.extract(SON)
    UDelSON_b = UDel_b.extract(SON)
    GPCCSON_b = GPCC_b.extract(SON)
    
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
    UDelDJF = UDel.extract(DJF)
    GPCCDJF = GPCC.extract(DJF)
    CRUDJF_b = CRU_b.extract(DJF)
    UDelDJF_b = UDel_b.extract(DJF)
    GPCCDJF_b = GPCC_b.extract(DJF)
    
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
    UDelMAM = UDel.extract(MAM)
    GPCCMAM = GPCC.extract(MAM)
    CRUMAM_b = CRU_b.extract(MAM)
    UDelMAM_b = UDel_b.extract(MAM)
    GPCCMAM_b = GPCC_b.extract(MAM)
    
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
    UDelJJA = UDel.extract(JJA)
    GPCCJJA = GPCC.extract(JJA)
    CRUJJA_b = CRU_b.extract(JJA)
    UDelJJA_b = UDel_b.extract(JJA)
    GPCCJJA_b = GPCC_b.extract(JJA)
    
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
    UDelSON = UDelSON.aggregated_by('year', iris.analysis.MEAN)
    GPCCSON = GPCCSON.aggregated_by('year', iris.analysis.MEAN)
    CRUSON_b = CRUSON_b.aggregated_by('year', iris.analysis.MEAN)  
    UDelSON_b = UDelSON_b.aggregated_by('year', iris.analysis.MEAN)
    GPCCSON_b = GPCCSON_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    UDelDJF = UDelDJF.aggregated_by('year', iris.analysis.MEAN)
    GPCCDJF = GPCCDJF.aggregated_by('year', iris.analysis.MEAN)
    CRUDJF_b = CRUDJF_b.aggregated_by('year', iris.analysis.MEAN)  
    UDelDJF_b = UDelDJF_b.aggregated_by('year', iris.analysis.MEAN)
    GPCCDJF_b = GPCCDJF_b.aggregated_by('year', iris.analysis.MEAN)
 
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
    UDelMAM = UDelMAM.aggregated_by('year', iris.analysis.MEAN)
    GPCCMAM = GPCCMAM.aggregated_by('year', iris.analysis.MEAN)
    CRUMAM_b = CRUMAM_b.aggregated_by('year', iris.analysis.MEAN)  
    UDelMAM_b = UDelMAM_b.aggregated_by('year', iris.analysis.MEAN)
    GPCCMAM_b = GPCCMAM_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    UDelJJA = UDelJJA.aggregated_by('year', iris.analysis.MEAN)
    GPCCJJA = GPCCJJA.aggregated_by('year', iris.analysis.MEAN)
    CRUJJA_b = CRUJJA_b.aggregated_by('year', iris.analysis.MEAN)  
    UDelJJA_b = UDelJJA_b.aggregated_by('year', iris.analysis.MEAN)
    GPCCJJA_b = GPCCJJA_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    UDelYR = UDel.aggregated_by('year', iris.analysis.MEAN)
    GPCCYR = GPCC.aggregated_by('year', iris.analysis.MEAN)
    CRUYR_b = CRU_b.aggregated_by('year', iris.analysis.MEAN)  
    UDelYR_b = UDel_b.aggregated_by('year', iris.analysis.MEAN)
    GPCCYR_b = GPCC_b.aggregated_by('year', iris.analysis.MEAN)
    
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
    UDelSON_grid_areas = iris.analysis.cartography.area_weights(UDelSON)
    GPCCSON_grid_areas = iris.analysis.cartography.area_weights(GPCCSON)
    CRUSON_b_grid_areas = iris.analysis.cartography.area_weights(CRUSON_b)
    UDelSON_b_grid_areas = iris.analysis.cartography.area_weights(UDelSON_b)
    GPCCSON_b_grid_areas = iris.analysis.cartography.area_weights(GPCCSON_b)
    
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
    UDelDJF_grid_areas = iris.analysis.cartography.area_weights(UDelDJF)
    GPCCDJF_grid_areas = iris.analysis.cartography.area_weights(GPCCDJF)
    CRUDJF_b_grid_areas = iris.analysis.cartography.area_weights(CRUDJF_b)
    UDelDJF_b_grid_areas = iris.analysis.cartography.area_weights(UDelDJF_b)
    GPCCDJF_b_grid_areas = iris.analysis.cartography.area_weights(GPCCDJF_b)
    
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
    UDelMAM_grid_areas = iris.analysis.cartography.area_weights(UDelMAM)
    GPCCMAM_grid_areas = iris.analysis.cartography.area_weights(GPCCMAM)
    CRUMAM_b_grid_areas = iris.analysis.cartography.area_weights(CRUMAM_b)
    UDelMAM_b_grid_areas = iris.analysis.cartography.area_weights(UDelMAM_b)
    GPCCMAM_b_grid_areas = iris.analysis.cartography.area_weights(GPCCMAM_b)
    
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
    UDelJJA_grid_areas = iris.analysis.cartography.area_weights(UDelJJA)
    GPCCJJA_grid_areas = iris.analysis.cartography.area_weights(GPCCJJA)
    CRUJJA_b_grid_areas = iris.analysis.cartography.area_weights(CRUJJA_b)
    UDelJJA_b_grid_areas = iris.analysis.cartography.area_weights(UDelJJA_b)
    GPCCJJA_b_grid_areas = iris.analysis.cartography.area_weights(GPCCJJA_b)
    
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
    UDelYR_grid_areas = iris.analysis.cartography.area_weights(UDelYR)
    GPCCYR_grid_areas = iris.analysis.cartography.area_weights(GPCCYR)
    CRUYR_b_grid_areas = iris.analysis.cartography.area_weights(CRUYR_b)
    UDelYR_b_grid_areas = iris.analysis.cartography.area_weights(UDelYR_b)
    GPCCYR_b_grid_areas = iris.analysis.cartography.area_weights(GPCCYR_b)
    
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
    UDelSON_mean = UDelSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelSON_grid_areas)
    GPCCSON_mean = GPCCSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCSON_grid_areas)
    CRUSON_b_mean = CRUSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUSON_b_grid_areas) 
    UDelSON_b_mean = UDelSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelSON_b_grid_areas)
    GPCCSON_b_mean = GPCCSON_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCSON_b_grid_areas)
     
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
    UDelDJF_mean = UDelDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelDJF_grid_areas)
    GPCCDJF_mean = GPCCDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCDJF_grid_areas)
    CRUDJF_b_mean = CRUDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUDJF_b_grid_areas) 
    UDelDJF_b_mean = UDelDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelDJF_b_grid_areas)
    GPCCDJF_b_mean = GPCCDJF_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCDJF_b_grid_areas)
    
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
    UDelMAM_mean = UDelMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelMAM_grid_areas) 
    GPCCMAM_mean = GPCCMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCMAM_grid_areas)
    CRUMAM_b_mean = CRUMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUMAM_b_grid_areas) 
    UDelMAM_b_mean = UDelMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelMAM_b_grid_areas)
    GPCCMAM_b_mean = GPCCMAM_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCMAM_b_grid_areas)
    
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
    UDelJJA_mean = UDelJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelJJA_grid_areas) 
    GPCCJJA_mean = GPCCJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCJJA_grid_areas)
    CRUJJA_b_mean = CRUJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUJJA_b_grid_areas) 
    UDelJJA_b_mean = UDelJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelJJA_b_grid_areas)
    GPCCJJA_b_mean = GPCCJJA_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCJJA_b_grid_areas)
    
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
    UDelYR_mean = UDelYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelYR_grid_areas)
    GPCCYR_mean = GPCCYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCYR_grid_areas)
    CRUYR_b_mean = CRUYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUYR_b_grid_areas) 
    UDelYR_b_mean = UDelYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelYR_b_grid_areas)
    GPCCYR_b_mean = GPCCYR_b.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCYR_b_grid_areas)
    
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
    UDelSON_b_mean = UDelSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCCSON_b_mean = GPCCSON_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    
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
    UDelDJF_b_mean = UDelDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCCDJF_b_mean = GPCCDJF_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    
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
    UDelMAM_b_mean = UDelMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCCMAM_b_mean = GPCCMAM_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    
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
    UDelJJA_b_mean = UDelJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCCJJA_b_mean = GPCCJJA_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    
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
    UDelYR_b_mean = UDelYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    GPCCYR_b_mean = GPCCYR_b_mean.collapsed(['time'], iris.analysis.MEAN) 
    
    #create average of baseline observed data
    ObsSONY_b = (CRUSON_b_mean.data + UDelSON_b_mean.data + GPCCSON_b_mean.data)/3.
    ObsDJFY_b = (CRUDJF_b_mean.data + UDelDJF_b_mean.data + GPCCDJF_b_mean.data)/3.
    ObsMAMY_b = (CRUMAM_b_mean.data + UDelMAM_b_mean.data + GPCCMAM_b_mean.data)/3.
    ObsJJAY_b = (CRUJJA_b_mean.data + UDelJJA_b_mean.data + GPCCJJA_b_mean.data)/3.
    ObsY_b = (CRUYR_b_mean.data + UDelYR_b_mean.data + GPCCYR_b_mean.data)/3.
    
    #We want to see the change in temperature from the baseline for Observed
    CRUSON_mean = CRUSON_mean.data - CRUSON_b_mean.data
    UDelSON_mean = UDelSON_mean.data - UDelSON_b_mean.data
    GPCCSON_mean = GPCCSON_mean.data - GPCCSON_b_mean.data
    
    CRUDJF_mean = CRUDJF_mean.data - CRUDJF_b_mean.data
    UDelDJF_mean = UDelDJF_mean.data - UDelDJF_b_mean.data
    GPCCDJF_mean = GPCCDJF_mean.data - GPCCDJF_b_mean.data
    
    CRUMAM_mean = CRUMAM_mean.data - CRUMAM_b_mean.data
    UDelMAM_mean = UDelMAM_mean.data - UDelMAM_b_mean.data
    GPCCMAM_mean = GPCCMAM_mean.data - GPCCMAM_b_mean.data
    
    CRUJJA_mean = CRUJJA_mean.data - CRUJJA_b_mean.data
    UDelJJA_mean = UDelJJA_mean.data - UDelJJA_b_mean.data
    GPCCJJA_mean = GPCCJJA_mean.data - GPCCJJA_b_mean.data
    
    CRUYR_mean = CRUYR_mean.data - CRUYR_b_mean.data
    UDelYR_mean = UDelYR_mean.data - UDelYR_b_mean.data
    GPCCYR_mean = GPCCYR_mean.data - GPCCYR_b_mean.data
    
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
    
    ObsSONY = (CRUSON_mean.data + UDelSON_mean.data + GPCCSON_mean.data)/3.
    ObsDJFY = (CRUDJF_mean.data + UDelDJF_mean.data + GPCCDJF_mean.data)/3.
    ObsMAMY = (CRUMAM_mean.data + UDelMAM_mean.data + GPCCMAM_mean.data)/3.
    ObsJJAY = (CRUJJA_mean.data + UDelJJA_mean.data + GPCCJJA_mean.data)/3.
    ObsY = (CRUYR_mean.data + UDelYR_mean.data + GPCCYR_mean.data)/3.
    
    #we want to see the absolute precipitation amounts
    CCCmaCanRCMSON_a_mean = (CCCmaCanRCMSON_mean.data + ObsSONY_b)
    CCCmaSMHISON_a_mean = (CCCmaSMHISON_mean.data + ObsSONY_b) 
    CNRMSON_a_mean = (CNRMSON_mean.data + ObsSONY_b)                      
    CNRMSMHISON_a_mean = (CNRMSMHISON_mean.data + ObsSONY_b)   
    CSIROSON_a_mean = (CSIROSON_mean.data + ObsSONY_b)
    ICHECDMISON_a_mean = (ICHECDMISON_mean.data + ObsSONY_b)  
    ICHECCCLMSON_a_mean = (ICHECCCLMSON_mean.data + ObsSONY_b) 
    ICHECKNMISON_a_mean = (ICHECKNMISON_mean.data + ObsSONY_b) 
    ICHECMPISON_a_mean = (ICHECMPISON_mean.data + ObsSONY_b) 
    ICHECSMHISON_a_mean = (ICHECSMHISON_mean.data + ObsSONY_b) 
    IPSLSON_a_mean = (IPSLSON_mean.data + ObsSONY_b) 
    MIROCSON_a_mean = (MIROCSON_mean.data + ObsSONY_b) 
    MOHCCCLMSON_a_mean = (MOHCCCLMSON_mean.data + ObsSONY_b) 
    MOHCKNMISON_a_mean = (MOHCKNMISON_mean.data + ObsSONY_b) 
    MOHCSMHISON_a_mean = (MOHCSMHISON_mean.data + ObsSONY_b) 
    MPICCLMSON_a_mean = (MPICCLMSON_mean.data + ObsSONY_b)        
    MPIREMOSON_a_mean = (MPIREMOSON_mean.data + ObsSONY_b)           
    MPISMHISON_a_mean = (MPISMHISON_mean.data + ObsSONY_b) 
    NCCSMHISON_a_mean = (NCCSMHISON_mean.data  + ObsSONY_b)  
    NOAASON_a_mean = (NOAASON_mean.data  + ObsSONY_b) 
    
    CCCmaCanRCMDJF_a_mean = (CCCmaCanRCMDJF_mean.data + ObsDJFY_b)
    CCCmaSMHIDJF_a_mean = (CCCmaSMHIDJF_mean.data + ObsDJFY_b) 
    CNRMDJF_a_mean = (CNRMDJF_mean.data + ObsDJFY_b)                      
    CNRMSMHIDJF_a_mean = (CNRMSMHIDJF_mean.data + ObsDJFY_b)   
    CSIRODJF_a_mean = (CSIRODJF_mean.data + ObsDJFY_b)
    ICHECDMIDJF_a_mean = (ICHECDMIDJF_mean.data + ObsDJFY_b)  
    ICHECCCLMDJF_a_mean = (ICHECCCLMDJF_mean.data + ObsDJFY_b) 
    ICHECKNMIDJF_a_mean = (ICHECKNMIDJF_mean.data + ObsDJFY_b) 
    ICHECMPIDJF_a_mean = (ICHECMPIDJF_mean.data + ObsDJFY_b) 
    ICHECSMHIDJF_a_mean = (ICHECSMHIDJF_mean.data + ObsDJFY_b) 
    IPSLDJF_a_mean = (IPSLDJF_mean.data + ObsDJFY_b) 
    MIROCDJF_a_mean = (MIROCDJF_mean.data + ObsDJFY_b) 
    MOHCCCLMDJF_a_mean = (MOHCCCLMDJF_mean.data + ObsDJFY_b) 
    MOHCKNMIDJF_a_mean = (MOHCKNMIDJF_mean.data + ObsDJFY_b) 
    MOHCSMHIDJF_a_mean = (MOHCSMHIDJF_mean.data + ObsDJFY_b) 
    MPICCLMDJF_a_mean = (MPICCLMDJF_mean.data + ObsDJFY_b)        
    MPIREMODJF_a_mean = (MPIREMODJF_mean.data + ObsDJFY_b)           
    MPISMHIDJF_a_mean = (MPISMHIDJF_mean.data + ObsDJFY_b) 
    NCCSMHIDJF_a_mean = (NCCSMHIDJF_mean.data + ObsDJFY_b)  
    NOAADJF_a_mean = (NOAADJF_mean.data + ObsDJFY_b) 
    
    CCCmaCanRCMMAM_a_mean = (CCCmaCanRCMMAM_mean.data + ObsMAMY_b)
    CCCmaSMHIMAM_a_mean = (CCCmaSMHIMAM_mean.data + ObsMAMY_b) 
    CNRMMAM_a_mean = (CNRMMAM_mean.data + ObsMAMY_b)                      
    CNRMSMHIMAM_a_mean = (CNRMSMHIMAM_mean.data + ObsMAMY_b)   
    CSIROMAM_a_mean = (CSIROMAM_mean.data + ObsMAMY_b)
    ICHECDMIMAM_a_mean = (ICHECDMIMAM_mean.data + ObsMAMY_b)  
    ICHECCCLMMAM_a_mean = (ICHECCCLMMAM_mean.data + ObsMAMY_b) 
    ICHECKNMIMAM_a_mean = (ICHECKNMIMAM_mean.data + ObsMAMY_b) 
    ICHECMPIMAM_a_mean = (ICHECMPIMAM_mean.data + ObsMAMY_b) 
    ICHECSMHIMAM_a_mean = (ICHECSMHIMAM_mean.data + ObsMAMY_b) 
    IPSLMAM_a_mean = (IPSLMAM_mean.data + ObsMAMY_b) 
    MIROCMAM_a_mean = (MIROCMAM_mean.data + ObsMAMY_b) 
    MOHCCCLMMAM_a_mean = (MOHCCCLMMAM_mean.data + ObsMAMY_b) 
    MOHCKNMIMAM_a_mean = (MOHCKNMIMAM_mean.data + ObsMAMY_b) 
    MOHCSMHIMAM_a_mean = (MOHCSMHIMAM_mean.data + ObsMAMY_b) 
    MPICCLMMAM_a_mean = (MPICCLMMAM_mean.data + ObsMAMY_b)        
    MPIREMOMAM_a_mean = (MPIREMOMAM_mean.data + ObsMAMY_b)           
    MPISMHIMAM_a_mean = (MPISMHIMAM_mean.data + ObsMAMY_b) 
    NCCSMHIMAM_a_mean = (NCCSMHIMAM_mean.data + ObsMAMY_b)  
    NOAAMAM_a_mean = (NOAAMAM_mean.data + ObsMAMY_b) 
    
    CCCmaCanRCMJJA_a_mean = (CCCmaCanRCMJJA_mean.data + ObsJJAY_b)
    CCCmaSMHIJJA_a_mean = (CCCmaSMHIJJA_mean.data + ObsJJAY_b) 
    CNRMJJA_a_mean = (CNRMJJA_mean.data + ObsJJAY_b)                      
    CNRMSMHIJJA_a_mean = (CNRMSMHIJJA_mean.data + ObsJJAY_b)   
    CSIROJJA_a_mean = (CSIROJJA_mean.data + ObsJJAY_b)
    ICHECDMIJJA_a_mean = (ICHECDMIJJA_mean.data + ObsJJAY_b)  
    ICHECCCLMJJA_a_mean = (ICHECCCLMJJA_mean.data + ObsJJAY_b) 
    ICHECKNMIJJA_a_mean = (ICHECKNMIJJA_mean.data + ObsJJAY_b) 
    ICHECMPIJJA_a_mean = (ICHECMPIJJA_mean.data + ObsJJAY_b) 
    ICHECSMHIJJA_a_mean = (ICHECSMHIJJA_mean.data + ObsJJAY_b) 
    IPSLJJA_a_mean = (IPSLJJA_mean.data + ObsJJAY_b) 
    MIROCJJA_a_mean = (MIROCJJA_mean.data + ObsJJAY_b) 
    MOHCCCLMJJA_a_mean = (MOHCCCLMJJA_mean.data + ObsJJAY_b) 
    MOHCKNMIJJA_a_mean = (MOHCKNMIJJA_mean.data + ObsJJAY_b) 
    MOHCSMHIJJA_a_mean = (MOHCSMHIJJA_mean.data + ObsJJAY_b) 
    MPICCLMJJA_a_mean = (MPICCLMJJA_mean.data + ObsJJAY_b)        
    MPIREMOJJA_a_mean = (MPIREMOJJA_mean.data + ObsJJAY_b)           
    MPISMHIJJA_a_mean = (MPISMHIJJA_mean.data + ObsJJAY_b) 
    NCCSMHIJJA_a_mean = (NCCSMHIJJA_mean.data + ObsJJAY_b)  
    NOAAJJA_a_mean = (NOAAJJA_mean.data + ObsJJAY_b) 
    
    CCCmaCanRCMYR_a_mean = (CCCmaCanRCMYR_mean.data + ObsY_b)
    CCCmaSMHIYR_a_mean = (CCCmaSMHIYR_mean.data + ObsY_b) 
    CNRMYR_a_mean = (CNRMYR_mean.data + ObsY_b)                      
    CNRMSMHIYR_a_mean = (CNRMSMHIYR_mean.data + ObsY_b)   
    CSIROYR_a_mean = (CSIROYR_mean.data + ObsY_b)
    ICHECDMIYR_a_mean = (ICHECDMIYR_mean.data + ObsY_b)  
    ICHECCCLMYR_a_mean = (ICHECCCLMYR_mean.data + ObsY_b) 
    ICHECKNMIYR_a_mean = (ICHECKNMIYR_mean.data + ObsY_b) 
    ICHECMPIYR_a_mean = (ICHECMPIYR_mean.data + ObsY_b) 
    ICHECSMHIYR_a_mean = (ICHECSMHIYR_mean.data + ObsY_b) 
    IPSLYR_a_mean = (IPSLYR_mean.data + ObsY_b) 
    MIROCYR_a_mean = (MIROCYR_mean.data + ObsY_b) 
    MOHCCCLMYR_a_mean = (MOHCCCLMYR_mean.data + ObsY_b) 
    MOHCKNMIYR_a_mean = (MOHCKNMIYR_mean.data + ObsY_b) 
    MOHCSMHIYR_a_mean = (MOHCSMHIYR_mean.data + ObsY_b) 
    MPICCLMYR_a_mean = (MPICCLMYR_mean.data + ObsY_b)        
    MPIREMOYR_a_mean = (MPIREMOYR_mean.data + ObsY_b)           
    MPISMHIYR_a_mean = (MPISMHIYR_mean.data + ObsY_b)  
    NCCSMHIYR_a_mean = (NCCSMHIYR_mean.data + ObsY_b)  
    NOAAYR_a_mean = (NOAAYR_mean.data + ObsY_b) 
    
    CCCmaCanRCMSON85_a_mean = (CCCmaCanRCMSON85_mean.data  + ObsSONY_b)
    CCCmaSMHISON85_a_mean = (CCCmaSMHISON85_mean.data + ObsSONY_b) 
    CNRMSON85_a_mean = (CNRMSON85_mean.data + ObsSONY_b)                      
    CNRMSMHISON85_a_mean = (CNRMSMHISON85_mean.data + ObsSONY_b)   
    CSIROSON85_a_mean = (CSIROSON85_mean.data + ObsSONY_b)
    ICHECDMISON85_a_mean = (ICHECDMISON85_mean.data + ObsSONY_b)  
    ICHECCCLMSON85_a_mean = (ICHECCCLMSON85_mean.data + ObsSONY_b) 
    ICHECKNMISON85_a_mean = (ICHECKNMISON85_mean.data + ObsSONY_b) 
    ICHECMPISON85_a_mean = (ICHECMPISON85_mean.data + ObsSONY_b) 
    ICHECSMHISON85_a_mean = (ICHECSMHISON85_mean.data + ObsSONY_b) 
    IPSLSON85_a_mean = (IPSLSON85_mean.data + ObsSONY_b) 
    MIROCSON85_a_mean = (MIROCSON85_mean.data + ObsSONY_b) 
    MOHCCCLMSON85_a_mean = (MOHCCCLMSON85_mean.data + ObsSONY_b) 
    MOHCKNMISON85_a_mean = (MOHCKNMISON85_mean.data + ObsSONY_b) 
    MOHCSMHISON85_a_mean = (MOHCSMHISON85_mean.data + ObsSONY_b) 
    MPICCLMSON85_a_mean = (MPICCLMSON85_mean.data + ObsSONY_b)        
    MPIREMOSON85_a_mean = (MPIREMOSON85_mean.data + ObsSONY_b)           
    MPISMHISON85_a_mean = (MPISMHISON85_mean.data + ObsSONY_b) 
    NCCSMHISON85_a_mean = (NCCSMHISON85_mean.data + ObsSONY_b)  
    NOAASON85_a_mean = (NOAASON85_mean.data  + ObsSONY_b) 
    
    CCCmaCanRCMDJF85_a_mean = (CCCmaCanRCMDJF85_mean.data + ObsDJFY_b)
    CCCmaSMHIDJF85_a_mean = (CCCmaSMHIDJF85_mean.data + ObsDJFY_b) 
    CNRMDJF85_a_mean = (CNRMDJF85_mean.data + ObsDJFY_b)                      
    CNRMSMHIDJF85_a_mean = (CNRMSMHIDJF85_mean.data + ObsDJFY_b)   
    CSIRODJF85_a_mean = (CSIRODJF85_mean.data + ObsDJFY_b)
    ICHECDMIDJF85_a_mean = (ICHECDMIDJF85_mean.data + ObsDJFY_b)  
    ICHECCCLMDJF85_a_mean = (ICHECCCLMDJF85_mean.data + ObsDJFY_b) 
    ICHECKNMIDJF85_a_mean = (ICHECKNMIDJF85_mean.data + ObsDJFY_b) 
    ICHECMPIDJF85_a_mean = (ICHECMPIDJF85_mean.data + ObsDJFY_b) 
    ICHECSMHIDJF85_a_mean = (ICHECSMHIDJF85_mean.data + ObsDJFY_b) 
    IPSLDJF85_a_mean = (IPSLDJF85_mean.data + ObsDJFY_b) 
    MIROCDJF85_a_mean = (MIROCDJF85_mean.data + ObsDJFY_b) 
    MOHCCCLMDJF85_a_mean = (MOHCCCLMDJF85_mean.data + ObsDJFY_b) 
    MOHCKNMIDJF85_a_mean = (MOHCKNMIDJF85_mean.data + ObsDJFY_b) 
    MOHCSMHIDJF85_a_mean = (MOHCSMHIDJF85_mean.data + ObsDJFY_b) 
    MPICCLMDJF85_a_mean = (MPICCLMDJF85_mean.data + ObsDJFY_b)        
    MPIREMODJF85_a_mean = (MPIREMODJF85_mean.data + ObsDJFY_b)           
    MPISMHIDJF85_a_mean = (MPISMHIDJF85_mean.data + ObsDJFY_b) 
    NCCSMHIDJF85_a_mean = (NCCSMHIDJF85_mean.data + ObsDJFY_b)  
    NOAADJF85_a_mean = (NOAADJF85_mean.data + ObsDJFY_b) 
    
    CCCmaCanRCMMAM85_a_mean = (CCCmaCanRCMMAM85_mean.data + ObsMAMY_b)
    CCCmaSMHIMAM85_a_mean = (CCCmaSMHIMAM85_mean.data + ObsMAMY_b) 
    CNRMMAM85_a_mean = (CNRMMAM85_mean.data + ObsMAMY_b)                      
    CNRMSMHIMAM85_a_mean = (CNRMSMHIMAM85_mean.data + ObsMAMY_b)   
    CSIROMAM85_a_mean = (CSIROMAM85_mean.data + ObsMAMY_b)
    ICHECDMIMAM85_a_mean = (ICHECDMIMAM85_mean.data + ObsMAMY_b)  
    ICHECCCLMMAM85_a_mean = (ICHECCCLMMAM85_mean.data + ObsMAMY_b) 
    ICHECKNMIMAM85_a_mean = (ICHECKNMIMAM85_mean.data + ObsMAMY_b) 
    ICHECMPIMAM85_a_mean = (ICHECMPIMAM85_mean.data + ObsMAMY_b) 
    ICHECSMHIMAM85_a_mean = (ICHECSMHIMAM85_mean.data + ObsMAMY_b) 
    IPSLMAM85_a_mean = (IPSLMAM85_mean.data + ObsMAMY_b) 
    MIROCMAM85_a_mean = (MIROCMAM85_mean.data + ObsMAMY_b) 
    MOHCCCLMMAM85_a_mean = (MOHCCCLMMAM85_mean.data + ObsMAMY_b) 
    MOHCKNMIMAM85_a_mean = (MOHCKNMIMAM85_mean.data + ObsMAMY_b) 
    MOHCSMHIMAM85_a_mean = (MOHCSMHIMAM85_mean.data + ObsMAMY_b) 
    MPICCLMMAM85_a_mean = (MPICCLMMAM85_mean.data + ObsMAMY_b)        
    MPIREMOMAM85_a_mean = (MPIREMOMAM85_mean.data + ObsMAMY_b)           
    MPISMHIMAM85_a_mean = (MPISMHIMAM85_mean.data + ObsMAMY_b)  
    NCCSMHIMAM85_a_mean = (NCCSMHIMAM85_mean.data + ObsMAMY_b)  
    NOAAMAM85_a_mean = (NOAAMAM85_mean.data + ObsMAMY_b) 
    
    CCCmaCanRCMJJA85_a_mean = (CCCmaCanRCMJJA85_mean.data + ObsJJAY_b)
    CCCmaSMHIJJA85_a_mean = (CCCmaSMHIJJA85_mean.data + ObsJJAY_b) 
    CNRMJJA85_a_mean = (CNRMJJA85_mean.data + ObsJJAY_b)                      
    CNRMSMHIJJA85_a_mean = (CNRMSMHIJJA85_mean.data + ObsJJAY_b)   
    CSIROJJA85_a_mean = (CSIROJJA85_mean.data + ObsJJAY_b)
    ICHECDMIJJA85_a_mean = (ICHECDMIJJA85_mean.data + ObsJJAY_b)  
    ICHECCCLMJJA85_a_mean = (ICHECCCLMJJA85_mean.data + ObsJJAY_b) 
    ICHECKNMIJJA85_a_mean = (ICHECKNMIJJA85_mean.data + ObsJJAY_b) 
    ICHECMPIJJA85_a_mean = (ICHECMPIJJA85_mean.data + ObsJJAY_b) 
    ICHECSMHIJJA85_a_mean = (ICHECSMHIJJA85_mean.data + ObsJJAY_b) 
    IPSLJJA85_a_mean = (IPSLJJA85_mean.data + ObsJJAY_b) 
    MIROCJJA85_a_mean = (MIROCJJA85_mean.data + ObsJJAY_b) 
    MOHCCCLMJJA85_a_mean = (MOHCCCLMJJA85_mean.data + ObsJJAY_b) 
    MOHCKNMIJJA85_a_mean = (MOHCKNMIJJA85_mean.data + ObsJJAY_b) 
    MOHCSMHIJJA85_a_mean = (MOHCSMHIJJA85_mean.data + ObsJJAY_b) 
    MPICCLMJJA85_a_mean = (MPICCLMJJA85_mean.data + ObsJJAY_b)        
    MPIREMOJJA85_a_mean = (MPIREMOJJA85_mean.data + ObsJJAY_b)           
    MPISMHIJJA85_a_mean = (MPISMHIJJA85_mean.data + ObsJJAY_b) 
    NCCSMHIJJA85_a_mean = (NCCSMHIJJA85_mean.data + ObsJJAY_b)  
    NOAAJJA85_a_mean = (NOAAJJA85_mean.data + ObsJJAY_b) 
    
    CCCmaCanRCMYR85_a_mean = (CCCmaCanRCMYR85_mean.data + ObsY_b)
    CCCmaSMHIYR85_a_mean = (CCCmaSMHIYR85_mean.data + ObsY_b) 
    CNRMYR85_a_mean = (CNRMYR85_mean.data + ObsY_b)                      
    CNRMSMHIYR85_a_mean = (CNRMSMHIYR85_mean.data + ObsY_b)   
    CSIROYR85_a_mean = (CSIROYR85_mean.data + ObsY_b)
    ICHECDMIYR85_a_mean = (ICHECDMIYR85_mean.data + ObsY_b)  
    ICHECCCLMYR85_a_mean = (ICHECCCLMYR85_mean.data + ObsY_b) 
    ICHECKNMIYR85_a_mean = (ICHECKNMIYR85_mean.data + ObsY_b) 
    ICHECMPIYR85_a_mean = (ICHECMPIYR85_mean.data + ObsY_b) 
    ICHECSMHIYR85_a_mean = (ICHECSMHIYR85_mean.data + ObsY_b) 
    IPSLYR85_a_mean = (IPSLYR85_mean.data + ObsY_b) 
    MIROCYR85_a_mean = (MIROCYR85_mean.data + ObsY_b) 
    MOHCCCLMYR85_a_mean = (MOHCCCLMYR85_mean.data + ObsY_b) 
    MOHCKNMIYR85_a_mean = (MOHCKNMIYR85_mean.data + ObsY_b) 
    MOHCSMHIYR85_a_mean = (MOHCSMHIYR85_mean.data + ObsY_b) 
    MPICCLMYR85_a_mean = (MPICCLMYR85_mean.data + ObsY_b)        
    MPIREMOYR85_a_mean = (MPIREMOYR85_mean.data + ObsY_b)           
    MPISMHIYR85_a_mean = (MPISMHIYR85_mean.data + ObsY_b) 
    NCCSMHIYR85_a_mean = (NCCSMHIYR85_mean.data + ObsY_b)  
    NOAAYR85_a_mean = (NOAAYR85_mean.data + ObsY_b)
    
    CRUSON_a_mean = CRUSON_mean.data + CRUSON_b_mean.data
    UDelSON_a_mean = UDelSON_mean.data + UDelSON_b_mean.data
    GPCCSON_a_mean = GPCCSON_mean.data + GPCCSON_b_mean.data
    
    CRUDJF_a_mean = CRUDJF_mean.data + CRUDJF_b_mean.data
    UDelDJF_a_mean = UDelDJF_mean.data + UDelDJF_b_mean.data
    GPCCDJF_a_mean = GPCCDJF_mean.data + GPCCDJF_b_mean.data
    
    CRUMAM_a_mean = CRUMAM_mean.data + CRUMAM_b_mean.data
    UDelMAM_a_mean = UDelMAM_mean.data + UDelMAM_b_mean.data
    GPCCMAM_a_mean = GPCCMAM_mean.data + GPCCMAM_b_mean.data
    
    CRUJJA_a_mean = CRUJJA_mean.data + CRUJJA_b_mean.data
    UDelJJA_a_mean = UDelJJA_mean.data + UDelJJA_b_mean.data
    GPCCJJA_a_mean = GPCCJJA_mean.data + GPCCJJA_b_mean.data
    
    CRUYR_a_mean = CRUYR_mean.data + CRUYR_b_mean.data
    UDelYR_a_mean = UDelYR_mean.data + UDelYR_b_mean.data
    GPCCYR_a_mean = GPCCYR_mean.data + GPCCYR_b_mean.data
    
    
    ObsSONY_a = (CRUSON_a_mean + UDelSON_a_mean + GPCCSON_a_mean)/3.
    ObsDJFY_a = (CRUDJF_a_mean + UDelDJF_a_mean + GPCCDJF_a_mean)/3.
    ObsMAMY_a = (CRUMAM_a_mean + UDelMAM_a_mean + GPCCMAM_a_mean)/3.
    ObsJJAY_a = (CRUJJA_a_mean + UDelJJA_a_mean + GPCCJJA_a_mean)/3.
    ObsY_a = (CRUYR_a_mean + UDelYR_a_mean + GPCCYR_a_mean)/3.
    

                
    
    #import minimum and maximum numbers (from the output_Pr_a_mean_AnnualSeasonal.csv file, negative numbers considered zero (0)
    Min_45_YR = (614.41,587.69,744.10,715.74,823.73,888.63,793.01,680.61,733.15,747.74,637.63,509.92,650.92,717.16,744.76,699.99,585.75,645.67,848.23,813.57,605.98,824.41,750.61,847.93,885.06,488.23,729.33,720.38,581.93,886.46,868.21,729.32,765.72,825.57,847.32,767.55,841.63,798.91,749.22,801.35,645.93,617.78,728.88,658.64,715.55,643.56,703.19,709.44,676.12,860.45,733.44,728.95,749.91,764.98,614.86,794.88,815.82,804.02,699.25,709.32,733.35,736.24,755.12,671.13,793.05)
    Min_45_SON = (0.00,0.00,0.00,92.36,39.46,0.00,220.46,0.00,0.00,56.11,0.00,0.00,0.00,0.00,34.60,79.75,0.00,0.00,0.00,0.00,45.08,0.00,0.00,0.00,11.22,0.00,0.00,0.00,0.00,0.00,0.00,50.20,24.47,0.00,67.39,0.00,88.38,0.00,12.03,36.57,1.88,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,31.12,0.00,0.00,0.00,0.00,0.00,0.00,71.66,36.92,0.00,0.00,0.00,0.00,0.00,0.00,0.00)
    Min_45_DJF = (1522.87,1252.31,1982.91,1554.85,2250.12,1807.56,1658.26,1657.74,1835.86,1835.38,1069.93,1100.82,1689.71,1485.43,1712.13,1735.12,1558.65,1331.28,1988.47,2017.55,1670.12,2055.10,2163.86,1694.16,2302.67,1457.24,1892.56,1983.39,1005.90,1787.15,2117.24,1952.98,1813.08,2111.16,1841.06,1780.87,1953.05,969.47,1706.56,1836.04,1306.83,1425.83,1795.24,1166.69,1833.93,1311.45,1459.33,1578.24,1891.31,1706.13,2012.77,2087.29,1524.53,1804.10,1415.49,2028.70,1890.21,2023.37,1364.01,2149.62,1811.21,1747.15,1821.08,1351.26,1970.85)
    Min_45_MAM = (562.05,503.46,616.52,708.11,693.90,813.13,799.98,479.44,561.53,616.95,632.74,527.95,713.06,870.80,858.29,739.19,687.19,475.21,637.48,575.33,568.99,308.81,566.24,788.31,805.64,255.03,557.84,617.38,526.82,466.45,671.61,585.70,752.98,638.14,647.73,613.61,817.29,387.55,750.68,410.52,626.58,569.52,638.01,301.59,653.79,676.41,431.31,738.70,473.84,659.36,234.91,506.88,786.47,478.16,591.61,786.75,795.01,542.59,592.23,454.67,648.37,615.09,736.09,532.48,338.01)
    Min_45_JJA = (0.00,1.76,0.00,3.18,0.00,0.00,0.00,0.00,10.68,0.00,0.00,0.00,5.75,14.89,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.08,0.00,0.82,0.00,0.00,0.00,0.00,5.09,8.44,3.97,0.00,0.00,0.00,5.31,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)
    Ave_45_YR = (1031.49,1011.58,1116.86,1023.08,1077.39,1069.91,1113.87,1055.73,1065.43,1063.08,1070.65,1003.54,1075.83,1009.73,1053.53,1103.88,1052.17,1000.86,1064.56,1023.68,1039.24,1096.15,1121.01,1032.79,1087.51,1111.40,989.48,1006.91,1045.67,1086.81,1039.83,1064.95,1057.14,1045.95,1034.66,1022.71,1050.99,994.56,1094.01,1061.55,996.43,972.70,1025.40,960.10,1055.23,1090.41,1024.61,1062.93,1020.98,1071.23,992.76,1061.56,1044.88,1005.77,1058.28,1036.44,1143.73,990.34,1009.99,1072.87,1064.92,981.89,1073.15,1026.90,1012.44)
    Ave_45_SON = (285.77,248.00,385.46,307.87,430.22,378.31,533.82,443.67,378.44,389.31,459.21,289.20,270.50,206.24,379.61,349.13,237.25,275.96,248.66,274.78,359.57,412.91,344.63,302.03,433.32,382.60,277.82,287.12,348.74,279.50,315.71,348.79,406.69,243.26,296.35,270.63,403.32,248.69,350.52,380.03,224.64,294.17,323.84,347.92,354.65,347.87,287.57,234.07,188.11,369.86,306.02,290.65,327.81,439.62,284.68,164.11,340.86,271.23,271.75,288.31,422.15,319.67,355.02,316.26,336.21)
    Ave_45_DJF = (2617.68,2551.91,2898.92,2472.67,2677.83,2582.61,2666.70,2697.30,2682.22,2698.73,2640.30,2625.80,2724.08,2517.26,2673.17,2875.21,2739.74,2606.93,2816.25,2703.26,2459.92,2658.91,2875.13,2514.27,2693.95,2769.60,2548.20,2696.56,2639.54,2760.55,2595.21,2702.22,2624.84,2733.94,2715.82,2637.40,2510.86,2503.09,2771.02,2647.32,2643.78,2457.40,2632.23,2445.09,2610.09,2757.13,2689.02,2731.06,2714.96,2673.37,2610.63,2777.20,2650.44,2479.53,2643.37,2688.10,2897.48,2497.46,2656.27,2639.66,2681.38,2508.41,2715.07,2621.01,2640.01)
    Ave_45_MAM = (1189.40,1190.38,1126.81,1256.96,1165.14,1262.47,1201.47,1038.09,1162.57,1125.75,1138.21,1054.83,1249.32,1245.11,1112.60,1148.64,1196.54,1085.06,1147.14,1084.00,1289.01,1260.48,1198.25,1262.37,1183.91,1244.31,1088.48,1019.44,1140.32,1255.59,1195.22,1174.67,1155.52,1167.98,1080.73,1144.12,1243.22,1175.38,1208.24,1172.55,1086.56,1099.49,1098.49,1012.05,1225.40,1228.72,1065.44,1244.41,1131.60,1202.61,1013.07,1138.07,1174.48,1065.02,1251.35,1239.35,1300.63,1129.38,1067.58,1324.09,1129.56,1047.49,1176.50,1143.66,1034.89)
    Ave_45_JJA = (39.76,60.50,54.86,57.20,42.77,59.71,50.99,51.94,44.95,43.98,42.18,50.85,65.69,73.14,44.85,52.39,41.60,41.82,43.29,39.83,50.89,57.14,63.75,55.21,44.44,53.87,39.02,32.03,60.80,57.43,48.86,40.76,46.73,44.23,42.08,44.81,50.33,54.26,42.20,51.11,37.53,43.60,42.82,40.61,34.83,34.59,54.92,47.90,55.01,46.47,38.77,47.85,32.98,43.14,49.64,59.92,43.80,67.47,41.79,44.96,33.78,57.03,43.59,32.54,45.19)
    Max_45_YR = (1269.15,1516.43,1406.15,1406.07,1367.10,1424.82,1527.66,1592.25,1348.00,1308.80,1639.35,1327.90,1362.85,1488.45,1500.88,1364.59,1355.99,1403.25,1481.35,1317.56,1547.95,1397.77,1494.84,1291.62,1385.92,1459.76,1174.32,1539.11,1343.27,1290.95,1215.60,1359.21,1383.95,1343.59,1411.90,1411.89,1441.66,1389.31,1556.30,1742.09,1301.56,1460.52,1345.87,1266.76,1365.60,1686.43,1360.53,1339.31,1347.98,1409.94,1267.80,1233.20,1349.93,1216.68,1551.03,1322.32,1576.87,1269.66,1609.97,1286.81,1564.08,1354.99,1341.47,1356.79,1250.82)
    Max_45_SON = (771.33,1153.97,881.35,556.72,1194.45,702.79,1308.88,1300.97,1100.28,849.31,1077.24,785.02,564.81,592.54,1157.13,832.82,655.62,728.78,514.51,736.16,831.17,964.69,1213.58,1254.23,975.69,831.69,770.56,618.93,1346.08,907.91,805.65,752.12,1105.76,672.81,746.68,783.10,1014.14,590.84,923.33,818.63,585.57,961.53,786.42,1121.30,1130.92,865.28,508.82,892.73,740.55,932.07,665.11,817.58,798.74,1940.13,1081.04,509.67,878.81,708.19,707.04,553.27,844.77,867.76,908.61,1207.54,740.94)
    Max_45_DJF = (3759.17,3712.70,4204.45,3369.62,3465.43,3497.44,3534.25,3768.53,3551.60,4026.90,3507.66,3476.90,3775.53,2962.39,4421.90,3893.91,3689.63,4205.06,4486.56,3395.02,3261.30,3722.77,3423.93,3143.89,3358.76,4044.48,3341.63,4386.02,3424.48,3429.25,3210.19,3535.40,3374.04,3711.70,4218.26,3861.15,3217.29,3104.82,4637.61,3695.32,3483.59,4027.77,3584.98,3681.78,3373.20,4143.28,4164.16,4096.72,3662.98,3995.04,3454.47,3630.39,3290.61,3322.07,3702.97,3764.04,4349.08,3893.94,3859.77,3306.02,3796.76,3546.09,3321.81,3340.90,3243.91)
    Max_45_MAM = (1661.41,1964.15,1428.24,2414.89,1905.54,2439.71,1649.43,1452.86,2359.94,1728.02,1995.62,1932.75,1800.90,2688.51,1670.11,1584.55,1944.36,1686.48,1525.59,1860.69,2182.18,2199.42,2663.04,2010.50,1694.84,1726.69,1675.36,1438.66,2116.37,1601.93,1962.37,1673.14,2200.24,1663.81,1501.14,1592.70,2061.71,2265.60,2136.21,2342.55,2177.39,1725.65,1754.62,1486.01,2320.81,2634.60,1540.04,2001.81,2001.88,2345.92,1470.67,2025.80,1824.97,1601.05,2245.63,1833.17,2418.61,1677.48,1969.89,2280.69,2138.84,1667.20,1955.95,1693.54,1569.09)
    Max_45_JJA = (95.00,147.54,192.65,170.58,134.10,183.21,171.02,203.29,80.15,138.54,93.65,145.10,216.57,176.44,145.72,143.08,161.91,127.27,95.16,147.74,133.32,168.65,196.30,158.76,107.52,153.30,92.65,90.97,147.99,202.07,191.66,175.25,201.64,137.43,97.23,101.61,99.52,125.94,97.03,126.15,76.89,98.11,82.57,115.31,81.65,111.02,154.29,119.71,156.10,150.35,118.52,122.89,142.06,230.89,143.94,240.10,90.86,290.65,126.63,120.81,103.24,159.38,150.19,76.63,107.44)
    Min_85_YR = (776.97,699.34,831.80,669.90,825.72,623.86,692.29,596.74,777.93,769.77,806.26,776.05,771.68,724.29,658.87,543.36,780.68,840.02,739.45,651.88,776.70,839.96,823.58,642.82,598.75,829.85,885.48,679.68,575.19,747.65,808.86,888.25,643.67,705.52,751.65,740.02,691.24,755.19,593.71,689.72,753.74,643.84,665.36,701.30,738.56,803.35,522.49,647.63,624.87,752.37,671.78,849.33,777.82,659.37,667.27,721.43,553.86,762.92,602.64,655.25,708.82,605.35,810.63,724.61,748.27)
    Min_85_SON = (0.00,0.00,0.00,0.41,0.00,0.00,27.00,4.43,64.10,0.00,111.27,21.95,23.17,67.18,0.00,0.70,67.51,23.21,0.00,0.00,0.00,0.00,0.00,115.10,104.36,108.81,77.52,0.00,36.05,0.00,0.00,104.99,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,3.06,0.00,3.92,0.00,0.00,0.00,40.93,0.00,65.41,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,40.76,10.07,0.00,34.12)
    Min_85_DJF = (1993.93,1546.07,1715.60,1721.79,1811.02,1051.79,1588.46,1188.32,1574.22,1756.74,1759.52,1970.26,1758.82,1795.50,690.62,1178.14,1963.66,1738.39,1605.98,798.60,1944.02,1947.38,1602.34,1939.91,1248.82,2068.28,2101.78,1639.69,1084.75,1526.44,1343.17,2182.84,1130.00,1870.88,1766.08,2070.22,1545.56,1576.16,1340.24,1112.74,1970.12,1579.20,1548.11,1792.36,1887.09,1967.41,1693.02,1353.47,1249.35,1517.76,1542.22,2194.43,1653.89,1779.89,1578.30,1931.90,1136.55,1821.36,1588.94,1466.48,1894.11,1336.10,1951.76,1483.10,1323.83)
    Min_85_MAM = (751.00,725.85,847.57,457.26,648.41,637.16,460.81,496.50,910.79,540.80,480.25,661.95,602.00,466.02,725.30,500.46,644.97,834.40,599.40,406.57,399.64,631.52,748.83,427.10,640.94,818.41,669.30,372.70,450.92,461.19,513.23,528.98,823.27,575.55,757.54,445.76,939.60,794.20,376.02,783.43,637.69,454.33,563.89,359.48,706.74,460.62,477.57,594.65,481.82,433.74,604.06,617.81,674.73,709.39,684.34,689.45,528.66,737.36,773.64,489.18,563.34,338.96,851.39,486.16,228.38)
    Min_85_JJA = (0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,11.32,0.00,0.00,0.00,5.89,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,3.05,14.18,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00)
    Ave_85_YR = (1112.97,1058.39,1047.07,941.46,1047.14,1053.36,1034.90,1021.37,1071.49,1018.67,1015.77,1060.12,1086.38,1057.59,1013.85,970.97,1108.35,1086.09,1010.98,1013.58,1030.12,1042.04,1117.94,1032.68,1014.85,1120.45,1044.78,1037.37,994.82,1034.19,1037.19,1142.64,1104.55,1029.09,1090.11,1116.13,977.96,999.55,1039.95,1088.71,1092.22,996.52,1077.94,1111.21,1099.51,1071.58,1109.20,1021.70,976.43,1041.57,1008.77,1084.21,1045.08,984.92,1022.81,1052.04,1013.73,1069.86,1033.28,968.41,1022.02,996.12,1092.87,1027.93,983.54)
    Ave_85_SON = (471.77,331.61,315.28,236.69,262.23,308.44,376.84,375.95,292.75,335.36,512.27,306.43,316.94,380.67,242.99,308.29,290.52,355.69,306.63,305.66,273.26,362.46,239.84,346.59,339.07,294.54,309.24,312.39,367.82,298.07,256.31,485.74,461.63,355.97,298.30,359.51,323.27,265.73,154.51,404.57,291.41,277.76,374.42,369.15,297.62,275.80,345.78,256.46,195.92,330.99,188.65,297.23,303.51,181.29,276.57,188.09,287.74,287.93,171.70,266.50,178.97,290.73,348.50,294.23,280.33)
    Ave_85_DJF = (2830.36,2679.02,2661.65,2439.01,2651.15,2658.08,2749.46,2549.99,2643.30,2589.28,2486.69,2805.90,2788.91,2592.19,2453.19,2578.51,2913.74,2681.56,2546.16,2570.96,2723.44,2686.29,2875.15,2585.23,2509.57,2774.49,2712.47,2700.31,2379.61,2752.96,2755.45,2849.45,2741.05,2553.74,2769.67,2743.58,2347.69,2498.87,2694.50,2716.94,2825.43,2646.96,2657.43,2752.67,2960.03,2882.12,2717.22,2699.76,2585.68,2610.26,2668.64,2877.60,2683.43,2643.94,2683.54,2741.01,2576.61,2715.45,2668.62,2467.65,2718.66,2610.25,2687.60,2692.41,2518.50)
    Ave_85_MAM = (1102.49,1183.53,1147.91,1047.19,1229.10,1197.12,971.90,1115.65,1302.10,1114.36,1011.78,1102.51,1202.43,1204.15,1304.35,958.38,1182.56,1249.36,1145.08,1138.83,1070.39,1087.17,1294.45,1147.80,1169.83,1356.78,1100.73,1106.76,1173.37,1039.29,1081.31,1185.45,1187.24,1166.63,1244.46,1314.97,1202.33,1187.09,1255.13,1198.10,1220.30,1036.81,1242.49,1280.89,1121.98,1106.97,1310.97,1106.53,1092.05,1187.27,1134.09,1133.95,1155.33,1082.93,1079.15,1254.33,1156.73,1246.63,1253.37,1107.46,1163.42,1051.23,1295.14,1101.95,1109.62)
    Ave_85_JJA = (55.75,45.06,60.14,47.07,50.98,54.56,41.43,49.37,51.25,39.92,50.13,35.07,43.55,58.83,47.61,45.57,55.37,62.85,42.41,43.93,60.10,38.47,58.74,56.91,45.58,60.59,54.92,36.70,59.98,55.04,53.19,57.93,34.60,44.43,45.11,52.35,41.05,49.50,51.92,40.79,39.15,31.29,34.34,49.26,27.77,28.75,60.24,30.57,37.01,40.90,42.21,36.97,44.68,37.49,49.91,30.95,39.07,34.48,36.63,35.20,32.94,37.37,37.47,30.52,31.50)
    Max_85_YR = (1380.20,1642.95,1243.51,1210.54,1310.14,1380.49,1362.36,1407.65,1382.98,1374.51,1257.42,1495.84,1337.68,1366.70,1511.76,1323.30,1435.99,1273.56,1247.01,1427.03,1244.18,1402.18,1359.38,1434.64,1366.65,1349.19,1203.42,1296.77,1264.95,1362.37,1387.13,1441.11,1289.43,1314.34,1407.03,1496.71,1194.56,1461.73,1656.04,1307.47,1341.23,1320.63,1411.49,1552.70,1527.61,1720.67,1365.51,1485.16,1255.99,1419.21,1424.31,1364.30,1361.56,1396.04,1340.29,1513.22,1484.13,1294.66,1414.37,1403.26,1396.54,1556.52,1512.72,1326.65,1247.87)
    Max_85_SON = (1120.28,735.85,652.96,471.33,662.32,604.67,982.61,795.34,855.42,1153.36,976.18,888.55,850.83,1208.09,634.10,716.07,939.59,1086.79,895.62,761.94,819.91,799.03,625.48,1081.76,1168.19,475.64,886.03,779.84,820.49,670.63,946.76,1492.25,1181.43,1224.35,553.20,1060.75,670.01,577.85,377.90,1101.43,874.28,800.37,1012.47,827.96,983.65,658.77,1067.47,712.46,627.19,969.37,557.40,937.27,590.17,535.69,738.77,628.29,1170.15,872.49,775.44,785.44,416.10,899.39,990.74,763.21,685.63)
    Max_85_DJF = (4179.28,4042.47,3389.92,3679.93,3401.07,3649.72,3764.59,3908.48,4046.64,3440.54,3916.35,4251.92,3606.25,3775.48,3537.93,4051.83,4147.07,3583.92,3097.04,4126.15,3809.57,3959.68,3659.10,4003.41,3444.17,3623.03,3505.62,3358.98,3445.52,3881.51,3939.25,3983.88,3415.51,3626.07,3872.85,3794.31,3170.34,3767.45,3815.02,3586.97,3694.55,3745.90,3828.97,4237.06,4349.31,4286.15,3486.09,3886.35,3172.16,3309.23,3902.11,4249.64,3947.32,4035.41,3643.86,4011.51,3639.90,3474.07,3861.09,3365.26,3892.15,4094.27,3964.41,3751.58,3640.32)
    Max_85_MAM = (1604.11,2036.98,1489.00,1805.24,1668.10,1697.94,1362.67,1776.14,2143.22,1921.35,1474.06,1628.98,1950.28,2239.55,2301.27,1403.95,1831.64,1735.38,1774.86,2175.01,1799.65,1753.15,1979.78,1851.99,2071.94,2090.93,1483.57,1671.54,1824.69,1501.26,1609.79,2261.58,1843.08,1702.44,1734.79,2156.53,1998.17,1645.41,3090.03,1820.93,1715.26,1687.67,2006.37,2325.91,1530.32,1997.22,1942.58,2111.92,2368.50,2071.17,1748.59,2607.35,2022.35,1572.47,2014.97,2289.87,2527.58,2498.28,2117.35,1972.60,1754.59,2111.83,2003.71,1686.35,1774.73)
    Max_85_JJA = (115.75,104.48,156.18,287.55,135.38,115.91,128.32,109.25,148.74,101.56,144.20,173.67,116.37,164.52,204.98,297.97,125.94,272.39,107.28,81.82,122.48,79.57,176.95,227.11,159.35,140.66,95.96,94.76,305.68,154.12,136.06,214.51,92.43,69.25,156.43,185.38,116.97,260.50,130.46,126.37,93.10,82.95,74.10,124.85,64.84,51.40,286.63,99.21,157.61,151.42,98.73,111.65,269.29,91.29,176.72,104.10,117.84,111.69,188.28,99.48,71.65,160.10,98.16,108.03,73.77)

    # set x-axes
    X = np.array([1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006]) 
    X2 = np.array ([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070])
    
    
    #-------------------------------------------------------------------------
    #PART 7: PLOT LINE GRAPH
    import csv
    with open('output_Pr_a_mean_AnnualSeasonal.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Parameter', 'Means'])
        
        writer.writerow(["CCCmaCanRCMYR_a_mean"] + CCCmaCanRCMYR_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIYR_a_mean"] + CCCmaSMHIYR_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMYR_a_mean"] + CNRMYR_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIYR_a_mean"] +CNRMSMHIYR_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CSIROYR_a_mean"] +CSIROYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIYR_a_mean"] +ICHECDMIYR_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLMYR_a_mean"] +ICHECCCLMYR_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIYR_a_mean"] +ICHECKNMIYR_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPIYR_a_mean"] +ICHECMPIYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHIYR_a_mean"] +ICHECSMHIYR_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLYR_a_mean"] +IPSLYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCYR_a_mean"] +MIROCYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMYR_a_mean"] +MOHCCCLMYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMIYR_a_mean"] +MOHCKNMIYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHIYR_a_mean"] +MOHCSMHIYR_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLMYR_a_mean"] +MPICCLMYR_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOYR_a_mean"] +MPIREMOYR_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHIYR_a_mean"] +MPISMHIYR_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHIYR_a_mean"] +NCCSMHIYR_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAAYR_a_mean"] +NOAAYR_a_mean.flatten().astype(np.str).tolist())

        writer.writerow(["CCCmaCanRCMYR85_a_mean"] + CCCmaCanRCMYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIYR85_a_mean"] + CCCmaSMHIYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMYR85_a_mean"] + CNRMYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIYR85_a_mean"] +CNRMSMHIYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CSIROYR85_a_mean"] +CSIROYR85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIYR85_a_mean"] +ICHECDMIYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECCCLMYR85_a_mean"] +ICHECCCLMYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIYR85_a_mean"] +ICHECKNMIYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPIYR85_a_mean"] +ICHECMPIYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHIYR85_a_mean"] +ICHECSMHIYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLYR85_a_mean"] +IPSLYR85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCYR85_a_mean"] +MIROCYR85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMYR85_a_mean"] +MOHCCCLMYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCKNMIYR85_a_mean"] +MOHCKNMIYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCSMHIYR85_a_mean"] +MOHCSMHIYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MPICCLMYR85_a_mean"] +MPICCLMYR85_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOYR85_a_mean"] +MPIREMOYR85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHIYR85_a_mean"] +MPISMHIYR85_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["NCCSMHIYR85_a_mean"] +NCCSMHIYR85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["NOAAYR85_a_mean"] +NOAAYR85_a_mean.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCMSON_a_mean"] + CCCmaCanRCMSON_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHISON_a_mean"] + CCCmaSMHISON_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMSON_a_mean"] + CNRMSON_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHISON_a_mean"] +CNRMSMHISON_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIROSON_a_mean"] +CSIROSON_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMISON_a_mean"] +ICHECDMISON_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["ICHECCCLMSON_a_mean"] +ICHECCCLMSON_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMISON_a_mean"] +ICHECKNMISON_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPISON_a_mean"] +ICHECMPISON_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["ICHECSMHISON_a_mean"] +ICHECSMHISON_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["IPSLSON_a_mean"] +IPSLSON_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCSON_a_mean"] +MIROCSON_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMSON_a_mean"] +MOHCCCLMSON_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMISON_a_mean"] +MOHCKNMISON_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHISON_a_mean"] +MOHCSMHISON_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMSON_a_mean"] +MPICCLMSON_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOSON_a_mean"] +MPIREMOSON_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["MPISMHISON_a_mean"] +MPISMHISON_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["NCCSMHISON_a_mean"] +NCCSMHISON_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAASON_a_mean"] +NOAASON_a_mean.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCMSON85_a_mean"] + CCCmaCanRCMSON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHISON85_a_mean"] + CCCmaSMHISON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMSON85_a_mean"] + CNRMSON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHISON85_a_mean"] +CNRMSMHISON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIROSON85_a_mean"] +CSIROSON85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMISON85_a_mean"] +ICHECDMISON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECCCLMSON85_a_mean"] +ICHECCCLMSON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMISON85_a_mean"] +ICHECKNMISON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPISON85_a_mean"] +ICHECMPISON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHISON85_a_mean"] +ICHECSMHISON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["IPSLSON85_a_mean"] +IPSLSON85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCSON85_a_mean"] +MIROCSON85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMSON85_a_mean"] +MOHCCCLMSON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MOHCKNMISON85_a_mean"] +MOHCKNMISON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHISON85_a_mean"] +MOHCSMHISON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMSON85_a_mean"] +MPICCLMSON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMOSON85_a_mean"] +MPIREMOSON85_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["MPISMHISON85_a_mean"] +MPISMHISON85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["NCCSMHISON85_a_mean"] +NCCSMHISON85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NOAASON85_a_mean"] +NOAASON85_a_mean.flatten().astype(np.str).tolist())

        writer.writerow(["CCCmaCanRCMDJF_a_mean"] + CCCmaCanRCMDJF_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIDJF_a_mean"] + CCCmaSMHIDJF_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMDJF_a_mean"] + CNRMDJF_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIDJF_a_mean"] +CNRMSMHIDJF_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRODJF_a_mean"] +CSIRODJF_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIDJF_a_mean"] +ICHECDMIDJF_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLMDJF_a_mean"] +ICHECCCLMDJF_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIDJF_a_mean"] +ICHECKNMIDJF_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPIDJF_a_mean"] +ICHECMPIDJF_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["ICHECSMHIDJF_a_mean"] +ICHECSMHIDJF_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLDJF_a_mean"] +IPSLDJF_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCDJF_a_mean"] +MIROCDJF_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMDJF_a_mean"] +MOHCCCLMDJF_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["MOHCKNMIDJF_a_mean"] +MOHCKNMIDJF_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHIDJF_a_mean"] +MOHCSMHIDJF_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["MPICCLMDJF_a_mean"] +MPICCLMDJF_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMODJF_a_mean"] +MPIREMODJF_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["MPISMHIDJF_a_mean"] +MPISMHIDJF_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["NCCSMHIDJF_a_mean"] +NCCSMHIDJF_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAADJF_a_mean"] +NOAADJF_a_mean.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCMDJF85_a_mean"] + CCCmaCanRCMDJF85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIDJF85_a_mean"] + CCCmaSMHIDJF85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMDJF85_a_mean"] + CNRMDJF85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIDJF85_a_mean"] +CNRMSMHIDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIRODJF85_a_mean"] +CSIRODJF85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIDJF85_a_mean"] +ICHECDMIDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLMDJF85_a_mean"] +ICHECCCLMDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIDJF85_a_mean"] +ICHECKNMIDJF85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPIDJF85_a_mean"] +ICHECMPIDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHIDJF85_a_mean"] +ICHECSMHIDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLDJF85_a_mean"] +IPSLDJF85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCDJF85_a_mean"] +MIROCDJF85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMDJF85_a_mean"] +MOHCCCLMDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCKNMIDJF85_a_mean"] +MOHCKNMIDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHIDJF85_a_mean"] +MOHCSMHIDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMDJF85_a_mean"] +MPICCLMDJF85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMODJF85_a_mean"] +MPIREMODJF85_a_mean.flatten().astype(np.str).tolist())   
        writer.writerow(["MPISMHIDJF85_a_mean"] +MPISMHIDJF85_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["NCCSMHIDJF85_a_mean"] +NCCSMHIDJF85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NOAADJF85_a_mean"] +NOAADJF85_a_mean.flatten().astype(np.str).tolist())

        writer.writerow(["CCCmaCanRCMMAM_a_mean"] + CCCmaCanRCMMAM_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIMAM_a_mean"] + CCCmaSMHIMAM_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMMAM_a_mean"] + CNRMMAM_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIMAM_a_mean"] +CNRMSMHIMAM_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["CSIROMAM_a_mean"] +CSIROMAM_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIMAM_a_mean"] +ICHECDMIMAM_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLMMAM_a_mean"] +ICHECCCLMMAM_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMIMAM_a_mean"] +ICHECKNMIMAM_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPIMAM_a_mean"] +ICHECMPIMAM_a_mean.flatten().astype(np.str).tolist())  
        writer.writerow(["ICHECSMHIMAM_a_mean"] +ICHECSMHIMAM_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLMAM_a_mean"] +IPSLMAM_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCMAM_a_mean"] +MIROCMAM_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMMAM_a_mean"] +MOHCCCLMMAM_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCKNMIMAM_a_mean"] +MOHCKNMIMAM_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHIMAM_a_mean"] +MOHCSMHIMAM_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMMAM_a_mean"] +MPICCLMMAM_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOMAM_a_mean"] +MPIREMOMAM_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHIMAM_a_mean"] +MPISMHIMAM_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHIMAM_a_mean"] +NCCSMHIMAM_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAAMAM_a_mean"] +NOAAMAM_a_mean.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCMMAM85_a_mean"] + CCCmaCanRCMMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIMAM85_a_mean"] + CCCmaSMHIMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMMAM85_a_mean"] + CNRMMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIMAM85_a_mean"] +CNRMSMHIMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIROMAM85_a_mean"] +CSIROMAM85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIMAM85_a_mean"] +ICHECDMIMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLMMAM85_a_mean"] +ICHECCCLMMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMIMAM85_a_mean"] +ICHECKNMIMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPIMAM85_a_mean"] +ICHECMPIMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHIMAM85_a_mean"] +ICHECSMHIMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLMAM85_a_mean"] +IPSLMAM85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCMAM85_a_mean"] +MIROCMAM85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMMAM85_a_mean"] +MOHCCCLMMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCKNMIMAM85_a_mean"] +MOHCKNMIMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHIMAM85_a_mean"] +MOHCSMHIMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMMAM85_a_mean"] +MPICCLMMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["MPIREMOMAM85_a_mean"] +MPIREMOMAM85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHIMAM85_a_mean"] +MPISMHIMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHIMAM85_a_mean"] +NCCSMHIMAM85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NOAAMAM85_a_mean"] +NOAAMAM85_a_mean.flatten().astype(np.str).tolist()) 

        writer.writerow(["CCCmaCanRCMJJA_a_mean"] + CCCmaCanRCMJJA_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIJJA_a_mean"] + CCCmaSMHIJJA_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMJJA_a_mean"] + CNRMJJA_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIJJA_a_mean"] +CNRMSMHIJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIROJJA_a_mean"] +CSIROJJA_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIJJA_a_mean"] +ICHECDMIJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLMJJA_a_mean"] +ICHECCCLMJJA_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMIJJA_a_mean"] +ICHECKNMIJJA_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPIJJA_a_mean"] +ICHECMPIJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHIJJA_a_mean"] +ICHECSMHIJJA_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["IPSLJJA_a_mean"] +IPSLJJA_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCJJA_a_mean"] +MIROCJJA_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMJJA_a_mean"] +MOHCCCLMJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCKNMIJJA_a_mean"] +MOHCKNMIJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHIJJA_a_mean"] +MOHCSMHIJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMJJA_a_mean"] +MPICCLMJJA_a_mean.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOJJA_a_mean"] +MPIREMOJJA_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHIJJA_a_mean"] +MPISMHIJJA_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHIJJA_a_mean"] +NCCSMHIJJA_a_mean.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAAJJA_a_mean"] +NOAAJJA_a_mean.flatten().astype(np.str).tolist()) 

        writer.writerow(["CCCmaCanRCMJJA85_a_mean"] + CCCmaCanRCMJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIJJA85_a_mean"] + CCCmaSMHIJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMJJA85_a_mean"] + CNRMJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIJJA85_a_mean"] +CNRMSMHIJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["CSIROJJA85_a_mean"] +CSIROJJA85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIJJA85_a_mean"] +ICHECDMIJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECCCLMJJA85_a_mean"] +ICHECCCLMJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECKNMIJJA85_a_mean"] +ICHECKNMIJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["ICHECMPIJJA85_a_mean"] +ICHECMPIJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECSMHIJJA85_a_mean"] +ICHECSMHIJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["IPSLJJA85_a_mean"] +IPSLJJA85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCJJA85_a_mean"] +MIROCJJA85_a_mean.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMJJA85_a_mean"] +MOHCCCLMJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCKNMIJJA85_a_mean"] +MOHCKNMIJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MOHCSMHIJJA85_a_mean"] +MOHCSMHIJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPICCLMJJA85_a_mean"] +MPICCLMJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPIREMOJJA85_a_mean"] +MPIREMOJJA85_a_mean.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHIJJA85_a_mean"] +MPISMHIJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NCCSMHIJJA85_a_mean"] +NCCSMHIJJA85_a_mean.flatten().astype(np.str).tolist())
        writer.writerow(["NOAAJJA85_a_mean"] +NOAAJJA85_a_mean.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CRUYR"] + CRUYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUSONY"] + CRUSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUDJFY"] + CRUDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUMAMY"] + CRUMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUJJAY"] + CRUJJA_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["UDelYR"] + UDelYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelSONY"] + UDelSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelDJFY"] + UDelDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelMAMY"] + UDelMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelJJAY"] + UDelJJA_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["GPCCYR"] + GPCCYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCSONY"] + GPCCSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCDJFY"] + GPCCDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCMAMY"] + GPCCMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCJJAY"] + GPCCJJA_mean.data.flatten().astype(np.str).tolist())
    
    
    #PART 7A: Regional Climate Models Line Graph
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUSON_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelSON_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCSON_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUSON_mean.data,UDelSON_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_mean.data,UDelSON_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_mean.data,CRUSON_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi SON 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_SON_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUDJF_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelDJF_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCDJF_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUDJF_mean.data,UDelDJF_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_mean.data,UDelDJF_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_mean.data,CRUDJF_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi DJF 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_DJF_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUMAM_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelMAM_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCMAM_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUMAM_mean.data,UDelMAM_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_mean.data,UDelMAM_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_mean.data,CRUMAM_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi MAM 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_MAM_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUJJA_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelJJA_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCJJA_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUJJA_mean.data,UDelJJA_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_mean.data,UDelJJA_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_mean.data,CRUJJA_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi JJA 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_JJA_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUYR_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelYR_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCYR_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUYR_mean.data,UDelYR_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_mean.data,UDelYR_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_mean.data,CRUYR_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Annual_ALL4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUSON_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelSON_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCSON_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUSON_mean.data,UDelSON_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_mean.data,UDelSON_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_mean.data,CRUSON_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi SON 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_SON_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUDJF_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelDJF_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCDJF_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUDJF_mean.data,UDelDJF_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_mean.data,UDelDJF_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_mean.data,CRUDJF_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi DJF 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_DJF_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUMAM_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelMAM_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCMAM_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUMAM_mean.data,UDelMAM_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_mean.data,UDelMAM_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_mean.data,CRUMAM_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi MAM 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_MAM_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUJJA_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelJJA_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCJJA_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUJJA_mean.data,UDelJJA_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_mean.data,UDelJJA_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_mean.data,CRUJJA_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi JJA 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_JJA_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUYR_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelYR_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCYR_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUYR_mean.data,UDelYR_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_mean.data,UDelYR_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_mean.data,CRUYR_mean.data, color='grey', alpha='0.5')
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
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Annual_ALL8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()   

    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUSON_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelSON_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCSON_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUSON_a_mean,UDelSON_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_a_mean,UDelSON_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_a_mean,CRUSON_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOSON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHISON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAASON_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsSONY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_45_SON, label='Average RCM', lw=3, color='cyan')
    plt.plot(X2, Min_45_SON, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_45_SON, label = 'Maximum RCM', lw=3, color='blue')
              
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi SON 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_SON_MMA4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUDJF_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelDJF_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCDJF_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUDJF_a_mean,UDelDJF_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_a_mean,UDelDJF_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_a_mean,CRUDJF_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIRODJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMODJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIDJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAADJF_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsDJFY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_45_DJF, label='Average RCM', lw=3, color='cyan') 
    plt.plot(X2, Min_45_DJF, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_45_DJF, label = 'Maximum RCM', lw=3, color='blue')
            
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi DJF 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_DJF_MMA4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUMAM_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelMAM_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCMAM_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUMAM_a_mean,UDelMAM_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_a_mean,UDelMAM_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_a_mean,CRUMAM_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAAMAM_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsMAMY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_45_MAM, label='Average RCM', lw=3, color='cyan') 
    plt.plot(X2, Min_45_MAM, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_45_MAM, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi MAM 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_MAM_MMA4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUJJA_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelJJA_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCJJA_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUJJA_a_mean,UDelJJA_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_a_mean,UDelJJA_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_a_mean,CRUJJA_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAAJJA_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsJJAY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_45_JJA, label='Average RCM', lw=3, color='cyan') 
    plt.plot(X2, Min_45_JJA, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_45_JJA, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi JJA 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_JJA_MMA4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUYR_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelYR_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCYR_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUYR_a_mean,UDelYR_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_a_mean,UDelYR_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_a_mean,CRUYR_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAAYR_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_45_YR, label='Average RCM', lw=3, color='cyan')
    plt.plot(X2, Min_45_YR, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_45_YR, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi 1961-2070 RCP 4.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Annual_MMA4.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUSON_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelSON_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCSON_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUSON_a_mean,UDelSON_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_a_mean,UDelSON_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_a_mean,CRUSON_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOSON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHISON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAASON85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsSONY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_85_SON, label='Average RCM', lw=3, color='cyan')
    plt.plot(X2, Min_85_SON, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_85_SON, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi SON 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_SON_MMA8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUDJF_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelDJF_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCDJF_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUDJF_a_mean,UDelDJF_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_a_mean,UDelDJF_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_a_mean,CRUDJF_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIRODJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMODJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIDJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAADJF85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsDJFY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_85_DJF, label='Average RCM', lw=3, color='cyan')
    plt.plot(X2, Min_85_DJF, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_85_DJF, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi DJF 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_DJF_MMA8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUMAM_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelMAM_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCMAM_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUMAM_a_mean,UDelMAM_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_a_mean,UDelMAM_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_a_mean,CRUMAM_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAAMAM85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsMAMY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_85_MAM, label='Average RCM', lw=3, color='cyan')  
    plt.plot(X2, Min_85_MAM, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_85_MAM, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi MAM 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_MAM_MMA8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUJJA_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelJJA_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCJJA_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUJJA_a_mean,UDelJJA_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_a_mean,UDelJJA_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_a_mean,CRUJJA_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAAJJA85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsJJAY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_85_JJA, label='Average RCM', lw=3, color='cyan')
    plt.plot(X2, Min_85_JJA, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_85_JJA, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi JJA 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_JJA_MMA8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUYR_a_mean, lw=1, color='grey')   
    plt.plot(X,UDelYR_a_mean, lw=1, color='grey')
    plt.plot(X,GPCCYR_a_mean, lw=1, color='grey')
    plt.fill_between(X,CRUYR_a_mean,UDelYR_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_a_mean,UDelYR_a_mean, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_a_mean,CRUYR_a_mean, color='grey', alpha='0.5')
    plt.plot(X2, CCCmaCanRCMYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CCCmaSMHIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CNRMSMHIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, CSIROYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECDMIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECCCLMYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECKNMIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECMPIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, ICHECSMHIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, IPSLYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MIROCYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCCCLMYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCKNMIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MOHCSMHIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPICCLMYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPIREMOYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, MPISMHIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NCCSMHIYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X2, NOAAYR85_a_mean, lw=1, color='grey', linestyle='--')
    plt.plot(X, ObsY_a, label='Observed', lw=3, color='black')
    plt.plot(X2, Ave_85_YR, label='Average RCM', lw=3, color='cyan') 
    plt.plot(X2, Min_85_YR, label = 'Minimum RCM', lw=3, color='magenta')
    plt.plot(X2, Max_85_YR, label = 'Maximum RCM', lw=3, color='blue')
    
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=2)
    
    #create a title
    plt.title('Pr for Central Malawi 1961-2070 RCP 8.5', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Annual_MMA8.5.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #PART 7B: Average Line Graph
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUSON_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelSON_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCSON_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUSON_mean.data,UDelSON_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_mean.data,UDelSON_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCSON_mean.data,CRUSON_mean.data, color='grey', alpha='0.5')
    plt.plot(X, ObsSONY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageSONRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageSONRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('Pr for Central Malawi SON 1961-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_SON_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUDJF_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelDJF_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCDJF_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUDJF_mean.data,UDelDJF_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_mean.data,UDelDJF_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCDJF_mean.data,CRUDJF_mean.data, color='grey', alpha='0.5')
    plt.plot(X, ObsDJFY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageDJFRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageDJFRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('Pr for Central Malawi DJF 1961-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_DJF_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show() 
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUMAM_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelMAM_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCMAM_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUMAM_mean.data,UDelMAM_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_mean.data,UDelMAM_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCMAM_mean.data,CRUMAM_mean.data, color='grey', alpha='0.5')
    plt.plot(X, ObsMAMY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageMAMRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageMAMRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('Pr for Central Malawi MAM 1961-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_MAM_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
   
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUJJA_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelJJA_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCJJA_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUJJA_mean.data,UDelJJA_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_mean.data,UDelJJA_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCJJA_mean.data,CRUJJA_mean.data, color='grey', alpha='0.5')
    plt.plot(X, ObsJJAY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageJJARY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageJJARY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('Pr for Central Malawi JJA 1961-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_JJA_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
    #limit x axis    
    plt.xlim((1961,2070)) 
    
    #assign the line colours and set x axis to 'year' rather than 'time'
    plt.plot(X,CRUYR_mean.data, lw=1, color='grey')   
    plt.plot(X,UDelYR_mean.data, lw=1, color='grey')
    plt.plot(X,GPCCYR_mean.data, lw=1, color='grey')
    plt.fill_between(X,CRUYR_mean.data,UDelYR_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_mean.data,UDelYR_mean.data, color='grey', alpha='0.5')
    plt.fill_between(X,GPCCYR_mean.data,CRUYR_mean.data, color='grey', alpha='0.5')
    plt.plot(X, ObsY, label='Observed', lw=3, color='black')
    plt.plot(X2, AverageRY, label='Average RCM RCP 4.5', lw=1.5, color='cyan')
    plt.plot(X2, AverageRY85, label='Average RCM RCP 8.5', lw=1.5, color='magenta')
            
    #set a title for the y axis
    plt.ylabel('Precipitation Rate (mm per year)')
    
    #create a legend and set its location to under the graph
    plt.legend(loc=2, bbox_to_anchor=(1.05,1), fancybox=True, shadow=True)
    
    #create a title
    plt.title('Pr for Central Malawi 1961-2070', fontsize=11)   
    
    #add grid lines
    plt.grid()
    
    #save the image of the graph and include full legend
    plt.savefig('Pr_LineGraph_Annual_AVE.png', bbox_inches='tight')

    #show the graph in the console
    iplt.show()
    
if __name__ == '__main__':
    main()
    