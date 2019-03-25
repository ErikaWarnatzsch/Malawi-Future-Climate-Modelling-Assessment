"""
Created on Thursday May 24th 2018

@author: s0899345
"""

import numpy as np
import iris
import iris.coord_categorisation as iriscc
import iris.analysis.cartography
import cf_units
from cf_units import Unit

#this file is split into parts as follows:
    #PART 1: Load and Format Observed Data
    #PART 2: Format Data 
    #PART 3: print data

def main():
    #-------------------------------------------------------------------------
    #PART 1: LOAD HISTORICAL AND OBSERVED DATA
    #bring in all the files we need and give them a name
    CRUpr= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.pre.dat.nc'
    UDelpr= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_precip.mon.total.v401.nc'
    GPCCpr= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/ESRL_PSD_GPCC_precip.mon.combined.total.v7.nc'
    CRUtas= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.tmp.dat.nc'
    UDeltas= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_air.mon.mean.v401.nc'
    CRUtasmin= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.01.1901.2016.tmn.dat.nc'
    CRUtasmax= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.01.1901.2016.tmx.dat.nc'
    CCCmaCanRCM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_mon_197101-200012.nc'
    CCCmaSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'   
    CNRM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_mon_197101-200012.nc'
    CNRMSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'
    CSIRO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'
    ICHECDMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_mon_197101-200012.nc'   
    ICHECCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_mon_197101-200012.nc' 
    ICHECKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_mon_197101-200012.nc'
    ICHECMPI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_mon_197101-200012.nc'
    ICHECSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'
    IPSL = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'
    MIROC =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc' 
    MOHCCCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_mon_197101-200012.nc' 
    MOHCKNMI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_mon_197101-200012.nc'
    MOHCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'
    MPICCLM = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_mon_197101-200012.nc' 
    MPIREMO = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_mon_197101-200012.nc' 
    MPISMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'
    NCCSMHI = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'   
    NOAA = '/exports/csce/datastore/geos/users/s0899345/AFR_44_Evo/Historical_Monthly/evspsbl_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_mon_197101-200012.nc'   
    
    #Load exactly one cube from given file
    CRUpr = iris.load_cube(CRUpr, 'precipitation')
    UDelpr = iris.load_cube(UDelpr)
    GPCCpr = iris.load_cube(GPCCpr)
    CRUtas = iris.load_cube(CRUtas, 'near-surface temperature')
    UDeltas = iris.load_cube(UDeltas)
    CRUtasmin = iris.load_cube(CRUtasmin, 'near-surface temperature minimum')  
    CRUtasmax = iris.load_cube(CRUtasmax, 'near-surface temperature maximum')  
    
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
    
    #guess bounds  
    CRUpr.coord('latitude').guess_bounds()
    UDelpr.coord('latitude').guess_bounds()
    GPCCpr.coord('latitude').guess_bounds()
    CRUtas.coord('latitude').guess_bounds()
    UDeltas.coord('latitude').guess_bounds()
    CRUtasmin.coord('latitude').guess_bounds()
    CRUtasmax.coord('latitude').guess_bounds()
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
    
    CRUpr.coord('longitude').guess_bounds()
    UDelpr.coord('longitude').guess_bounds()
    GPCCpr.coord('longitude').guess_bounds()
    CRUtas.coord('longitude').guess_bounds()
    UDeltas.coord('longitude').guess_bounds()
    CRUtasmin.coord('longitude').guess_bounds()
    CRUtasmax.coord('longitude').guess_bounds()
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
    
    
    #-------------------------------------------------------------------------
    #PART 2: FORMAT DATA GENERAL
    #time constraint to make obsered data only from 1971-2000 for monthly comparison
    iris.FUTURE.cell_datetime_objects = True
    t_constraint_obs = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CRUpr = CRUpr.extract(t_constraint_obs)
    UDelpr = UDelpr.extract(t_constraint_obs)
    GPCCpr = GPCCpr.extract(t_constraint_obs)
    CRUtas = CRUtas.extract(t_constraint_obs)
    UDeltas = UDeltas.extract(t_constraint_obs)
    CRUtasmin = CRUtasmin.extract(t_constraint_obs)
    CRUtasmax = CRUtasmax.extract(t_constraint_obs)
    
    #we are only interested in the latitude and longitude relevant to Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -12)    
    
    CRUpr = CRUpr.extract(Central_Malawi)
    UDelpr = UDelpr.extract(Central_Malawi)
    GPCCpr = GPCCpr.extract(Central_Malawi)
    CRUtas = CRUtas.extract(Central_Malawi)
    UDeltas = UDeltas.extract(Central_Malawi)
    CRUtasmin = CRUtasmin.extract(Central_Malawi)
    CRUtasmax = CRUtasmax.extract(Central_Malawi)
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
    
    #rename units to make names match after conversion
    CRUpr.units = Unit('mm per month')
    UDelpr.units = Unit('mm per month')
    GPCCpr.units = Unit('mm per month')
    CRUtas.units = Unit('Celsius') # This fixes CRUtas which is in 'Degrees Celsius' to read 'Celsius'
    UDeltas.units = Unit('Celsius') # This fixes UDEltas which is in 'degC' to read 'Celsius'
    
    
    #-------------------------------------------------------------------------
    #PART 3 FORMAT DATA MONTHLY
              
    #Convert units to match, UDelpr data in cm per month but want precipitation rate in mm per month. Since there are 10mm in a cm, the conversion is:
    Convert=10
    UDelpr_m = UDelpr*Convert
    
    #Convert evaporation units from kg m-2 s-1 to mm month-1. Since kg m-2 of water to mm of water is 1 to 1, there are 60sec/min, 60min/hour, and 24hour/day, 365.25days/year and 12months/year the conversion is:
    Convert=60*60*24*365.25/12
    
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
    
    #add month data to files
    iriscc.add_month_number(CRUpr, 'time')
    iriscc.add_month_number(UDelpr_m, 'time')
    iriscc.add_month_number(GPCCpr, 'time')
    iriscc.add_month_number(CRUtas, 'time')
    iriscc.add_month_number(UDeltas, 'time')
    iriscc.add_month_number(CRUtasmin, 'time')
    iriscc.add_month_number(CRUtasmax, 'time')
    iriscc.add_month_number(CCCmaCanRCM_m, 'time')
    iriscc.add_month_number(CCCmaSMHI_m, 'time')
    iriscc.add_month_number(CNRM_m, 'time')
    iriscc.add_month_number(CNRMSMHI_m, 'time')
    iriscc.add_month_number(CSIRO_m, 'time')
    iriscc.add_month_number(ICHECDMI_m, 'time')
    iriscc.add_month_number(ICHECCCLM_m, 'time')
    iriscc.add_month_number(ICHECKNMI_m, 'time')
    iriscc.add_month_number(ICHECMPI_m, 'time')
    iriscc.add_month_number(ICHECSMHI_m, 'time')
    iriscc.add_month_number(IPSL_m, 'time')
    iriscc.add_month_number(MIROC_m, 'time')
    iriscc.add_month_number(MOHCCCLM_m, 'time')
    iriscc.add_month_number(MOHCKNMI_m, 'time')
    iriscc.add_month_number(MOHCSMHI_m, 'time')
    iriscc.add_month_number(MPICCLM_m, 'time')
    iriscc.add_month_number(MPIREMO_m, 'time')
    iriscc.add_month_number(MPISMHI_m, 'time')
    iriscc.add_month_number(NCCSMHI_m, 'time')
    iriscc.add_month_number(NOAA_m, 'time')
    
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month
    CRUpr_m = CRUpr.aggregated_by('month_number', iris.analysis.MEAN)
    UDelpr_m = UDelpr_m.aggregated_by('month_number', iris.analysis.MEAN)
    GPCCpr_m = GPCCpr.aggregated_by('month_number', iris.analysis.MEAN)
    CRUtas_m = CRUtas.aggregated_by('month_number', iris.analysis.MEAN)
    UDeltas_m = UDeltas.aggregated_by('month_number', iris.analysis.MEAN)
    CRUtasmin_m = CRUtasmin.aggregated_by('month_number', iris.analysis.MEAN)
    CRUtasmax_m = CRUtasmax.aggregated_by('month_number', iris.analysis.MEAN)
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
    
    #Returns an array of area weights, with the same dimensions as the cube
    CRUpr_m_grid_areas = iris.analysis.cartography.area_weights(CRUpr_m)
    UDelpr_m_grid_areas = iris.analysis.cartography.area_weights(UDelpr_m)
    GPCCpr_m_grid_areas = iris.analysis.cartography.area_weights(GPCCpr_m)
    CRUtas_m_grid_areas = iris.analysis.cartography.area_weights(CRUtas_m)
    UDeltas_m_grid_areas = iris.analysis.cartography.area_weights (UDeltas_m)
    CRUtasmin_m_grid_areas = iris.analysis.cartography.area_weights(CRUtasmin_m)
    CRUtasmax_m_grid_areas = iris.analysis.cartography.area_weights(CRUtasmax_m)
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
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CRUpr_m_mean = CRUpr_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUpr_m_grid_areas)
    UDelpr_m_mean = UDelpr_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelpr_m_grid_areas)
    GPCCpr_m_mean = GPCCpr_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCpr_m_grid_areas)
    CRUtas_m_mean = CRUtas_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtas_m_grid_areas)
    UDeltas_m_mean = UDeltas_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDeltas_m_grid_areas)
    CRUtasmin_m_mean = CRUtasmin_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmin_m_grid_areas)
    CRUtasmax_m_mean = CRUtasmax_m.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmax_m_grid_areas)
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
    
    #create average of observed baseline data
    Obs_pr = (CRUpr_m_mean.data + UDelpr_m_mean.data + GPCCpr_m_mean.data)/3
    Obs_tas = (CRUtas_m_mean.data + UDeltas_m_mean.data)/2
    Obs_tasmin = CRUtasmin_m_mean.data
    Obs_tasmax = CRUtasmax_m_mean.data
    Ave_evo = (CCCmaCanRCM_m_mean.data + CCCmaSMHI_m_mean.data + CNRM_m_mean.data + CNRMSMHI_m_mean.data + CSIRO_m_mean.data + ICHECDMI_m_mean.data + ICHECCCLM_m_mean.data + ICHECKNMI_m_mean.data + ICHECMPI_m_mean.data + ICHECSMHI_m_mean.data + IPSL_m_mean.data + MIROC_m_mean.data + MOHCCCLM_m_mean.data + MOHCKNMI_m_mean.data + MOHCSMHI_m_mean.data + MPICCLM_m_mean.data + MPIREMO_m_mean.data + MPISMHI_m_mean.data + NCCSMHI_m_mean.data + NOAA_m_mean.data)/20
    
    
    #-------------------------------------------------------------------------
    #PART 4: PRINT MONTHLY DATA
    import csv
    with open('output_Historical_monthly.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Parameter', 'Means'])
    
        writer.writerow(["Observed_Pr"] + Obs_pr.data.flatten().astype(np.str).tolist())
        writer.writerow(["Observed_Tas"] + Obs_tas.data.flatten().astype(np.str).tolist())
        writer.writerow(["Observed_Tasmin"] + Obs_tasmin.data.flatten().astype(np.str).tolist())
        writer.writerow(["Observed_Tasmax"] + Obs_tasmax.data.flatten().astype(np.str).tolist())
        writer.writerow(["Historical_Evo"] + Ave_evo.data.flatten().astype(np.str).tolist())

    #-------------------------------------------------------------------------
    #PART 5: FORMAT ANNUAL AND SEASONAL DATA
    #Convert units to match, UDelpr data in cm per month but want precipitation rate in mm per year. Since there are 12 months in the year and 10mm in a cm, the conversion is:
    Convert=10*12
    UDelpr = UDelpr*Convert
    
    #Convert units to match, CRUpr and GPCCpr data in mm per month but want precipitation rate in mm per year. Since there are 12 months in the year, the conversion is:
    Convert=12
    CRUpr = CRUpr*Convert
    GPCCpr = GPCCpr*Convert
    
    #Convert evaporation units from kg m-2 s-1 to mm year-1. Since kg m-2 of water to mm of water is 1 to 1, there are 60sec/min, 60min/hour, 24hour/day 365.25days/year the conversion is:
    Convert=60*60*24*365.25
    
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
    
    #add year data to files
    iriscc.add_year(CRUpr,'time')
    iriscc.add_year(UDelpr,'time')
    iriscc.add_year(GPCCpr,'time')
    iriscc.add_year(CRUtas,'time')
    iriscc.add_year(UDeltas,'time')
    iriscc.add_year(CRUtasmin,'time')
    iriscc.add_year(CRUtasmax,'time')
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
    
    #limit to a season
    SON = iris.Constraint(season='son')
    DJF = iris.Constraint(season='djf')
    MAM = iris.Constraint(season='mam')
    JJA = iris.Constraint(season='jja')
    
    #add season data to files
    iriscc.add_season(CRUpr,'time')
    iriscc.add_season(UDelpr,'time')
    iriscc.add_season(GPCCpr,'time')
    iriscc.add_season(CRUtas,'time')
    iriscc.add_season(UDeltas,'time')
    iriscc.add_season(CRUtasmin,'time')
    iriscc.add_season(CRUtasmax,'time')
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
    
    #extract only the season we are interested in
    CRUprSON = CRUpr.extract(SON)
    UDelprSON = UDelpr.extract(SON)
    GPCCprSON = GPCCpr.extract(SON)
    CRUtasSON = CRUtas.extract(SON)
    UDeltasSON = UDeltas.extract(SON)
    CRUtasminSON = CRUtasmin.extract(SON)
    CRUtasmaxSON = CRUtasmax.extract(SON)
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
    
    CRUprDJF = CRUpr.extract(DJF)
    UDelprDJF = UDelpr.extract(DJF)
    GPCCprDJF = GPCCpr.extract(DJF)
    CRUtasDJF = CRUtas.extract(DJF)
    UDeltasDJF = UDeltas.extract(DJF)
    CRUtasminDJF = CRUtasmin.extract(DJF)
    CRUtasmaxDJF = CRUtasmax.extract(DJF)
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
    
    CRUprMAM = CRUpr.extract(MAM)
    UDelprMAM = UDelpr.extract(MAM)
    GPCCprMAM = GPCCpr.extract(MAM)
    CRUtasMAM = CRUtas.extract(MAM)
    UDeltasMAM = UDeltas.extract(MAM)
    CRUtasminMAM = CRUtasmin.extract(MAM)
    CRUtasmaxMAM = CRUtasmax.extract(MAM)
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
    
    CRUprJJA = CRUpr.extract(JJA)
    UDelprJJA = UDelpr.extract(JJA)
    GPCCprJJA = GPCCpr.extract(JJA)
    CRUtasJJA = CRUtas.extract(JJA)
    UDeltasJJA = UDeltas.extract(JJA)
    CRUtasminJJA = CRUtasmin.extract(JJA)
    CRUtasmaxJJA = CRUtasmax.extract(JJA)
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
    
    #We are interested in plotting the data by year, so we need to take a mean of all the data by year
    CRUprSON = CRUprSON.aggregated_by('year', iris.analysis.MEAN)
    UDelprSON = UDelprSON.aggregated_by('year', iris.analysis.MEAN)
    GPCCprSON = GPCCprSON.aggregated_by('year', iris.analysis.MEAN)
    CRUtasSON = CRUtasSON.aggregated_by('year', iris.analysis.MEAN)
    UDeltasSON = UDeltasSON.aggregated_by('year', iris.analysis.MEAN)
    CRUtasminSON = CRUtasminSON.aggregated_by('year', iris.analysis.MEAN)
    CRUtasmaxSON = CRUtasmaxSON.aggregated_by('year', iris.analysis.MEAN)
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
    
    CRUprDJF = CRUprDJF.aggregated_by('year', iris.analysis.MEAN)
    UDelprDJF = UDelprDJF.aggregated_by('year', iris.analysis.MEAN)
    GPCCprDJF = GPCCprDJF.aggregated_by('year', iris.analysis.MEAN)
    CRUtasDJF = CRUtasDJF.aggregated_by('year', iris.analysis.MEAN)
    UDeltasDJF = UDeltasDJF.aggregated_by('year', iris.analysis.MEAN)
    CRUtasminDJF = CRUtasminDJF.aggregated_by('year', iris.analysis.MEAN)
    CRUtasmaxDJF = CRUtasmaxDJF.aggregated_by('year', iris.analysis.MEAN)
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
    
    CRUprMAM = CRUprMAM.aggregated_by('year', iris.analysis.MEAN)
    UDelprMAM = UDelprMAM.aggregated_by('year', iris.analysis.MEAN)
    GPCCprMAM = GPCCprMAM.aggregated_by('year', iris.analysis.MEAN)
    CRUtasMAM = CRUtasMAM.aggregated_by('year', iris.analysis.MEAN)
    UDeltasMAM = UDeltasMAM.aggregated_by('year', iris.analysis.MEAN)
    CRUtasminMAM = CRUtasminMAM.aggregated_by('year', iris.analysis.MEAN)
    CRUtasmaxMAM = CRUtasmaxMAM.aggregated_by('year', iris.analysis.MEAN)
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
    
    CRUprJJA = CRUprJJA.aggregated_by('year', iris.analysis.MEAN)
    UDelprJJA = UDelprJJA.aggregated_by('year', iris.analysis.MEAN)
    GPCCprJJA = GPCCprJJA.aggregated_by('year', iris.analysis.MEAN)
    CRUtasJJA = CRUtasJJA.aggregated_by('year', iris.analysis.MEAN)
    UDeltasJJA = UDeltasJJA.aggregated_by('year', iris.analysis.MEAN)
    CRUtasminJJA = CRUtasminJJA.aggregated_by('year', iris.analysis.MEAN)
    CRUtasmaxJJA = CRUtasmaxJJA.aggregated_by('year', iris.analysis.MEAN)
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
    
    CRUprYR = CRUpr.aggregated_by('year', iris.analysis.MEAN)
    UDelprYR = UDelpr.aggregated_by('year', iris.analysis.MEAN)
    GPCCprYR = GPCCpr.aggregated_by('year', iris.analysis.MEAN)
    CRUtasYR = CRUtas.aggregated_by('year', iris.analysis.MEAN)
    UDeltasYR = UDeltas.aggregated_by('year', iris.analysis.MEAN)
    CRUtasminYR = CRUtasmin.aggregated_by('year', iris.analysis.MEAN)
    CRUtasmaxYR = CRUtasmax.aggregated_by('year', iris.analysis.MEAN)
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
    
    #Returns an array of area weights, with the same dimensions as the cube
    CRUprSON_grid_areas = iris.analysis.cartography.area_weights(CRUprSON)
    UDelprSON_grid_areas = iris.analysis.cartography.area_weights(UDelprSON)
    GPCCprSON_grid_areas = iris.analysis.cartography.area_weights(GPCCprSON)
    CRUtasSON_grid_areas = iris.analysis.cartography.area_weights(CRUtasSON)
    UDeltasSON_grid_areas = iris.analysis.cartography.area_weights(UDeltasSON)
    CRUtasminSON_grid_areas = iris.analysis.cartography.area_weights(CRUtasminSON)
    CRUtasmaxSON_grid_areas = iris.analysis.cartography.area_weights(CRUtasmaxSON)
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
    
    CRUprDJF_grid_areas = iris.analysis.cartography.area_weights(CRUprDJF)
    UDelprDJF_grid_areas = iris.analysis.cartography.area_weights(UDelprDJF)
    GPCCprDJF_grid_areas = iris.analysis.cartography.area_weights(GPCCprDJF)
    CRUtasDJF_grid_areas = iris.analysis.cartography.area_weights(CRUtasDJF)
    UDeltasDJF_grid_areas = iris.analysis.cartography.area_weights(UDeltasDJF)
    CRUtasminDJF_grid_areas = iris.analysis.cartography.area_weights(CRUtasminDJF)
    CRUtasmaxDJF_grid_areas = iris.analysis.cartography.area_weights(CRUtasmaxDJF)
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
    
    CRUprMAM_grid_areas = iris.analysis.cartography.area_weights(CRUprMAM)
    UDelprMAM_grid_areas = iris.analysis.cartography.area_weights(UDelprMAM)
    GPCCprMAM_grid_areas = iris.analysis.cartography.area_weights(GPCCprMAM)
    CRUtasMAM_grid_areas = iris.analysis.cartography.area_weights(CRUtasMAM)
    UDeltasMAM_grid_areas = iris.analysis.cartography.area_weights(UDeltasMAM)
    CRUtasminMAM_grid_areas = iris.analysis.cartography.area_weights(CRUtasminMAM)
    CRUtasmaxMAM_grid_areas = iris.analysis.cartography.area_weights(CRUtasmaxMAM)
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
    
    CRUprJJA_grid_areas = iris.analysis.cartography.area_weights(CRUprJJA)
    UDelprJJA_grid_areas = iris.analysis.cartography.area_weights(UDelprJJA)
    GPCCprJJA_grid_areas = iris.analysis.cartography.area_weights(GPCCprJJA)
    CRUtasJJA_grid_areas = iris.analysis.cartography.area_weights(CRUtasJJA)
    UDeltasJJA_grid_areas = iris.analysis.cartography.area_weights(UDeltasJJA)
    CRUtasminJJA_grid_areas = iris.analysis.cartography.area_weights(CRUtasminJJA)
    CRUtasmaxJJA_grid_areas = iris.analysis.cartography.area_weights(CRUtasmaxJJA)
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
    
    CRUprYR_grid_areas = iris.analysis.cartography.area_weights(CRUprYR)
    UDelprYR_grid_areas = iris.analysis.cartography.area_weights(UDelprYR)
    GPCCprYR_grid_areas = iris.analysis.cartography.area_weights(GPCCprYR)
    CRUtasYR_grid_areas = iris.analysis.cartography.area_weights(CRUtasYR)
    UDeltasYR_grid_areas = iris.analysis.cartography.area_weights(UDeltasYR)
    CRUtasminYR_grid_areas = iris.analysis.cartography.area_weights(CRUtasminYR)
    CRUtasmaxYR_grid_areas = iris.analysis.cartography.area_weights(CRUtasmaxYR)
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
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CRUprSON_mean = CRUprSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUprSON_grid_areas)
    UDelprSON_mean = UDelprSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelprSON_grid_areas)
    GPCCprSON_mean = GPCCprSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCprSON_grid_areas)
    CRUtasSON_mean = CRUtasSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasSON_grid_areas)
    UDeltasSON_mean = UDeltasSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDeltasSON_grid_areas)
    CRUtasminSON_mean = CRUtasminSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasminSON_grid_areas)
    CRUtasmaxSON_mean = CRUtasmaxSON.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmaxSON_grid_areas)
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
    
    CRUprDJF_mean = CRUprDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUprDJF_grid_areas)
    UDelprDJF_mean = UDelprDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelprDJF_grid_areas)
    GPCCprDJF_mean = GPCCprDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCprDJF_grid_areas)
    CRUtasDJF_mean = CRUtasDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasDJF_grid_areas)
    UDeltasDJF_mean = UDeltasDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDeltasDJF_grid_areas)
    CRUtasminDJF_mean = CRUtasminDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasminDJF_grid_areas)
    CRUtasmaxDJF_mean = CRUtasmaxDJF.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmaxDJF_grid_areas)
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
    
    CRUprMAM_mean = CRUprMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUprMAM_grid_areas)
    UDelprMAM_mean = UDelprMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelprMAM_grid_areas)
    GPCCprMAM_mean = GPCCprMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCprMAM_grid_areas)
    CRUtasMAM_mean = CRUtasMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasMAM_grid_areas)
    UDeltasMAM_mean = UDeltasMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDeltasMAM_grid_areas)
    CRUtasminMAM_mean = CRUtasminMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasminMAM_grid_areas)
    CRUtasmaxMAM_mean = CRUtasmaxMAM.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmaxMAM_grid_areas)
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
    
    CRUprJJA_mean = CRUprJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUprJJA_grid_areas)
    UDelprJJA_mean = UDelprJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelprJJA_grid_areas)
    GPCCprJJA_mean = GPCCprJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCprJJA_grid_areas)
    CRUtasJJA_mean = CRUtasJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasJJA_grid_areas)
    UDeltasJJA_mean = UDeltasJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDeltasJJA_grid_areas)
    CRUtasminJJA_mean = CRUtasminJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasminJJA_grid_areas)
    CRUtasmaxJJA_mean = CRUtasmaxJJA.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmaxJJA_grid_areas)
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
    
    CRUprYR_mean = CRUprYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUprYR_grid_areas)
    UDelprYR_mean = UDelprYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDelprYR_grid_areas)
    GPCCprYR_mean = GPCCprYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCCprYR_grid_areas)
    CRUtasYR_mean = CRUtasYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasYR_grid_areas)
    UDeltasYR_mean = UDeltasYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDeltasYR_grid_areas)
    CRUtasminYR_mean = CRUtasminYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasminYR_grid_areas)
    CRUtasmaxYR_mean = CRUtasmaxYR.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRUtasmaxYR_grid_areas)
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
    
    
    #-------------------------------------------------------------------------
    #PART 6: PRINT ANNUAL AND SEASONAL DATA 
    import csv
    with open('output_Historical_AnnualSeasonal.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Parameter', 'Means'])
        
        writer.writerow(["CRUprYR_mean"] + CRUprYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelprYR_mean"] + UDelprYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCprYR_mean"] + GPCCprYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasYR_mean"] + CRUtasYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDeltasYR_mean"] + UDeltasYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasminYR_mean"] + CRUtasminYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasmaxYR_mean"] + CRUtasmaxYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaCanRCMYR_mean"] + CCCmaCanRCMYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIYR_mean"] + CCCmaSMHIYR_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMYR_mean"] + CNRMYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIYR_mean"] +CNRMSMHIYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CSIROYR_mean"] +CSIROYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIYR_mean"] +ICHECDMIYR_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLMYR_mean"] +ICHECCCLMYR_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIYR_mean"] +ICHECKNMIYR_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPIYR_mean"] +ICHECMPIYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHIYR_mean"] +ICHECSMHIYR_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLYR_mean"] +IPSLYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCYR_mean"] +MIROCYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMYR_mean"] +MOHCCCLMYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMIYR_mean"] +MOHCKNMIYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHIYR_mean"] +MOHCSMHIYR_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLMYR_mean"] +MPICCLMYR_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOYR_mean"] +MPIREMOYR_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHIYR_mean"] +MPISMHIYR_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHIYR_mean"] +NCCSMHIYR_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAAYR_mean"] +NOAAYR_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CRUprSON_mean"] + CRUprSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelprSON_mean"] + UDelprSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCprSON_mean"] + GPCCprSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasSON_mean"] + CRUtasSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDeltasSON_mean"] + UDeltasSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasminSON_mean"] + CRUtasminSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasmaxSON_mean"] + CRUtasmaxSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaCanRCMSON_mean"] + CCCmaCanRCMSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHISON_mean"] + CCCmaSMHISON_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMSON_mean"] + CNRMSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHISON_mean"] +CNRMSMHISON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CSIROSON_mean"] +CSIROSON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMISON_mean"] +ICHECDMISON_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLMSON_mean"] +ICHECCCLMSON_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMISON_mean"] +ICHECKNMISON_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPISON_mean"] +ICHECMPISON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHISON_mean"] +ICHECSMHISON_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLSON_mean"] +IPSLSON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCSON_mean"] +MIROCSON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMSON_mean"] +MOHCCCLMSON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMISON_mean"] +MOHCKNMISON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHISON_mean"] +MOHCSMHISON_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLMSON_mean"] +MPICCLMSON_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOSON_mean"] +MPIREMOSON_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHISON_mean"] +MPISMHISON_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHISON_mean"] +NCCSMHISON_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAASON_mean"] +NOAASON_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CRUprDJF_mean"] + CRUprDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelprDJF_mean"] + UDelprDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCprDJF_mean"] + GPCCprDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasDJF_mean"] + CRUtasDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDeltasDJF_mean"] + UDeltasDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasminDJF_mean"] + CRUtasminDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasmaxDJF_mean"] + CRUtasmaxDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaCanRCMDJF_mean"] + CCCmaCanRCMDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIDJF_mean"] + CCCmaSMHIDJF_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMDJF_mean"] + CNRMDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIDJF_mean"] +CNRMSMHIDJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CSIRODJF_mean"] +CSIRODJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIDJF_mean"] +ICHECDMIDJF_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLMDJF_mean"] +ICHECCCLMDJF_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIDJF_mean"] +ICHECKNMIDJF_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPIDJF_mean"] +ICHECMPIDJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHIDJF_mean"] +ICHECSMHIDJF_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLDJF_mean"] +IPSLDJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCDJF_mean"] +MIROCDJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMDJF_mean"] +MOHCCCLMDJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMIDJF_mean"] +MOHCKNMIDJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHIDJF_mean"] +MOHCSMHIDJF_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLMDJF_mean"] +MPICCLMDJF_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMODJF_mean"] +MPIREMODJF_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHIDJF_mean"] +MPISMHIDJF_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHIDJF_mean"] +NCCSMHIDJF_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAADJF_mean"] +NOAADJF_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CRUprMAM_mean"] + CRUprMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelprMAM_mean"] + UDelprMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCprMAM_mean"] + GPCCprMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasMAM_mean"] + CRUtasMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDeltasMAM_mean"] + UDeltasMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasminMAM_mean"] + CRUtasminMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasmaxMAM_mean"] + CRUtasmaxMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaCanRCMMAM_mean"] + CCCmaCanRCMMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIMAM_mean"] + CCCmaSMHIMAM_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMMAM_mean"] + CNRMMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIMAM_mean"] +CNRMSMHIMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CSIROMAM_mean"] +CSIROMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIMAM_mean"] +ICHECDMIMAM_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLMMAM_mean"] +ICHECCCLMMAM_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIMAM_mean"] +ICHECKNMIMAM_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPIMAM_mean"] +ICHECMPIMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHIMAM_mean"] +ICHECSMHIMAM_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLMAM_mean"] +IPSLMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCMAM_mean"] +MIROCMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMMAM_mean"] +MOHCCCLMMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMIMAM_mean"] +MOHCKNMIMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHIMAM_mean"] +MOHCSMHIMAM_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLMMAM_mean"] +MPICCLMMAM_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOMAM_mean"] +MPIREMOMAM_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHIMAM_mean"] +MPISMHIMAM_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHIMAM_mean"] +NCCSMHIMAM_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAAMAM_mean"] +NOAAMAM_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CRUprJJA_mean"] + CRUprJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDelprJJA_mean"] + UDelprJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["GPCCprJJA_mean"] + GPCCprJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasJJA_mean"] + CRUtasJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["UDeltasJJA_mean"] + UDeltasJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasminJJA_mean"] + CRUtasminJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CRUtasmaxJJA_mean"] + CRUtasmaxJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaCanRCMJJA_mean"] + CCCmaCanRCMJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHIJJA_mean"] + CCCmaSMHIJJA_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["CNRMJJA_mean"] + CNRMJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHIJJA_mean"] +CNRMSMHIJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CSIROJJA_mean"] +CSIROJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMIJJA_mean"] +ICHECDMIJJA_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLMJJA_mean"] +ICHECCCLMJJA_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMIJJA_mean"] +ICHECKNMIJJA_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPIJJA_mean"] +ICHECMPIJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHIJJA_mean"] +ICHECSMHIJJA_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["IPSLJJA_mean"] +IPSLJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROCJJA_mean"] +MIROCJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLMJJA_mean"] +MOHCCCLMJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMIJJA_mean"] +MOHCKNMIJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHIJJA_mean"] +MOHCSMHIJJA_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLMJJA_mean"] +MPICCLMJJA_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMOJJA_mean"] +MPIREMOJJA_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["MPISMHIJJA_mean"] +MPISMHIJJA_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NCCSMHIJJA_mean"] +NCCSMHIJJA_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAAJJA_mean"] +NOAAJJA_mean.data.flatten().astype(np.str).tolist())
    
if __name__ == '__main__':
    main()
    
    
    