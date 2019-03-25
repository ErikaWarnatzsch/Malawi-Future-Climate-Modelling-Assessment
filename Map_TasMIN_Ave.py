"""
Created on Monday 02 July 2018

@author: s0899345
"""
import matplotlib.pyplot as plt
import matplotlib.cm as mpl_cm
import numpy as np
import cf_units
from cf_units import Unit
import datetime
import iris
import iris.plot as iplt
import cartopy
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import iris.analysis.cartography
import iris.coord_categorisation as iriscc

#this file is split into parts as follows:
    #PART 1: load and format all past models 
    #PART 2: load and format all future models
    #PART 3: load and format observed data
    #PART 4: format data to be spatially and seasonally specific
    #PART 5: format data to be plot and time specific
    #PART 6: print data
    #PART 7: plot maps

def main():
    iris.FUTURE.netcdf_promote=True    
    
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT PAST MODELS 
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
    #PART 2: LOAD and FORMAT PROJECTED MODELS   
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
    
    
    #---------------------------------------------------------------------------------------------------------------------
    #PART 3: OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU= '/exports/csce/datastore/geos/users/s0899345/Climate_Modelling/Actual_Data/cru_ts4.01.1901.2016.tmn.dat.nc'
        
    #Load exactly one cube from given file
    CRU = iris.load_cube(CRU, 'near-surface temperature minimum')  
    
    #guess bounds  
    CRU.coord('latitude').guess_bounds()
    
    CRU.coord('longitude').guess_bounds()
    
    #---------------------------------------------------------------------------------------------------------------------
    #PART 4: FORMAT DATA TO BE SPATIALLY AND SEASONALLY SPECIFIC 
    
    #regrid all models to have same latitude and longitude system, all regridded to model with lowest resolution
    CCCmaSMHI_b = CCCmaSMHI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    CNRM_b = CNRM_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    CNRMSMHI_b = CNRMSMHI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    CSIRO_b = CSIRO_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    ICHECDMI_b = ICHECDMI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    ICHECCCLM_b = ICHECCCLM_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    ICHECKNMI_b = ICHECKNMI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    ICHECMPI_b = ICHECMPI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    ICHECSMHI_b = ICHECSMHI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    IPSL_b = IPSL_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MIROC_b = MIROC_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MOHCCCLM_b = MOHCCCLM_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MOHCKNMI_b = MOHCKNMI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MOHCSMHI_b = MOHCSMHI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MPICCLM_b = MPICCLM_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MPIREMO_b = MPIREMO_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    MPISMHI_b = MPISMHI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    NCCSMHI_b = NCCSMHI_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    NOAA_b = NOAA_b.regrid(CCCmaCanRCM_b, iris.analysis.Linear())
    
    CCCmaSMHI = CCCmaSMHI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    CNRM = CNRM.regrid(CCCmaCanRCM, iris.analysis.Linear())
    CNRMSMHI = CNRMSMHI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    CSIRO = CSIRO.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECDMI = ICHECDMI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECCCLM = ICHECCCLM.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECKNMI = ICHECKNMI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECMPI = ICHECMPI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECSMHI = ICHECSMHI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    IPSL = IPSL.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MIROC = MIROC.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MOHCCCLM = MOHCCCLM.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MOHCKNMI = MOHCKNMI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MOHCSMHI = MOHCSMHI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MPICCLM = MPICCLM.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MPIREMO = MPIREMO.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MPISMHI = MPISMHI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    NCCSMHI = NCCSMHI.regrid(CCCmaCanRCM, iris.analysis.Linear())
    NOAA = NOAA.regrid(CCCmaCanRCM, iris.analysis.Linear())
    
    CCCmaSMHI85 = CCCmaSMHI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    CNRM85 = CNRM85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    CNRMSMHI85 = CNRMSMHI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    CSIRO85 = CSIRO85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECDMI85 = ICHECDMI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECCCLM85 = ICHECCCLM85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECKNMI85 = ICHECKNMI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECMPI85 = ICHECMPI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    ICHECSMHI85 = ICHECSMHI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    IPSL85 = IPSL85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MIROC85 = MIROC85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MOHCCCLM85 = MOHCCCLM85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MOHCKNMI85 = MOHCKNMI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MOHCSMHI85 = MOHCSMHI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MPICCLM85 = MPICCLM85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MPIREMO85 = MPIREMO85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    MPISMHI85 = MPISMHI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    NCCSMHI85 = NCCSMHI85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    NOAA85 = NOAA85.regrid(CCCmaCanRCM, iris.analysis.Linear())
    
    CRU = CRU.regrid(CCCmaCanRCM, iris.analysis.Linear())
            
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
    
    CRU.units = Unit('Celsius') # This fixes CRU which is in 'Degrees Celsius' to read 'Celsius'
    
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
    
    
    #-------------------------------------------------------------------------
    #PART 5: FORMAT FILES TO BE TIME AND PLOT SPECIFIC 
    #PART 5A: COMPLETE FORMATING FOR BASELINE AND OBSERVED DATA
    #We are interested in plotting the data for the average of the time period. 
    CCCmaCanRCMSON_b = CCCmaCanRCMSON_b.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHISON_b = CCCmaSMHISON_b.collapsed('year', iris.analysis.MEAN)
    CNRMSON_b = CNRMSON_b.collapsed('year', iris.analysis.MEAN)
    CNRMSMHISON_b = CNRMSMHISON_b.collapsed('year', iris.analysis.MEAN)
    CSIROSON_b = CSIROSON_b.collapsed('year', iris.analysis.MEAN)
    ICHECDMISON_b = ICHECDMISON_b.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMSON_b = ICHECCCLMSON_b.collapsed('year', iris.analysis.MEAN)
    ICHECKNMISON_b = ICHECKNMISON_b.collapsed('year', iris.analysis.MEAN)
    ICHECMPISON_b = ICHECMPISON_b.collapsed('year', iris.analysis.MEAN)
    ICHECSMHISON_b = ICHECSMHISON_b.collapsed('year', iris.analysis.MEAN)
    IPSLSON_b = IPSLSON_b.collapsed('year', iris.analysis.MEAN)
    MIROCSON_b = MIROCSON_b.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMSON_b = MOHCCCLMSON_b.collapsed('year', iris.analysis.MEAN)
    MOHCKNMISON_b = MOHCKNMISON_b.collapsed('year', iris.analysis.MEAN)
    MOHCSMHISON_b = MOHCSMHISON_b.collapsed('year', iris.analysis.MEAN)
    MPICCLMSON_b = MPICCLMSON_b.collapsed('year', iris.analysis.MEAN)
    MPIREMOSON_b = MPIREMOSON_b.collapsed('year', iris.analysis.MEAN)
    MPISMHISON_b = MPISMHISON_b.collapsed('year', iris.analysis.MEAN)
    NCCSMHISON_b = NCCSMHISON_b.collapsed('year', iris.analysis.MEAN)
    NOAASON_b = NOAASON_b.collapsed('year', iris.analysis.MEAN)
    
    CRUSON = CRUSON.collapsed('year', iris.analysis.MEAN)  
  
    CCCmaCanRCMDJF_b = CCCmaCanRCMDJF_b.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIDJF_b = CCCmaSMHIDJF_b.collapsed('year', iris.analysis.MEAN)
    CNRMDJF_b = CNRMDJF_b.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIDJF_b = CNRMSMHIDJF_b.collapsed('year', iris.analysis.MEAN)
    CSIRODJF_b = CSIRODJF_b.collapsed('year', iris.analysis.MEAN)
    ICHECDMIDJF_b = ICHECDMIDJF_b.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMDJF_b = ICHECCCLMDJF_b.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIDJF_b = ICHECKNMIDJF_b.collapsed('year', iris.analysis.MEAN)
    ICHECMPIDJF_b = ICHECMPIDJF_b.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIDJF_b = ICHECSMHIDJF_b.collapsed('year', iris.analysis.MEAN)
    IPSLDJF_b = IPSLDJF_b.collapsed('year', iris.analysis.MEAN)
    MIROCDJF_b = MIROCDJF_b.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMDJF_b = MOHCCCLMDJF_b.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIDJF_b = MOHCKNMIDJF_b.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIDJF_b = MOHCSMHIDJF_b.collapsed('year', iris.analysis.MEAN)
    MPICCLMDJF_b = MPICCLMDJF_b.collapsed('year', iris.analysis.MEAN)
    MPIREMODJF_b = MPIREMODJF_b.collapsed('year', iris.analysis.MEAN)
    MPISMHIDJF_b = MPISMHIDJF_b.collapsed('year', iris.analysis.MEAN)
    NCCSMHIDJF_b = NCCSMHIDJF_b.collapsed('year', iris.analysis.MEAN)
    NOAADJF_b = NOAADJF_b.collapsed('year', iris.analysis.MEAN)
    
    CRUDJF = CRUDJF.collapsed('year', iris.analysis.MEAN)  
   
    CCCmaCanRCMMAM_b = CCCmaCanRCMMAM_b.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIMAM_b = CCCmaSMHIMAM_b.collapsed('year', iris.analysis.MEAN)
    CNRMMAM_b = CNRMMAM_b.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIMAM_b = CNRMSMHIMAM_b.collapsed('year', iris.analysis.MEAN)
    CSIROMAM_b = CSIROMAM_b.collapsed('year', iris.analysis.MEAN)
    ICHECDMIMAM_b = ICHECDMIMAM_b.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMMAM_b = ICHECCCLMMAM_b.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIMAM_b = ICHECKNMIMAM_b.collapsed('year', iris.analysis.MEAN)
    ICHECMPIMAM_b = ICHECMPIMAM_b.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIMAM_b = ICHECSMHIMAM_b.collapsed('year', iris.analysis.MEAN)
    IPSLMAM_b = IPSLMAM_b.collapsed('year', iris.analysis.MEAN)
    MIROCMAM_b = MIROCMAM_b.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMMAM_b = MOHCCCLMMAM_b.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIMAM_b = MOHCKNMIMAM_b.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIMAM_b = MOHCSMHIMAM_b.collapsed('year', iris.analysis.MEAN)
    MPICCLMMAM_b = MPICCLMMAM_b.collapsed('year', iris.analysis.MEAN)
    MPIREMOMAM_b = MPIREMOMAM_b.collapsed('year', iris.analysis.MEAN)
    MPISMHIMAM_b = MPISMHIMAM_b.collapsed('year', iris.analysis.MEAN)
    NCCSMHIMAM_b = NCCSMHIMAM_b.collapsed('year', iris.analysis.MEAN)
    NOAAMAM_b = NOAAMAM_b.collapsed('year', iris.analysis.MEAN)
    
    CRUMAM = CRUMAM.collapsed('year', iris.analysis.MEAN)  
    
    CCCmaCanRCMJJA_b = CCCmaCanRCMJJA_b.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIJJA_b = CCCmaSMHIJJA_b.collapsed('year', iris.analysis.MEAN)
    CNRMJJA_b = CNRMJJA_b.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIJJA_b = CNRMSMHIJJA_b.collapsed('year', iris.analysis.MEAN)
    CSIROJJA_b = CSIROJJA_b.collapsed('year', iris.analysis.MEAN)
    ICHECDMIJJA_b = ICHECDMIJJA_b.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMJJA_b = ICHECCCLMJJA_b.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIJJA_b = ICHECKNMIJJA_b.collapsed('year', iris.analysis.MEAN)
    ICHECMPIJJA_b = ICHECMPIJJA_b.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIJJA_b = ICHECSMHIJJA_b.collapsed('year', iris.analysis.MEAN)
    IPSLJJA_b = IPSLJJA_b.collapsed('year', iris.analysis.MEAN)
    MIROCJJA_b = MIROCJJA_b.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMJJA_b = MOHCCCLMJJA_b.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIJJA_b = MOHCKNMIJJA_b.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIJJA_b = MOHCSMHIJJA_b.collapsed('year', iris.analysis.MEAN)
    MPICCLMJJA_b = MPICCLMJJA_b.collapsed('year', iris.analysis.MEAN)
    MPIREMOJJA_b = MPIREMOJJA_b.collapsed('year', iris.analysis.MEAN)
    MPISMHIJJA_b = MPISMHIJJA_b.collapsed('year', iris.analysis.MEAN)
    NCCSMHIJJA_b = NCCSMHIJJA_b.collapsed('year', iris.analysis.MEAN)
    NOAAJJA_b = NOAAJJA_b.collapsed('year', iris.analysis.MEAN)
    
    CRUJJA = CRUJJA.collapsed('year', iris.analysis.MEAN)  
    
    CCCmaCanRCMYR_b = CCCmaCanRCM_b.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIYR_b = CCCmaSMHI_b.collapsed('year', iris.analysis.MEAN)
    CNRMYR_b = CNRM_b.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIYR_b = CNRMSMHI_b.collapsed('year', iris.analysis.MEAN)
    CSIROYR_b = CSIRO_b.collapsed('year', iris.analysis.MEAN)
    ICHECDMIYR_b = ICHECDMI_b.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMYR_b = ICHECCCLM_b.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIYR_b = ICHECKNMI_b.collapsed('year', iris.analysis.MEAN)
    ICHECMPIYR_b = ICHECMPI_b.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIYR_b = ICHECSMHI_b.collapsed('year', iris.analysis.MEAN)
    IPSLYR_b = IPSL_b.collapsed('year', iris.analysis.MEAN)
    MIROCYR_b = MIROC_b.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMYR_b = MOHCCCLM_b.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIYR_b = MOHCKNMI_b.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIYR_b = MOHCSMHI_b.collapsed('year', iris.analysis.MEAN)
    MPICCLMYR_b = MPICCLM_b.collapsed('year', iris.analysis.MEAN)
    MPIREMOYR_b = MPIREMO_b.collapsed('year', iris.analysis.MEAN)
    MPISMHIYR_b = MPISMHI_b.collapsed('year', iris.analysis.MEAN)
    NCCSMHIYR_b = NCCSMHI_b.collapsed('year', iris.analysis.MEAN)
    NOAAYR_b = NOAA_b.collapsed('year', iris.analysis.MEAN)
    
    CRUYR = CRU.collapsed('year', iris.analysis.MEAN) 
    
    #make units match, they already do but the name of the units doesn't. 
    CCCmaCanRCMSON_b.units = Unit('Celsius')
    CCCmaSMHISON_b.units = Unit('Celsius')
    CNRMSON_b.units = Unit('Celsius')
    CNRMSMHISON_b.units = Unit('Celsius')
    CSIROSON_b.units = Unit('Celsius')
    ICHECDMISON_b.units = Unit('Celsius')
    ICHECCCLMSON_b.units = Unit('Celsius')
    ICHECKNMISON_b.units = Unit('Celsius')
    ICHECMPISON_b.units = Unit('Celsius')
    ICHECSMHISON_b.units = Unit('Celsius')
    IPSLSON_b.units = Unit('Celsius')
    MIROCSON_b.units = Unit('Celsius')
    MOHCCCLMSON_b.units = Unit('Celsius')
    MOHCKNMISON_b.units = Unit('Celsius')
    MOHCSMHISON_b.units = Unit('Celsius')
    MPICCLMSON_b.units = Unit('Celsius')
    MPIREMOSON_b.units = Unit('Celsius')
    MPISMHISON_b.units = Unit('Celsius')
    NCCSMHISON_b.units = Unit('Celsius')
    NOAASON_b.units = Unit('Celsius')
    
    CRUSON.units = Unit('Celsius')
    
    CCCmaCanRCMDJF_b.units = Unit('Celsius')
    CCCmaSMHIDJF_b.units = Unit('Celsius')
    CNRMDJF_b.units = Unit('Celsius')
    CNRMSMHIDJF_b.units = Unit('Celsius')
    CSIRODJF_b.units = Unit('Celsius')
    ICHECDMIDJF_b.units = Unit('Celsius')
    ICHECCCLMDJF_b.units = Unit('Celsius')
    ICHECKNMIDJF_b.units = Unit('Celsius')
    ICHECMPIDJF_b.units = Unit('Celsius')
    ICHECSMHIDJF_b.units = Unit('Celsius')
    IPSLDJF_b.units = Unit('Celsius')
    MIROCDJF_b.units = Unit('Celsius')
    MOHCCCLMDJF_b.units = Unit('Celsius')
    MOHCKNMIDJF_b.units = Unit('Celsius')
    MOHCSMHIDJF_b.units = Unit('Celsius')
    MPICCLMDJF_b.units = Unit('Celsius')
    MPIREMODJF_b.units = Unit('Celsius')
    MPISMHIDJF_b.units = Unit('Celsius')
    NCCSMHIDJF_b.units = Unit('Celsius')
    NOAADJF_b.units = Unit('Celsius')
    
    CRUDJF.units = Unit('Celsius')
    
    CCCmaCanRCMMAM_b.units = Unit('Celsius')
    CCCmaSMHIMAM_b.units = Unit('Celsius')
    CNRMMAM_b.units = Unit('Celsius')
    CNRMSMHIMAM_b.units = Unit('Celsius')
    CSIROMAM_b.units = Unit('Celsius')
    ICHECDMIMAM_b.units = Unit('Celsius')
    ICHECCCLMMAM_b.units = Unit('Celsius')
    ICHECKNMIMAM_b.units = Unit('Celsius')
    ICHECMPIMAM_b.units = Unit('Celsius')
    ICHECSMHIMAM_b.units = Unit('Celsius')
    IPSLMAM_b.units = Unit('Celsius')
    MIROCMAM_b.units = Unit('Celsius')
    MOHCCCLMMAM_b.units = Unit('Celsius')
    MOHCKNMIMAM_b.units = Unit('Celsius')
    MOHCSMHIMAM_b.units = Unit('Celsius')
    MPICCLMMAM_b.units = Unit('Celsius')
    MPIREMOMAM_b.units = Unit('Celsius')
    MPISMHIMAM_b.units = Unit('Celsius')
    NCCSMHIMAM_b.units = Unit('Celsius')
    NOAAMAM_b.units = Unit('Celsius')
    
    CRUMAM.units = Unit('Celsius')  
    
    CCCmaCanRCMJJA_b.units = Unit('Celsius')
    CCCmaSMHIJJA_b.units = Unit('Celsius')
    CNRMJJA_b.units = Unit('Celsius')
    CNRMSMHIJJA_b.units = Unit('Celsius')
    CSIROJJA_b.units = Unit('Celsius')
    ICHECDMIJJA_b.units = Unit('Celsius')
    ICHECCCLMJJA_b.units = Unit('Celsius')
    ICHECKNMIJJA_b.units = Unit('Celsius')
    ICHECMPIJJA_b.units = Unit('Celsius')
    ICHECSMHIJJA_b.units = Unit('Celsius')
    IPSLJJA_b.units = Unit('Celsius')
    MIROCJJA_b.units = Unit('Celsius')
    MOHCCCLMJJA_b.units = Unit('Celsius')
    MOHCKNMIJJA_b.units = Unit('Celsius')
    MOHCSMHIJJA_b.units = Unit('Celsius')
    MPICCLMJJA_b.units = Unit('Celsius')
    MPIREMOJJA_b.units = Unit('Celsius')
    MPISMHIJJA_b.units = Unit('Celsius')
    NCCSMHIJJA_b.units = Unit('Celsius')
    NOAAJJA_b.units = Unit('Celsius')
    
    CRUJJA.units = Unit('Celsius')  
    
    CCCmaCanRCMYR_b.units = Unit('Celsius')
    CCCmaSMHIYR_b.units = Unit('Celsius')
    CNRMYR_b.units = Unit('Celsius')
    CNRMSMHIYR_b.units = Unit('Celsius')
    CSIROYR_b.units = Unit('Celsius')
    ICHECDMIYR_b.units = Unit('Celsius')
    ICHECCCLMYR_b.units = Unit('Celsius')
    ICHECKNMIYR_b.units = Unit('Celsius')
    ICHECMPIYR_b.units = Unit('Celsius')
    ICHECSMHIYR_b.units = Unit('Celsius')
    IPSLYR_b.units = Unit('Celsius')
    MIROCYR_b.units = Unit('Celsius')
    MOHCCCLMYR_b.units = Unit('Celsius')
    MOHCKNMIYR_b.units = Unit('Celsius')
    MOHCSMHIYR_b.units = Unit('Celsius')
    MPICCLMYR_b.units = Unit('Celsius')
    MPIREMOYR_b.units = Unit('Celsius')
    MPISMHIYR_b.units = Unit('Celsius')
    NCCSMHIYR_b.units = Unit('Celsius')
    NOAAYR_b.units = Unit('Celsius')
    
    CRUYR.units = Unit('Celsius') 
    
    #Create averages
    ObsSON = (CRUSON)    
    ObsDJF = (CRUDJF)
    ObsMAM = (CRUMAM)
    ObsJJA = (CRUJJA)
    ObsYR = (CRUYR)
    
    #fix unit names, data in Celsius, but called 'Kelvin'...     
    ObsSON.units = Unit('Celsius')
    ObsDJF.units = Unit('Celsius')
    ObsMAM.units = Unit('Celsius')
    ObsJJA.units = Unit('Celsius')
    ObsYR.units = Unit('Celsius')
    
    
    #-------------------------------------------------------------------------
    #PART 5B: 2030 FORMATING
    #time constraint to make all series the same (2020-2049)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_30 = iris.Constraint(time=lambda cell: 2020 <= cell.point.year <= 2049)

    CCCmaCanRCMSON_30 = CCCmaCanRCMSON.extract(t_constraint_30)
    CCCmaSMHISON_30 = CCCmaSMHISON.extract(t_constraint_30)
    CNRMSON_30 =CNRMSON.extract(t_constraint_30)
    CNRMSMHISON_30 =CNRMSMHISON.extract(t_constraint_30)
    CSIROSON_30 =CSIROSON.extract(t_constraint_30)
    ICHECDMISON_30 =ICHECDMISON.extract(t_constraint_30)
    ICHECCCLMSON_30 =ICHECCCLMSON.extract(t_constraint_30)
    ICHECKNMISON_30 =ICHECKNMISON.extract(t_constraint_30)
    ICHECMPISON_30 =ICHECMPISON.extract(t_constraint_30)
    ICHECSMHISON_30 =ICHECSMHISON.extract(t_constraint_30)
    IPSLSON_30 =IPSLSON.extract(t_constraint_30)
    MIROCSON_30 =MIROCSON.extract(t_constraint_30)
    MOHCCCLMSON_30 =MOHCCCLMSON.extract(t_constraint_30)
    MOHCKNMISON_30 =MOHCKNMISON.extract(t_constraint_30)
    MOHCSMHISON_30 =MOHCSMHISON.extract(t_constraint_30)
    MPICCLMSON_30 =MPICCLMSON.extract(t_constraint_30)
    MPIREMOSON_30 =MPIREMOSON.extract(t_constraint_30)
    MPISMHISON_30 =MPISMHISON.extract(t_constraint_30)
    NCCSMHISON_30 =NCCSMHISON.extract(t_constraint_30)
    NOAASON_30 =NOAASON.extract(t_constraint_30) 
    
    CCCmaCanRCMSON85_30 = CCCmaCanRCMSON85.extract(t_constraint_30)
    CCCmaSMHISON85_30 =  CCCmaSMHISON85.extract(t_constraint_30)
    CNRMSON85_30 = CNRMSON85.extract(t_constraint_30)
    CNRMSMHISON85_30 = CNRMSMHISON85.extract(t_constraint_30)
    CSIROSON85_30 = CSIROSON85.extract(t_constraint_30)
    ICHECDMISON85_30 = ICHECDMISON85.extract(t_constraint_30)
    ICHECCCLMSON85_30 = ICHECCCLMSON85.extract(t_constraint_30)
    ICHECKNMISON85_30 = ICHECKNMISON85.extract(t_constraint_30)
    ICHECMPISON85_30 = ICHECMPISON85.extract(t_constraint_30)
    ICHECSMHISON85_30 = ICHECSMHISON85.extract(t_constraint_30)
    IPSLSON85_30 = IPSLSON85.extract(t_constraint_30)
    MIROCSON85_30 = MIROCSON85.extract(t_constraint_30)
    MOHCCCLMSON85_30 = MOHCCCLMSON85.extract(t_constraint_30)
    MOHCKNMISON85_30 = MOHCKNMISON85.extract(t_constraint_30)
    MOHCSMHISON85_30 = MOHCSMHISON85.extract(t_constraint_30)
    MPICCLMSON85_30 = MPICCLMSON85.extract(t_constraint_30)
    MPIREMOSON85_30 = MPIREMOSON85.extract(t_constraint_30)
    MPISMHISON85_30 = MPISMHISON85.extract(t_constraint_30)
    NCCSMHISON85_30 = NCCSMHISON85.extract(t_constraint_30)
    NOAASON85_30 =NOAASON85.extract(t_constraint_30) 
    
    CCCmaCanRCMDJF_30 = CCCmaCanRCMDJF.extract(t_constraint_30)
    CCCmaSMHIDJF_30 = CCCmaSMHIDJF.extract(t_constraint_30)
    CNRMDJF_30 =CNRMDJF.extract(t_constraint_30)
    CNRMSMHIDJF_30 =CNRMSMHIDJF.extract(t_constraint_30)
    CSIRODJF_30 =CSIRODJF.extract(t_constraint_30)
    ICHECDMIDJF_30 =ICHECDMIDJF.extract(t_constraint_30)
    ICHECCCLMDJF_30 =ICHECCCLMDJF.extract(t_constraint_30)
    ICHECKNMIDJF_30 =ICHECKNMIDJF.extract(t_constraint_30)
    ICHECMPIDJF_30 =ICHECMPIDJF.extract(t_constraint_30)
    ICHECSMHIDJF_30 =ICHECSMHIDJF.extract(t_constraint_30)
    IPSLDJF_30 =IPSLDJF.extract(t_constraint_30)
    MIROCDJF_30 =MIROCDJF.extract(t_constraint_30)
    MOHCCCLMDJF_30 =MOHCCCLMDJF.extract(t_constraint_30)
    MOHCKNMIDJF_30 =MOHCKNMIDJF.extract(t_constraint_30)
    MOHCSMHIDJF_30 =MOHCSMHIDJF.extract(t_constraint_30)
    MPICCLMDJF_30 =MPICCLMDJF.extract(t_constraint_30)
    MPIREMODJF_30 =MPIREMODJF.extract(t_constraint_30)
    MPISMHIDJF_30 =MPISMHIDJF.extract(t_constraint_30)
    NCCSMHIDJF_30 =NCCSMHIDJF.extract(t_constraint_30)
    NOAADJF_30 =NOAADJF.extract(t_constraint_30) 
    
    CCCmaCanRCMDJF85_30 = CCCmaCanRCMDJF85.extract(t_constraint_30)
    CCCmaSMHIDJF85_30 =  CCCmaSMHIDJF85.extract(t_constraint_30)
    CNRMDJF85_30 = CNRMDJF85.extract(t_constraint_30)
    CNRMSMHIDJF85_30 = CNRMSMHIDJF85.extract(t_constraint_30)
    CSIRODJF85_30 = CSIRODJF85.extract(t_constraint_30)
    ICHECDMIDJF85_30 = ICHECDMIDJF85.extract(t_constraint_30)
    ICHECCCLMDJF85_30 = ICHECCCLMDJF85.extract(t_constraint_30)
    ICHECKNMIDJF85_30 = ICHECKNMIDJF85.extract(t_constraint_30)
    ICHECMPIDJF85_30 = ICHECMPIDJF85.extract(t_constraint_30)
    ICHECSMHIDJF85_30 = ICHECSMHIDJF85.extract(t_constraint_30)
    IPSLDJF85_30 = IPSLDJF85.extract(t_constraint_30)
    MIROCDJF85_30 = MIROCDJF85.extract(t_constraint_30)
    MOHCCCLMDJF85_30 = MOHCCCLMDJF85.extract(t_constraint_30)
    MOHCKNMIDJF85_30 = MOHCKNMIDJF85.extract(t_constraint_30)
    MOHCSMHIDJF85_30 = MOHCSMHIDJF85.extract(t_constraint_30)
    MPICCLMDJF85_30 = MPICCLMDJF85.extract(t_constraint_30)
    MPIREMODJF85_30 = MPIREMODJF85.extract(t_constraint_30)
    MPISMHIDJF85_30 = MPISMHIDJF85.extract(t_constraint_30)
    NCCSMHIDJF85_30 = NCCSMHIDJF85.extract(t_constraint_30)
    NOAADJF85_30 =NOAADJF85.extract(t_constraint_30) 
    
    CCCmaCanRCMMAM_30 =  CCCmaCanRCMMAM.extract(t_constraint_30)
    CCCmaSMHIMAM_30 =  CCCmaSMHIMAM.extract(t_constraint_30)
    CNRMMAM_30 = CNRMMAM.extract(t_constraint_30)
    CNRMSMHIMAM_30 = CNRMSMHIMAM.extract(t_constraint_30)
    CSIROMAM_30 = CSIROMAM.extract(t_constraint_30)
    ICHECDMIMAM_30 = ICHECDMIMAM.extract(t_constraint_30)
    ICHECCCLMMAM_30 = ICHECCCLMMAM.extract(t_constraint_30)
    ICHECKNMIMAM_30 = ICHECKNMIMAM.extract(t_constraint_30)
    ICHECMPIMAM_30 = ICHECMPIMAM.extract(t_constraint_30)
    ICHECSMHIMAM_30 = ICHECSMHIMAM.extract(t_constraint_30)
    IPSLMAM_30 = IPSLMAM.extract(t_constraint_30)
    MIROCMAM_30 = MIROCMAM.extract(t_constraint_30)
    MOHCCCLMMAM_30 = MOHCCCLMMAM.extract(t_constraint_30)
    MOHCKNMIMAM_30 = MOHCKNMIMAM.extract(t_constraint_30)
    MOHCSMHIMAM_30 = MOHCSMHIMAM.extract(t_constraint_30)
    MPICCLMMAM_30 = MPICCLMMAM.extract(t_constraint_30)
    MPIREMOMAM_30 = MPIREMOMAM.extract(t_constraint_30)
    MPISMHIMAM_30 = MPISMHIMAM.extract(t_constraint_30)
    NCCSMHIMAM_30 = NCCSMHIMAM.extract(t_constraint_30)
    NOAAMAM_30 = NOAAMAM.extract(t_constraint_30) 
    
    CCCmaCanRCMMAM85_30 = CCCmaCanRCMMAM85.extract(t_constraint_30)
    CCCmaSMHIMAM85_30 =  CCCmaSMHIMAM85.extract(t_constraint_30)
    CNRMMAM85_30 = CNRMMAM85.extract(t_constraint_30)
    CNRMSMHIMAM85_30 = CNRMSMHIMAM85.extract(t_constraint_30)
    CSIROMAM85_30 = CSIROMAM85.extract(t_constraint_30)
    ICHECDMIMAM85_30 = ICHECDMIMAM85.extract(t_constraint_30)
    ICHECCCLMMAM85_30 = ICHECCCLMMAM85.extract(t_constraint_30)
    ICHECKNMIMAM85_30 = ICHECKNMIMAM85.extract(t_constraint_30)
    ICHECMPIMAM85_30 = ICHECMPIMAM85.extract(t_constraint_30)
    ICHECSMHIMAM85_30 = ICHECSMHIMAM85.extract(t_constraint_30)
    IPSLMAM85_30 = IPSLMAM85.extract(t_constraint_30)
    MIROCMAM85_30 = MIROCMAM85.extract(t_constraint_30)
    MOHCCCLMMAM85_30 = MOHCCCLMMAM85.extract(t_constraint_30)
    MOHCKNMIMAM85_30 = MOHCKNMIMAM85.extract(t_constraint_30)
    MOHCSMHIMAM85_30 = MOHCSMHIMAM85.extract(t_constraint_30)
    MPICCLMMAM85_30 = MPICCLMMAM85.extract(t_constraint_30)
    MPIREMOMAM85_30 = MPIREMOMAM85.extract(t_constraint_30)
    MPISMHIMAM85_30 = MPISMHIMAM85.extract(t_constraint_30)
    NCCSMHIMAM85_30 = NCCSMHIMAM85.extract(t_constraint_30)
    NOAAMAM85_30 =NOAAMAM85.extract(t_constraint_30) 
    
    CCCmaCanRCMJJA_30 =  CCCmaCanRCMJJA.extract(t_constraint_30)
    CCCmaSMHIJJA_30 =  CCCmaSMHIJJA.extract(t_constraint_30)
    CNRMJJA_30 = CNRMJJA.extract(t_constraint_30)
    CNRMSMHIJJA_30 = CNRMSMHIJJA.extract(t_constraint_30)
    CSIROJJA_30 = CSIROJJA.extract(t_constraint_30)
    ICHECDMIJJA_30 = ICHECDMIJJA.extract(t_constraint_30)
    ICHECCCLMJJA_30 = ICHECCCLMJJA.extract(t_constraint_30)
    ICHECKNMIJJA_30 = ICHECKNMIJJA.extract(t_constraint_30)
    ICHECMPIJJA_30 = ICHECMPIJJA.extract(t_constraint_30)
    ICHECSMHIJJA_30 = ICHECSMHIJJA.extract(t_constraint_30)
    IPSLJJA_30 = IPSLJJA.extract(t_constraint_30)
    MIROCJJA_30 = MIROCJJA.extract(t_constraint_30)
    MOHCCCLMJJA_30 = MOHCCCLMJJA.extract(t_constraint_30)
    MOHCKNMIJJA_30 = MOHCKNMIJJA.extract(t_constraint_30)
    MOHCSMHIJJA_30 = MOHCSMHIJJA.extract(t_constraint_30)
    MPICCLMJJA_30 = MPICCLMJJA.extract(t_constraint_30)
    MPIREMOJJA_30 = MPIREMOJJA.extract(t_constraint_30)
    MPISMHIJJA_30 = MPISMHIJJA.extract(t_constraint_30)
    NCCSMHIJJA_30 = NCCSMHIJJA.extract(t_constraint_30)
    NOAAJJA_30 = NOAAJJA.extract(t_constraint_30) 
    
    CCCmaCanRCMJJA85_30 = CCCmaCanRCMJJA85.extract(t_constraint_30)
    CCCmaSMHIJJA85_30 =  CCCmaSMHIJJA85.extract(t_constraint_30)
    CNRMJJA85_30 = CNRMJJA85.extract(t_constraint_30)
    CNRMSMHIJJA85_30 = CNRMSMHIJJA85.extract(t_constraint_30)
    CSIROJJA85_30 = CSIROJJA85.extract(t_constraint_30)
    ICHECDMIJJA85_30 = ICHECDMIJJA85.extract(t_constraint_30)
    ICHECCCLMJJA85_30 = ICHECCCLMJJA85.extract(t_constraint_30)
    ICHECKNMIJJA85_30 = ICHECKNMIJJA85.extract(t_constraint_30)
    ICHECMPIJJA85_30 = ICHECMPIJJA85.extract(t_constraint_30)
    ICHECSMHIJJA85_30 = ICHECSMHIJJA85.extract(t_constraint_30)
    IPSLJJA85_30 = IPSLJJA85.extract(t_constraint_30)
    MIROCJJA85_30 = MIROCJJA85.extract(t_constraint_30)
    MOHCCCLMJJA85_30 = MOHCCCLMJJA85.extract(t_constraint_30)
    MOHCKNMIJJA85_30 = MOHCKNMIJJA85.extract(t_constraint_30)
    MOHCSMHIJJA85_30 = MOHCSMHIJJA85.extract(t_constraint_30)
    MPICCLMJJA85_30 = MPICCLMJJA85.extract(t_constraint_30)
    MPIREMOJJA85_30 = MPIREMOJJA85.extract(t_constraint_30)
    MPISMHIJJA85_30 = MPISMHIJJA85.extract(t_constraint_30)
    NCCSMHIJJA85_30 = NCCSMHIJJA85.extract(t_constraint_30)
    NOAAJJA85_30 =NOAAJJA85.extract(t_constraint_30) 
    
    CCCmaCanRCM_30 =  CCCmaCanRCM.extract(t_constraint_30)
    CCCmaSMHI_30 =  CCCmaSMHI.extract(t_constraint_30)
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
    CCCmaSMHI85_30 =  CCCmaSMHI85.extract(t_constraint_30)
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
    NOAA85_30 =NOAA85.extract(t_constraint_30) 
    
    #We are interested in plotting the data for the average of the time period. 
    CCCmaCanRCMSON_30 = CCCmaCanRCMSON_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHISON_30 = CCCmaSMHISON_30.collapsed('year', iris.analysis.MEAN)
    CNRMSON_30 = CNRMSON_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHISON_30 = CNRMSMHISON_30.collapsed('year', iris.analysis.MEAN)
    CSIROSON_30 = CSIROSON_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMISON_30 = ICHECDMISON_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMSON_30 = ICHECCCLMSON_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMISON_30 = ICHECKNMISON_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPISON_30 = ICHECMPISON_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHISON_30 = ICHECSMHISON_30.collapsed('year', iris.analysis.MEAN)
    IPSLSON_30 = IPSLSON_30.collapsed('year', iris.analysis.MEAN)
    MIROCSON_30 = MIROCSON_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMSON_30 = MOHCCCLMSON_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMISON_30 = MOHCKNMISON_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHISON_30 = MOHCSMHISON_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMSON_30 = MPICCLMSON_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOSON_30 = MPIREMOSON_30.collapsed('year', iris.analysis.MEAN)
    MPISMHISON_30 = MPISMHISON_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHISON_30 = NCCSMHISON_30.collapsed('year', iris.analysis.MEAN)
    NOAASON_30 = NOAASON_30.collapsed('year', iris.analysis.MEAN)
  
    CCCmaCanRCMDJF_30 = CCCmaCanRCMDJF_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIDJF_30 = CCCmaSMHIDJF_30.collapsed('year', iris.analysis.MEAN)
    CNRMDJF_30 = CNRMDJF_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIDJF_30 = CNRMSMHIDJF_30.collapsed('year', iris.analysis.MEAN)
    CSIRODJF_30 = CSIRODJF_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIDJF_30 = ICHECDMIDJF_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMDJF_30 = ICHECCCLMDJF_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIDJF_30 = ICHECKNMIDJF_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIDJF_30 = ICHECMPIDJF_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIDJF_30 = ICHECSMHIDJF_30.collapsed('year', iris.analysis.MEAN)
    IPSLDJF_30 = IPSLDJF_30.collapsed('year', iris.analysis.MEAN)
    MIROCDJF_30 = MIROCDJF_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMDJF_30 = MOHCCCLMDJF_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIDJF_30 = MOHCKNMIDJF_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIDJF_30 = MOHCSMHIDJF_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMDJF_30 = MPICCLMDJF_30.collapsed('year', iris.analysis.MEAN)
    MPIREMODJF_30 = MPIREMODJF_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIDJF_30 = MPISMHIDJF_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIDJF_30 = NCCSMHIDJF_30.collapsed('year', iris.analysis.MEAN)
    NOAADJF_30 = NOAADJF_30.collapsed('year', iris.analysis.MEAN)
   
    CCCmaCanRCMMAM_30 = CCCmaCanRCMMAM_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIMAM_30 = CCCmaSMHIMAM_30.collapsed('year', iris.analysis.MEAN)
    CNRMMAM_30 = CNRMMAM_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIMAM_30 = CNRMSMHIMAM_30.collapsed('year', iris.analysis.MEAN)
    CSIROMAM_30 = CSIROMAM_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIMAM_30 = ICHECDMIMAM_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMMAM_30 = ICHECCCLMMAM_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIMAM_30 = ICHECKNMIMAM_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIMAM_30 = ICHECMPIMAM_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIMAM_30 = ICHECSMHIMAM_30.collapsed('year', iris.analysis.MEAN)
    IPSLMAM_30 = IPSLMAM_30.collapsed('year', iris.analysis.MEAN)
    MIROCMAM_30 = MIROCMAM_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMMAM_30 = MOHCCCLMMAM_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIMAM_30 = MOHCKNMIMAM_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIMAM_30 = MOHCSMHIMAM_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMMAM_30 = MPICCLMMAM_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOMAM_30 = MPIREMOMAM_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIMAM_30 = MPISMHIMAM_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIMAM_30 = NCCSMHIMAM_30.collapsed('year', iris.analysis.MEAN)
    NOAAMAM_30 = NOAAMAM_30.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMJJA_30 = CCCmaCanRCMJJA_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIJJA_30 = CCCmaSMHIJJA_30.collapsed('year', iris.analysis.MEAN)
    CNRMJJA_30 = CNRMJJA_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIJJA_30 = CNRMSMHIJJA_30.collapsed('year', iris.analysis.MEAN)
    CSIROJJA_30 = CSIROJJA_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIJJA_30 = ICHECDMIJJA_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMJJA_30 = ICHECCCLMJJA_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIJJA_30 = ICHECKNMIJJA_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIJJA_30 = ICHECMPIJJA_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIJJA_30 = ICHECSMHIJJA_30.collapsed('year', iris.analysis.MEAN)
    IPSLJJA_30 = IPSLJJA_30.collapsed('year', iris.analysis.MEAN)
    MIROCJJA_30 = MIROCJJA_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMJJA_30 = MOHCCCLMJJA_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIJJA_30 = MOHCKNMIJJA_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIJJA_30 = MOHCSMHIJJA_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMJJA_30 = MPICCLMJJA_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOJJA_30 = MPIREMOJJA_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIJJA_30 = MPISMHIJJA_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIJJA_30 = NCCSMHIJJA_30.collapsed('year', iris.analysis.MEAN)
    NOAAJJA_30 = NOAAJJA_30.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMYR_30 = CCCmaCanRCM_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIYR_30 = CCCmaSMHI_30.collapsed('year', iris.analysis.MEAN)
    CNRMYR_30 = CNRM_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIYR_30 = CNRMSMHI_30.collapsed('year', iris.analysis.MEAN)
    CSIROYR_30 = CSIRO_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIYR_30 = ICHECDMI_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMYR_30 = ICHECCCLM_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIYR_30 = ICHECKNMI_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIYR_30 = ICHECMPI_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIYR_30 = ICHECSMHI_30.collapsed('year', iris.analysis.MEAN)
    IPSLYR_30 = IPSL_30.collapsed('year', iris.analysis.MEAN)
    MIROCYR_30 = MIROC_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMYR_30 = MOHCCCLM_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIYR_30 = MOHCKNMI_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIYR_30 = MOHCSMHI_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMYR_30 = MPICCLM_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOYR_30 = MPIREMO_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIYR_30 = MPISMHI_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIYR_30 = NCCSMHI_30.collapsed('year', iris.analysis.MEAN)
    NOAAYR_30 = NOAA_30.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMSON85_30 = CCCmaCanRCMSON85_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHISON85_30 = CCCmaSMHISON85_30.collapsed('year', iris.analysis.MEAN)
    CNRMSON85_30 = CNRMSON85_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHISON85_30 = CNRMSMHISON85_30.collapsed('year', iris.analysis.MEAN)
    CSIROSON85_30 = CSIROSON85_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMISON85_30 = ICHECDMISON85_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMSON85_30 = ICHECCCLMSON85_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMISON85_30 = ICHECKNMISON85_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPISON85_30 = ICHECMPISON85_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHISON85_30 = ICHECSMHISON85_30.collapsed('year', iris.analysis.MEAN)
    IPSLSON85_30 = IPSLSON85_30.collapsed('year', iris.analysis.MEAN)
    MIROCSON85_30 = MIROCSON85_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMSON85_30 = MOHCCCLMSON85_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMISON85_30 = MOHCKNMISON85_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHISON85_30 = MOHCSMHISON85_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMSON85_30 = MPICCLMSON85_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOSON85_30 = MPIREMOSON85_30.collapsed('year', iris.analysis.MEAN)
    MPISMHISON85_30 = MPISMHISON85_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHISON85_30 = NCCSMHISON85_30.collapsed('year', iris.analysis.MEAN)
    NOAASON85_30 = NOAASON85_30.collapsed('year', iris.analysis.MEAN)
  
    CCCmaCanRCMDJF85_30 = CCCmaCanRCMDJF85_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIDJF85_30 = CCCmaSMHIDJF85_30.collapsed('year', iris.analysis.MEAN)
    CNRMDJF85_30 = CNRMDJF85_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIDJF85_30 = CNRMSMHIDJF85_30.collapsed('year', iris.analysis.MEAN)
    CSIRODJF85_30 = CSIRODJF85_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIDJF85_30 = ICHECDMIDJF85_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMDJF85_30 = ICHECCCLMDJF85_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIDJF85_30 = ICHECKNMIDJF85_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIDJF85_30 = ICHECMPIDJF85_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIDJF85_30 = ICHECSMHIDJF85_30.collapsed('year', iris.analysis.MEAN)
    IPSLDJF85_30 = IPSLDJF85_30.collapsed('year', iris.analysis.MEAN)
    MIROCDJF85_30 = MIROCDJF85_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMDJF85_30 = MOHCCCLMDJF85_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIDJF85_30 = MOHCKNMIDJF85_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIDJF85_30 = MOHCSMHIDJF85_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMDJF85_30 = MPICCLMDJF85_30.collapsed('year', iris.analysis.MEAN)
    MPIREMODJF85_30 = MPIREMODJF85_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIDJF85_30 = MPISMHIDJF85_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIDJF85_30 = NCCSMHIDJF85_30.collapsed('year', iris.analysis.MEAN)
    NOAADJF85_30 = NOAADJF85_30.collapsed('year', iris.analysis.MEAN)
   
    CCCmaCanRCMMAM85_30 = CCCmaCanRCMMAM85_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIMAM85_30 = CCCmaSMHIMAM85_30.collapsed('year', iris.analysis.MEAN)
    CNRMMAM85_30 = CNRMMAM85_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIMAM85_30 = CNRMSMHIMAM85_30.collapsed('year', iris.analysis.MEAN)
    CSIROMAM85_30 = CSIROMAM85_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIMAM85_30 = ICHECDMIMAM85_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMMAM85_30 = ICHECCCLMMAM85_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIMAM85_30 = ICHECKNMIMAM85_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIMAM85_30 = ICHECMPIMAM85_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIMAM85_30 = ICHECSMHIMAM85_30.collapsed('year', iris.analysis.MEAN)
    IPSLMAM85_30 = IPSLMAM85_30.collapsed('year', iris.analysis.MEAN)
    MIROCMAM85_30 = MIROCMAM85_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMMAM85_30 = MOHCCCLMMAM85_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIMAM85_30 = MOHCKNMIMAM85_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIMAM85_30 = MOHCSMHIMAM85_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMMAM85_30 = MPICCLMMAM85_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOMAM85_30 = MPIREMOMAM85_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIMAM85_30 = MPISMHIMAM85_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIMAM85_30 = NCCSMHIMAM85_30.collapsed('year', iris.analysis.MEAN)
    NOAAMAM85_30 = NOAAMAM85_30.collapsed('year', iris.analysis.MEAN)
   
    CCCmaCanRCMJJA85_30 = CCCmaCanRCMJJA85_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIJJA85_30 = CCCmaSMHIJJA85_30.collapsed('year', iris.analysis.MEAN)
    CNRMJJA85_30 = CNRMJJA85_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIJJA85_30 = CNRMSMHIJJA85_30.collapsed('year', iris.analysis.MEAN)
    CSIROJJA85_30 = CSIROJJA85_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIJJA85_30 = ICHECDMIJJA85_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMJJA85_30 = ICHECCCLMJJA85_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIJJA85_30 = ICHECKNMIJJA85_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIJJA85_30 = ICHECMPIJJA85_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIJJA85_30 = ICHECSMHIJJA85_30.collapsed('year', iris.analysis.MEAN)
    IPSLJJA85_30 = IPSLJJA85_30.collapsed('year', iris.analysis.MEAN)
    MIROCJJA85_30 = MIROCJJA85_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMJJA85_30 = MOHCCCLMJJA85_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIJJA85_30 = MOHCKNMIJJA85_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIJJA85_30 = MOHCSMHIJJA85_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMJJA85_30 = MPICCLMJJA85_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOJJA85_30 = MPIREMOJJA85_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIJJA85_30 = MPISMHIJJA85_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIJJA85_30 = NCCSMHIJJA85_30.collapsed('year', iris.analysis.MEAN)
    NOAAJJA85_30 = NOAAJJA85_30.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMYR85_30 = CCCmaCanRCM85_30.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIYR85_30 = CCCmaSMHI85_30.collapsed('year', iris.analysis.MEAN)
    CNRMYR85_30 = CNRM85_30.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIYR85_30 = CNRMSMHI85_30.collapsed('year', iris.analysis.MEAN)
    CSIROYR85_30 = CSIRO85_30.collapsed('year', iris.analysis.MEAN)
    ICHECDMIYR85_30 = ICHECDMI85_30.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMYR85_30 = ICHECCCLM85_30.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIYR85_30 = ICHECKNMI85_30.collapsed('year', iris.analysis.MEAN)
    ICHECMPIYR85_30 = ICHECMPI85_30.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIYR85_30 = ICHECSMHI85_30.collapsed('year', iris.analysis.MEAN)
    IPSLYR85_30 = IPSL85_30.collapsed('year', iris.analysis.MEAN)
    MIROCYR85_30 = MIROC85_30.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMYR85_30 = MOHCCCLM85_30.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIYR85_30 = MOHCKNMI85_30.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIYR85_30 = MOHCSMHI85_30.collapsed('year', iris.analysis.MEAN)
    MPICCLMYR85_30 = MPICCLM85_30.collapsed('year', iris.analysis.MEAN)
    MPIREMOYR85_30 = MPIREMO85_30.collapsed('year', iris.analysis.MEAN)
    MPISMHIYR85_30 = MPISMHI85_30.collapsed('year', iris.analysis.MEAN)
    NCCSMHIYR85_30 = NCCSMHI85_30.collapsed('year', iris.analysis.MEAN)
    NOAAYR85_30 = NOAA85_30.collapsed('year', iris.analysis.MEAN)
       
    #make units match, they already do but the name of the units doesn't. 
    CCCmaCanRCMSON_30.units = Unit('Celsius')
    CCCmaSMHISON_30.units = Unit('Celsius')
    CNRMSON_30.units = Unit('Celsius')
    CNRMSMHISON_30.units = Unit('Celsius')
    CSIROSON_30.units = Unit('Celsius')
    ICHECDMISON_30.units = Unit('Celsius')
    ICHECCCLMSON_30.units = Unit('Celsius')
    ICHECKNMISON_30.units = Unit('Celsius')
    ICHECMPISON_30.units = Unit('Celsius')
    ICHECSMHISON_30.units = Unit('Celsius')
    IPSLSON_30.units = Unit('Celsius')
    MIROCSON_30.units = Unit('Celsius')
    MOHCCCLMSON_30.units = Unit('Celsius')
    MOHCKNMISON_30.units = Unit('Celsius')
    MOHCSMHISON_30.units = Unit('Celsius')
    MPICCLMSON_30.units = Unit('Celsius')
    MPIREMOSON_30.units = Unit('Celsius')
    MPISMHISON_30.units = Unit('Celsius')
    NCCSMHISON_30.units = Unit('Celsius')
    NOAASON_30.units = Unit('Celsius')
 
    CCCmaCanRCMDJF_30.units = Unit('Celsius')
    CCCmaSMHIDJF_30.units = Unit('Celsius')
    CNRMDJF_30.units = Unit('Celsius')
    CNRMSMHIDJF_30.units = Unit('Celsius')
    CSIRODJF_30.units = Unit('Celsius')
    ICHECDMIDJF_30.units = Unit('Celsius')
    ICHECCCLMDJF_30.units = Unit('Celsius')
    ICHECKNMIDJF_30.units = Unit('Celsius')
    ICHECMPIDJF_30.units = Unit('Celsius')
    ICHECSMHIDJF_30.units = Unit('Celsius')
    IPSLDJF_30.units = Unit('Celsius')
    MIROCDJF_30.units = Unit('Celsius')
    MOHCCCLMDJF_30.units = Unit('Celsius')
    MOHCKNMIDJF_30.units = Unit('Celsius')
    MOHCSMHIDJF_30.units = Unit('Celsius')
    MPICCLMDJF_30.units = Unit('Celsius')
    MPIREMODJF_30.units = Unit('Celsius')
    MPISMHIDJF_30.units = Unit('Celsius')
    NCCSMHIDJF_30.units = Unit('Celsius')
    NOAADJF_30.units = Unit('Celsius')
    
    CCCmaCanRCMMAM_30.units = Unit('Celsius')
    CCCmaSMHIMAM_30.units = Unit('Celsius')
    CNRMMAM_30.units = Unit('Celsius')
    CNRMSMHIMAM_30.units = Unit('Celsius')
    CSIROMAM_30.units = Unit('Celsius')
    ICHECDMIMAM_30.units = Unit('Celsius')
    ICHECCCLMMAM_30.units = Unit('Celsius')
    ICHECKNMIMAM_30.units = Unit('Celsius')
    ICHECMPIMAM_30.units = Unit('Celsius')
    ICHECSMHIMAM_30.units = Unit('Celsius')
    IPSLMAM_30.units = Unit('Celsius')
    MIROCMAM_30.units = Unit('Celsius')
    MOHCCCLMMAM_30.units = Unit('Celsius')
    MOHCKNMIMAM_30.units = Unit('Celsius')
    MOHCSMHIMAM_30.units = Unit('Celsius')
    MPICCLMMAM_30.units = Unit('Celsius')
    MPIREMOMAM_30.units = Unit('Celsius')
    MPISMHIMAM_30.units = Unit('Celsius')
    NCCSMHIMAM_30.units = Unit('Celsius')
    NOAAMAM_30.units = Unit('Celsius')
    
    CCCmaCanRCMJJA_30.units = Unit('Celsius')
    CCCmaSMHIJJA_30.units = Unit('Celsius')
    CNRMJJA_30.units = Unit('Celsius')
    CNRMSMHIJJA_30.units = Unit('Celsius')
    CSIROJJA_30.units = Unit('Celsius')
    ICHECDMIJJA_30.units = Unit('Celsius')
    ICHECCCLMJJA_30.units = Unit('Celsius')
    ICHECKNMIJJA_30.units = Unit('Celsius')
    ICHECMPIJJA_30.units = Unit('Celsius')
    ICHECSMHIJJA_30.units = Unit('Celsius')
    IPSLJJA_30.units = Unit('Celsius')
    MIROCJJA_30.units = Unit('Celsius')
    MOHCCCLMJJA_30.units = Unit('Celsius')
    MOHCKNMIJJA_30.units = Unit('Celsius')
    MOHCSMHIJJA_30.units = Unit('Celsius')
    MPICCLMJJA_30.units = Unit('Celsius')
    MPIREMOJJA_30.units = Unit('Celsius')
    MPISMHIJJA_30.units = Unit('Celsius')
    NCCSMHIJJA_30.units = Unit('Celsius')
    NOAAJJA_30.units = Unit('Celsius')
    
    CCCmaCanRCMYR_30.units = Unit('Celsius')
    CCCmaSMHIYR_30.units = Unit('Celsius')
    CNRMYR_30.units = Unit('Celsius')
    CNRMSMHIYR_30.units = Unit('Celsius')
    CSIROYR_30.units = Unit('Celsius')
    ICHECDMIYR_30.units = Unit('Celsius')
    ICHECCCLMYR_30.units = Unit('Celsius')
    ICHECKNMIYR_30.units = Unit('Celsius')
    ICHECMPIYR_30.units = Unit('Celsius')
    ICHECSMHIYR_30.units = Unit('Celsius')
    IPSLYR_30.units = Unit('Celsius')
    MIROCYR_30.units = Unit('Celsius')
    MOHCCCLMYR_30.units = Unit('Celsius')
    MOHCKNMIYR_30.units = Unit('Celsius')
    MOHCSMHIYR_30.units = Unit('Celsius')
    MPICCLMYR_30.units = Unit('Celsius')
    MPIREMOYR_30.units = Unit('Celsius')
    MPISMHIYR_30.units = Unit('Celsius')
    NCCSMHIYR_30.units = Unit('Celsius')
    NOAAYR_30.units = Unit('Celsius')
    
    CCCmaCanRCMSON85_30.units = Unit('Celsius')
    CCCmaSMHISON85_30.units = Unit('Celsius')
    CNRMSON85_30.units = Unit('Celsius')
    CNRMSMHISON85_30.units = Unit('Celsius')
    CSIROSON85_30.units = Unit('Celsius')
    ICHECDMISON85_30.units = Unit('Celsius')
    ICHECCCLMSON85_30.units = Unit('Celsius')
    ICHECKNMISON85_30.units = Unit('Celsius')
    ICHECMPISON85_30.units = Unit('Celsius')
    ICHECSMHISON85_30.units = Unit('Celsius')
    IPSLSON85_30.units = Unit('Celsius')
    MIROCSON85_30.units = Unit('Celsius')
    MOHCCCLMSON85_30.units = Unit('Celsius')
    MOHCKNMISON85_30.units = Unit('Celsius')
    MOHCSMHISON85_30.units = Unit('Celsius')
    MPICCLMSON85_30.units = Unit('Celsius')
    MPIREMOSON85_30.units = Unit('Celsius')
    MPISMHISON85_30.units = Unit('Celsius')
    NCCSMHISON85_30.units = Unit('Celsius')
    NOAASON85_30.units = Unit('Celsius')
 
    CCCmaCanRCMDJF85_30.units = Unit('Celsius')
    CCCmaSMHIDJF85_30.units = Unit('Celsius')
    CNRMDJF85_30.units = Unit('Celsius')
    CNRMSMHIDJF85_30.units = Unit('Celsius')
    CSIRODJF85_30.units = Unit('Celsius')
    ICHECDMIDJF85_30.units = Unit('Celsius')
    ICHECCCLMDJF85_30.units = Unit('Celsius')
    ICHECKNMIDJF85_30.units = Unit('Celsius')
    ICHECMPIDJF85_30.units = Unit('Celsius')
    ICHECSMHIDJF85_30.units = Unit('Celsius')
    IPSLDJF85_30.units = Unit('Celsius')
    MIROCDJF85_30.units = Unit('Celsius')
    MOHCCCLMDJF85_30.units = Unit('Celsius')
    MOHCKNMIDJF85_30.units = Unit('Celsius')
    MOHCSMHIDJF85_30.units = Unit('Celsius')
    MPICCLMDJF85_30.units = Unit('Celsius')
    MPIREMODJF85_30.units = Unit('Celsius')
    MPISMHIDJF85_30.units = Unit('Celsius')
    NCCSMHIDJF85_30.units = Unit('Celsius')
    NOAADJF85_30.units = Unit('Celsius')
    
    CCCmaCanRCMMAM85_30.units = Unit('Celsius')
    CCCmaSMHIMAM85_30.units = Unit('Celsius')
    CNRMMAM85_30.units = Unit('Celsius')
    CNRMSMHIMAM85_30.units = Unit('Celsius')
    CSIROMAM85_30.units = Unit('Celsius')
    ICHECDMIMAM85_30.units = Unit('Celsius')
    ICHECCCLMMAM85_30.units = Unit('Celsius')
    ICHECKNMIMAM85_30.units = Unit('Celsius')
    ICHECMPIMAM85_30.units = Unit('Celsius')
    ICHECSMHIMAM85_30.units = Unit('Celsius')
    IPSLMAM85_30.units = Unit('Celsius')
    MIROCMAM85_30.units = Unit('Celsius')
    MOHCCCLMMAM85_30.units = Unit('Celsius')
    MOHCKNMIMAM85_30.units = Unit('Celsius')
    MOHCSMHIMAM85_30.units = Unit('Celsius')
    MPICCLMMAM85_30.units = Unit('Celsius')
    MPIREMOMAM85_30.units = Unit('Celsius')
    MPISMHIMAM85_30.units = Unit('Celsius')
    NCCSMHIMAM85_30.units = Unit('Celsius')
    NOAAMAM85_30.units = Unit('Celsius')
    
    CCCmaCanRCMJJA85_30.units = Unit('Celsius')
    CCCmaSMHIJJA85_30.units = Unit('Celsius')
    CNRMJJA85_30.units = Unit('Celsius')
    CNRMSMHIJJA85_30.units = Unit('Celsius')
    CSIROJJA85_30.units = Unit('Celsius')
    ICHECDMIJJA85_30.units = Unit('Celsius')
    ICHECCCLMJJA85_30.units = Unit('Celsius')
    ICHECKNMIJJA85_30.units = Unit('Celsius')
    ICHECMPIJJA85_30.units = Unit('Celsius')
    ICHECSMHIJJA85_30.units = Unit('Celsius')
    IPSLJJA85_30.units = Unit('Celsius')
    MIROCJJA85_30.units = Unit('Celsius')
    MOHCCCLMJJA85_30.units = Unit('Celsius')
    MOHCKNMIJJA85_30.units = Unit('Celsius')
    MOHCSMHIJJA85_30.units = Unit('Celsius')
    MPICCLMJJA85_30.units = Unit('Celsius')
    MPIREMOJJA85_30.units = Unit('Celsius')
    MPISMHIJJA85_30.units = Unit('Celsius')
    NCCSMHIJJA85_30.units = Unit('Celsius')
    NOAAJJA85_30.units = Unit('Celsius')
    
    CCCmaCanRCMYR85_30.units = Unit('Celsius')
    CCCmaSMHIYR85_30.units = Unit('Celsius')
    CNRMYR85_30.units = Unit('Celsius')
    CNRMSMHIYR85_30.units = Unit('Celsius')
    CSIROYR85_30.units = Unit('Celsius')
    ICHECDMIYR85_30.units = Unit('Celsius')
    ICHECCCLMYR85_30.units = Unit('Celsius')
    ICHECKNMIYR85_30.units = Unit('Celsius')
    ICHECMPIYR85_30.units = Unit('Celsius')
    ICHECSMHIYR85_30.units = Unit('Celsius')
    IPSLYR85_30.units = Unit('Celsius')
    MIROCYR85_30.units = Unit('Celsius')
    MOHCCCLMYR85_30.units = Unit('Celsius')
    MOHCKNMIYR85_30.units = Unit('Celsius')
    MOHCSMHIYR85_30.units = Unit('Celsius')
    MPICCLMYR85_30.units = Unit('Celsius')
    MPIREMOYR85_30.units = Unit('Celsius')
    MPISMHIYR85_30.units = Unit('Celsius')
    NCCSMHIYR85_30.units = Unit('Celsius')
    NOAAYR85_30.units = Unit('Celsius')
    
    #create change in temperature
    CCCmaCanRCMSON_30_diff = (CCCmaCanRCMSON_30 - CCCmaCanRCMSON_b)
    CCCmaSMHISON_30_diff = (CCCmaSMHISON_30 - CCCmaSMHISON_b)
    CNRMSON_30_diff = (CNRMSON_30 - CNRMSON_b)
    CNRMSMHISON_30_diff = (CNRMSMHISON_30 - CNRMSMHISON_b)  
    CSIROSON_30_diff = (CSIROSON_30 - CSIROSON_b)
    ICHECDMISON_30_diff = (ICHECDMISON_30 - ICHECDMISON_b) 
    ICHECCCLMSON_30_diff = (ICHECCCLMSON_30 - ICHECCCLMSON_b)
    ICHECKNMISON_30_diff = (ICHECKNMISON_30 - ICHECKNMISON_b)
    ICHECMPISON_30_diff = (ICHECMPISON_30 - ICHECMPISON_b)
    ICHECSMHISON_30_diff = (ICHECSMHISON_30 - ICHECSMHISON_b)
    IPSLSON_30_diff = (IPSLSON_30 - IPSLSON_b)
    MIROCSON_30_diff = (MIROCSON_30 - MIROCSON_b)
    MOHCCCLMSON_30_diff = (MOHCCCLMSON_30 - MOHCCCLMSON_b)
    MOHCKNMISON_30_diff = (MOHCKNMISON_30 - MOHCKNMISON_b)
    MOHCSMHISON_30_diff = (MOHCSMHISON_30 - MOHCSMHISON_b)
    MPICCLMSON_30_diff = (MPICCLMSON_30 - MPICCLMSON_b)      
    MPIREMOSON_30_diff = (MPIREMOSON_30 - MPIREMOSON_b)                         
    MPISMHISON_30_diff = (MPISMHISON_30 - MPISMHISON_b)
    NCCSMHISON_30_diff = (NCCSMHISON_30 - NCCSMHISON_b) 
    NOAASON_30_diff = (NOAASON_30 - NOAASON_b)
    
    CCCmaCanRCMDJF_30_diff = (CCCmaCanRCMDJF_30 - CCCmaCanRCMDJF_b)
    CCCmaSMHIDJF_30_diff = (CCCmaSMHIDJF_30 - CCCmaSMHIDJF_b)
    CNRMDJF_30_diff = (CNRMDJF_30 - CNRMDJF_b)
    CNRMSMHIDJF_30_diff = (CNRMSMHIDJF_30 - CNRMSMHIDJF_b)  
    CSIRODJF_30_diff = (CSIRODJF_30 - CSIRODJF_b)
    ICHECDMIDJF_30_diff = (ICHECDMIDJF_30 - ICHECDMIDJF_b) 
    ICHECCCLMDJF_30_diff = (ICHECCCLMDJF_30 - ICHECCCLMDJF_b)
    ICHECKNMIDJF_30_diff = (ICHECKNMIDJF_30 - ICHECKNMIDJF_b)
    ICHECMPIDJF_30_diff = (ICHECMPIDJF_30 - ICHECMPIDJF_b)
    ICHECSMHIDJF_30_diff = (ICHECSMHIDJF_30 - ICHECSMHIDJF_b)
    IPSLDJF_30_diff = (IPSLDJF_30 - IPSLDJF_b)
    MIROCDJF_30_diff = (MIROCDJF_30 - MIROCDJF_b)
    MOHCCCLMDJF_30_diff = (MOHCCCLMDJF_30 - MOHCCCLMDJF_b)
    MOHCKNMIDJF_30_diff = (MOHCKNMIDJF_30 - MOHCKNMIDJF_b)
    MOHCSMHIDJF_30_diff = (MOHCSMHIDJF_30 - MOHCSMHIDJF_b)
    MPICCLMDJF_30_diff = (MPICCLMDJF_30 - MPICCLMDJF_b)      
    MPIREMODJF_30_diff = (MPIREMODJF_30 - MPIREMODJF_b)                         
    MPISMHIDJF_30_diff = (MPISMHIDJF_30 - MPISMHIDJF_b)
    NCCSMHIDJF_30_diff = (NCCSMHIDJF_30 - NCCSMHIDJF_b) 
    NOAADJF_30_diff = (NOAADJF_30 - NOAADJF_b)
    
    CCCmaCanRCMMAM_30_diff = (CCCmaCanRCMMAM_30 - CCCmaCanRCMMAM_b)
    CCCmaSMHIMAM_30_diff = (CCCmaSMHIMAM_30 - CCCmaSMHIMAM_b)
    CNRMMAM_30_diff = (CNRMMAM_30 - CNRMMAM_b)
    CNRMSMHIMAM_30_diff = (CNRMSMHIMAM_30 - CNRMSMHIMAM_b)  
    CSIROMAM_30_diff = (CSIROMAM_30 - CSIROMAM_b)
    ICHECDMIMAM_30_diff = (ICHECDMIMAM_30 - ICHECDMIMAM_b) 
    ICHECCCLMMAM_30_diff = (ICHECCCLMMAM_30 - ICHECCCLMMAM_b)
    ICHECKNMIMAM_30_diff = (ICHECKNMIMAM_30 - ICHECKNMIMAM_b)
    ICHECMPIMAM_30_diff = (ICHECMPIMAM_30 - ICHECMPIMAM_b)
    ICHECSMHIMAM_30_diff = (ICHECSMHIMAM_30 - ICHECSMHIMAM_b)
    IPSLMAM_30_diff = (IPSLMAM_30 - IPSLMAM_b)
    MIROCMAM_30_diff = (MIROCMAM_30 - MIROCMAM_b)
    MOHCCCLMMAM_30_diff = (MOHCCCLMMAM_30 - MOHCCCLMMAM_b)
    MOHCKNMIMAM_30_diff = (MOHCKNMIMAM_30 - MOHCKNMIMAM_b)
    MOHCSMHIMAM_30_diff = (MOHCSMHIMAM_30 - MOHCSMHIMAM_b)
    MPICCLMMAM_30_diff = (MPICCLMMAM_30 - MPICCLMMAM_b)      
    MPIREMOMAM_30_diff = (MPIREMOMAM_30 - MPIREMOMAM_b)                         
    MPISMHIMAM_30_diff = (MPISMHIMAM_30 - MPISMHIMAM_b)
    NCCSMHIMAM_30_diff = (NCCSMHIMAM_30 - NCCSMHIMAM_b) 
    NOAAMAM_30_diff = (NOAAMAM_30 - NOAAMAM_b)
    
    CCCmaCanRCMJJA_30_diff = (CCCmaCanRCMJJA_30 - CCCmaCanRCMJJA_b)
    CCCmaSMHIJJA_30_diff = (CCCmaSMHIJJA_30 - CCCmaSMHIJJA_b)
    CNRMJJA_30_diff = (CNRMJJA_30 - CNRMJJA_b)
    CNRMSMHIJJA_30_diff = (CNRMSMHIJJA_30 - CNRMSMHIJJA_b)  
    CSIROJJA_30_diff = (CSIROJJA_30 - CSIROJJA_b)
    ICHECDMIJJA_30_diff = (ICHECDMIJJA_30 - ICHECDMIJJA_b) 
    ICHECCCLMJJA_30_diff = (ICHECCCLMJJA_30 - ICHECCCLMJJA_b)
    ICHECKNMIJJA_30_diff = (ICHECKNMIJJA_30 - ICHECKNMIJJA_b)
    ICHECMPIJJA_30_diff = (ICHECMPIJJA_30 - ICHECMPIJJA_b)
    ICHECSMHIJJA_30_diff = (ICHECSMHIJJA_30 - ICHECSMHIJJA_b)
    IPSLJJA_30_diff = (IPSLJJA_30 - IPSLJJA_b)
    MIROCJJA_30_diff = (MIROCJJA_30 - MIROCJJA_b)
    MOHCCCLMJJA_30_diff = (MOHCCCLMJJA_30 - MOHCCCLMJJA_b)
    MOHCKNMIJJA_30_diff = (MOHCKNMIJJA_30 - MOHCKNMIJJA_b)
    MOHCSMHIJJA_30_diff = (MOHCSMHIJJA_30 - MOHCSMHIJJA_b)
    MPICCLMJJA_30_diff = (MPICCLMJJA_30 - MPICCLMJJA_b)      
    MPIREMOJJA_30_diff = (MPIREMOJJA_30 - MPIREMOJJA_b)                         
    MPISMHIJJA_30_diff = (MPISMHIJJA_30 - MPISMHIJJA_b)
    NCCSMHIJJA_30_diff = (NCCSMHIJJA_30 - NCCSMHIJJA_b) 
    NOAAJJA_30_diff = (NOAAJJA_30 - NOAAJJA_b)
    
    CCCmaCanRCMYR_30_diff = (CCCmaCanRCMYR_30 - CCCmaCanRCMYR_b)
    CCCmaSMHIYR_30_diff = (CCCmaSMHIYR_30 - CCCmaSMHIYR_b)
    CNRMYR_30_diff = (CNRMYR_30 - CNRMYR_b)
    CNRMSMHIYR_30_diff = (CNRMSMHIYR_30 - CNRMSMHIYR_b)  
    CSIROYR_30_diff = (CSIROYR_30 - CSIROYR_b)
    ICHECDMIYR_30_diff = (ICHECDMIYR_30 - ICHECDMIYR_b) 
    ICHECCCLMYR_30_diff = (ICHECCCLMYR_30 - ICHECCCLMYR_b)
    ICHECKNMIYR_30_diff = (ICHECKNMIYR_30 - ICHECKNMIYR_b)
    ICHECMPIYR_30_diff = (ICHECMPIYR_30 - ICHECMPIYR_b)
    ICHECSMHIYR_30_diff = (ICHECSMHIYR_30 - ICHECSMHIYR_b)
    IPSLYR_30_diff = (IPSLYR_30 - IPSLYR_b)
    MIROCYR_30_diff = (MIROCYR_30 - MIROCYR_b)
    MOHCCCLMYR_30_diff = (MOHCCCLMYR_30 - MOHCCCLMYR_b)
    MOHCKNMIYR_30_diff = (MOHCKNMIYR_30 - MOHCKNMIYR_b)
    MOHCSMHIYR_30_diff = (MOHCSMHIYR_30 - MOHCSMHIYR_b)
    MPICCLMYR_30_diff = (MPICCLMYR_30 - MPICCLMYR_b)      
    MPIREMOYR_30_diff = (MPIREMOYR_30 - MPIREMOYR_b)                         
    MPISMHIYR_30_diff = (MPISMHIYR_30 - MPISMHIYR_b)
    NCCSMHIYR_30_diff = (NCCSMHIYR_30 - NCCSMHIYR_b) 
    NOAAYR_30_diff = (NOAAYR_30 - NOAAYR_b)
    
    CCCmaCanRCMSON85_30_diff = (CCCmaCanRCMSON85_30 - CCCmaCanRCMSON_b)
    CCCmaSMHISON85_30_diff = (CCCmaSMHISON85_30 - CCCmaSMHISON_b)
    CNRMSON85_30_diff = (CNRMSON85_30 - CNRMSON_b)
    CNRMSMHISON85_30_diff = (CNRMSMHISON85_30 - CNRMSMHISON_b)  
    CSIROSON85_30_diff = (CSIROSON85_30 - CSIROSON_b)
    ICHECDMISON85_30_diff = (ICHECDMISON85_30 - ICHECDMISON_b) 
    ICHECCCLMSON85_30_diff = (ICHECCCLMSON85_30 - ICHECCCLMSON_b)
    ICHECKNMISON85_30_diff = (ICHECKNMISON85_30 - ICHECKNMISON_b)
    ICHECMPISON85_30_diff = (ICHECMPISON85_30 - ICHECMPISON_b)
    ICHECSMHISON85_30_diff = (ICHECSMHISON85_30 - ICHECSMHISON_b)
    IPSLSON85_30_diff = (IPSLSON85_30 - IPSLSON_b)
    MIROCSON85_30_diff = (MIROCSON85_30 - MIROCSON_b)
    MOHCCCLMSON85_30_diff = (MOHCCCLMSON85_30 - MOHCCCLMSON_b)
    MOHCKNMISON85_30_diff = (MOHCKNMISON85_30 - MOHCKNMISON_b)
    MOHCSMHISON85_30_diff = (MOHCSMHISON85_30 - MOHCSMHISON_b)
    MPICCLMSON85_30_diff = (MPICCLMSON85_30 - MPICCLMSON_b)      
    MPIREMOSON85_30_diff = (MPIREMOSON85_30 - MPIREMOSON_b)                         
    MPISMHISON85_30_diff = (MPISMHISON85_30 - MPISMHISON_b)
    NCCSMHISON85_30_diff = (NCCSMHISON85_30 - NCCSMHISON_b) 
    NOAASON85_30_diff = (NOAASON85_30 - NOAASON_b)
    
    CCCmaCanRCMDJF85_30_diff = (CCCmaCanRCMDJF85_30 - CCCmaCanRCMDJF_b)
    CCCmaSMHIDJF85_30_diff = (CCCmaSMHIDJF85_30 - CCCmaSMHIDJF_b)
    CNRMDJF85_30_diff = (CNRMDJF85_30 - CNRMDJF_b)
    CNRMSMHIDJF85_30_diff = (CNRMSMHIDJF85_30 - CNRMSMHIDJF_b)  
    CSIRODJF85_30_diff = (CSIRODJF85_30 - CSIRODJF_b)
    ICHECDMIDJF85_30_diff = (ICHECDMIDJF85_30 - ICHECDMIDJF_b) 
    ICHECCCLMDJF85_30_diff = (ICHECCCLMDJF85_30 - ICHECCCLMDJF_b)
    ICHECKNMIDJF85_30_diff = (ICHECKNMIDJF85_30 - ICHECKNMIDJF_b)
    ICHECMPIDJF85_30_diff = (ICHECMPIDJF85_30 - ICHECMPIDJF_b)
    ICHECSMHIDJF85_30_diff = (ICHECSMHIDJF85_30 - ICHECSMHIDJF_b)
    IPSLDJF85_30_diff = (IPSLDJF85_30 - IPSLDJF_b)
    MIROCDJF85_30_diff = (MIROCDJF85_30 - MIROCDJF_b)
    MOHCCCLMDJF85_30_diff = (MOHCCCLMDJF85_30 - MOHCCCLMDJF_b)
    MOHCKNMIDJF85_30_diff = (MOHCKNMIDJF85_30 - MOHCKNMIDJF_b)
    MOHCSMHIDJF85_30_diff = (MOHCSMHIDJF85_30 - MOHCSMHIDJF_b)
    MPICCLMDJF85_30_diff = (MPICCLMDJF85_30 - MPICCLMDJF_b)      
    MPIREMODJF85_30_diff = (MPIREMODJF85_30 - MPIREMODJF_b)                         
    MPISMHIDJF85_30_diff = (MPISMHIDJF85_30 - MPISMHIDJF_b)
    NCCSMHIDJF85_30_diff = (NCCSMHIDJF85_30 - NCCSMHIDJF_b) 
    NOAADJF85_30_diff = (NOAADJF85_30 - NOAADJF_b)
    
    CCCmaCanRCMMAM85_30_diff = (CCCmaCanRCMMAM85_30 - CCCmaCanRCMMAM_b)
    CCCmaSMHIMAM85_30_diff = (CCCmaSMHIMAM85_30 - CCCmaSMHIMAM_b)
    CNRMMAM85_30_diff = (CNRMMAM85_30 - CNRMMAM_b)
    CNRMSMHIMAM85_30_diff = (CNRMSMHIMAM85_30 - CNRMSMHIMAM_b)  
    CSIROMAM85_30_diff = (CSIROMAM85_30 - CSIROMAM_b)
    ICHECDMIMAM85_30_diff = (ICHECDMIMAM85_30 - ICHECDMIMAM_b) 
    ICHECCCLMMAM85_30_diff = (ICHECCCLMMAM85_30 - ICHECCCLMMAM_b)
    ICHECKNMIMAM85_30_diff = (ICHECKNMIMAM85_30 - ICHECKNMIMAM_b)
    ICHECMPIMAM85_30_diff = (ICHECMPIMAM85_30 - ICHECMPIMAM_b)
    ICHECSMHIMAM85_30_diff = (ICHECSMHIMAM85_30 - ICHECSMHIMAM_b)
    IPSLMAM85_30_diff = (IPSLMAM85_30 - IPSLMAM_b)
    MIROCMAM85_30_diff = (MIROCMAM85_30 - MIROCMAM_b)
    MOHCCCLMMAM85_30_diff = (MOHCCCLMMAM85_30 - MOHCCCLMMAM_b)
    MOHCKNMIMAM85_30_diff = (MOHCKNMIMAM85_30 - MOHCKNMIMAM_b)
    MOHCSMHIMAM85_30_diff = (MOHCSMHIMAM85_30 - MOHCSMHIMAM_b)
    MPICCLMMAM85_30_diff = (MPICCLMMAM85_30 - MPICCLMMAM_b)      
    MPIREMOMAM85_30_diff = (MPIREMOMAM85_30 - MPIREMOMAM_b)                         
    MPISMHIMAM85_30_diff = (MPISMHIMAM85_30 - MPISMHIMAM_b)
    NCCSMHIMAM85_30_diff = (NCCSMHIMAM85_30 - NCCSMHIMAM_b) 
    NOAAMAM85_30_diff = (NOAAMAM85_30 - NOAAMAM_b)
    
    CCCmaCanRCMJJA85_30_diff = (CCCmaCanRCMJJA85_30 - CCCmaCanRCMJJA_b)
    CCCmaSMHIJJA85_30_diff = (CCCmaSMHIJJA85_30 - CCCmaSMHIJJA_b)
    CNRMJJA85_30_diff = (CNRMJJA85_30 - CNRMJJA_b)
    CNRMSMHIJJA85_30_diff = (CNRMSMHIJJA85_30 - CNRMSMHIJJA_b)  
    CSIROJJA85_30_diff = (CSIROJJA85_30 - CSIROJJA_b)
    ICHECDMIJJA85_30_diff = (ICHECDMIJJA85_30 - ICHECDMIJJA_b) 
    ICHECCCLMJJA85_30_diff = (ICHECCCLMJJA85_30 - ICHECCCLMJJA_b)
    ICHECKNMIJJA85_30_diff = (ICHECKNMIJJA85_30 - ICHECKNMIJJA_b)
    ICHECMPIJJA85_30_diff = (ICHECMPIJJA85_30 - ICHECMPIJJA_b)
    ICHECSMHIJJA85_30_diff = (ICHECSMHIJJA85_30 - ICHECSMHIJJA_b)
    IPSLJJA85_30_diff = (IPSLJJA85_30 - IPSLJJA_b)
    MIROCJJA85_30_diff = (MIROCJJA85_30 - MIROCJJA_b)
    MOHCCCLMJJA85_30_diff = (MOHCCCLMJJA85_30 - MOHCCCLMJJA_b)
    MOHCKNMIJJA85_30_diff = (MOHCKNMIJJA85_30 - MOHCKNMIJJA_b)
    MOHCSMHIJJA85_30_diff = (MOHCSMHIJJA85_30 - MOHCSMHIJJA_b)
    MPICCLMJJA85_30_diff = (MPICCLMJJA85_30 - MPICCLMJJA_b)      
    MPIREMOJJA85_30_diff = (MPIREMOJJA85_30 - MPIREMOJJA_b)                         
    MPISMHIJJA85_30_diff = (MPISMHIJJA85_30 - MPISMHIJJA_b)
    NCCSMHIJJA85_30_diff = (NCCSMHIJJA85_30 - NCCSMHIJJA_b) 
    NOAAJJA85_30_diff = (NOAAJJA85_30 - NOAAJJA_b)
    
    CCCmaCanRCMYR85_30_diff = (CCCmaCanRCMYR85_30 - CCCmaCanRCMYR_b)
    CCCmaSMHIYR85_30_diff = (CCCmaSMHIYR85_30 - CCCmaSMHIYR_b)
    CNRMYR85_30_diff = (CNRMYR85_30 - CNRMYR_b)
    CNRMSMHIYR85_30_diff = (CNRMSMHIYR85_30 - CNRMSMHIYR_b)  
    CSIROYR85_30_diff = (CSIROYR85_30 - CSIROYR_b)
    ICHECDMIYR85_30_diff = (ICHECDMIYR85_30 - ICHECDMIYR_b) 
    ICHECCCLMYR85_30_diff = (ICHECCCLMYR85_30 - ICHECCCLMYR_b)
    ICHECKNMIYR85_30_diff = (ICHECKNMIYR85_30 - ICHECKNMIYR_b)
    ICHECMPIYR85_30_diff = (ICHECMPIYR85_30 - ICHECMPIYR_b)
    ICHECSMHIYR85_30_diff = (ICHECSMHIYR85_30 - ICHECSMHIYR_b)
    IPSLYR85_30_diff = (IPSLYR85_30 - IPSLYR_b)
    MIROCYR85_30_diff = (MIROCYR85_30 - MIROCYR_b)
    MOHCCCLMYR85_30_diff = (MOHCCCLMYR85_30 - MOHCCCLMYR_b)
    MOHCKNMIYR85_30_diff = (MOHCKNMIYR85_30 - MOHCKNMIYR_b)
    MOHCSMHIYR85_30_diff = (MOHCSMHIYR85_30 - MOHCSMHIYR_b)
    MPICCLMYR85_30_diff = (MPICCLMYR85_30 - MPICCLMYR_b)      
    MPIREMOYR85_30_diff = (MPIREMOYR85_30 - MPIREMOYR_b)                         
    MPISMHIYR85_30_diff = (MPISMHIYR85_30 - MPISMHIYR_b)
    NCCSMHIYR85_30_diff = (NCCSMHIYR85_30 - NCCSMHIYR_b) 
    NOAAYR85_30_diff = (NOAAYR85_30 - NOAAYR_b)
    
    #create adjusted absolute temperature
    CCCmaCanRCMSON_30_adj =  (CCCmaCanRCMSON_30_diff + ObsSON)
    CCCmaSMHISON_30_adj =  (CCCmaSMHISON_30_diff + ObsSON)
    CNRMSON_30_adj =  (CNRMSON_30_diff + ObsSON)
    CNRMSMHISON_30_adj =  (CNRMSMHISON_30_diff + ObsSON)  
    CSIROSON_30_adj =  (CSIROSON_30_diff + ObsSON)
    ICHECDMISON_30_adj =  (ICHECDMISON_30_diff + ObsSON) 
    ICHECCCLMSON_30_adj =  (ICHECCCLMSON_30_diff + ObsSON)
    ICHECKNMISON_30_adj =  (ICHECKNMISON_30_diff + ObsSON)
    ICHECMPISON_30_adj =  (ICHECMPISON_30_diff + ObsSON)
    ICHECSMHISON_30_adj =  (ICHECSMHISON_30_diff + ObsSON)
    IPSLSON_30_adj =  (IPSLSON_30_diff + ObsSON)
    MIROCSON_30_adj =  (MIROCSON_30_diff + ObsSON)
    MOHCCCLMSON_30_adj =  (MOHCCCLMSON_30_diff + ObsSON)
    MOHCKNMISON_30_adj =  (MOHCKNMISON_30_diff + ObsSON)
    MOHCSMHISON_30_adj =  (MOHCSMHISON_30_diff + ObsSON)
    MPICCLMSON_30_adj =  (MPICCLMSON_30_diff + ObsSON)      
    MPIREMOSON_30_adj =  (MPIREMOSON_30_diff + ObsSON)                         
    MPISMHISON_30_adj =  (MPISMHISON_30_diff + ObsSON)
    NCCSMHISON_30_adj =  (NCCSMHISON_30_diff + ObsSON) 
    NOAASON_30_adj =  (NOAASON_30_diff + ObsSON)
    
    CCCmaCanRCMDJF_30_adj =  (CCCmaCanRCMDJF_30_diff  + ObsDJF)
    CCCmaSMHIDJF_30_adj =  (CCCmaSMHIDJF_30_diff + ObsDJF)
    CNRMDJF_30_adj =  (CNRMDJF_30_diff + ObsDJF)
    CNRMSMHIDJF_30_adj =  (CNRMSMHIDJF_30_diff + ObsDJF)  
    CSIRODJF_30_adj =  (CSIRODJF_30_diff + ObsDJF)
    ICHECDMIDJF_30_adj =  (ICHECDMIDJF_30_diff + ObsDJF) 
    ICHECCCLMDJF_30_adj =  (ICHECCCLMDJF_30_diff + ObsDJF)
    ICHECKNMIDJF_30_adj =  (ICHECKNMIDJF_30_diff + ObsDJF)
    ICHECMPIDJF_30_adj =  (ICHECMPIDJF_30_diff + ObsDJF)
    ICHECSMHIDJF_30_adj =  (ICHECSMHIDJF_30_diff + ObsDJF)
    IPSLDJF_30_adj =  (IPSLDJF_30_diff + ObsDJF)
    MIROCDJF_30_adj =  (MIROCDJF_30_diff + ObsDJF)
    MOHCCCLMDJF_30_adj =  (MOHCCCLMDJF_30_diff + ObsDJF)
    MOHCKNMIDJF_30_adj =  (MOHCKNMIDJF_30_diff + ObsDJF)
    MOHCSMHIDJF_30_adj =  (MOHCSMHIDJF_30_diff + ObsDJF)
    MPICCLMDJF_30_adj =  (MPICCLMDJF_30_diff + ObsDJF)      
    MPIREMODJF_30_adj =  (MPIREMODJF_30_diff + ObsDJF)                         
    MPISMHIDJF_30_adj =  (MPISMHIDJF_30_diff + ObsDJF)
    NCCSMHIDJF_30_adj =  (NCCSMHIDJF_30_diff + ObsDJF) 
    NOAADJF_30_adj =  (NOAADJF_30_diff + ObsDJF)
    
    CCCmaCanRCMMAM_30_adj =  (CCCmaCanRCMMAM_30_diff + ObsMAM)
    CCCmaSMHIMAM_30_adj =  (CCCmaSMHIMAM_30_diff + ObsMAM)
    CNRMMAM_30_adj =  (CNRMMAM_30_diff + ObsMAM)
    CNRMSMHIMAM_30_adj =  (CNRMSMHIMAM_30_diff + ObsMAM)  
    CSIROMAM_30_adj =  (CSIROMAM_30_diff + ObsMAM)
    ICHECDMIMAM_30_adj =  (ICHECDMIMAM_30_diff + ObsMAM) 
    ICHECCCLMMAM_30_adj =  (ICHECCCLMMAM_30_diff + ObsMAM)
    ICHECKNMIMAM_30_adj =  (ICHECKNMIMAM_30_diff + ObsMAM)
    ICHECMPIMAM_30_adj =  (ICHECMPIMAM_30_diff + ObsMAM)
    ICHECSMHIMAM_30_adj =  (ICHECSMHIMAM_30_diff + ObsMAM)
    IPSLMAM_30_adj =  (IPSLMAM_30_diff + ObsMAM)
    MIROCMAM_30_adj =  (MIROCMAM_30_diff + ObsMAM)
    MOHCCCLMMAM_30_adj =  (MOHCCCLMMAM_30_diff + ObsMAM)
    MOHCKNMIMAM_30_adj =  (MOHCKNMIMAM_30_diff + ObsMAM)
    MOHCSMHIMAM_30_adj =  (MOHCSMHIMAM_30_diff + ObsMAM)
    MPICCLMMAM_30_adj =  (MPICCLMMAM_30_diff + ObsMAM)      
    MPIREMOMAM_30_adj =  (MPIREMOMAM_30_diff + ObsMAM)                         
    MPISMHIMAM_30_adj =  (MPISMHIMAM_30_diff + ObsMAM)
    NCCSMHIMAM_30_adj =  (NCCSMHIMAM_30_diff + ObsMAM) 
    NOAAMAM_30_adj =  (NOAAMAM_30_diff + ObsMAM)
    
    CCCmaCanRCMJJA_30_adj =  (CCCmaCanRCMJJA_30_diff + ObsJJA)
    CCCmaSMHIJJA_30_adj =  (CCCmaSMHIJJA_30_diff + ObsJJA)
    CNRMJJA_30_adj =  (CNRMJJA_30_diff + ObsJJA)
    CNRMSMHIJJA_30_adj =  (CNRMSMHIJJA_30_diff + ObsJJA)  
    CSIROJJA_30_adj =  (CSIROJJA_30_diff + ObsJJA)
    ICHECDMIJJA_30_adj =  (ICHECDMIJJA_30_diff + ObsJJA) 
    ICHECCCLMJJA_30_adj =  (ICHECCCLMJJA_30_diff + ObsJJA)
    ICHECKNMIJJA_30_adj =  (ICHECKNMIJJA_30_diff + ObsJJA)
    ICHECMPIJJA_30_adj =  (ICHECMPIJJA_30_diff + ObsJJA)
    ICHECSMHIJJA_30_adj =  (ICHECSMHIJJA_30_diff + ObsJJA)
    IPSLJJA_30_adj =  (IPSLJJA_30_diff + ObsJJA)
    MIROCJJA_30_adj =  (MIROCJJA_30_diff + ObsJJA)
    MOHCCCLMJJA_30_adj =  (MOHCCCLMJJA_30_diff + ObsJJA)
    MOHCKNMIJJA_30_adj =  (MOHCKNMIJJA_30_diff + ObsJJA)
    MOHCSMHIJJA_30_adj =  (MOHCSMHIJJA_30_diff + ObsJJA)
    MPICCLMJJA_30_adj =  (MPICCLMJJA_30_diff + ObsJJA)      
    MPIREMOJJA_30_adj =  (MPIREMOJJA_30_diff + ObsJJA)                         
    MPISMHIJJA_30_adj =  (MPISMHIJJA_30_diff + ObsJJA)
    NCCSMHIJJA_30_adj =  (NCCSMHIJJA_30_diff + ObsJJA) 
    NOAAJJA_30_adj =  (NOAAJJA_30_diff + ObsJJA)
    
    CCCmaCanRCMYR_30_adj =  (CCCmaCanRCMYR_30_diff + ObsYR)
    CCCmaSMHIYR_30_adj =  (CCCmaSMHIYR_30_diff + ObsYR)
    CNRMYR_30_adj =  (CNRMYR_30_diff + ObsYR)
    CNRMSMHIYR_30_adj =  (CNRMSMHIYR_30_diff + ObsYR)  
    CSIROYR_30_adj =  (CSIROYR_30_diff + ObsYR)
    ICHECDMIYR_30_adj =  (ICHECDMIYR_30_diff + ObsYR) 
    ICHECCCLMYR_30_adj =  (ICHECCCLMYR_30_diff + ObsYR)
    ICHECKNMIYR_30_adj =  (ICHECKNMIYR_30_diff + ObsYR)
    ICHECMPIYR_30_adj =  (ICHECMPIYR_30_diff + ObsYR)
    ICHECSMHIYR_30_adj =  (ICHECSMHIYR_30_diff + ObsYR)
    IPSLYR_30_adj =  (IPSLYR_30_diff + ObsYR)
    MIROCYR_30_adj =  (MIROCYR_30_diff + ObsYR)
    MOHCCCLMYR_30_adj =  (MOHCCCLMYR_30_diff + ObsYR)
    MOHCKNMIYR_30_adj =  (MOHCKNMIYR_30_diff + ObsYR)
    MOHCSMHIYR_30_adj =  (MOHCSMHIYR_30_diff + ObsYR)
    MPICCLMYR_30_adj =  (MPICCLMYR_30_diff + ObsYR)      
    MPIREMOYR_30_adj =  (MPIREMOYR_30_diff + ObsYR)                         
    MPISMHIYR_30_adj =  (MPISMHIYR_30_diff + ObsYR)
    NCCSMHIYR_30_adj =  (NCCSMHIYR_30_diff + ObsYR) 
    NOAAYR_30_adj =  (NOAAYR_30_diff + ObsYR)
    
    CCCmaCanRCMSON85_30_adj =  (CCCmaCanRCMSON85_30_diff + ObsSON)
    CCCmaSMHISON85_30_adj =  (CCCmaSMHISON85_30_diff + ObsSON)
    CNRMSON85_30_adj =  (CNRMSON85_30_diff + ObsSON)
    CNRMSMHISON85_30_adj =  (CNRMSMHISON85_30_diff + ObsSON)  
    CSIROSON85_30_adj =  (CSIROSON85_30_diff + ObsSON)
    ICHECDMISON85_30_adj =  (ICHECDMISON85_30_diff + ObsSON) 
    ICHECCCLMSON85_30_adj =  (ICHECCCLMSON85_30_diff + ObsSON)
    ICHECKNMISON85_30_adj =  (ICHECKNMISON85_30_diff + ObsSON)
    ICHECMPISON85_30_adj =  (ICHECMPISON85_30_diff + ObsSON)
    ICHECSMHISON85_30_adj =  (ICHECSMHISON85_30_diff + ObsSON)
    IPSLSON85_30_adj =  (IPSLSON85_30_diff + ObsSON)
    MIROCSON85_30_adj =  (MIROCSON85_30_diff + ObsSON)
    MOHCCCLMSON85_30_adj =  (MOHCCCLMSON85_30_diff + ObsSON)
    MOHCKNMISON85_30_adj =  (MOHCKNMISON85_30_diff + ObsSON)
    MOHCSMHISON85_30_adj =  (MOHCSMHISON85_30_diff + ObsSON)
    MPICCLMSON85_30_adj =  (MPICCLMSON85_30_diff + ObsSON)      
    MPIREMOSON85_30_adj =  (MPIREMOSON85_30_diff + ObsSON)                         
    MPISMHISON85_30_adj =  (MPISMHISON85_30_diff + ObsSON)
    NCCSMHISON85_30_adj =  (NCCSMHISON85_30_diff + ObsSON) 
    NOAASON85_30_adj =  (NOAASON85_30_diff + ObsSON)
    
    CCCmaCanRCMDJF85_30_adj =  (CCCmaCanRCMDJF85_30_diff + ObsDJF)
    CCCmaSMHIDJF85_30_adj =  (CCCmaSMHIDJF85_30_diff + ObsDJF)
    CNRMDJF85_30_adj =  (CNRMDJF85_30_diff + ObsDJF)
    CNRMSMHIDJF85_30_adj =  (CNRMSMHIDJF85_30_diff + ObsDJF)  
    CSIRODJF85_30_adj =  (CSIRODJF85_30_diff + ObsDJF)
    ICHECDMIDJF85_30_adj =  (ICHECDMIDJF85_30_diff + ObsDJF) 
    ICHECCCLMDJF85_30_adj =  (ICHECCCLMDJF85_30_diff + ObsDJF)
    ICHECKNMIDJF85_30_adj =  (ICHECKNMIDJF85_30_diff + ObsDJF)
    ICHECMPIDJF85_30_adj =  (ICHECMPIDJF85_30_diff + ObsDJF)
    ICHECSMHIDJF85_30_adj =  (ICHECSMHIDJF85_30_diff + ObsDJF)
    IPSLDJF85_30_adj =  (IPSLDJF85_30_diff + ObsDJF)
    MIROCDJF85_30_adj =  (MIROCDJF85_30_diff + ObsDJF)
    MOHCCCLMDJF85_30_adj =  (MOHCCCLMDJF85_30_diff + ObsDJF)
    MOHCKNMIDJF85_30_adj =  (MOHCKNMIDJF85_30_diff + ObsDJF)
    MOHCSMHIDJF85_30_adj =  (MOHCSMHIDJF85_30_diff + ObsDJF)
    MPICCLMDJF85_30_adj =  (MPICCLMDJF85_30_diff + ObsDJF)      
    MPIREMODJF85_30_adj =  (MPIREMODJF85_30_diff + ObsDJF)                         
    MPISMHIDJF85_30_adj =  (MPISMHIDJF85_30_diff + ObsDJF)
    NCCSMHIDJF85_30_adj =  (NCCSMHIDJF85_30_diff + ObsDJF) 
    NOAADJF85_30_adj =  (NOAADJF85_30_diff + ObsDJF)
    
    CCCmaCanRCMMAM85_30_adj =  (CCCmaCanRCMMAM85_30_diff + ObsMAM)
    CCCmaSMHIMAM85_30_adj =  (CCCmaSMHIMAM85_30_diff + ObsMAM)
    CNRMMAM85_30_adj =  (CNRMMAM85_30_diff + ObsMAM)
    CNRMSMHIMAM85_30_adj =  (CNRMSMHIMAM85_30_diff + ObsMAM)  
    CSIROMAM85_30_adj =  (CSIROMAM85_30_diff + ObsMAM)
    ICHECDMIMAM85_30_adj =  (ICHECDMIMAM85_30_diff + ObsMAM) 
    ICHECCCLMMAM85_30_adj =  (ICHECCCLMMAM85_30_diff + ObsMAM)
    ICHECKNMIMAM85_30_adj =  (ICHECKNMIMAM85_30_diff + ObsMAM)
    ICHECMPIMAM85_30_adj =  (ICHECMPIMAM85_30_diff + ObsMAM)
    ICHECSMHIMAM85_30_adj =  (ICHECSMHIMAM85_30_diff + ObsMAM)
    IPSLMAM85_30_adj =  (IPSLMAM85_30_diff + ObsMAM)
    MIROCMAM85_30_adj =  (MIROCMAM85_30_diff + ObsMAM)
    MOHCCCLMMAM85_30_adj =  (MOHCCCLMMAM85_30_diff + ObsMAM)
    MOHCKNMIMAM85_30_adj =  (MOHCKNMIMAM85_30_diff + ObsMAM)
    MOHCSMHIMAM85_30_adj =  (MOHCSMHIMAM85_30_diff + ObsMAM)
    MPICCLMMAM85_30_adj =  (MPICCLMMAM85_30_diff + ObsMAM)      
    MPIREMOMAM85_30_adj =  (MPIREMOMAM85_30_diff + ObsMAM)                         
    MPISMHIMAM85_30_adj =  (MPISMHIMAM85_30_diff + ObsMAM)
    NCCSMHIMAM85_30_adj =  (NCCSMHIMAM85_30_diff + ObsMAM) 
    NOAAMAM85_30_adj =  (NOAAMAM85_30_diff + ObsMAM)
    
    CCCmaCanRCMJJA85_30_adj =  (CCCmaCanRCMJJA85_30_diff + ObsJJA)
    CCCmaSMHIJJA85_30_adj =  (CCCmaSMHIJJA85_30_diff + ObsJJA)
    CNRMJJA85_30_adj =  (CNRMJJA85_30_diff + ObsJJA)
    CNRMSMHIJJA85_30_adj =  (CNRMSMHIJJA85_30_diff + ObsJJA)  
    CSIROJJA85_30_adj =  (CSIROJJA85_30_diff + ObsJJA)
    ICHECDMIJJA85_30_adj =  (ICHECDMIJJA85_30_diff + ObsJJA) 
    ICHECCCLMJJA85_30_adj =  (ICHECCCLMJJA85_30_diff + ObsJJA)
    ICHECKNMIJJA85_30_adj =  (ICHECKNMIJJA85_30_diff + ObsJJA)
    ICHECMPIJJA85_30_adj =  (ICHECMPIJJA85_30_diff + ObsJJA)
    ICHECSMHIJJA85_30_adj =  (ICHECSMHIJJA85_30_diff + ObsJJA)
    IPSLJJA85_30_adj =  (IPSLJJA85_30_diff + ObsJJA)
    MIROCJJA85_30_adj =  (MIROCJJA85_30_diff + ObsJJA)
    MOHCCCLMJJA85_30_adj =  (MOHCCCLMJJA85_30_diff + ObsJJA)
    MOHCKNMIJJA85_30_adj =  (MOHCKNMIJJA85_30_diff + ObsJJA)
    MOHCSMHIJJA85_30_adj =  (MOHCSMHIJJA85_30_diff + ObsJJA)
    MPICCLMJJA85_30_adj =  (MPICCLMJJA85_30_diff + ObsJJA)      
    MPIREMOJJA85_30_adj =  (MPIREMOJJA85_30_diff + ObsJJA)                         
    MPISMHIJJA85_30_adj =  (MPISMHIJJA85_30_diff + ObsJJA)
    NCCSMHIJJA85_30_adj =  (NCCSMHIJJA85_30_diff + ObsJJA) 
    NOAAJJA85_30_adj =  (NOAAJJA85_30_diff + ObsJJA)
    
    CCCmaCanRCMYR85_30_adj =  (CCCmaCanRCMYR85_30_diff + ObsYR)
    CCCmaSMHIYR85_30_adj =  (CCCmaSMHIYR85_30_diff + ObsYR)
    CNRMYR85_30_adj =  (CNRMYR85_30_diff + ObsYR)
    CNRMSMHIYR85_30_adj =  (CNRMSMHIYR85_30_diff + ObsYR)  
    CSIROYR85_30_adj =  (CSIROYR85_30_diff + ObsYR)
    ICHECDMIYR85_30_adj =  (ICHECDMIYR85_30_diff + ObsYR) 
    ICHECCCLMYR85_30_adj =  (ICHECCCLMYR85_30_diff + ObsYR)
    ICHECKNMIYR85_30_adj =  (ICHECKNMIYR85_30_diff + ObsYR)
    ICHECMPIYR85_30_adj =  (ICHECMPIYR85_30_diff + ObsYR)
    ICHECSMHIYR85_30_adj =  (ICHECSMHIYR85_30_diff + ObsYR)
    IPSLYR85_30_adj =  (IPSLYR85_30_diff + ObsYR)
    MIROCYR85_30_adj =  (MIROCYR85_30_diff + ObsYR)
    MOHCCCLMYR85_30_adj =  (MOHCCCLMYR85_30_diff + ObsYR)
    MOHCKNMIYR85_30_adj =  (MOHCKNMIYR85_30_diff + ObsYR)
    MOHCSMHIYR85_30_adj =  (MOHCSMHIYR85_30_diff + ObsYR)
    MPICCLMYR85_30_adj =  (MPICCLMYR85_30_diff + ObsYR)      
    MPIREMOYR85_30_adj =  (MPIREMOYR85_30_diff + ObsYR)                         
    MPISMHIYR85_30_adj =  (MPISMHIYR85_30_diff + ObsYR)
    NCCSMHIYR85_30_adj =  (NCCSMHIYR85_30_diff + ObsYR) 
    NOAAYR85_30_adj =  (NOAAYR85_30_diff + ObsYR)
    
    #Create averages
    AverageSON_30 = (CCCmaCanRCMSON_30_adj + CCCmaSMHISON_30_adj + CNRMSON_30_adj + CNRMSMHISON_30_adj + CSIROSON_30_adj + ICHECDMISON_30_adj + ICHECCCLMSON_30_adj + ICHECKNMISON_30_adj + ICHECMPISON_30_adj + ICHECSMHISON_30_adj + IPSLSON_30_adj + MIROCSON_30_adj + MOHCCCLMSON_30_adj + MOHCKNMISON_30_adj + MOHCSMHISON_30_adj + MPICCLMSON_30_adj + MPIREMOSON_30_adj + MPISMHISON_30_adj + NCCSMHISON_30_adj + NOAASON_30_adj)/20.
    AverageDJF_30 = (CCCmaCanRCMDJF_30_adj + CCCmaSMHIDJF_30_adj + CNRMDJF_30_adj + CNRMSMHIDJF_30_adj + CSIRODJF_30_adj + ICHECDMIDJF_30_adj + ICHECCCLMDJF_30_adj + ICHECKNMIDJF_30_adj + ICHECMPIDJF_30_adj + ICHECSMHIDJF_30_adj + IPSLDJF_30_adj + MIROCDJF_30_adj + MOHCCCLMDJF_30_adj + MOHCKNMIDJF_30_adj + MOHCSMHIDJF_30_adj + MPICCLMDJF_30_adj + MPIREMODJF_30_adj + MPISMHIDJF_30_adj + NCCSMHIDJF_30_adj + NOAADJF_30_adj)/20.
    AverageMAM_30 = (CCCmaCanRCMMAM_30_adj + CCCmaSMHIMAM_30_adj + CNRMMAM_30_adj + CNRMSMHIMAM_30_adj + CSIROMAM_30_adj + ICHECDMIMAM_30_adj + ICHECCCLMMAM_30_adj + ICHECKNMIMAM_30_adj + ICHECMPIMAM_30_adj + ICHECSMHIMAM_30_adj + IPSLMAM_30_adj + MIROCMAM_30_adj + MOHCCCLMMAM_30_adj + MOHCKNMIMAM_30_adj + MOHCSMHIMAM_30_adj + MPICCLMMAM_30_adj + MPIREMOMAM_30_adj + MPISMHIMAM_30_adj + NCCSMHIMAM_30_adj + NOAAMAM_30_adj)/20.
    AverageJJA_30 = (CCCmaCanRCMJJA_30_adj + CCCmaSMHIJJA_30_adj + CNRMJJA_30_adj + CNRMSMHIJJA_30_adj + CSIROJJA_30_adj + ICHECDMIJJA_30_adj + ICHECCCLMJJA_30_adj + ICHECKNMIJJA_30_adj + ICHECMPIJJA_30_adj + ICHECSMHIJJA_30_adj + IPSLJJA_30_adj + MIROCJJA_30_adj + MOHCCCLMJJA_30_adj + MOHCKNMIJJA_30_adj + MOHCSMHIJJA_30_adj + MPICCLMJJA_30_adj + MPIREMOJJA_30_adj + MPISMHIJJA_30_adj + NCCSMHIJJA_30_adj + NOAAJJA_30_adj)/20.
    Average_30 = (CCCmaCanRCMYR_30_adj + CCCmaSMHIYR_30_adj + CNRMYR_30_adj + CNRMSMHIYR_30_adj + CSIROYR_30_adj + ICHECDMIYR_30_adj + ICHECCCLMYR_30_adj + ICHECKNMIYR_30_adj + ICHECMPIYR_30_adj + ICHECSMHIYR_30_adj + IPSLYR_30_adj + MIROCYR_30_adj + MOHCCCLMYR_30_adj + MOHCKNMIYR_30_adj + MOHCSMHIYR_30_adj + MPICCLMYR_30_adj + MPIREMOYR_30_adj + MPISMHIYR_30_adj + NCCSMHIYR_30_adj + NOAAYR_30_adj)/20.
    
    AverageSON85_30 = (CCCmaCanRCMSON85_30_adj + CCCmaSMHISON85_30_adj + CNRMSON85_30_adj + CNRMSMHISON85_30_adj + CSIROSON85_30_adj + ICHECDMISON85_30_adj + ICHECCCLMSON85_30_adj + ICHECKNMISON85_30_adj + ICHECMPISON85_30_adj + ICHECSMHISON85_30_adj + IPSLSON85_30_adj + MIROCSON85_30_adj + MOHCCCLMSON85_30_adj + MOHCKNMISON85_30_adj + MOHCSMHISON85_30_adj + MPICCLMSON85_30_adj + MPIREMOSON85_30_adj + MPISMHISON85_30_adj + NCCSMHISON85_30_adj + NOAASON85_30_adj)/20.
    AverageDJF85_30 = (CCCmaCanRCMDJF85_30_adj + CCCmaSMHIDJF85_30_adj + CNRMDJF85_30_adj + CNRMSMHIDJF85_30_adj + CSIRODJF85_30_adj + ICHECDMIDJF85_30_adj + ICHECCCLMDJF85_30_adj + ICHECKNMIDJF85_30_adj + ICHECMPIDJF85_30_adj + ICHECSMHIDJF85_30_adj + IPSLDJF85_30_adj + MIROCDJF85_30_adj + MOHCCCLMDJF85_30_adj + MOHCKNMIDJF85_30_adj + MOHCSMHIDJF85_30_adj + MPICCLMDJF85_30_adj + MPIREMODJF85_30_adj + MPISMHIDJF85_30_adj + NCCSMHIDJF85_30_adj + NOAADJF85_30_adj)/20.
    AverageMAM85_30 = (CCCmaCanRCMMAM85_30_adj + CCCmaSMHIMAM85_30_adj + CNRMMAM85_30_adj + CNRMSMHIMAM85_30_adj + CSIROMAM85_30_adj + ICHECDMIMAM85_30_adj + ICHECCCLMMAM85_30_adj + ICHECKNMIMAM85_30_adj + ICHECMPIMAM85_30_adj + ICHECSMHIMAM85_30_adj + IPSLMAM85_30_adj + MIROCMAM85_30_adj + MOHCCCLMMAM85_30_adj + MOHCKNMIMAM85_30_adj + MOHCSMHIMAM85_30_adj + MPICCLMMAM85_30_adj + MPIREMOMAM85_30_adj + MPISMHIMAM85_30_adj + NCCSMHIMAM85_30_adj + NOAAMAM85_30_adj)/20.
    AverageJJA85_30 = (CCCmaCanRCMJJA85_30_adj + CCCmaSMHIJJA85_30_adj + CNRMJJA85_30_adj + CNRMSMHIJJA85_30_adj + CSIROJJA85_30_adj + ICHECDMIJJA85_30_adj + ICHECCCLMJJA85_30_adj + ICHECKNMIJJA85_30_adj + ICHECMPIJJA85_30_adj + ICHECSMHIJJA85_30_adj + IPSLJJA85_30_adj + MIROCJJA85_30_adj + MOHCCCLMJJA85_30_adj + MOHCKNMIJJA85_30_adj + MOHCSMHIJJA85_30_adj + MPICCLMJJA85_30_adj + MPIREMOJJA85_30_adj + MPISMHIJJA85_30_adj + NCCSMHIJJA85_30_adj + NOAAJJA85_30_adj)/20.
    Average85_30 = (CCCmaCanRCMYR85_30_adj + CCCmaSMHIYR85_30_adj + CNRMYR85_30_adj + CNRMSMHIYR85_30_adj + CSIROYR85_30_adj + ICHECDMIYR85_30_adj + ICHECCCLMYR85_30_adj + ICHECKNMIYR85_30_adj + ICHECMPIYR85_30_adj + ICHECSMHIYR85_30_adj + IPSLYR85_30_adj + MIROCYR85_30_adj + MOHCCCLMYR85_30_adj + MOHCKNMIYR85_30_adj + MOHCSMHIYR85_30_adj + MPICCLMYR85_30_adj + MPIREMOYR85_30_adj + MPISMHIYR85_30_adj + NCCSMHIYR85_30_adj + NOAAYR85_30_adj)/20.
    
    AverageSON_30_diff = (CCCmaCanRCMSON_30_diff + CCCmaSMHISON_30_diff + CNRMSON_30_diff + CNRMSMHISON_30_diff + CSIROSON_30_diff + ICHECDMISON_30_diff + ICHECCCLMSON_30_diff + ICHECKNMISON_30_diff + ICHECMPISON_30_diff + ICHECSMHISON_30_diff + IPSLSON_30_diff + MIROCSON_30_diff + MOHCCCLMSON_30_diff + MOHCKNMISON_30_diff + MOHCSMHISON_30_diff + MPICCLMSON_30_diff + MPIREMOSON_30_diff + MPISMHISON_30_diff + NCCSMHISON_30_diff + NOAASON_30_diff)/20.
    AverageDJF_30_diff = (CCCmaCanRCMDJF_30_diff + CCCmaSMHIDJF_30_diff + CNRMDJF_30_diff + CNRMSMHIDJF_30_diff + CSIRODJF_30_diff + ICHECDMIDJF_30_diff + ICHECCCLMDJF_30_diff + ICHECKNMIDJF_30_diff + ICHECMPIDJF_30_diff + ICHECSMHIDJF_30_diff + IPSLDJF_30_diff + MIROCDJF_30_diff + MOHCCCLMDJF_30_diff + MOHCKNMIDJF_30_diff + MOHCSMHIDJF_30_diff + MPICCLMDJF_30_diff + MPIREMODJF_30_diff + MPISMHIDJF_30_diff + NCCSMHIDJF_30_diff + NOAADJF_30_diff)/20.
    AverageMAM_30_diff = (CCCmaCanRCMMAM_30_diff + CCCmaSMHIMAM_30_diff + CNRMMAM_30_diff + CNRMSMHIMAM_30_diff + CSIROMAM_30_diff + ICHECDMIMAM_30_diff + ICHECCCLMMAM_30_diff + ICHECKNMIMAM_30_diff + ICHECMPIMAM_30_diff + ICHECSMHIMAM_30_diff + IPSLMAM_30_diff + MIROCMAM_30_diff + MOHCCCLMMAM_30_diff + MOHCKNMIMAM_30_diff + MOHCSMHIMAM_30_diff + MPICCLMMAM_30_diff + MPIREMOMAM_30_diff + MPISMHIMAM_30_diff + NCCSMHIMAM_30_diff + NOAAMAM_30_diff)/20.
    AverageJJA_30_diff = (CCCmaCanRCMJJA_30_diff + CCCmaSMHIJJA_30_diff + CNRMJJA_30_diff + CNRMSMHIJJA_30_diff + CSIROJJA_30_diff + ICHECDMIJJA_30_diff + ICHECCCLMJJA_30_diff + ICHECKNMIJJA_30_diff + ICHECMPIJJA_30_diff + ICHECSMHIJJA_30_diff + IPSLJJA_30_diff + MIROCJJA_30_diff + MOHCCCLMJJA_30_diff + MOHCKNMIJJA_30_diff + MOHCSMHIJJA_30_diff + MPICCLMJJA_30_diff + MPIREMOJJA_30_diff + MPISMHIJJA_30_diff + NCCSMHIJJA_30_diff + NOAAJJA_30_diff)/20.
    Average_30_diff = (CCCmaCanRCMYR_30_diff + CCCmaSMHIYR_30_diff + CNRMYR_30_diff + CNRMSMHIYR_30_diff + CSIROYR_30_diff + ICHECDMIYR_30_diff + ICHECCCLMYR_30_diff + ICHECKNMIYR_30_diff + ICHECMPIYR_30_diff + ICHECSMHIYR_30_diff + IPSLYR_30_diff + MIROCYR_30_diff + MOHCCCLMYR_30_diff + MOHCKNMIYR_30_diff + MOHCSMHIYR_30_diff + MPICCLMYR_30_diff + MPIREMOYR_30_diff + MPISMHIYR_30_diff + NCCSMHIYR_30_diff + NOAAYR_30_diff)/20.
    
    AverageSON85_30_diff = (CCCmaCanRCMSON85_30_diff + CCCmaSMHISON85_30_diff + CNRMSON85_30_diff + CNRMSMHISON85_30_diff + CSIROSON85_30_diff + ICHECDMISON85_30_diff + ICHECCCLMSON85_30_diff + ICHECKNMISON85_30_diff + ICHECMPISON85_30_diff + ICHECSMHISON85_30_diff + IPSLSON85_30_diff + MIROCSON85_30_diff + MOHCCCLMSON85_30_diff + MOHCKNMISON85_30_diff + MOHCSMHISON85_30_diff + MPICCLMSON85_30_diff + MPIREMOSON85_30_diff + MPISMHISON85_30_diff + NCCSMHISON85_30_diff + NOAASON85_30_diff)/20.
    AverageDJF85_30_diff = (CCCmaCanRCMDJF85_30_diff + CCCmaSMHIDJF85_30_diff + CNRMDJF85_30_diff + CNRMSMHIDJF85_30_diff + CSIRODJF85_30_diff + ICHECDMIDJF85_30_diff + ICHECCCLMDJF85_30_diff + ICHECKNMIDJF85_30_diff + ICHECMPIDJF85_30_diff + ICHECSMHIDJF85_30_diff + IPSLDJF85_30_diff + MIROCDJF85_30_diff + MOHCCCLMDJF85_30_diff + MOHCKNMIDJF85_30_diff + MOHCSMHIDJF85_30_diff + MPICCLMDJF85_30_diff + MPIREMODJF85_30_diff + MPISMHIDJF85_30_diff + NCCSMHIDJF85_30_diff + NOAADJF85_30_diff)/20.
    AverageMAM85_30_diff = (CCCmaCanRCMMAM85_30_diff + CCCmaSMHIMAM85_30_diff + CNRMMAM85_30_diff + CNRMSMHIMAM85_30_diff + CSIROMAM85_30_diff + ICHECDMIMAM85_30_diff + ICHECCCLMMAM85_30_diff + ICHECKNMIMAM85_30_diff + ICHECMPIMAM85_30_diff + ICHECSMHIMAM85_30_diff + IPSLMAM85_30_diff + MIROCMAM85_30_diff + MOHCCCLMMAM85_30_diff + MOHCKNMIMAM85_30_diff + MOHCSMHIMAM85_30_diff + MPICCLMMAM85_30_diff + MPIREMOMAM85_30_diff + MPISMHIMAM85_30_diff + NCCSMHIMAM85_30_diff + NOAAMAM85_30_diff)/20.
    AverageJJA85_30_diff = (CCCmaCanRCMJJA85_30_diff + CCCmaSMHIJJA85_30_diff + CNRMJJA85_30_diff + CNRMSMHIJJA85_30_diff + CSIROJJA85_30_diff + ICHECDMIJJA85_30_diff + ICHECCCLMJJA85_30_diff + ICHECKNMIJJA85_30_diff + ICHECMPIJJA85_30_diff + ICHECSMHIJJA85_30_diff + IPSLJJA85_30_diff + MIROCJJA85_30_diff + MOHCCCLMJJA85_30_diff + MOHCKNMIJJA85_30_diff + MOHCSMHIJJA85_30_diff + MPICCLMJJA85_30_diff + MPIREMOJJA85_30_diff + MPISMHIJJA85_30_diff + NCCSMHIJJA85_30_diff + NOAAJJA85_30_diff)/20.
    Average85_30_diff = (CCCmaCanRCMYR85_30_diff + CCCmaSMHIYR85_30_diff + CNRMYR85_30_diff + CNRMSMHIYR85_30_diff + CSIROYR85_30_diff + ICHECDMIYR85_30_diff + ICHECCCLMYR85_30_diff + ICHECKNMIYR85_30_diff + ICHECMPIYR85_30_diff + ICHECSMHIYR85_30_diff + IPSLYR85_30_diff + MIROCYR85_30_diff + MOHCCCLMYR85_30_diff + MOHCKNMIYR85_30_diff + MOHCSMHIYR85_30_diff + MPICCLMYR85_30_diff + MPIREMOYR85_30_diff + MPISMHIYR85_30_diff + NCCSMHIYR85_30_diff + NOAAYR85_30_diff)/20.
    
    
    #-------------------------------------------------------------------------
    #PART 5C: 2050 FORMATING
    #time constraint to make all series the same (2040-2069)
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_50 = iris.Constraint(time=lambda cell: 2040 <= cell.point.year <= 2069)

    CCCmaCanRCMSON_50 = CCCmaCanRCMSON.extract(t_constraint_50)
    CCCmaSMHISON_50 = CCCmaSMHISON.extract(t_constraint_50)
    CNRMSON_50 =CNRMSON.extract(t_constraint_50)
    CNRMSMHISON_50 =CNRMSMHISON.extract(t_constraint_50)
    CSIROSON_50 =CSIROSON.extract(t_constraint_50)
    ICHECDMISON_50 =ICHECDMISON.extract(t_constraint_50)
    ICHECCCLMSON_50 =ICHECCCLMSON.extract(t_constraint_50)
    ICHECKNMISON_50 =ICHECKNMISON.extract(t_constraint_50)
    ICHECMPISON_50 =ICHECMPISON.extract(t_constraint_50)
    ICHECSMHISON_50 =ICHECSMHISON.extract(t_constraint_50)
    IPSLSON_50 =IPSLSON.extract(t_constraint_50)
    MIROCSON_50 =MIROCSON.extract(t_constraint_50)
    MOHCCCLMSON_50 =MOHCCCLMSON.extract(t_constraint_50)
    MOHCKNMISON_50 =MOHCKNMISON.extract(t_constraint_50)
    MOHCSMHISON_50 =MOHCSMHISON.extract(t_constraint_50)
    MPICCLMSON_50 =MPICCLMSON.extract(t_constraint_50)
    MPIREMOSON_50 =MPIREMOSON.extract(t_constraint_50)
    MPISMHISON_50 =MPISMHISON.extract(t_constraint_50)
    NCCSMHISON_50 =NCCSMHISON.extract(t_constraint_50)
    NOAASON_50 =NOAASON.extract(t_constraint_50) 
    
    CCCmaCanRCMSON85_50 = CCCmaCanRCMSON85.extract(t_constraint_50)
    CCCmaSMHISON85_50 =  CCCmaSMHISON85.extract(t_constraint_50)
    CNRMSON85_50 = CNRMSON85.extract(t_constraint_50)
    CNRMSMHISON85_50 = CNRMSMHISON85.extract(t_constraint_50)
    CSIROSON85_50 = CSIROSON85.extract(t_constraint_50)
    ICHECDMISON85_50 = ICHECDMISON85.extract(t_constraint_50)
    ICHECCCLMSON85_50 = ICHECCCLMSON85.extract(t_constraint_50)
    ICHECKNMISON85_50 = ICHECKNMISON85.extract(t_constraint_50)
    ICHECMPISON85_50 = ICHECMPISON85.extract(t_constraint_50)
    ICHECSMHISON85_50 = ICHECSMHISON85.extract(t_constraint_50)
    IPSLSON85_50 = IPSLSON85.extract(t_constraint_50)
    MIROCSON85_50 = MIROCSON85.extract(t_constraint_50)
    MOHCCCLMSON85_50 = MOHCCCLMSON85.extract(t_constraint_50)
    MOHCKNMISON85_50 = MOHCKNMISON85.extract(t_constraint_50)
    MOHCSMHISON85_50 = MOHCSMHISON85.extract(t_constraint_50)
    MPICCLMSON85_50 = MPICCLMSON85.extract(t_constraint_50)
    MPIREMOSON85_50 = MPIREMOSON85.extract(t_constraint_50)
    MPISMHISON85_50 = MPISMHISON85.extract(t_constraint_50)
    NCCSMHISON85_50 = NCCSMHISON85.extract(t_constraint_50)
    NOAASON85_50 =NOAASON85.extract(t_constraint_50) 
    
    CCCmaCanRCMDJF_50 = CCCmaCanRCMDJF.extract(t_constraint_50)
    CCCmaSMHIDJF_50 = CCCmaSMHIDJF.extract(t_constraint_50)
    CNRMDJF_50 =CNRMDJF.extract(t_constraint_50)
    CNRMSMHIDJF_50 =CNRMSMHIDJF.extract(t_constraint_50)
    CSIRODJF_50 =CSIRODJF.extract(t_constraint_50)
    ICHECDMIDJF_50 =ICHECDMIDJF.extract(t_constraint_50)
    ICHECCCLMDJF_50 =ICHECCCLMDJF.extract(t_constraint_50)
    ICHECKNMIDJF_50 =ICHECKNMIDJF.extract(t_constraint_50)
    ICHECMPIDJF_50 =ICHECMPIDJF.extract(t_constraint_50)
    ICHECSMHIDJF_50 =ICHECSMHIDJF.extract(t_constraint_50)
    IPSLDJF_50 =IPSLDJF.extract(t_constraint_50)
    MIROCDJF_50 =MIROCDJF.extract(t_constraint_50)
    MOHCCCLMDJF_50 =MOHCCCLMDJF.extract(t_constraint_50)
    MOHCKNMIDJF_50 =MOHCKNMIDJF.extract(t_constraint_50)
    MOHCSMHIDJF_50 =MOHCSMHIDJF.extract(t_constraint_50)
    MPICCLMDJF_50 =MPICCLMDJF.extract(t_constraint_50)
    MPIREMODJF_50 =MPIREMODJF.extract(t_constraint_50)
    MPISMHIDJF_50 =MPISMHIDJF.extract(t_constraint_50)
    NCCSMHIDJF_50 =NCCSMHIDJF.extract(t_constraint_50)
    NOAADJF_50 =NOAADJF.extract(t_constraint_50) 
    
    CCCmaCanRCMDJF85_50 = CCCmaCanRCMDJF85.extract(t_constraint_50)
    CCCmaSMHIDJF85_50 =  CCCmaSMHIDJF85.extract(t_constraint_50)
    CNRMDJF85_50 = CNRMDJF85.extract(t_constraint_50)
    CNRMSMHIDJF85_50 = CNRMSMHIDJF85.extract(t_constraint_50)
    CSIRODJF85_50 = CSIRODJF85.extract(t_constraint_50)
    ICHECDMIDJF85_50 = ICHECDMIDJF85.extract(t_constraint_50)
    ICHECCCLMDJF85_50 = ICHECCCLMDJF85.extract(t_constraint_50)
    ICHECKNMIDJF85_50 = ICHECKNMIDJF85.extract(t_constraint_50)
    ICHECMPIDJF85_50 = ICHECMPIDJF85.extract(t_constraint_50)
    ICHECSMHIDJF85_50 = ICHECSMHIDJF85.extract(t_constraint_50)
    IPSLDJF85_50 = IPSLDJF85.extract(t_constraint_50)
    MIROCDJF85_50 = MIROCDJF85.extract(t_constraint_50)
    MOHCCCLMDJF85_50 = MOHCCCLMDJF85.extract(t_constraint_50)
    MOHCKNMIDJF85_50 = MOHCKNMIDJF85.extract(t_constraint_50)
    MOHCSMHIDJF85_50 = MOHCSMHIDJF85.extract(t_constraint_50)
    MPICCLMDJF85_50 = MPICCLMDJF85.extract(t_constraint_50)
    MPIREMODJF85_50 = MPIREMODJF85.extract(t_constraint_50)
    MPISMHIDJF85_50 = MPISMHIDJF85.extract(t_constraint_50)
    NCCSMHIDJF85_50 = NCCSMHIDJF85.extract(t_constraint_50)
    NOAADJF85_50 =NOAADJF85.extract(t_constraint_50) 
    
    CCCmaCanRCMMAM_50 =  CCCmaCanRCMMAM.extract(t_constraint_50)
    CCCmaSMHIMAM_50 =  CCCmaSMHIMAM.extract(t_constraint_50)
    CNRMMAM_50 = CNRMMAM.extract(t_constraint_50)
    CNRMSMHIMAM_50 = CNRMSMHIMAM.extract(t_constraint_50)
    CSIROMAM_50 = CSIROMAM.extract(t_constraint_50)
    ICHECDMIMAM_50 = ICHECDMIMAM.extract(t_constraint_50)
    ICHECCCLMMAM_50 = ICHECCCLMMAM.extract(t_constraint_50)
    ICHECKNMIMAM_50 = ICHECKNMIMAM.extract(t_constraint_50)
    ICHECMPIMAM_50 = ICHECMPIMAM.extract(t_constraint_50)
    ICHECSMHIMAM_50 = ICHECSMHIMAM.extract(t_constraint_50)
    IPSLMAM_50 = IPSLMAM.extract(t_constraint_50)
    MIROCMAM_50 = MIROCMAM.extract(t_constraint_50)
    MOHCCCLMMAM_50 = MOHCCCLMMAM.extract(t_constraint_50)
    MOHCKNMIMAM_50 = MOHCKNMIMAM.extract(t_constraint_50)
    MOHCSMHIMAM_50 = MOHCSMHIMAM.extract(t_constraint_50)
    MPICCLMMAM_50 = MPICCLMMAM.extract(t_constraint_50)
    MPIREMOMAM_50 = MPIREMOMAM.extract(t_constraint_50)
    MPISMHIMAM_50 = MPISMHIMAM.extract(t_constraint_50)
    NCCSMHIMAM_50 = NCCSMHIMAM.extract(t_constraint_50)
    NOAAMAM_50 = NOAAMAM.extract(t_constraint_50) 
    
    CCCmaCanRCMMAM85_50 = CCCmaCanRCMMAM85.extract(t_constraint_50)
    CCCmaSMHIMAM85_50 =  CCCmaSMHIMAM85.extract(t_constraint_50)
    CNRMMAM85_50 = CNRMMAM85.extract(t_constraint_50)
    CNRMSMHIMAM85_50 = CNRMSMHIMAM85.extract(t_constraint_50)
    CSIROMAM85_50 = CSIROMAM85.extract(t_constraint_50)
    ICHECDMIMAM85_50 = ICHECDMIMAM85.extract(t_constraint_50)
    ICHECCCLMMAM85_50 = ICHECCCLMMAM85.extract(t_constraint_50)
    ICHECKNMIMAM85_50 = ICHECKNMIMAM85.extract(t_constraint_50)
    ICHECMPIMAM85_50 = ICHECMPIMAM85.extract(t_constraint_50)
    ICHECSMHIMAM85_50 = ICHECSMHIMAM85.extract(t_constraint_50)
    IPSLMAM85_50 = IPSLMAM85.extract(t_constraint_50)
    MIROCMAM85_50 = MIROCMAM85.extract(t_constraint_50)
    MOHCCCLMMAM85_50 = MOHCCCLMMAM85.extract(t_constraint_50)
    MOHCKNMIMAM85_50 = MOHCKNMIMAM85.extract(t_constraint_50)
    MOHCSMHIMAM85_50 = MOHCSMHIMAM85.extract(t_constraint_50)
    MPICCLMMAM85_50 = MPICCLMMAM85.extract(t_constraint_50)
    MPIREMOMAM85_50 = MPIREMOMAM85.extract(t_constraint_50)
    MPISMHIMAM85_50 = MPISMHIMAM85.extract(t_constraint_50)
    NCCSMHIMAM85_50 = NCCSMHIMAM85.extract(t_constraint_50)
    NOAAMAM85_50 =NOAAMAM85.extract(t_constraint_50) 
    
    CCCmaCanRCMJJA_50 =  CCCmaCanRCMJJA.extract(t_constraint_50)
    CCCmaSMHIJJA_50 =  CCCmaSMHIJJA.extract(t_constraint_50)
    CNRMJJA_50 = CNRMJJA.extract(t_constraint_50)
    CNRMSMHIJJA_50 = CNRMSMHIJJA.extract(t_constraint_50)
    CSIROJJA_50 = CSIROJJA.extract(t_constraint_50)
    ICHECDMIJJA_50 = ICHECDMIJJA.extract(t_constraint_50)
    ICHECCCLMJJA_50 = ICHECCCLMJJA.extract(t_constraint_50)
    ICHECKNMIJJA_50 = ICHECKNMIJJA.extract(t_constraint_50)
    ICHECMPIJJA_50 = ICHECMPIJJA.extract(t_constraint_50)
    ICHECSMHIJJA_50 = ICHECSMHIJJA.extract(t_constraint_50)
    IPSLJJA_50 = IPSLJJA.extract(t_constraint_50)
    MIROCJJA_50 = MIROCJJA.extract(t_constraint_50)
    MOHCCCLMJJA_50 = MOHCCCLMJJA.extract(t_constraint_50)
    MOHCKNMIJJA_50 = MOHCKNMIJJA.extract(t_constraint_50)
    MOHCSMHIJJA_50 = MOHCSMHIJJA.extract(t_constraint_50)
    MPICCLMJJA_50 = MPICCLMJJA.extract(t_constraint_50)
    MPIREMOJJA_50 = MPIREMOJJA.extract(t_constraint_50)
    MPISMHIJJA_50 = MPISMHIJJA.extract(t_constraint_50)
    NCCSMHIJJA_50 = NCCSMHIJJA.extract(t_constraint_50)
    NOAAJJA_50 = NOAAJJA.extract(t_constraint_50) 
    
    CCCmaCanRCMJJA85_50 = CCCmaCanRCMJJA85.extract(t_constraint_50)
    CCCmaSMHIJJA85_50 =  CCCmaSMHIJJA85.extract(t_constraint_50)
    CNRMJJA85_50 = CNRMJJA85.extract(t_constraint_50)
    CNRMSMHIJJA85_50 = CNRMSMHIJJA85.extract(t_constraint_50)
    CSIROJJA85_50 = CSIROJJA85.extract(t_constraint_50)
    ICHECDMIJJA85_50 = ICHECDMIJJA85.extract(t_constraint_50)
    ICHECCCLMJJA85_50 = ICHECCCLMJJA85.extract(t_constraint_50)
    ICHECKNMIJJA85_50 = ICHECKNMIJJA85.extract(t_constraint_50)
    ICHECMPIJJA85_50 = ICHECMPIJJA85.extract(t_constraint_50)
    ICHECSMHIJJA85_50 = ICHECSMHIJJA85.extract(t_constraint_50)
    IPSLJJA85_50 = IPSLJJA85.extract(t_constraint_50)
    MIROCJJA85_50 = MIROCJJA85.extract(t_constraint_50)
    MOHCCCLMJJA85_50 = MOHCCCLMJJA85.extract(t_constraint_50)
    MOHCKNMIJJA85_50 = MOHCKNMIJJA85.extract(t_constraint_50)
    MOHCSMHIJJA85_50 = MOHCSMHIJJA85.extract(t_constraint_50)
    MPICCLMJJA85_50 = MPICCLMJJA85.extract(t_constraint_50)
    MPIREMOJJA85_50 = MPIREMOJJA85.extract(t_constraint_50)
    MPISMHIJJA85_50 = MPISMHIJJA85.extract(t_constraint_50)
    NCCSMHIJJA85_50 = NCCSMHIJJA85.extract(t_constraint_50)
    NOAAJJA85_50 =NOAAJJA85.extract(t_constraint_50) 
    
    CCCmaCanRCM_50 =  CCCmaCanRCM.extract(t_constraint_50)
    CCCmaSMHI_50 =  CCCmaSMHI.extract(t_constraint_50)
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
    CCCmaSMHI85_50 =  CCCmaSMHI85.extract(t_constraint_50)
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
    NOAA85_50 =NOAA85.extract(t_constraint_50) 
    
    #We are interested in plotting the data for the average of the time period. 
    CCCmaCanRCMSON_50 = CCCmaCanRCMSON_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHISON_50 = CCCmaSMHISON_50.collapsed('year', iris.analysis.MEAN)
    CNRMSON_50 = CNRMSON_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHISON_50 = CNRMSMHISON_50.collapsed('year', iris.analysis.MEAN)
    CSIROSON_50 = CSIROSON_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMISON_50 = ICHECDMISON_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMSON_50 = ICHECCCLMSON_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMISON_50 = ICHECKNMISON_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPISON_50 = ICHECMPISON_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHISON_50 = ICHECSMHISON_50.collapsed('year', iris.analysis.MEAN)
    IPSLSON_50 = IPSLSON_50.collapsed('year', iris.analysis.MEAN)
    MIROCSON_50 = MIROCSON_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMSON_50 = MOHCCCLMSON_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMISON_50 = MOHCKNMISON_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHISON_50 = MOHCSMHISON_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMSON_50 = MPICCLMSON_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOSON_50 = MPIREMOSON_50.collapsed('year', iris.analysis.MEAN)
    MPISMHISON_50 = MPISMHISON_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHISON_50 = NCCSMHISON_50.collapsed('year', iris.analysis.MEAN)
    NOAASON_50 = NOAASON_50.collapsed('year', iris.analysis.MEAN)
  
    CCCmaCanRCMDJF_50 = CCCmaCanRCMDJF_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIDJF_50 = CCCmaSMHIDJF_50.collapsed('year', iris.analysis.MEAN)
    CNRMDJF_50 = CNRMDJF_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIDJF_50 = CNRMSMHIDJF_50.collapsed('year', iris.analysis.MEAN)
    CSIRODJF_50 = CSIRODJF_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIDJF_50 = ICHECDMIDJF_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMDJF_50 = ICHECCCLMDJF_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIDJF_50 = ICHECKNMIDJF_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIDJF_50 = ICHECMPIDJF_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIDJF_50 = ICHECSMHIDJF_50.collapsed('year', iris.analysis.MEAN)
    IPSLDJF_50 = IPSLDJF_50.collapsed('year', iris.analysis.MEAN)
    MIROCDJF_50 = MIROCDJF_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMDJF_50 = MOHCCCLMDJF_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIDJF_50 = MOHCKNMIDJF_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIDJF_50 = MOHCSMHIDJF_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMDJF_50 = MPICCLMDJF_50.collapsed('year', iris.analysis.MEAN)
    MPIREMODJF_50 = MPIREMODJF_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIDJF_50 = MPISMHIDJF_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIDJF_50 = NCCSMHIDJF_50.collapsed('year', iris.analysis.MEAN)
    NOAADJF_50 = NOAADJF_50.collapsed('year', iris.analysis.MEAN)
   
    CCCmaCanRCMMAM_50 = CCCmaCanRCMMAM_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIMAM_50 = CCCmaSMHIMAM_50.collapsed('year', iris.analysis.MEAN)
    CNRMMAM_50 = CNRMMAM_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIMAM_50 = CNRMSMHIMAM_50.collapsed('year', iris.analysis.MEAN)
    CSIROMAM_50 = CSIROMAM_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIMAM_50 = ICHECDMIMAM_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMMAM_50 = ICHECCCLMMAM_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIMAM_50 = ICHECKNMIMAM_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIMAM_50 = ICHECMPIMAM_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIMAM_50 = ICHECSMHIMAM_50.collapsed('year', iris.analysis.MEAN)
    IPSLMAM_50 = IPSLMAM_50.collapsed('year', iris.analysis.MEAN)
    MIROCMAM_50 = MIROCMAM_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMMAM_50 = MOHCCCLMMAM_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIMAM_50 = MOHCKNMIMAM_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIMAM_50 = MOHCSMHIMAM_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMMAM_50 = MPICCLMMAM_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOMAM_50 = MPIREMOMAM_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIMAM_50 = MPISMHIMAM_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIMAM_50 = NCCSMHIMAM_50.collapsed('year', iris.analysis.MEAN)
    NOAAMAM_50 = NOAAMAM_50.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMJJA_50 = CCCmaCanRCMJJA_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIJJA_50 = CCCmaSMHIJJA_50.collapsed('year', iris.analysis.MEAN)
    CNRMJJA_50 = CNRMJJA_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIJJA_50 = CNRMSMHIJJA_50.collapsed('year', iris.analysis.MEAN)
    CSIROJJA_50 = CSIROJJA_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIJJA_50 = ICHECDMIJJA_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMJJA_50 = ICHECCCLMJJA_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIJJA_50 = ICHECKNMIJJA_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIJJA_50 = ICHECMPIJJA_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIJJA_50 = ICHECSMHIJJA_50.collapsed('year', iris.analysis.MEAN)
    IPSLJJA_50 = IPSLJJA_50.collapsed('year', iris.analysis.MEAN)
    MIROCJJA_50 = MIROCJJA_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMJJA_50 = MOHCCCLMJJA_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIJJA_50 = MOHCKNMIJJA_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIJJA_50 = MOHCSMHIJJA_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMJJA_50 = MPICCLMJJA_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOJJA_50 = MPIREMOJJA_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIJJA_50 = MPISMHIJJA_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIJJA_50 = NCCSMHIJJA_50.collapsed('year', iris.analysis.MEAN)
    NOAAJJA_50 = NOAAJJA_50.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMYR_50 = CCCmaCanRCM_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIYR_50 = CCCmaSMHI_50.collapsed('year', iris.analysis.MEAN)
    CNRMYR_50 = CNRM_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIYR_50 = CNRMSMHI_50.collapsed('year', iris.analysis.MEAN)
    CSIROYR_50 = CSIRO_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIYR_50 = ICHECDMI_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMYR_50 = ICHECCCLM_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIYR_50 = ICHECKNMI_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIYR_50 = ICHECMPI_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIYR_50 = ICHECSMHI_50.collapsed('year', iris.analysis.MEAN)
    IPSLYR_50 = IPSL_50.collapsed('year', iris.analysis.MEAN)
    MIROCYR_50 = MIROC_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMYR_50 = MOHCCCLM_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIYR_50 = MOHCKNMI_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIYR_50 = MOHCSMHI_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMYR_50 = MPICCLM_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOYR_50 = MPIREMO_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIYR_50 = MPISMHI_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIYR_50 = NCCSMHI_50.collapsed('year', iris.analysis.MEAN)
    NOAAYR_50 = NOAA_50.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMSON85_50 = CCCmaCanRCMSON85_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHISON85_50 = CCCmaSMHISON85_50.collapsed('year', iris.analysis.MEAN)
    CNRMSON85_50 = CNRMSON85_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHISON85_50 = CNRMSMHISON85_50.collapsed('year', iris.analysis.MEAN)
    CSIROSON85_50 = CSIROSON85_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMISON85_50 = ICHECDMISON85_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMSON85_50 = ICHECCCLMSON85_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMISON85_50 = ICHECKNMISON85_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPISON85_50 = ICHECMPISON85_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHISON85_50 = ICHECSMHISON85_50.collapsed('year', iris.analysis.MEAN)
    IPSLSON85_50 = IPSLSON85_50.collapsed('year', iris.analysis.MEAN)
    MIROCSON85_50 = MIROCSON85_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMSON85_50 = MOHCCCLMSON85_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMISON85_50 = MOHCKNMISON85_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHISON85_50 = MOHCSMHISON85_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMSON85_50 = MPICCLMSON85_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOSON85_50 = MPIREMOSON85_50.collapsed('year', iris.analysis.MEAN)
    MPISMHISON85_50 = MPISMHISON85_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHISON85_50 = NCCSMHISON85_50.collapsed('year', iris.analysis.MEAN)
    NOAASON85_50 = NOAASON85_50.collapsed('year', iris.analysis.MEAN)
  
    CCCmaCanRCMDJF85_50 = CCCmaCanRCMDJF85_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIDJF85_50 = CCCmaSMHIDJF85_50.collapsed('year', iris.analysis.MEAN)
    CNRMDJF85_50 = CNRMDJF85_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIDJF85_50 = CNRMSMHIDJF85_50.collapsed('year', iris.analysis.MEAN)
    CSIRODJF85_50 = CSIRODJF85_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIDJF85_50 = ICHECDMIDJF85_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMDJF85_50 = ICHECCCLMDJF85_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIDJF85_50 = ICHECKNMIDJF85_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIDJF85_50 = ICHECMPIDJF85_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIDJF85_50 = ICHECSMHIDJF85_50.collapsed('year', iris.analysis.MEAN)
    IPSLDJF85_50 = IPSLDJF85_50.collapsed('year', iris.analysis.MEAN)
    MIROCDJF85_50 = MIROCDJF85_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMDJF85_50 = MOHCCCLMDJF85_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIDJF85_50 = MOHCKNMIDJF85_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIDJF85_50 = MOHCSMHIDJF85_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMDJF85_50 = MPICCLMDJF85_50.collapsed('year', iris.analysis.MEAN)
    MPIREMODJF85_50 = MPIREMODJF85_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIDJF85_50 = MPISMHIDJF85_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIDJF85_50 = NCCSMHIDJF85_50.collapsed('year', iris.analysis.MEAN)
    NOAADJF85_50 = NOAADJF85_50.collapsed('year', iris.analysis.MEAN)
   
    CCCmaCanRCMMAM85_50 = CCCmaCanRCMMAM85_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIMAM85_50 = CCCmaSMHIMAM85_50.collapsed('year', iris.analysis.MEAN)
    CNRMMAM85_50 = CNRMMAM85_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIMAM85_50 = CNRMSMHIMAM85_50.collapsed('year', iris.analysis.MEAN)
    CSIROMAM85_50 = CSIROMAM85_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIMAM85_50 = ICHECDMIMAM85_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMMAM85_50 = ICHECCCLMMAM85_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIMAM85_50 = ICHECKNMIMAM85_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIMAM85_50 = ICHECMPIMAM85_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIMAM85_50 = ICHECSMHIMAM85_50.collapsed('year', iris.analysis.MEAN)
    IPSLMAM85_50 = IPSLMAM85_50.collapsed('year', iris.analysis.MEAN)
    MIROCMAM85_50 = MIROCMAM85_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMMAM85_50 = MOHCCCLMMAM85_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIMAM85_50 = MOHCKNMIMAM85_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIMAM85_50 = MOHCSMHIMAM85_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMMAM85_50 = MPICCLMMAM85_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOMAM85_50 = MPIREMOMAM85_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIMAM85_50 = MPISMHIMAM85_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIMAM85_50 = NCCSMHIMAM85_50.collapsed('year', iris.analysis.MEAN)
    NOAAMAM85_50 = NOAAMAM85_50.collapsed('year', iris.analysis.MEAN)
   
    CCCmaCanRCMJJA85_50 = CCCmaCanRCMJJA85_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIJJA85_50 = CCCmaSMHIJJA85_50.collapsed('year', iris.analysis.MEAN)
    CNRMJJA85_50 = CNRMJJA85_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIJJA85_50 = CNRMSMHIJJA85_50.collapsed('year', iris.analysis.MEAN)
    CSIROJJA85_50 = CSIROJJA85_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIJJA85_50 = ICHECDMIJJA85_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMJJA85_50 = ICHECCCLMJJA85_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIJJA85_50 = ICHECKNMIJJA85_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIJJA85_50 = ICHECMPIJJA85_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIJJA85_50 = ICHECSMHIJJA85_50.collapsed('year', iris.analysis.MEAN)
    IPSLJJA85_50 = IPSLJJA85_50.collapsed('year', iris.analysis.MEAN)
    MIROCJJA85_50 = MIROCJJA85_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMJJA85_50 = MOHCCCLMJJA85_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIJJA85_50 = MOHCKNMIJJA85_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIJJA85_50 = MOHCSMHIJJA85_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMJJA85_50 = MPICCLMJJA85_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOJJA85_50 = MPIREMOJJA85_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIJJA85_50 = MPISMHIJJA85_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIJJA85_50 = NCCSMHIJJA85_50.collapsed('year', iris.analysis.MEAN)
    NOAAJJA85_50 = NOAAJJA85_50.collapsed('year', iris.analysis.MEAN)
    
    CCCmaCanRCMYR85_50 = CCCmaCanRCM85_50.collapsed('year', iris.analysis.MEAN)
    CCCmaSMHIYR85_50 = CCCmaSMHI85_50.collapsed('year', iris.analysis.MEAN)
    CNRMYR85_50 = CNRM85_50.collapsed('year', iris.analysis.MEAN)
    CNRMSMHIYR85_50 = CNRMSMHI85_50.collapsed('year', iris.analysis.MEAN)
    CSIROYR85_50 = CSIRO85_50.collapsed('year', iris.analysis.MEAN)
    ICHECDMIYR85_50 = ICHECDMI85_50.collapsed('year', iris.analysis.MEAN)
    ICHECCCLMYR85_50 = ICHECCCLM85_50.collapsed('year', iris.analysis.MEAN)
    ICHECKNMIYR85_50 = ICHECKNMI85_50.collapsed('year', iris.analysis.MEAN)
    ICHECMPIYR85_50 = ICHECMPI85_50.collapsed('year', iris.analysis.MEAN)
    ICHECSMHIYR85_50 = ICHECSMHI85_50.collapsed('year', iris.analysis.MEAN)
    IPSLYR85_50 = IPSL85_50.collapsed('year', iris.analysis.MEAN)
    MIROCYR85_50 = MIROC85_50.collapsed('year', iris.analysis.MEAN)
    MOHCCCLMYR85_50 = MOHCCCLM85_50.collapsed('year', iris.analysis.MEAN)
    MOHCKNMIYR85_50 = MOHCKNMI85_50.collapsed('year', iris.analysis.MEAN)
    MOHCSMHIYR85_50 = MOHCSMHI85_50.collapsed('year', iris.analysis.MEAN)
    MPICCLMYR85_50 = MPICCLM85_50.collapsed('year', iris.analysis.MEAN)
    MPIREMOYR85_50 = MPIREMO85_50.collapsed('year', iris.analysis.MEAN)
    MPISMHIYR85_50 = MPISMHI85_50.collapsed('year', iris.analysis.MEAN)
    NCCSMHIYR85_50 = NCCSMHI85_50.collapsed('year', iris.analysis.MEAN)
    NOAAYR85_50 = NOAA85_50.collapsed('year', iris.analysis.MEAN)
       
    #make units match, they already do but the name of the units doesn't. 
    CCCmaCanRCMSON_50.units = Unit('Celsius')
    CCCmaSMHISON_50.units = Unit('Celsius')
    CNRMSON_50.units = Unit('Celsius')
    CNRMSMHISON_50.units = Unit('Celsius')
    CSIROSON_50.units = Unit('Celsius')
    ICHECDMISON_50.units = Unit('Celsius')
    ICHECCCLMSON_50.units = Unit('Celsius')
    ICHECKNMISON_50.units = Unit('Celsius')
    ICHECMPISON_50.units = Unit('Celsius')
    ICHECSMHISON_50.units = Unit('Celsius')
    IPSLSON_50.units = Unit('Celsius')
    MIROCSON_50.units = Unit('Celsius')
    MOHCCCLMSON_50.units = Unit('Celsius')
    MOHCKNMISON_50.units = Unit('Celsius')
    MOHCSMHISON_50.units = Unit('Celsius')
    MPICCLMSON_50.units = Unit('Celsius')
    MPIREMOSON_50.units = Unit('Celsius')
    MPISMHISON_50.units = Unit('Celsius')
    NCCSMHISON_50.units = Unit('Celsius')
    NOAASON_50.units = Unit('Celsius')
 
    CCCmaCanRCMDJF_50.units = Unit('Celsius')
    CCCmaSMHIDJF_50.units = Unit('Celsius')
    CNRMDJF_50.units = Unit('Celsius')
    CNRMSMHIDJF_50.units = Unit('Celsius')
    CSIRODJF_50.units = Unit('Celsius')
    ICHECDMIDJF_50.units = Unit('Celsius')
    ICHECCCLMDJF_50.units = Unit('Celsius')
    ICHECKNMIDJF_50.units = Unit('Celsius')
    ICHECMPIDJF_50.units = Unit('Celsius')
    ICHECSMHIDJF_50.units = Unit('Celsius')
    IPSLDJF_50.units = Unit('Celsius')
    MIROCDJF_50.units = Unit('Celsius')
    MOHCCCLMDJF_50.units = Unit('Celsius')
    MOHCKNMIDJF_50.units = Unit('Celsius')
    MOHCSMHIDJF_50.units = Unit('Celsius')
    MPICCLMDJF_50.units = Unit('Celsius')
    MPIREMODJF_50.units = Unit('Celsius')
    MPISMHIDJF_50.units = Unit('Celsius')
    NCCSMHIDJF_50.units = Unit('Celsius')
    NOAADJF_50.units = Unit('Celsius')
    
    CCCmaCanRCMMAM_50.units = Unit('Celsius')
    CCCmaSMHIMAM_50.units = Unit('Celsius')
    CNRMMAM_50.units = Unit('Celsius')
    CNRMSMHIMAM_50.units = Unit('Celsius')
    CSIROMAM_50.units = Unit('Celsius')
    ICHECDMIMAM_50.units = Unit('Celsius')
    ICHECCCLMMAM_50.units = Unit('Celsius')
    ICHECKNMIMAM_50.units = Unit('Celsius')
    ICHECMPIMAM_50.units = Unit('Celsius')
    ICHECSMHIMAM_50.units = Unit('Celsius')
    IPSLMAM_50.units = Unit('Celsius')
    MIROCMAM_50.units = Unit('Celsius')
    MOHCCCLMMAM_50.units = Unit('Celsius')
    MOHCKNMIMAM_50.units = Unit('Celsius')
    MOHCSMHIMAM_50.units = Unit('Celsius')
    MPICCLMMAM_50.units = Unit('Celsius')
    MPIREMOMAM_50.units = Unit('Celsius')
    MPISMHIMAM_50.units = Unit('Celsius')
    NCCSMHIMAM_50.units = Unit('Celsius')
    NOAAMAM_50.units = Unit('Celsius')
    
    CCCmaCanRCMJJA_50.units = Unit('Celsius')
    CCCmaSMHIJJA_50.units = Unit('Celsius')
    CNRMJJA_50.units = Unit('Celsius')
    CNRMSMHIJJA_50.units = Unit('Celsius')
    CSIROJJA_50.units = Unit('Celsius')
    ICHECDMIJJA_50.units = Unit('Celsius')
    ICHECCCLMJJA_50.units = Unit('Celsius')
    ICHECKNMIJJA_50.units = Unit('Celsius')
    ICHECMPIJJA_50.units = Unit('Celsius')
    ICHECSMHIJJA_50.units = Unit('Celsius')
    IPSLJJA_50.units = Unit('Celsius')
    MIROCJJA_50.units = Unit('Celsius')
    MOHCCCLMJJA_50.units = Unit('Celsius')
    MOHCKNMIJJA_50.units = Unit('Celsius')
    MOHCSMHIJJA_50.units = Unit('Celsius')
    MPICCLMJJA_50.units = Unit('Celsius')
    MPIREMOJJA_50.units = Unit('Celsius')
    MPISMHIJJA_50.units = Unit('Celsius')
    NCCSMHIJJA_50.units = Unit('Celsius')
    NOAAJJA_50.units = Unit('Celsius')
    
    CCCmaCanRCMYR_50.units = Unit('Celsius')
    CCCmaSMHIYR_50.units = Unit('Celsius')
    CNRMYR_50.units = Unit('Celsius')
    CNRMSMHIYR_50.units = Unit('Celsius')
    CSIROYR_50.units = Unit('Celsius')
    ICHECDMIYR_50.units = Unit('Celsius')
    ICHECCCLMYR_50.units = Unit('Celsius')
    ICHECKNMIYR_50.units = Unit('Celsius')
    ICHECMPIYR_50.units = Unit('Celsius')
    ICHECSMHIYR_50.units = Unit('Celsius')
    IPSLYR_50.units = Unit('Celsius')
    MIROCYR_50.units = Unit('Celsius')
    MOHCCCLMYR_50.units = Unit('Celsius')
    MOHCKNMIYR_50.units = Unit('Celsius')
    MOHCSMHIYR_50.units = Unit('Celsius')
    MPICCLMYR_50.units = Unit('Celsius')
    MPIREMOYR_50.units = Unit('Celsius')
    MPISMHIYR_50.units = Unit('Celsius')
    NCCSMHIYR_50.units = Unit('Celsius')
    NOAAYR_50.units = Unit('Celsius')
    
    CCCmaCanRCMSON85_50.units = Unit('Celsius')
    CCCmaSMHISON85_50.units = Unit('Celsius')
    CNRMSON85_50.units = Unit('Celsius')
    CNRMSMHISON85_50.units = Unit('Celsius')
    CSIROSON85_50.units = Unit('Celsius')
    ICHECDMISON85_50.units = Unit('Celsius')
    ICHECCCLMSON85_50.units = Unit('Celsius')
    ICHECKNMISON85_50.units = Unit('Celsius')
    ICHECMPISON85_50.units = Unit('Celsius')
    ICHECSMHISON85_50.units = Unit('Celsius')
    IPSLSON85_50.units = Unit('Celsius')
    MIROCSON85_50.units = Unit('Celsius')
    MOHCCCLMSON85_50.units = Unit('Celsius')
    MOHCKNMISON85_50.units = Unit('Celsius')
    MOHCSMHISON85_50.units = Unit('Celsius')
    MPICCLMSON85_50.units = Unit('Celsius')
    MPIREMOSON85_50.units = Unit('Celsius')
    MPISMHISON85_50.units = Unit('Celsius')
    NCCSMHISON85_50.units = Unit('Celsius')
    NOAASON85_50.units = Unit('Celsius')
 
    CCCmaCanRCMDJF85_50.units = Unit('Celsius')
    CCCmaSMHIDJF85_50.units = Unit('Celsius')
    CNRMDJF85_50.units = Unit('Celsius')
    CNRMSMHIDJF85_50.units = Unit('Celsius')
    CSIRODJF85_50.units = Unit('Celsius')
    ICHECDMIDJF85_50.units = Unit('Celsius')
    ICHECCCLMDJF85_50.units = Unit('Celsius')
    ICHECKNMIDJF85_50.units = Unit('Celsius')
    ICHECMPIDJF85_50.units = Unit('Celsius')
    ICHECSMHIDJF85_50.units = Unit('Celsius')
    IPSLDJF85_50.units = Unit('Celsius')
    MIROCDJF85_50.units = Unit('Celsius')
    MOHCCCLMDJF85_50.units = Unit('Celsius')
    MOHCKNMIDJF85_50.units = Unit('Celsius')
    MOHCSMHIDJF85_50.units = Unit('Celsius')
    MPICCLMDJF85_50.units = Unit('Celsius')
    MPIREMODJF85_50.units = Unit('Celsius')
    MPISMHIDJF85_50.units = Unit('Celsius')
    NCCSMHIDJF85_50.units = Unit('Celsius')
    NOAADJF85_50.units = Unit('Celsius')
    
    CCCmaCanRCMMAM85_50.units = Unit('Celsius')
    CCCmaSMHIMAM85_50.units = Unit('Celsius')
    CNRMMAM85_50.units = Unit('Celsius')
    CNRMSMHIMAM85_50.units = Unit('Celsius')
    CSIROMAM85_50.units = Unit('Celsius')
    ICHECDMIMAM85_50.units = Unit('Celsius')
    ICHECCCLMMAM85_50.units = Unit('Celsius')
    ICHECKNMIMAM85_50.units = Unit('Celsius')
    ICHECMPIMAM85_50.units = Unit('Celsius')
    ICHECSMHIMAM85_50.units = Unit('Celsius')
    IPSLMAM85_50.units = Unit('Celsius')
    MIROCMAM85_50.units = Unit('Celsius')
    MOHCCCLMMAM85_50.units = Unit('Celsius')
    MOHCKNMIMAM85_50.units = Unit('Celsius')
    MOHCSMHIMAM85_50.units = Unit('Celsius')
    MPICCLMMAM85_50.units = Unit('Celsius')
    MPIREMOMAM85_50.units = Unit('Celsius')
    MPISMHIMAM85_50.units = Unit('Celsius')
    NCCSMHIMAM85_50.units = Unit('Celsius')
    NOAAMAM85_50.units = Unit('Celsius')
    
    CCCmaCanRCMJJA85_50.units = Unit('Celsius')
    CCCmaSMHIJJA85_50.units = Unit('Celsius')
    CNRMJJA85_50.units = Unit('Celsius')
    CNRMSMHIJJA85_50.units = Unit('Celsius')
    CSIROJJA85_50.units = Unit('Celsius')
    ICHECDMIJJA85_50.units = Unit('Celsius')
    ICHECCCLMJJA85_50.units = Unit('Celsius')
    ICHECKNMIJJA85_50.units = Unit('Celsius')
    ICHECMPIJJA85_50.units = Unit('Celsius')
    ICHECSMHIJJA85_50.units = Unit('Celsius')
    IPSLJJA85_50.units = Unit('Celsius')
    MIROCJJA85_50.units = Unit('Celsius')
    MOHCCCLMJJA85_50.units = Unit('Celsius')
    MOHCKNMIJJA85_50.units = Unit('Celsius')
    MOHCSMHIJJA85_50.units = Unit('Celsius')
    MPICCLMJJA85_50.units = Unit('Celsius')
    MPIREMOJJA85_50.units = Unit('Celsius')
    MPISMHIJJA85_50.units = Unit('Celsius')
    NCCSMHIJJA85_50.units = Unit('Celsius')
    NOAAJJA85_50.units = Unit('Celsius')
    
    CCCmaCanRCMYR85_50.units = Unit('Celsius')
    CCCmaSMHIYR85_50.units = Unit('Celsius')
    CNRMYR85_50.units = Unit('Celsius')
    CNRMSMHIYR85_50.units = Unit('Celsius')
    CSIROYR85_50.units = Unit('Celsius')
    ICHECDMIYR85_50.units = Unit('Celsius')
    ICHECCCLMYR85_50.units = Unit('Celsius')
    ICHECKNMIYR85_50.units = Unit('Celsius')
    ICHECMPIYR85_50.units = Unit('Celsius')
    ICHECSMHIYR85_50.units = Unit('Celsius')
    IPSLYR85_50.units = Unit('Celsius')
    MIROCYR85_50.units = Unit('Celsius')
    MOHCCCLMYR85_50.units = Unit('Celsius')
    MOHCKNMIYR85_50.units = Unit('Celsius')
    MOHCSMHIYR85_50.units = Unit('Celsius')
    MPICCLMYR85_50.units = Unit('Celsius')
    MPIREMOYR85_50.units = Unit('Celsius')
    MPISMHIYR85_50.units = Unit('Celsius')
    NCCSMHIYR85_50.units = Unit('Celsius')
    NOAAYR85_50.units = Unit('Celsius')
    
    #create change in temperature
    CCCmaCanRCMSON_50_diff = (CCCmaCanRCMSON_50 - CCCmaCanRCMSON_b)
    CCCmaSMHISON_50_diff = (CCCmaSMHISON_50 - CCCmaSMHISON_b)
    CNRMSON_50_diff = (CNRMSON_50 - CNRMSON_b)
    CNRMSMHISON_50_diff = (CNRMSMHISON_50 - CNRMSMHISON_b)  
    CSIROSON_50_diff = (CSIROSON_50 - CSIROSON_b)
    ICHECDMISON_50_diff = (ICHECDMISON_50 - ICHECDMISON_b) 
    ICHECCCLMSON_50_diff = (ICHECCCLMSON_50 - ICHECCCLMSON_b)
    ICHECKNMISON_50_diff = (ICHECKNMISON_50 - ICHECKNMISON_b)
    ICHECMPISON_50_diff = (ICHECMPISON_50 - ICHECMPISON_b)
    ICHECSMHISON_50_diff = (ICHECSMHISON_50 - ICHECSMHISON_b)
    IPSLSON_50_diff = (IPSLSON_50 - IPSLSON_b)
    MIROCSON_50_diff = (MIROCSON_50 - MIROCSON_b)
    MOHCCCLMSON_50_diff = (MOHCCCLMSON_50 - MOHCCCLMSON_b)
    MOHCKNMISON_50_diff = (MOHCKNMISON_50 - MOHCKNMISON_b)
    MOHCSMHISON_50_diff = (MOHCSMHISON_50 - MOHCSMHISON_b)
    MPICCLMSON_50_diff = (MPICCLMSON_50 - MPICCLMSON_b)      
    MPIREMOSON_50_diff = (MPIREMOSON_50 - MPIREMOSON_b)                         
    MPISMHISON_50_diff = (MPISMHISON_50 - MPISMHISON_b)
    NCCSMHISON_50_diff = (NCCSMHISON_50 - NCCSMHISON_b) 
    NOAASON_50_diff = (NOAASON_50 - NOAASON_b)
    
    CCCmaCanRCMDJF_50_diff = (CCCmaCanRCMDJF_50 - CCCmaCanRCMDJF_b)
    CCCmaSMHIDJF_50_diff = (CCCmaSMHIDJF_50 - CCCmaSMHIDJF_b)
    CNRMDJF_50_diff = (CNRMDJF_50 - CNRMDJF_b)
    CNRMSMHIDJF_50_diff = (CNRMSMHIDJF_50 - CNRMSMHIDJF_b)  
    CSIRODJF_50_diff = (CSIRODJF_50 - CSIRODJF_b)
    ICHECDMIDJF_50_diff = (ICHECDMIDJF_50 - ICHECDMIDJF_b) 
    ICHECCCLMDJF_50_diff = (ICHECCCLMDJF_50 - ICHECCCLMDJF_b)
    ICHECKNMIDJF_50_diff = (ICHECKNMIDJF_50 - ICHECKNMIDJF_b)
    ICHECMPIDJF_50_diff = (ICHECMPIDJF_50 - ICHECMPIDJF_b)
    ICHECSMHIDJF_50_diff = (ICHECSMHIDJF_50 - ICHECSMHIDJF_b)
    IPSLDJF_50_diff = (IPSLDJF_50 - IPSLDJF_b)
    MIROCDJF_50_diff = (MIROCDJF_50 - MIROCDJF_b)
    MOHCCCLMDJF_50_diff = (MOHCCCLMDJF_50 - MOHCCCLMDJF_b)
    MOHCKNMIDJF_50_diff = (MOHCKNMIDJF_50 - MOHCKNMIDJF_b)
    MOHCSMHIDJF_50_diff = (MOHCSMHIDJF_50 - MOHCSMHIDJF_b)
    MPICCLMDJF_50_diff = (MPICCLMDJF_50 - MPICCLMDJF_b)      
    MPIREMODJF_50_diff = (MPIREMODJF_50 - MPIREMODJF_b)                         
    MPISMHIDJF_50_diff = (MPISMHIDJF_50 - MPISMHIDJF_b)
    NCCSMHIDJF_50_diff = (NCCSMHIDJF_50 - NCCSMHIDJF_b) 
    NOAADJF_50_diff = (NOAADJF_50 - NOAADJF_b)
    
    CCCmaCanRCMMAM_50_diff = (CCCmaCanRCMMAM_50 - CCCmaCanRCMMAM_b)
    CCCmaSMHIMAM_50_diff = (CCCmaSMHIMAM_50 - CCCmaSMHIMAM_b)
    CNRMMAM_50_diff = (CNRMMAM_50 - CNRMMAM_b)
    CNRMSMHIMAM_50_diff = (CNRMSMHIMAM_50 - CNRMSMHIMAM_b)  
    CSIROMAM_50_diff = (CSIROMAM_50 - CSIROMAM_b)
    ICHECDMIMAM_50_diff = (ICHECDMIMAM_50 - ICHECDMIMAM_b) 
    ICHECCCLMMAM_50_diff = (ICHECCCLMMAM_50 - ICHECCCLMMAM_b)
    ICHECKNMIMAM_50_diff = (ICHECKNMIMAM_50 - ICHECKNMIMAM_b)
    ICHECMPIMAM_50_diff = (ICHECMPIMAM_50 - ICHECMPIMAM_b)
    ICHECSMHIMAM_50_diff = (ICHECSMHIMAM_50 - ICHECSMHIMAM_b)
    IPSLMAM_50_diff = (IPSLMAM_50 - IPSLMAM_b)
    MIROCMAM_50_diff = (MIROCMAM_50 - MIROCMAM_b)
    MOHCCCLMMAM_50_diff = (MOHCCCLMMAM_50 - MOHCCCLMMAM_b)
    MOHCKNMIMAM_50_diff = (MOHCKNMIMAM_50 - MOHCKNMIMAM_b)
    MOHCSMHIMAM_50_diff = (MOHCSMHIMAM_50 - MOHCSMHIMAM_b)
    MPICCLMMAM_50_diff = (MPICCLMMAM_50 - MPICCLMMAM_b)      
    MPIREMOMAM_50_diff = (MPIREMOMAM_50 - MPIREMOMAM_b)                         
    MPISMHIMAM_50_diff = (MPISMHIMAM_50 - MPISMHIMAM_b)
    NCCSMHIMAM_50_diff = (NCCSMHIMAM_50 - NCCSMHIMAM_b) 
    NOAAMAM_50_diff = (NOAAMAM_50 - NOAAMAM_b)
    
    CCCmaCanRCMJJA_50_diff = (CCCmaCanRCMJJA_50 - CCCmaCanRCMJJA_b)
    CCCmaSMHIJJA_50_diff = (CCCmaSMHIJJA_50 - CCCmaSMHIJJA_b)
    CNRMJJA_50_diff = (CNRMJJA_50 - CNRMJJA_b)
    CNRMSMHIJJA_50_diff = (CNRMSMHIJJA_50 - CNRMSMHIJJA_b)  
    CSIROJJA_50_diff = (CSIROJJA_50 - CSIROJJA_b)
    ICHECDMIJJA_50_diff = (ICHECDMIJJA_50 - ICHECDMIJJA_b) 
    ICHECCCLMJJA_50_diff = (ICHECCCLMJJA_50 - ICHECCCLMJJA_b)
    ICHECKNMIJJA_50_diff = (ICHECKNMIJJA_50 - ICHECKNMIJJA_b)
    ICHECMPIJJA_50_diff = (ICHECMPIJJA_50 - ICHECMPIJJA_b)
    ICHECSMHIJJA_50_diff = (ICHECSMHIJJA_50 - ICHECSMHIJJA_b)
    IPSLJJA_50_diff = (IPSLJJA_50 - IPSLJJA_b)
    MIROCJJA_50_diff = (MIROCJJA_50 - MIROCJJA_b)
    MOHCCCLMJJA_50_diff = (MOHCCCLMJJA_50 - MOHCCCLMJJA_b)
    MOHCKNMIJJA_50_diff = (MOHCKNMIJJA_50 - MOHCKNMIJJA_b)
    MOHCSMHIJJA_50_diff = (MOHCSMHIJJA_50 - MOHCSMHIJJA_b)
    MPICCLMJJA_50_diff = (MPICCLMJJA_50 - MPICCLMJJA_b)      
    MPIREMOJJA_50_diff = (MPIREMOJJA_50 - MPIREMOJJA_b)                         
    MPISMHIJJA_50_diff = (MPISMHIJJA_50 - MPISMHIJJA_b)
    NCCSMHIJJA_50_diff = (NCCSMHIJJA_50 - NCCSMHIJJA_b) 
    NOAAJJA_50_diff = (NOAAJJA_50 - NOAAJJA_b)
    
    CCCmaCanRCMYR_50_diff = (CCCmaCanRCMYR_50 - CCCmaCanRCMYR_b)
    CCCmaSMHIYR_50_diff = (CCCmaSMHIYR_50 - CCCmaSMHIYR_b)
    CNRMYR_50_diff = (CNRMYR_50 - CNRMYR_b)
    CNRMSMHIYR_50_diff = (CNRMSMHIYR_50 - CNRMSMHIYR_b)  
    CSIROYR_50_diff = (CSIROYR_50 - CSIROYR_b)
    ICHECDMIYR_50_diff = (ICHECDMIYR_50 - ICHECDMIYR_b) 
    ICHECCCLMYR_50_diff = (ICHECCCLMYR_50 - ICHECCCLMYR_b)
    ICHECKNMIYR_50_diff = (ICHECKNMIYR_50 - ICHECKNMIYR_b)
    ICHECMPIYR_50_diff = (ICHECMPIYR_50 - ICHECMPIYR_b)
    ICHECSMHIYR_50_diff = (ICHECSMHIYR_50 - ICHECSMHIYR_b)
    IPSLYR_50_diff = (IPSLYR_50 - IPSLYR_b)
    MIROCYR_50_diff = (MIROCYR_50 - MIROCYR_b)
    MOHCCCLMYR_50_diff = (MOHCCCLMYR_50 - MOHCCCLMYR_b)
    MOHCKNMIYR_50_diff = (MOHCKNMIYR_50 - MOHCKNMIYR_b)
    MOHCSMHIYR_50_diff = (MOHCSMHIYR_50 - MOHCSMHIYR_b)
    MPICCLMYR_50_diff = (MPICCLMYR_50 - MPICCLMYR_b)      
    MPIREMOYR_50_diff = (MPIREMOYR_50 - MPIREMOYR_b)                         
    MPISMHIYR_50_diff = (MPISMHIYR_50 - MPISMHIYR_b)
    NCCSMHIYR_50_diff = (NCCSMHIYR_50 - NCCSMHIYR_b) 
    NOAAYR_50_diff = (NOAAYR_50 - NOAAYR_b)
    
    CCCmaCanRCMSON85_50_diff = (CCCmaCanRCMSON85_50 - CCCmaCanRCMSON_b)
    CCCmaSMHISON85_50_diff = (CCCmaSMHISON85_50 - CCCmaSMHISON_b)
    CNRMSON85_50_diff = (CNRMSON85_50 - CNRMSON_b)
    CNRMSMHISON85_50_diff = (CNRMSMHISON85_50 - CNRMSMHISON_b)  
    CSIROSON85_50_diff = (CSIROSON85_50 - CSIROSON_b)
    ICHECDMISON85_50_diff = (ICHECDMISON85_50 - ICHECDMISON_b) 
    ICHECCCLMSON85_50_diff = (ICHECCCLMSON85_50 - ICHECCCLMSON_b)
    ICHECKNMISON85_50_diff = (ICHECKNMISON85_50 - ICHECKNMISON_b)
    ICHECMPISON85_50_diff = (ICHECMPISON85_50 - ICHECMPISON_b)
    ICHECSMHISON85_50_diff = (ICHECSMHISON85_50 - ICHECSMHISON_b)
    IPSLSON85_50_diff = (IPSLSON85_50 - IPSLSON_b)
    MIROCSON85_50_diff = (MIROCSON85_50 - MIROCSON_b)
    MOHCCCLMSON85_50_diff = (MOHCCCLMSON85_50 - MOHCCCLMSON_b)
    MOHCKNMISON85_50_diff = (MOHCKNMISON85_50 - MOHCKNMISON_b)
    MOHCSMHISON85_50_diff = (MOHCSMHISON85_50 - MOHCSMHISON_b)
    MPICCLMSON85_50_diff = (MPICCLMSON85_50 - MPICCLMSON_b)      
    MPIREMOSON85_50_diff = (MPIREMOSON85_50 - MPIREMOSON_b)                         
    MPISMHISON85_50_diff = (MPISMHISON85_50 - MPISMHISON_b)
    NCCSMHISON85_50_diff = (NCCSMHISON85_50 - NCCSMHISON_b) 
    NOAASON85_50_diff = (NOAASON85_50 - NOAASON_b)
    
    CCCmaCanRCMDJF85_50_diff = (CCCmaCanRCMDJF85_50 - CCCmaCanRCMDJF_b)
    CCCmaSMHIDJF85_50_diff = (CCCmaSMHIDJF85_50 - CCCmaSMHIDJF_b)
    CNRMDJF85_50_diff = (CNRMDJF85_50 - CNRMDJF_b)
    CNRMSMHIDJF85_50_diff = (CNRMSMHIDJF85_50 - CNRMSMHIDJF_b)  
    CSIRODJF85_50_diff = (CSIRODJF85_50 - CSIRODJF_b)
    ICHECDMIDJF85_50_diff = (ICHECDMIDJF85_50 - ICHECDMIDJF_b) 
    ICHECCCLMDJF85_50_diff = (ICHECCCLMDJF85_50 - ICHECCCLMDJF_b)
    ICHECKNMIDJF85_50_diff = (ICHECKNMIDJF85_50 - ICHECKNMIDJF_b)
    ICHECMPIDJF85_50_diff = (ICHECMPIDJF85_50 - ICHECMPIDJF_b)
    ICHECSMHIDJF85_50_diff = (ICHECSMHIDJF85_50 - ICHECSMHIDJF_b)
    IPSLDJF85_50_diff = (IPSLDJF85_50 - IPSLDJF_b)
    MIROCDJF85_50_diff = (MIROCDJF85_50 - MIROCDJF_b)
    MOHCCCLMDJF85_50_diff = (MOHCCCLMDJF85_50 - MOHCCCLMDJF_b)
    MOHCKNMIDJF85_50_diff = (MOHCKNMIDJF85_50 - MOHCKNMIDJF_b)
    MOHCSMHIDJF85_50_diff = (MOHCSMHIDJF85_50 - MOHCSMHIDJF_b)
    MPICCLMDJF85_50_diff = (MPICCLMDJF85_50 - MPICCLMDJF_b)      
    MPIREMODJF85_50_diff = (MPIREMODJF85_50 - MPIREMODJF_b)                         
    MPISMHIDJF85_50_diff = (MPISMHIDJF85_50 - MPISMHIDJF_b)
    NCCSMHIDJF85_50_diff = (NCCSMHIDJF85_50 - NCCSMHIDJF_b) 
    NOAADJF85_50_diff = (NOAADJF85_50 - NOAADJF_b)
    
    CCCmaCanRCMMAM85_50_diff = (CCCmaCanRCMMAM85_50 - CCCmaCanRCMMAM_b)
    CCCmaSMHIMAM85_50_diff = (CCCmaSMHIMAM85_50 - CCCmaSMHIMAM_b)
    CNRMMAM85_50_diff = (CNRMMAM85_50 - CNRMMAM_b)
    CNRMSMHIMAM85_50_diff = (CNRMSMHIMAM85_50 - CNRMSMHIMAM_b)  
    CSIROMAM85_50_diff = (CSIROMAM85_50 - CSIROMAM_b)
    ICHECDMIMAM85_50_diff = (ICHECDMIMAM85_50 - ICHECDMIMAM_b) 
    ICHECCCLMMAM85_50_diff = (ICHECCCLMMAM85_50 - ICHECCCLMMAM_b)
    ICHECKNMIMAM85_50_diff = (ICHECKNMIMAM85_50 - ICHECKNMIMAM_b)
    ICHECMPIMAM85_50_diff = (ICHECMPIMAM85_50 - ICHECMPIMAM_b)
    ICHECSMHIMAM85_50_diff = (ICHECSMHIMAM85_50 - ICHECSMHIMAM_b)
    IPSLMAM85_50_diff = (IPSLMAM85_50 - IPSLMAM_b)
    MIROCMAM85_50_diff = (MIROCMAM85_50 - MIROCMAM_b)
    MOHCCCLMMAM85_50_diff = (MOHCCCLMMAM85_50 - MOHCCCLMMAM_b)
    MOHCKNMIMAM85_50_diff = (MOHCKNMIMAM85_50 - MOHCKNMIMAM_b)
    MOHCSMHIMAM85_50_diff = (MOHCSMHIMAM85_50 - MOHCSMHIMAM_b)
    MPICCLMMAM85_50_diff = (MPICCLMMAM85_50 - MPICCLMMAM_b)      
    MPIREMOMAM85_50_diff = (MPIREMOMAM85_50 - MPIREMOMAM_b)                         
    MPISMHIMAM85_50_diff = (MPISMHIMAM85_50 - MPISMHIMAM_b)
    NCCSMHIMAM85_50_diff = (NCCSMHIMAM85_50 - NCCSMHIMAM_b) 
    NOAAMAM85_50_diff = (NOAAMAM85_50 - NOAAMAM_b)
    
    CCCmaCanRCMJJA85_50_diff = (CCCmaCanRCMJJA85_50 - CCCmaCanRCMJJA_b)
    CCCmaSMHIJJA85_50_diff = (CCCmaSMHIJJA85_50 - CCCmaSMHIJJA_b)
    CNRMJJA85_50_diff = (CNRMJJA85_50 - CNRMJJA_b)
    CNRMSMHIJJA85_50_diff = (CNRMSMHIJJA85_50 - CNRMSMHIJJA_b)  
    CSIROJJA85_50_diff = (CSIROJJA85_50 - CSIROJJA_b)
    ICHECDMIJJA85_50_diff = (ICHECDMIJJA85_50 - ICHECDMIJJA_b) 
    ICHECCCLMJJA85_50_diff = (ICHECCCLMJJA85_50 - ICHECCCLMJJA_b)
    ICHECKNMIJJA85_50_diff = (ICHECKNMIJJA85_50 - ICHECKNMIJJA_b)
    ICHECMPIJJA85_50_diff = (ICHECMPIJJA85_50 - ICHECMPIJJA_b)
    ICHECSMHIJJA85_50_diff = (ICHECSMHIJJA85_50 - ICHECSMHIJJA_b)
    IPSLJJA85_50_diff = (IPSLJJA85_50 - IPSLJJA_b)
    MIROCJJA85_50_diff = (MIROCJJA85_50 - MIROCJJA_b)
    MOHCCCLMJJA85_50_diff = (MOHCCCLMJJA85_50 - MOHCCCLMJJA_b)
    MOHCKNMIJJA85_50_diff = (MOHCKNMIJJA85_50 - MOHCKNMIJJA_b)
    MOHCSMHIJJA85_50_diff = (MOHCSMHIJJA85_50 - MOHCSMHIJJA_b)
    MPICCLMJJA85_50_diff = (MPICCLMJJA85_50 - MPICCLMJJA_b)      
    MPIREMOJJA85_50_diff = (MPIREMOJJA85_50 - MPIREMOJJA_b)                         
    MPISMHIJJA85_50_diff = (MPISMHIJJA85_50 - MPISMHIJJA_b)
    NCCSMHIJJA85_50_diff = (NCCSMHIJJA85_50 - NCCSMHIJJA_b) 
    NOAAJJA85_50_diff = (NOAAJJA85_50 - NOAAJJA_b)
    
    CCCmaCanRCMYR85_50_diff = (CCCmaCanRCMYR85_50 - CCCmaCanRCMYR_b)
    CCCmaSMHIYR85_50_diff = (CCCmaSMHIYR85_50 - CCCmaSMHIYR_b)
    CNRMYR85_50_diff = (CNRMYR85_50 - CNRMYR_b)
    CNRMSMHIYR85_50_diff = (CNRMSMHIYR85_50 - CNRMSMHIYR_b)  
    CSIROYR85_50_diff = (CSIROYR85_50 - CSIROYR_b)
    ICHECDMIYR85_50_diff = (ICHECDMIYR85_50 - ICHECDMIYR_b) 
    ICHECCCLMYR85_50_diff = (ICHECCCLMYR85_50 - ICHECCCLMYR_b)
    ICHECKNMIYR85_50_diff = (ICHECKNMIYR85_50 - ICHECKNMIYR_b)
    ICHECMPIYR85_50_diff = (ICHECMPIYR85_50 - ICHECMPIYR_b)
    ICHECSMHIYR85_50_diff = (ICHECSMHIYR85_50 - ICHECSMHIYR_b)
    IPSLYR85_50_diff = (IPSLYR85_50 - IPSLYR_b)
    MIROCYR85_50_diff = (MIROCYR85_50 - MIROCYR_b)
    MOHCCCLMYR85_50_diff = (MOHCCCLMYR85_50 - MOHCCCLMYR_b)
    MOHCKNMIYR85_50_diff = (MOHCKNMIYR85_50 - MOHCKNMIYR_b)
    MOHCSMHIYR85_50_diff = (MOHCSMHIYR85_50 - MOHCSMHIYR_b)
    MPICCLMYR85_50_diff = (MPICCLMYR85_50 - MPICCLMYR_b)      
    MPIREMOYR85_50_diff = (MPIREMOYR85_50 - MPIREMOYR_b)                         
    MPISMHIYR85_50_diff = (MPISMHIYR85_50 - MPISMHIYR_b)
    NCCSMHIYR85_50_diff = (NCCSMHIYR85_50 - NCCSMHIYR_b) 
    NOAAYR85_50_diff = (NOAAYR85_50 - NOAAYR_b)
    
    #create adjusted absolute temperature
    CCCmaCanRCMSON_50_adj =  (CCCmaCanRCMSON_50_diff + ObsSON)
    CCCmaSMHISON_50_adj =  (CCCmaSMHISON_50_diff + ObsSON)
    CNRMSON_50_adj =  (CNRMSON_50_diff + ObsSON)
    CNRMSMHISON_50_adj =  (CNRMSMHISON_50_diff + ObsSON)  
    CSIROSON_50_adj =  (CSIROSON_50_diff + ObsSON)
    ICHECDMISON_50_adj =  (ICHECDMISON_50_diff + ObsSON) 
    ICHECCCLMSON_50_adj =  (ICHECCCLMSON_50_diff + ObsSON)
    ICHECKNMISON_50_adj =  (ICHECKNMISON_50_diff + ObsSON)
    ICHECMPISON_50_adj =  (ICHECMPISON_50_diff + ObsSON)
    ICHECSMHISON_50_adj =  (ICHECSMHISON_50_diff + ObsSON)
    IPSLSON_50_adj =  (IPSLSON_50_diff + ObsSON)
    MIROCSON_50_adj =  (MIROCSON_50_diff + ObsSON)
    MOHCCCLMSON_50_adj =  (MOHCCCLMSON_50_diff + ObsSON)
    MOHCKNMISON_50_adj =  (MOHCKNMISON_50_diff + ObsSON)
    MOHCSMHISON_50_adj =  (MOHCSMHISON_50_diff + ObsSON)
    MPICCLMSON_50_adj =  (MPICCLMSON_50_diff + ObsSON)      
    MPIREMOSON_50_adj =  (MPIREMOSON_50_diff + ObsSON)                         
    MPISMHISON_50_adj =  (MPISMHISON_50_diff + ObsSON)
    NCCSMHISON_50_adj =  (NCCSMHISON_50_diff + ObsSON) 
    NOAASON_50_adj =  (NOAASON_50_diff + ObsSON)
    
    CCCmaCanRCMDJF_50_adj =  (CCCmaCanRCMDJF_50_diff  + ObsDJF)
    CCCmaSMHIDJF_50_adj =  (CCCmaSMHIDJF_50_diff + ObsDJF)
    CNRMDJF_50_adj =  (CNRMDJF_50_diff + ObsDJF)
    CNRMSMHIDJF_50_adj =  (CNRMSMHIDJF_50_diff + ObsDJF)  
    CSIRODJF_50_adj =  (CSIRODJF_50_diff + ObsDJF)
    ICHECDMIDJF_50_adj =  (ICHECDMIDJF_50_diff + ObsDJF) 
    ICHECCCLMDJF_50_adj =  (ICHECCCLMDJF_50_diff + ObsDJF)
    ICHECKNMIDJF_50_adj =  (ICHECKNMIDJF_50_diff + ObsDJF)
    ICHECMPIDJF_50_adj =  (ICHECMPIDJF_50_diff + ObsDJF)
    ICHECSMHIDJF_50_adj =  (ICHECSMHIDJF_50_diff + ObsDJF)
    IPSLDJF_50_adj =  (IPSLDJF_50_diff + ObsDJF)
    MIROCDJF_50_adj =  (MIROCDJF_50_diff + ObsDJF)
    MOHCCCLMDJF_50_adj =  (MOHCCCLMDJF_50_diff + ObsDJF)
    MOHCKNMIDJF_50_adj =  (MOHCKNMIDJF_50_diff + ObsDJF)
    MOHCSMHIDJF_50_adj =  (MOHCSMHIDJF_50_diff + ObsDJF)
    MPICCLMDJF_50_adj =  (MPICCLMDJF_50_diff + ObsDJF)      
    MPIREMODJF_50_adj =  (MPIREMODJF_50_diff + ObsDJF)                         
    MPISMHIDJF_50_adj =  (MPISMHIDJF_50_diff + ObsDJF)
    NCCSMHIDJF_50_adj =  (NCCSMHIDJF_50_diff + ObsDJF) 
    NOAADJF_50_adj =  (NOAADJF_50_diff + ObsDJF)
    
    CCCmaCanRCMMAM_50_adj =  (CCCmaCanRCMMAM_50_diff + ObsMAM)
    CCCmaSMHIMAM_50_adj =  (CCCmaSMHIMAM_50_diff + ObsMAM)
    CNRMMAM_50_adj =  (CNRMMAM_50_diff + ObsMAM)
    CNRMSMHIMAM_50_adj =  (CNRMSMHIMAM_50_diff + ObsMAM)  
    CSIROMAM_50_adj =  (CSIROMAM_50_diff + ObsMAM)
    ICHECDMIMAM_50_adj =  (ICHECDMIMAM_50_diff + ObsMAM) 
    ICHECCCLMMAM_50_adj =  (ICHECCCLMMAM_50_diff + ObsMAM)
    ICHECKNMIMAM_50_adj =  (ICHECKNMIMAM_50_diff + ObsMAM)
    ICHECMPIMAM_50_adj =  (ICHECMPIMAM_50_diff + ObsMAM)
    ICHECSMHIMAM_50_adj =  (ICHECSMHIMAM_50_diff + ObsMAM)
    IPSLMAM_50_adj =  (IPSLMAM_50_diff + ObsMAM)
    MIROCMAM_50_adj =  (MIROCMAM_50_diff + ObsMAM)
    MOHCCCLMMAM_50_adj =  (MOHCCCLMMAM_50_diff + ObsMAM)
    MOHCKNMIMAM_50_adj =  (MOHCKNMIMAM_50_diff + ObsMAM)
    MOHCSMHIMAM_50_adj =  (MOHCSMHIMAM_50_diff + ObsMAM)
    MPICCLMMAM_50_adj =  (MPICCLMMAM_50_diff + ObsMAM)      
    MPIREMOMAM_50_adj =  (MPIREMOMAM_50_diff + ObsMAM)                         
    MPISMHIMAM_50_adj =  (MPISMHIMAM_50_diff + ObsMAM)
    NCCSMHIMAM_50_adj =  (NCCSMHIMAM_50_diff + ObsMAM) 
    NOAAMAM_50_adj =  (NOAAMAM_50_diff + ObsMAM)
    
    CCCmaCanRCMJJA_50_adj =  (CCCmaCanRCMJJA_50_diff + ObsJJA)
    CCCmaSMHIJJA_50_adj =  (CCCmaSMHIJJA_50_diff + ObsJJA)
    CNRMJJA_50_adj =  (CNRMJJA_50_diff + ObsJJA)
    CNRMSMHIJJA_50_adj =  (CNRMSMHIJJA_50_diff + ObsJJA)  
    CSIROJJA_50_adj =  (CSIROJJA_50_diff + ObsJJA)
    ICHECDMIJJA_50_adj =  (ICHECDMIJJA_50_diff + ObsJJA) 
    ICHECCCLMJJA_50_adj =  (ICHECCCLMJJA_50_diff + ObsJJA)
    ICHECKNMIJJA_50_adj =  (ICHECKNMIJJA_50_diff + ObsJJA)
    ICHECMPIJJA_50_adj =  (ICHECMPIJJA_50_diff + ObsJJA)
    ICHECSMHIJJA_50_adj =  (ICHECSMHIJJA_50_diff + ObsJJA)
    IPSLJJA_50_adj =  (IPSLJJA_50_diff + ObsJJA)
    MIROCJJA_50_adj =  (MIROCJJA_50_diff + ObsJJA)
    MOHCCCLMJJA_50_adj =  (MOHCCCLMJJA_50_diff + ObsJJA)
    MOHCKNMIJJA_50_adj =  (MOHCKNMIJJA_50_diff + ObsJJA)
    MOHCSMHIJJA_50_adj =  (MOHCSMHIJJA_50_diff + ObsJJA)
    MPICCLMJJA_50_adj =  (MPICCLMJJA_50_diff + ObsJJA)      
    MPIREMOJJA_50_adj =  (MPIREMOJJA_50_diff + ObsJJA)                         
    MPISMHIJJA_50_adj =  (MPISMHIJJA_50_diff + ObsJJA)
    NCCSMHIJJA_50_adj =  (NCCSMHIJJA_50_diff + ObsJJA) 
    NOAAJJA_50_adj =  (NOAAJJA_50_diff + ObsJJA)
    
    CCCmaCanRCMYR_50_adj =  (CCCmaCanRCMYR_50_diff + ObsYR)
    CCCmaSMHIYR_50_adj =  (CCCmaSMHIYR_50_diff + ObsYR)
    CNRMYR_50_adj =  (CNRMYR_50_diff + ObsYR)
    CNRMSMHIYR_50_adj =  (CNRMSMHIYR_50_diff + ObsYR)  
    CSIROYR_50_adj =  (CSIROYR_50_diff + ObsYR)
    ICHECDMIYR_50_adj =  (ICHECDMIYR_50_diff + ObsYR) 
    ICHECCCLMYR_50_adj =  (ICHECCCLMYR_50_diff + ObsYR)
    ICHECKNMIYR_50_adj =  (ICHECKNMIYR_50_diff + ObsYR)
    ICHECMPIYR_50_adj =  (ICHECMPIYR_50_diff + ObsYR)
    ICHECSMHIYR_50_adj =  (ICHECSMHIYR_50_diff + ObsYR)
    IPSLYR_50_adj =  (IPSLYR_50_diff + ObsYR)
    MIROCYR_50_adj =  (MIROCYR_50_diff + ObsYR)
    MOHCCCLMYR_50_adj =  (MOHCCCLMYR_50_diff + ObsYR)
    MOHCKNMIYR_50_adj =  (MOHCKNMIYR_50_diff + ObsYR)
    MOHCSMHIYR_50_adj =  (MOHCSMHIYR_50_diff + ObsYR)
    MPICCLMYR_50_adj =  (MPICCLMYR_50_diff + ObsYR)      
    MPIREMOYR_50_adj =  (MPIREMOYR_50_diff + ObsYR)                         
    MPISMHIYR_50_adj =  (MPISMHIYR_50_diff + ObsYR)
    NCCSMHIYR_50_adj =  (NCCSMHIYR_50_diff + ObsYR) 
    NOAAYR_50_adj =  (NOAAYR_50_diff + ObsYR)
    
    CCCmaCanRCMSON85_50_adj =  (CCCmaCanRCMSON85_50_diff + ObsSON)
    CCCmaSMHISON85_50_adj =  (CCCmaSMHISON85_50_diff + ObsSON)
    CNRMSON85_50_adj =  (CNRMSON85_50_diff + ObsSON)
    CNRMSMHISON85_50_adj =  (CNRMSMHISON85_50_diff + ObsSON)  
    CSIROSON85_50_adj =  (CSIROSON85_50_diff + ObsSON)
    ICHECDMISON85_50_adj =  (ICHECDMISON85_50_diff + ObsSON) 
    ICHECCCLMSON85_50_adj =  (ICHECCCLMSON85_50_diff + ObsSON)
    ICHECKNMISON85_50_adj =  (ICHECKNMISON85_50_diff + ObsSON)
    ICHECMPISON85_50_adj =  (ICHECMPISON85_50_diff + ObsSON)
    ICHECSMHISON85_50_adj =  (ICHECSMHISON85_50_diff + ObsSON)
    IPSLSON85_50_adj =  (IPSLSON85_50_diff + ObsSON)
    MIROCSON85_50_adj =  (MIROCSON85_50_diff + ObsSON)
    MOHCCCLMSON85_50_adj =  (MOHCCCLMSON85_50_diff + ObsSON)
    MOHCKNMISON85_50_adj =  (MOHCKNMISON85_50_diff + ObsSON)
    MOHCSMHISON85_50_adj =  (MOHCSMHISON85_50_diff + ObsSON)
    MPICCLMSON85_50_adj =  (MPICCLMSON85_50_diff + ObsSON)      
    MPIREMOSON85_50_adj =  (MPIREMOSON85_50_diff + ObsSON)                         
    MPISMHISON85_50_adj =  (MPISMHISON85_50_diff + ObsSON)
    NCCSMHISON85_50_adj =  (NCCSMHISON85_50_diff + ObsSON) 
    NOAASON85_50_adj =  (NOAASON85_50_diff + ObsSON)
    
    CCCmaCanRCMDJF85_50_adj =  (CCCmaCanRCMDJF85_50_diff + ObsDJF)
    CCCmaSMHIDJF85_50_adj =  (CCCmaSMHIDJF85_50_diff + ObsDJF)
    CNRMDJF85_50_adj =  (CNRMDJF85_50_diff + ObsDJF)
    CNRMSMHIDJF85_50_adj =  (CNRMSMHIDJF85_50_diff + ObsDJF)  
    CSIRODJF85_50_adj =  (CSIRODJF85_50_diff + ObsDJF)
    ICHECDMIDJF85_50_adj =  (ICHECDMIDJF85_50_diff + ObsDJF) 
    ICHECCCLMDJF85_50_adj =  (ICHECCCLMDJF85_50_diff + ObsDJF)
    ICHECKNMIDJF85_50_adj =  (ICHECKNMIDJF85_50_diff + ObsDJF)
    ICHECMPIDJF85_50_adj =  (ICHECMPIDJF85_50_diff + ObsDJF)
    ICHECSMHIDJF85_50_adj =  (ICHECSMHIDJF85_50_diff + ObsDJF)
    IPSLDJF85_50_adj =  (IPSLDJF85_50_diff + ObsDJF)
    MIROCDJF85_50_adj =  (MIROCDJF85_50_diff + ObsDJF)
    MOHCCCLMDJF85_50_adj =  (MOHCCCLMDJF85_50_diff + ObsDJF)
    MOHCKNMIDJF85_50_adj =  (MOHCKNMIDJF85_50_diff + ObsDJF)
    MOHCSMHIDJF85_50_adj =  (MOHCSMHIDJF85_50_diff + ObsDJF)
    MPICCLMDJF85_50_adj =  (MPICCLMDJF85_50_diff + ObsDJF)      
    MPIREMODJF85_50_adj =  (MPIREMODJF85_50_diff + ObsDJF)                         
    MPISMHIDJF85_50_adj =  (MPISMHIDJF85_50_diff + ObsDJF)
    NCCSMHIDJF85_50_adj =  (NCCSMHIDJF85_50_diff + ObsDJF) 
    NOAADJF85_50_adj =  (NOAADJF85_50_diff + ObsDJF)
    
    CCCmaCanRCMMAM85_50_adj =  (CCCmaCanRCMMAM85_50_diff + ObsMAM)
    CCCmaSMHIMAM85_50_adj =  (CCCmaSMHIMAM85_50_diff + ObsMAM)
    CNRMMAM85_50_adj =  (CNRMMAM85_50_diff + ObsMAM)
    CNRMSMHIMAM85_50_adj =  (CNRMSMHIMAM85_50_diff + ObsMAM)  
    CSIROMAM85_50_adj =  (CSIROMAM85_50_diff + ObsMAM)
    ICHECDMIMAM85_50_adj =  (ICHECDMIMAM85_50_diff + ObsMAM) 
    ICHECCCLMMAM85_50_adj =  (ICHECCCLMMAM85_50_diff + ObsMAM)
    ICHECKNMIMAM85_50_adj =  (ICHECKNMIMAM85_50_diff + ObsMAM)
    ICHECMPIMAM85_50_adj =  (ICHECMPIMAM85_50_diff + ObsMAM)
    ICHECSMHIMAM85_50_adj =  (ICHECSMHIMAM85_50_diff + ObsMAM)
    IPSLMAM85_50_adj =  (IPSLMAM85_50_diff + ObsMAM)
    MIROCMAM85_50_adj =  (MIROCMAM85_50_diff + ObsMAM)
    MOHCCCLMMAM85_50_adj =  (MOHCCCLMMAM85_50_diff + ObsMAM)
    MOHCKNMIMAM85_50_adj =  (MOHCKNMIMAM85_50_diff + ObsMAM)
    MOHCSMHIMAM85_50_adj =  (MOHCSMHIMAM85_50_diff + ObsMAM)
    MPICCLMMAM85_50_adj =  (MPICCLMMAM85_50_diff + ObsMAM)      
    MPIREMOMAM85_50_adj =  (MPIREMOMAM85_50_diff + ObsMAM)                         
    MPISMHIMAM85_50_adj =  (MPISMHIMAM85_50_diff + ObsMAM)
    NCCSMHIMAM85_50_adj =  (NCCSMHIMAM85_50_diff + ObsMAM) 
    NOAAMAM85_50_adj =  (NOAAMAM85_50_diff + ObsMAM)
    
    CCCmaCanRCMJJA85_50_adj =  (CCCmaCanRCMJJA85_50_diff + ObsJJA)
    CCCmaSMHIJJA85_50_adj =  (CCCmaSMHIJJA85_50_diff + ObsJJA)
    CNRMJJA85_50_adj =  (CNRMJJA85_50_diff + ObsJJA)
    CNRMSMHIJJA85_50_adj =  (CNRMSMHIJJA85_50_diff + ObsJJA)  
    CSIROJJA85_50_adj =  (CSIROJJA85_50_diff + ObsJJA)
    ICHECDMIJJA85_50_adj =  (ICHECDMIJJA85_50_diff + ObsJJA) 
    ICHECCCLMJJA85_50_adj =  (ICHECCCLMJJA85_50_diff + ObsJJA)
    ICHECKNMIJJA85_50_adj =  (ICHECKNMIJJA85_50_diff + ObsJJA)
    ICHECMPIJJA85_50_adj =  (ICHECMPIJJA85_50_diff + ObsJJA)
    ICHECSMHIJJA85_50_adj =  (ICHECSMHIJJA85_50_diff + ObsJJA)
    IPSLJJA85_50_adj =  (IPSLJJA85_50_diff + ObsJJA)
    MIROCJJA85_50_adj =  (MIROCJJA85_50_diff + ObsJJA)
    MOHCCCLMJJA85_50_adj =  (MOHCCCLMJJA85_50_diff + ObsJJA)
    MOHCKNMIJJA85_50_adj =  (MOHCKNMIJJA85_50_diff + ObsJJA)
    MOHCSMHIJJA85_50_adj =  (MOHCSMHIJJA85_50_diff + ObsJJA)
    MPICCLMJJA85_50_adj =  (MPICCLMJJA85_50_diff + ObsJJA)      
    MPIREMOJJA85_50_adj =  (MPIREMOJJA85_50_diff + ObsJJA)                         
    MPISMHIJJA85_50_adj =  (MPISMHIJJA85_50_diff + ObsJJA)
    NCCSMHIJJA85_50_adj =  (NCCSMHIJJA85_50_diff + ObsJJA) 
    NOAAJJA85_50_adj =  (NOAAJJA85_50_diff + ObsJJA)
    
    CCCmaCanRCMYR85_50_adj =  (CCCmaCanRCMYR85_50_diff + ObsYR)
    CCCmaSMHIYR85_50_adj =  (CCCmaSMHIYR85_50_diff + ObsYR)
    CNRMYR85_50_adj =  (CNRMYR85_50_diff + ObsYR)
    CNRMSMHIYR85_50_adj =  (CNRMSMHIYR85_50_diff + ObsYR)  
    CSIROYR85_50_adj =  (CSIROYR85_50_diff + ObsYR)
    ICHECDMIYR85_50_adj =  (ICHECDMIYR85_50_diff + ObsYR) 
    ICHECCCLMYR85_50_adj =  (ICHECCCLMYR85_50_diff + ObsYR)
    ICHECKNMIYR85_50_adj =  (ICHECKNMIYR85_50_diff + ObsYR)
    ICHECMPIYR85_50_adj =  (ICHECMPIYR85_50_diff + ObsYR)
    ICHECSMHIYR85_50_adj =  (ICHECSMHIYR85_50_diff + ObsYR)
    IPSLYR85_50_adj =  (IPSLYR85_50_diff + ObsYR)
    MIROCYR85_50_adj =  (MIROCYR85_50_diff + ObsYR)
    MOHCCCLMYR85_50_adj =  (MOHCCCLMYR85_50_diff + ObsYR)
    MOHCKNMIYR85_50_adj =  (MOHCKNMIYR85_50_diff + ObsYR)
    MOHCSMHIYR85_50_adj =  (MOHCSMHIYR85_50_diff + ObsYR)
    MPICCLMYR85_50_adj =  (MPICCLMYR85_50_diff + ObsYR)      
    MPIREMOYR85_50_adj =  (MPIREMOYR85_50_diff + ObsYR)                         
    MPISMHIYR85_50_adj =  (MPISMHIYR85_50_diff + ObsYR)
    NCCSMHIYR85_50_adj =  (NCCSMHIYR85_50_diff + ObsYR) 
    NOAAYR85_50_adj =  (NOAAYR85_50_diff + ObsYR)
    
    #Create averages
    AverageSON_50 = (CCCmaCanRCMSON_50_adj + CCCmaSMHISON_50_adj + CNRMSON_50_adj + CNRMSMHISON_50_adj + CSIROSON_50_adj + ICHECDMISON_50_adj + ICHECCCLMSON_50_adj + ICHECKNMISON_50_adj + ICHECMPISON_50_adj + ICHECSMHISON_50_adj + IPSLSON_50_adj + MIROCSON_50_adj + MOHCCCLMSON_50_adj + MOHCKNMISON_50_adj + MOHCSMHISON_50_adj + MPICCLMSON_50_adj + MPIREMOSON_50_adj + MPISMHISON_50_adj + NCCSMHISON_50_adj + NOAASON_50_adj)/20.
    AverageDJF_50 = (CCCmaCanRCMDJF_50_adj + CCCmaSMHIDJF_50_adj + CNRMDJF_50_adj + CNRMSMHIDJF_50_adj + CSIRODJF_50_adj + ICHECDMIDJF_50_adj + ICHECCCLMDJF_50_adj + ICHECKNMIDJF_50_adj + ICHECMPIDJF_50_adj + ICHECSMHIDJF_50_adj + IPSLDJF_50_adj + MIROCDJF_50_adj + MOHCCCLMDJF_50_adj + MOHCKNMIDJF_50_adj + MOHCSMHIDJF_50_adj + MPICCLMDJF_50_adj + MPIREMODJF_50_adj + MPISMHIDJF_50_adj + NCCSMHIDJF_50_adj + NOAADJF_50_adj)/20.
    AverageMAM_50 = (CCCmaCanRCMMAM_50_adj + CCCmaSMHIMAM_50_adj + CNRMMAM_50_adj + CNRMSMHIMAM_50_adj + CSIROMAM_50_adj + ICHECDMIMAM_50_adj + ICHECCCLMMAM_50_adj + ICHECKNMIMAM_50_adj + ICHECMPIMAM_50_adj + ICHECSMHIMAM_50_adj + IPSLMAM_50_adj + MIROCMAM_50_adj + MOHCCCLMMAM_50_adj + MOHCKNMIMAM_50_adj + MOHCSMHIMAM_50_adj + MPICCLMMAM_50_adj + MPIREMOMAM_50_adj + MPISMHIMAM_50_adj + NCCSMHIMAM_50_adj + NOAAMAM_50_adj)/20.
    AverageJJA_50 = (CCCmaCanRCMJJA_50_adj + CCCmaSMHIJJA_50_adj + CNRMJJA_50_adj + CNRMSMHIJJA_50_adj + CSIROJJA_50_adj + ICHECDMIJJA_50_adj + ICHECCCLMJJA_50_adj + ICHECKNMIJJA_50_adj + ICHECMPIJJA_50_adj + ICHECSMHIJJA_50_adj + IPSLJJA_50_adj + MIROCJJA_50_adj + MOHCCCLMJJA_50_adj + MOHCKNMIJJA_50_adj + MOHCSMHIJJA_50_adj + MPICCLMJJA_50_adj + MPIREMOJJA_50_adj + MPISMHIJJA_50_adj + NCCSMHIJJA_50_adj + NOAAJJA_50_adj)/20.
    Average_50 = (CCCmaCanRCMYR_50_adj + CCCmaSMHIYR_50_adj + CNRMYR_50_adj + CNRMSMHIYR_50_adj + CSIROYR_50_adj + ICHECDMIYR_50_adj + ICHECCCLMYR_50_adj + ICHECKNMIYR_50_adj + ICHECMPIYR_50_adj + ICHECSMHIYR_50_adj + IPSLYR_50_adj + MIROCYR_50_adj + MOHCCCLMYR_50_adj + MOHCKNMIYR_50_adj + MOHCSMHIYR_50_adj + MPICCLMYR_50_adj + MPIREMOYR_50_adj + MPISMHIYR_50_adj + NCCSMHIYR_50_adj + NOAAYR_50_adj)/20.
    
    AverageSON85_50 = (CCCmaCanRCMSON85_50_adj + CCCmaSMHISON85_50_adj + CNRMSON85_50_adj + CNRMSMHISON85_50_adj + CSIROSON85_50_adj + ICHECDMISON85_50_adj + ICHECCCLMSON85_50_adj + ICHECKNMISON85_50_adj + ICHECMPISON85_50_adj + ICHECSMHISON85_50_adj + IPSLSON85_50_adj + MIROCSON85_50_adj + MOHCCCLMSON85_50_adj + MOHCKNMISON85_50_adj + MOHCSMHISON85_50_adj + MPICCLMSON85_50_adj + MPIREMOSON85_50_adj + MPISMHISON85_50_adj + NCCSMHISON85_50_adj + NOAASON85_50_adj)/20.
    AverageDJF85_50 = (CCCmaCanRCMDJF85_50_adj + CCCmaSMHIDJF85_50_adj + CNRMDJF85_50_adj + CNRMSMHIDJF85_50_adj + CSIRODJF85_50_adj + ICHECDMIDJF85_50_adj + ICHECCCLMDJF85_50_adj + ICHECKNMIDJF85_50_adj + ICHECMPIDJF85_50_adj + ICHECSMHIDJF85_50_adj + IPSLDJF85_50_adj + MIROCDJF85_50_adj + MOHCCCLMDJF85_50_adj + MOHCKNMIDJF85_50_adj + MOHCSMHIDJF85_50_adj + MPICCLMDJF85_50_adj + MPIREMODJF85_50_adj + MPISMHIDJF85_50_adj + NCCSMHIDJF85_50_adj + NOAADJF85_50_adj)/20.
    AverageMAM85_50 = (CCCmaCanRCMMAM85_50_adj + CCCmaSMHIMAM85_50_adj + CNRMMAM85_50_adj + CNRMSMHIMAM85_50_adj + CSIROMAM85_50_adj + ICHECDMIMAM85_50_adj + ICHECCCLMMAM85_50_adj + ICHECKNMIMAM85_50_adj + ICHECMPIMAM85_50_adj + ICHECSMHIMAM85_50_adj + IPSLMAM85_50_adj + MIROCMAM85_50_adj + MOHCCCLMMAM85_50_adj + MOHCKNMIMAM85_50_adj + MOHCSMHIMAM85_50_adj + MPICCLMMAM85_50_adj + MPIREMOMAM85_50_adj + MPISMHIMAM85_50_adj + NCCSMHIMAM85_50_adj + NOAAMAM85_50_adj)/20.
    AverageJJA85_50 = (CCCmaCanRCMJJA85_50_adj + CCCmaSMHIJJA85_50_adj + CNRMJJA85_50_adj + CNRMSMHIJJA85_50_adj + CSIROJJA85_50_adj + ICHECDMIJJA85_50_adj + ICHECCCLMJJA85_50_adj + ICHECKNMIJJA85_50_adj + ICHECMPIJJA85_50_adj + ICHECSMHIJJA85_50_adj + IPSLJJA85_50_adj + MIROCJJA85_50_adj + MOHCCCLMJJA85_50_adj + MOHCKNMIJJA85_50_adj + MOHCSMHIJJA85_50_adj + MPICCLMJJA85_50_adj + MPIREMOJJA85_50_adj + MPISMHIJJA85_50_adj + NCCSMHIJJA85_50_adj + NOAAJJA85_50_adj)/20.
    Average85_50 = (CCCmaCanRCMYR85_50_adj + CCCmaSMHIYR85_50_adj + CNRMYR85_50_adj + CNRMSMHIYR85_50_adj + CSIROYR85_50_adj + ICHECDMIYR85_50_adj + ICHECCCLMYR85_50_adj + ICHECKNMIYR85_50_adj + ICHECMPIYR85_50_adj + ICHECSMHIYR85_50_adj + IPSLYR85_50_adj + MIROCYR85_50_adj + MOHCCCLMYR85_50_adj + MOHCKNMIYR85_50_adj + MOHCSMHIYR85_50_adj + MPICCLMYR85_50_adj + MPIREMOYR85_50_adj + MPISMHIYR85_50_adj + NCCSMHIYR85_50_adj + NOAAYR85_50_adj)/20.
    
    AverageSON_50_diff = (CCCmaCanRCMSON_50_diff + CCCmaSMHISON_50_diff + CNRMSON_50_diff + CNRMSMHISON_50_diff + CSIROSON_50_diff + ICHECDMISON_50_diff + ICHECCCLMSON_50_diff + ICHECKNMISON_50_diff + ICHECMPISON_50_diff + ICHECSMHISON_50_diff + IPSLSON_50_diff + MIROCSON_50_diff + MOHCCCLMSON_50_diff + MOHCKNMISON_50_diff + MOHCSMHISON_50_diff + MPICCLMSON_50_diff + MPIREMOSON_50_diff + MPISMHISON_50_diff + NCCSMHISON_50_diff + NOAASON_50_diff)/20.
    AverageDJF_50_diff = (CCCmaCanRCMDJF_50_diff + CCCmaSMHIDJF_50_diff + CNRMDJF_50_diff + CNRMSMHIDJF_50_diff + CSIRODJF_50_diff + ICHECDMIDJF_50_diff + ICHECCCLMDJF_50_diff + ICHECKNMIDJF_50_diff + ICHECMPIDJF_50_diff + ICHECSMHIDJF_50_diff + IPSLDJF_50_diff + MIROCDJF_50_diff + MOHCCCLMDJF_50_diff + MOHCKNMIDJF_50_diff + MOHCSMHIDJF_50_diff + MPICCLMDJF_50_diff + MPIREMODJF_50_diff + MPISMHIDJF_50_diff + NCCSMHIDJF_50_diff + NOAADJF_50_diff)/20.
    AverageMAM_50_diff = (CCCmaCanRCMMAM_50_diff + CCCmaSMHIMAM_50_diff + CNRMMAM_50_diff + CNRMSMHIMAM_50_diff + CSIROMAM_50_diff + ICHECDMIMAM_50_diff + ICHECCCLMMAM_50_diff + ICHECKNMIMAM_50_diff + ICHECMPIMAM_50_diff + ICHECSMHIMAM_50_diff + IPSLMAM_50_diff + MIROCMAM_50_diff + MOHCCCLMMAM_50_diff + MOHCKNMIMAM_50_diff + MOHCSMHIMAM_50_diff + MPICCLMMAM_50_diff + MPIREMOMAM_50_diff + MPISMHIMAM_50_diff + NCCSMHIMAM_50_diff + NOAAMAM_50_diff)/20.
    AverageJJA_50_diff = (CCCmaCanRCMJJA_50_diff + CCCmaSMHIJJA_50_diff + CNRMJJA_50_diff + CNRMSMHIJJA_50_diff + CSIROJJA_50_diff + ICHECDMIJJA_50_diff + ICHECCCLMJJA_50_diff + ICHECKNMIJJA_50_diff + ICHECMPIJJA_50_diff + ICHECSMHIJJA_50_diff + IPSLJJA_50_diff + MIROCJJA_50_diff + MOHCCCLMJJA_50_diff + MOHCKNMIJJA_50_diff + MOHCSMHIJJA_50_diff + MPICCLMJJA_50_diff + MPIREMOJJA_50_diff + MPISMHIJJA_50_diff + NCCSMHIJJA_50_diff + NOAAJJA_50_diff)/20.
    Average_50_diff = (CCCmaCanRCMYR_50_diff + CCCmaSMHIYR_50_diff + CNRMYR_50_diff + CNRMSMHIYR_50_diff + CSIROYR_50_diff + ICHECDMIYR_50_diff + ICHECCCLMYR_50_diff + ICHECKNMIYR_50_diff + ICHECMPIYR_50_diff + ICHECSMHIYR_50_diff + IPSLYR_50_diff + MIROCYR_50_diff + MOHCCCLMYR_50_diff + MOHCKNMIYR_50_diff + MOHCSMHIYR_50_diff + MPICCLMYR_50_diff + MPIREMOYR_50_diff + MPISMHIYR_50_diff + NCCSMHIYR_50_diff + NOAAYR_50_diff)/20.
    
    AverageSON85_50_diff = (CCCmaCanRCMSON85_50_diff + CCCmaSMHISON85_50_diff + CNRMSON85_50_diff + CNRMSMHISON85_50_diff + CSIROSON85_50_diff + ICHECDMISON85_50_diff + ICHECCCLMSON85_50_diff + ICHECKNMISON85_50_diff + ICHECMPISON85_50_diff + ICHECSMHISON85_50_diff + IPSLSON85_50_diff + MIROCSON85_50_diff + MOHCCCLMSON85_50_diff + MOHCKNMISON85_50_diff + MOHCSMHISON85_50_diff + MPICCLMSON85_50_diff + MPIREMOSON85_50_diff + MPISMHISON85_50_diff + NCCSMHISON85_50_diff + NOAASON85_50_diff)/20.
    AverageDJF85_50_diff = (CCCmaCanRCMDJF85_50_diff + CCCmaSMHIDJF85_50_diff + CNRMDJF85_50_diff + CNRMSMHIDJF85_50_diff + CSIRODJF85_50_diff + ICHECDMIDJF85_50_diff + ICHECCCLMDJF85_50_diff + ICHECKNMIDJF85_50_diff + ICHECMPIDJF85_50_diff + ICHECSMHIDJF85_50_diff + IPSLDJF85_50_diff + MIROCDJF85_50_diff + MOHCCCLMDJF85_50_diff + MOHCKNMIDJF85_50_diff + MOHCSMHIDJF85_50_diff + MPICCLMDJF85_50_diff + MPIREMODJF85_50_diff + MPISMHIDJF85_50_diff + NCCSMHIDJF85_50_diff + NOAADJF85_50_diff)/20.
    AverageMAM85_50_diff = (CCCmaCanRCMMAM85_50_diff + CCCmaSMHIMAM85_50_diff + CNRMMAM85_50_diff + CNRMSMHIMAM85_50_diff + CSIROMAM85_50_diff + ICHECDMIMAM85_50_diff + ICHECCCLMMAM85_50_diff + ICHECKNMIMAM85_50_diff + ICHECMPIMAM85_50_diff + ICHECSMHIMAM85_50_diff + IPSLMAM85_50_diff + MIROCMAM85_50_diff + MOHCCCLMMAM85_50_diff + MOHCKNMIMAM85_50_diff + MOHCSMHIMAM85_50_diff + MPICCLMMAM85_50_diff + MPIREMOMAM85_50_diff + MPISMHIMAM85_50_diff + NCCSMHIMAM85_50_diff + NOAAMAM85_50_diff)/20.
    AverageJJA85_50_diff = (CCCmaCanRCMJJA85_50_diff + CCCmaSMHIJJA85_50_diff + CNRMJJA85_50_diff + CNRMSMHIJJA85_50_diff + CSIROJJA85_50_diff + ICHECDMIJJA85_50_diff + ICHECCCLMJJA85_50_diff + ICHECKNMIJJA85_50_diff + ICHECMPIJJA85_50_diff + ICHECSMHIJJA85_50_diff + IPSLJJA85_50_diff + MIROCJJA85_50_diff + MOHCCCLMJJA85_50_diff + MOHCKNMIJJA85_50_diff + MOHCSMHIJJA85_50_diff + MPICCLMJJA85_50_diff + MPIREMOJJA85_50_diff + MPISMHIJJA85_50_diff + NCCSMHIJJA85_50_diff + NOAAJJA85_50_diff)/20.
    Average85_50_diff = (CCCmaCanRCMYR85_50_diff + CCCmaSMHIYR85_50_diff + CNRMYR85_50_diff + CNRMSMHIYR85_50_diff + CSIROYR85_50_diff + ICHECDMIYR85_50_diff + ICHECCCLMYR85_50_diff + ICHECKNMIYR85_50_diff + ICHECMPIYR85_50_diff + ICHECSMHIYR85_50_diff + IPSLYR85_50_diff + MIROCYR85_50_diff + MOHCCCLMYR85_50_diff + MOHCKNMIYR85_50_diff + MOHCSMHIYR85_50_diff + MPICCLMYR85_50_diff + MPIREMOYR85_50_diff + MPISMHIYR85_50_diff + NCCSMHIYR85_50_diff + NOAAYR85_50_diff)/20.
    

    #-------------------------------------------------------------------------
    #PART 6: PRINT DATA
    #print data to determine colorbar range
    print "ObsSON"
    print np.amax(ObsSON.data)
    print np.amin(ObsSON.data)
    
    print "ObsDJF"
    print np.amax(ObsDJF.data)
    print np.amin(ObsDJF.data)
    
    print "ObsMAM"
    print np.amax(ObsMAM.data)
    print np.amin(ObsMAM.data)

    print "ObsJJA"
    print np.amax(ObsJJA.data)
    print np.amin(ObsJJA.data)
    
    print "Obs"
    print np.amax(ObsYR.data)
    print np.amin(ObsYR.data)
    
    
    print "Ave_30SON"
    print np.amax(AverageSON_30.data)
    print np.amin(AverageSON_30.data)
    
    print "Ave_30DJF"
    print np.amax(AverageDJF_30.data)
    print np.amin(AverageDJF_30.data)
    
    print "Ave_30MAM"
    print np.amax(AverageMAM_30.data)
    print np.amin(AverageMAM_30.data)
    
    print "Ave_30JJA"
    print np.amax(AverageJJA_30.data)
    print np.amin(AverageJJA_30.data)
    
    print "Ave_30"
    print np.amax(Average_30.data)
    print np.amin(Average_30.data)
    
    
    print "Ave85_30SON"
    print np.amax(AverageSON85_30.data)
    print np.amin(AverageSON85_30.data)
    
    print "Ave85_30DJF"
    print np.amax(AverageDJF85_30.data)
    print np.amin(AverageDJF85_30.data)
    
    print "Ave85_30MAM"
    print np.amax(AverageMAM85_30.data)
    print np.amin(AverageMAM85_30.data)
    
    print "Ave85_30JJA"
    print np.amax(AverageJJA85_30.data)
    print np.amin(AverageJJA85_30.data)
    
    print "Ave85_30"
    print np.amax(Average85_30.data)
    print np.amin(Average85_30.data)
    
    
    print "Ave_50SON"
    print np.amax(AverageSON_50.data)
    print np.amin(AverageSON_50.data)
    
    print "Ave_50DJF"
    print np.amax(AverageDJF_50.data)
    print np.amin(AverageDJF_50.data)
    
    print "Ave_50MAM"
    print np.amax(AverageMAM_50.data)
    print np.amin(AverageMAM_50.data)
    
    print "Ave_50JJA"
    print np.amax(AverageJJA_50.data)
    print np.amin(AverageJJA_50.data)
    
    print "Ave_50"
    print np.amax(Average_50.data)
    print np.amin(Average_50.data)
    
    
    print "Ave85_50SON"
    print np.amax(AverageSON85_50.data)
    print np.amin(AverageSON85_50.data)
    
    print "Ave85_50DJF"
    print np.amax(AverageDJF85_50.data)
    print np.amin(AverageDJF85_50.data)
    
    print "Ave85_50MAM"
    print np.amax(AverageMAM85_50.data)
    print np.amin(AverageMAM85_50.data)
    
    print "Ave85_50JJA"
    print np.amax(AverageJJA85_50.data)
    print np.amin(AverageJJA85_50.data)
        
    print "Ave85_50"
    print np.amax(Average85_50.data)
    print np.amin(Average85_50.data)
    
    
    print "Ave_30_diffSON"
    print np.amax(AverageSON_30_diff.data)
    print np.amin(AverageSON_30_diff.data)
    
    print "Ave_30_diffDJF"
    print np.amax(AverageDJF_30_diff.data)
    print np.amin(AverageDJF_30_diff.data)
    
    print "Ave_30_diffMAM"
    print np.amax(AverageMAM_30_diff.data)
    print np.amin(AverageMAM_30_diff.data)
    
    print "Ave_30_diffJJA"
    print np.amax(AverageJJA_30_diff.data)
    print np.amin(AverageJJA_30_diff.data)
    
    print "Ave_30_diff"
    print np.amax(Average_30_diff.data)
    print np.amin(Average_30_diff.data)
    
    
    print "Ave85_30_diffSON"
    print np.amax(AverageSON85_30_diff.data)
    print np.amin(AverageSON85_30_diff.data)
    
    print "Ave85_30_diffDJF"
    print np.amax(AverageDJF85_30_diff.data)
    print np.amin(AverageDJF85_30_diff.data)
    
    print "Ave85_30_diffMAM"
    print np.amax(AverageMAM85_30_diff.data)
    print np.amin(AverageMAM85_30_diff.data)
    
    print "Ave85_30_diffJJA"
    print np.amax(AverageJJA85_30_diff.data)
    print np.amin(AverageJJA85_30_diff.data)
    
    print "Ave85_30_diff"
    print np.amax(Average85_30_diff.data)
    print np.amin(Average85_30_diff.data)
    
    
    print "Ave_50_diffSON"
    print np.amax(AverageSON_50_diff.data)
    print np.amin(AverageSON_50_diff.data)
    
    print "Ave_50_diffDJF"
    print np.amax(AverageDJF_50_diff.data)
    print np.amin(AverageDJF_50_diff.data)
    
    print "Ave_50_diffMAM"
    print np.amax(AverageMAM_50_diff.data)
    print np.amin(AverageMAM_50_diff.data)
    
    print "Ave_50_diffJJA"
    print np.amax(AverageJJA_50_diff.data)
    print np.amin(AverageJJA_50_diff.data)
    
    print "Ave_50_diff"
    print np.amax(Average_50_diff.data)
    print np.amin(Average_50_diff.data)
    
    
    print "Ave85_50_diffSON"
    print np.amax(AverageSON85_50_diff.data)
    print np.amin(AverageSON85_50_diff.data)
    
    print "Ave85_50_diffDJF"
    print np.amax(AverageDJF85_50_diff.data)
    print np.amin(AverageDJF85_50_diff.data)
    
    print "Ave85_50_diffMAM"
    print np.amax(AverageMAM85_50_diff.data)
    print np.amin(AverageMAM85_50_diff.data)
    
    print "Ave85_50_diffJJA"
    print np.amax(AverageJJA85_50_diff.data)
    print np.amin(AverageJJA85_50_diff.data)
    
    print "Ave85_50_diff"
    print np.amax(Average85_50_diff.data)
    print np.amin(Average85_50_diff.data)
    
    #---------------------------------------------------------------------------------------------------------------------
    #PART 7: PLOT MAPS
    #load color palettes
    colourA = mpl_cm.get_cmap('YlOrRd')
    colourB = mpl_cm.get_cmap('Reds')
    
    #8Ai: ABSOLUTE TEMPERATURES - Annual
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 4.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_45_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average85_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 8.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_85_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 4.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_45_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average85_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 8.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_85_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(ObsYR, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 1971-2000 - Observed', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Observed_Annual', bbox_inches='tight')
    plt.show()
    
    
    #-------------------
    #8Aii: ABSOLUTE TEMPERATURES -Seasonal
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 4.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_45_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 4.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_45_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 4.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_45_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 4.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_45_JJA', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON85_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 8.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_85_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF85_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 8.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_85_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM85_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 8.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_85_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA85_30, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average RCP 8.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_30_85_JJA', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 4.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_45_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 4.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_45_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 4.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_45_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 4.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_45_JJA', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON85_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 8.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_85_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF85_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 8.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_85_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM85_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 8.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_85_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA85_50, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average RCP 8.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_50_85_JJA', bbox_inches='tight')
    plt.show()
   
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(ObsSON, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 1971-2000 - Observed SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Observed_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(ObsDJF, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 1971-2000 - Observed DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Observed_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(ObsMAM, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 1971-2000 - Observed MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Observed_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(ObsJJA, cmap=colourA, levels=np.arange(7,25,0.5), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 1971-2000 - Observed JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Observed_JJA', bbox_inches='tight')
    plt.show()
    
    
    #-------------------
    #8B: DIFFERENCE FROM BASELINE

    #8Bi: DIFFERENCE FROM BASELINE - Annual
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 4.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_45_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average85_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 8.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_85_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 4.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_45_Annual', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(Average85_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 8.5', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_85_Annual', bbox_inches='tight')
    plt.show()
              
    #-------------------
    #8Bii: DIFFERENCE FROM BASELINE-Seasonal
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 4.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_45_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 4.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_45_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 4.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_45_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 4.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_45_JJA', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON85_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 8.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_85_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF85_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 8.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_85_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM85_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 8.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_85_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA85_30_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2020-2049 - Average Difference RCP 8.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_30_85_JJA', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 4.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_45_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 4.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_45_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 4.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_45_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 4.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_45_JJA', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageSON85_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 8.5 SON', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_85_SON', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageDJF85_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 8.5 DJF', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_85_DJF', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageMAM85_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 8.5 MAM', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_85_MAM', bbox_inches='tight')
    plt.show()
    
    #plot map with physical features 
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.COASTLINE)   
    ax.add_feature(cartopy.feature.BORDERS)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    #set map boundary
    ax.set_extent([32.5, 36., -9, -17]) 
    #set axis tick marks
    ax.set_xticks([33, 34, 35]) 
    ax.set_yticks([-10, -12, -14, -16]) 
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #plot data and set colour range
    plot = iplt.contourf(AverageJJA85_50_diff, cmap=colourB, levels=np.arange(0,4,0.10), extend='both')
    #add colour bar index and a label
    plt.colorbar(plot, label='Celsius')
    #give map a title
    plt.title('TasMin 2040-2069 - Average Difference RCP 8.5 JJA', fontsize=10)
    #save the image of the graph and include full legend
    plt.savefig('TasMin_MAP_Ave_Diff_50_85_JJA', bbox_inches='tight')
    plt.show()
    
if __name__ == '__main__':
    main()