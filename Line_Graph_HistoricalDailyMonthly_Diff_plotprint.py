"""
Created on Monday 13 June 2019

@author: s0899345
"""

import matplotlib.pyplot as plt
import iris
import iris.coord_categorisation as iriscc
import iris.plot as iplt
import iris.analysis.cartography
import numpy as np
import calendar
import cf_units
from cf_units import Unit

#this file is split into parts as follows:
    #PART 1: load and format all past models
    #PART 2: load observed data
    #PART 3: format files to be plot specific for monthly plotting 
    #PART 4: re-baseline past files
    #PART 5: print yearly data
    
    
def main():
    #-------------------------------------------------------------------------
    #PART 1: LOAD and FORMAT ALL PAST MODELS   
    CCCmaCanRCM_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_tas =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_tas = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tas/Historical_daily/tas_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    CCCmaCanRCM_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_tasmin =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_tasmin = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmin/Historical_daily/tasmin_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    CCCmaCanRCM_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_tasmax =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_tasmax = '/exports/csce/datastore/geos/users/s0899345/AFR_44_tasmax/Historical_daily/tasmax_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    CCCmaCanRCM_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CCCma-CanESM2_historical_r1i1p1_CCCma-CanRCM4_r2_day_19710101-20001231.nc'
    CCCmaSMHI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CCCma-CanESM2_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    CNRM_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'
    CNRMSMHI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    CSIRO_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    ICHECDMI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r3i1p1_DMI-HIRHAM5_v2_day_19710101-20001231.nc'   
    ICHECCCLM_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'    
    ICHECKNMI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r1i1p1_KNMI-RACMO22T_v1_day_19710101-20001231.nc'
    ICHECMPI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'
    ICHECSMHI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_ICHEC-EC-EARTH_historical_r12i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    IPSL_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MIROC_pr =  '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MIROC-MIROC5_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc' 
    MOHCCCLM_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc' 
    MOHCKNMI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_KNMI-RACMO22T_v2_day_19710101-20001231.nc'
    MOHCSMHI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MOHC-HadGEM2-ES_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    MPICCLM_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_CLMcom-CCLM4-8-17_v1_day_19710101-20001231.nc'     
    MPIREMO_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_MPI-CSC-REMO2009_v1_day_19710101-20001231.nc'    
    MPISMHI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_MPI-M-MPI-ESM-LR_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    NCCSMHI_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_NCC-NorESM1-M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'   
    NOAA_pr = '/exports/csce/datastore/geos/users/s0899345/AFR_44_pr/Historical_daily/pr_AFR-44_NOAA-GFDL-GFDL-ESM2M_historical_r1i1p1_SMHI-RCA4_v1_day_19710101-20001231.nc'
    
    #Load exactly one cube from given file
    CCCmaCanRCM_tas =  iris.load_cube(CCCmaCanRCM_tas)
    CCCmaSMHI_tas =  iris.load_cube(CCCmaSMHI_tas)
    CNRM_tas =  iris.load_cube(CNRM_tas)
    CNRMSMHI_tas =  iris.load_cube(CNRMSMHI_tas)
    CSIRO_tas =  iris.load_cube(CSIRO_tas)
    ICHECDMI_tas =  iris.load_cube(ICHECDMI_tas, 'air_temperature')
    ICHECCCLM_tas =  iris.load_cube(ICHECCCLM_tas)
    ICHECKNMI_tas =  iris.load_cube(ICHECKNMI_tas)
    ICHECMPI_tas =  iris.load_cube(ICHECMPI_tas)
    ICHECSMHI_tas =  iris.load_cube(ICHECSMHI_tas)
    IPSL_tas =  iris.load_cube(IPSL_tas)
    MIROC_tas =  iris.load_cube(MIROC_tas)
    MOHCCCLM_tas =  iris.load_cube(MOHCCCLM_tas)
    MOHCKNMI_tas =  iris.load_cube(MOHCKNMI_tas)
    MOHCSMHI_tas =  iris.load_cube(MOHCSMHI_tas)
    MPICCLM_tas =  iris.load_cube(MPICCLM_tas)
    MPIREMO_tas =  iris.load_cube(MPIREMO_tas)
    MPISMHI_tas =  iris.load_cube(MPISMHI_tas)
    NCCSMHI_tas =  iris.load_cube(NCCSMHI_tas)
    NOAA_tas =  iris.load_cube(NOAA_tas)
    
    CCCmaCanRCM_tasmin =  iris.load_cube(CCCmaCanRCM_tasmin)
    CCCmaSMHI_tasmin =  iris.load_cube(CCCmaSMHI_tasmin)
    CNRM_tasmin =  iris.load_cube(CNRM_tasmin)
    CNRMSMHI_tasmin =  iris.load_cube(CNRMSMHI_tasmin)
    CSIRO_tasmin =  iris.load_cube(CSIRO_tasmin)
    ICHECDMI_tasmin =  iris.load_cube(ICHECDMI_tasmin, 'air_temperature')
    ICHECCCLM_tasmin =  iris.load_cube(ICHECCCLM_tasmin)
    ICHECKNMI_tasmin =  iris.load_cube(ICHECKNMI_tasmin)
    ICHECMPI_tasmin =  iris.load_cube(ICHECMPI_tasmin)
    ICHECSMHI_tasmin =  iris.load_cube(ICHECSMHI_tasmin)
    IPSL_tasmin =  iris.load_cube(IPSL_tasmin)
    MIROC_tasmin =  iris.load_cube(MIROC_tasmin)
    MOHCCCLM_tasmin =  iris.load_cube(MOHCCCLM_tasmin)
    MOHCKNMI_tasmin =  iris.load_cube(MOHCKNMI_tasmin)
    MOHCSMHI_tasmin =  iris.load_cube(MOHCSMHI_tasmin)
    MPICCLM_tasmin =  iris.load_cube(MPICCLM_tasmin)
    MPIREMO_tasmin =  iris.load_cube(MPIREMO_tasmin)
    MPISMHI_tasmin =  iris.load_cube(MPISMHI_tasmin)
    NCCSMHI_tasmin =  iris.load_cube(NCCSMHI_tasmin)
    NOAA_tasmin =  iris.load_cube(NOAA_tasmin)
    
    CCCmaCanRCM_tasmax =  iris.load_cube(CCCmaCanRCM_tasmax)
    CCCmaSMHI_tasmax =  iris.load_cube(CCCmaSMHI_tasmax)
    CNRM_tasmax =  iris.load_cube(CNRM_tasmax)
    CNRMSMHI_tasmax =  iris.load_cube(CNRMSMHI_tasmax)
    CSIRO_tasmax =  iris.load_cube(CSIRO_tasmax)
    ICHECDMI_tasmax =  iris.load_cube(ICHECDMI_tasmax, 'air_temperature')
    ICHECCCLM_tasmax =  iris.load_cube(ICHECCCLM_tasmax)
    ICHECKNMI_tasmax =  iris.load_cube(ICHECKNMI_tasmax)
    ICHECMPI_tasmax =  iris.load_cube(ICHECMPI_tasmax)
    ICHECSMHI_tasmax =  iris.load_cube(ICHECSMHI_tasmax)
    IPSL_tasmax =  iris.load_cube(IPSL_tasmax)
    MIROC_tasmax =  iris.load_cube(MIROC_tasmax)
    MOHCCCLM_tasmax =  iris.load_cube(MOHCCCLM_tasmax)
    MOHCKNMI_tasmax =  iris.load_cube(MOHCKNMI_tasmax)
    MOHCSMHI_tasmax =  iris.load_cube(MOHCSMHI_tasmax)
    MPICCLM_tasmax =  iris.load_cube(MPICCLM_tasmax)
    MPIREMO_tasmax =  iris.load_cube(MPIREMO_tasmax)
    MPISMHI_tasmax =  iris.load_cube(MPISMHI_tasmax)
    NCCSMHI_tasmax =  iris.load_cube(NCCSMHI_tasmax)
    NOAA_tasmax =  iris.load_cube(NOAA_tasmax)
    
    CCCmaCanRCM_pr =  iris.load_cube(CCCmaCanRCM_pr)
    CCCmaSMHI_pr =  iris.load_cube(CCCmaSMHI_pr)
    CNRM_pr =  iris.load_cube(CNRM_pr)
    CNRMSMHI_pr =  iris.load_cube(CNRMSMHI_pr)
    CSIRO_pr =  iris.load_cube(CSIRO_pr)
    ICHECDMI_pr =  iris.load_cube(ICHECDMI_pr, 'precipitation_flux')
    ICHECCCLM_pr =  iris.load_cube(ICHECCCLM_pr)
    ICHECKNMI_pr =  iris.load_cube(ICHECKNMI_pr)
    ICHECMPI_pr =  iris.load_cube(ICHECMPI_pr)
    ICHECSMHI_pr =  iris.load_cube(ICHECSMHI_pr)
    IPSL_pr =  iris.load_cube(IPSL_pr)
    MIROC_pr =  iris.load_cube(MIROC_pr)
    MOHCCCLM_pr =  iris.load_cube(MOHCCCLM_pr)
    MOHCKNMI_pr =  iris.load_cube(MOHCKNMI_pr)
    MOHCSMHI_pr =  iris.load_cube(MOHCSMHI_pr)
    MPICCLM_pr =  iris.load_cube(MPICCLM_pr)
    MPIREMO_pr =  iris.load_cube(MPIREMO_pr)
    MPISMHI_pr =  iris.load_cube(MPISMHI_pr)
    NCCSMHI_pr =  iris.load_cube(NCCSMHI_pr)
    NOAA_pr =  iris.load_cube(NOAA_pr)
    
    #remove flat latitude and longitude and only use grid latitude and grid longitude to make consistent with the observed data, also make sure all of the longitudes are monotonic. 
    lats = iris.coords.DimCoord(CCCmaCanRCM_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM_tas.remove_coord('latitude')
    CCCmaCanRCM_tas.remove_coord('longitude')
    CCCmaCanRCM_tas.remove_coord('grid_latitude')
    CCCmaCanRCM_tas.remove_coord('grid_longitude')
    CCCmaCanRCM_tas.add_dim_coord(lats, 1)
    CCCmaCanRCM_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI_tas.remove_coord('latitude')
    CCCmaSMHI_tas.remove_coord('longitude')
    CCCmaSMHI_tas.remove_coord('grid_latitude')
    CCCmaSMHI_tas.remove_coord('grid_longitude')
    CCCmaSMHI_tas.add_dim_coord(lats, 1)
    CCCmaSMHI_tas.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM_tas.remove_coord('latitude')
    CNRM_tas.remove_coord('longitude')
    CNRM_tas.remove_coord('grid_latitude')
    CNRM_tas.remove_coord('grid_longitude')
    CNRM_tas.add_dim_coord(lats, 1)
    CNRM_tas.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI_tas.remove_coord('latitude')
    CNRMSMHI_tas.remove_coord('longitude')
    CNRMSMHI_tas.remove_coord('grid_latitude')
    CNRMSMHI_tas.remove_coord('grid_longitude')
    CNRMSMHI_tas.add_dim_coord(lats, 1)
    CNRMSMHI_tas.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO_tas.remove_coord('latitude')
    CSIRO_tas.remove_coord('longitude')
    CSIRO_tas.remove_coord('grid_latitude')
    CSIRO_tas.remove_coord('grid_longitude')
    CSIRO_tas.add_dim_coord(lats, 1)
    CSIRO_tas.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI_tas.remove_coord('latitude')
    ICHECDMI_tas.remove_coord('longitude')
    ICHECDMI_tas.remove_coord('grid_latitude')
    ICHECDMI_tas.remove_coord('grid_longitude')
    ICHECDMI_tas.add_dim_coord(lats, 1)
    ICHECDMI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM_tas.remove_coord('latitude')
    ICHECCCLM_tas.remove_coord('longitude')
    ICHECCCLM_tas.remove_coord('grid_latitude')
    ICHECCCLM_tas.remove_coord('grid_longitude')
    ICHECCCLM_tas.add_dim_coord(lats, 1)
    ICHECCCLM_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI_tas.remove_coord('latitude')
    ICHECKNMI_tas.remove_coord('longitude')
    ICHECKNMI_tas.remove_coord('grid_latitude')
    ICHECKNMI_tas.remove_coord('grid_longitude')
    ICHECKNMI_tas.add_dim_coord(lats, 1)
    ICHECKNMI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI_tas.remove_coord('latitude')
    ICHECMPI_tas.remove_coord('longitude')
    ICHECMPI_tas.remove_coord('grid_latitude')
    ICHECMPI_tas.remove_coord('grid_longitude')
    ICHECMPI_tas.add_dim_coord(lats, 1)
    ICHECMPI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI_tas.remove_coord('latitude')
    ICHECSMHI_tas.remove_coord('longitude')
    ICHECSMHI_tas.remove_coord('grid_latitude')
    ICHECSMHI_tas.remove_coord('grid_longitude')
    ICHECSMHI_tas.add_dim_coord(lats, 1)
    ICHECSMHI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL_tas.remove_coord('latitude')
    IPSL_tas.remove_coord('longitude')
    IPSL_tas.remove_coord('grid_latitude')
    IPSL_tas.remove_coord('grid_longitude')
    IPSL_tas.add_dim_coord(lats, 1)
    IPSL_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC_tas.remove_coord('latitude')
    MIROC_tas.remove_coord('longitude')
    MIROC_tas.remove_coord('grid_latitude')
    MIROC_tas.remove_coord('grid_longitude')
    MIROC_tas.add_dim_coord(lats, 1)
    MIROC_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM_tas.remove_coord('latitude')
    MOHCCCLM_tas.remove_coord('longitude')
    MOHCCCLM_tas.remove_coord('grid_latitude')
    MOHCCCLM_tas.remove_coord('grid_longitude')
    MOHCCCLM_tas.add_dim_coord(lats, 1)
    MOHCCCLM_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI_tas.remove_coord('latitude')
    MOHCKNMI_tas.remove_coord('longitude')
    MOHCKNMI_tas.remove_coord('grid_latitude')
    MOHCKNMI_tas.remove_coord('grid_longitude')
    MOHCKNMI_tas.add_dim_coord(lats, 1)
    MOHCKNMI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI_tas.remove_coord('latitude')
    MOHCSMHI_tas.remove_coord('longitude')
    MOHCSMHI_tas.remove_coord('grid_latitude')
    MOHCSMHI_tas.remove_coord('grid_longitude')
    MOHCSMHI_tas.add_dim_coord(lats, 1)
    MOHCSMHI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM_tas.remove_coord('latitude')
    MPICCLM_tas.remove_coord('longitude')
    MPICCLM_tas.remove_coord('grid_latitude')
    MPICCLM_tas.remove_coord('grid_longitude')
    MPICCLM_tas.add_dim_coord(lats, 1)
    MPICCLM_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO_tas.remove_coord('latitude')
    MPIREMO_tas.remove_coord('longitude')
    MPIREMO_tas.remove_coord('grid_latitude')
    MPIREMO_tas.remove_coord('grid_longitude')
    MPIREMO_tas.add_dim_coord(lats, 1)
    MPIREMO_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI_tas.remove_coord('latitude')
    MPISMHI_tas.remove_coord('longitude')
    MPISMHI_tas.remove_coord('grid_latitude')
    MPISMHI_tas.remove_coord('grid_longitude')
    MPISMHI_tas.add_dim_coord(lats, 1)
    MPISMHI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI_tas.remove_coord('latitude')
    NCCSMHI_tas.remove_coord('longitude')
    NCCSMHI_tas.remove_coord('grid_latitude')
    NCCSMHI_tas.remove_coord('grid_longitude')
    NCCSMHI_tas.add_dim_coord(lats, 1)
    NCCSMHI_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA_tas.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons= NOAA_tas.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA_tas.remove_coord('latitude')
    NOAA_tas.remove_coord('longitude')
    NOAA_tas.remove_coord('grid_latitude')
    NOAA_tas.remove_coord('grid_longitude')
    NOAA_tas.add_dim_coord(lats, 1)
    NOAA_tas.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaCanRCM_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM_tasmin.remove_coord('latitude')
    CCCmaCanRCM_tasmin.remove_coord('longitude')
    CCCmaCanRCM_tasmin.remove_coord('grid_latitude')
    CCCmaCanRCM_tasmin.remove_coord('grid_longitude')
    CCCmaCanRCM_tasmin.add_dim_coord(lats, 1)
    CCCmaCanRCM_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI_tasmin.remove_coord('latitude')
    CCCmaSMHI_tasmin.remove_coord('longitude')
    CCCmaSMHI_tasmin.remove_coord('grid_latitude')
    CCCmaSMHI_tasmin.remove_coord('grid_longitude')
    CCCmaSMHI_tasmin.add_dim_coord(lats, 1)
    CCCmaSMHI_tasmin.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM_tasmin.remove_coord('latitude')
    CNRM_tasmin.remove_coord('longitude')
    CNRM_tasmin.remove_coord('grid_latitude')
    CNRM_tasmin.remove_coord('grid_longitude')
    CNRM_tasmin.add_dim_coord(lats, 1)
    CNRM_tasmin.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI_tasmin.remove_coord('latitude')
    CNRMSMHI_tasmin.remove_coord('longitude')
    CNRMSMHI_tasmin.remove_coord('grid_latitude')
    CNRMSMHI_tasmin.remove_coord('grid_longitude')
    CNRMSMHI_tasmin.add_dim_coord(lats, 1)
    CNRMSMHI_tasmin.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO_tasmin.remove_coord('latitude')
    CSIRO_tasmin.remove_coord('longitude')
    CSIRO_tasmin.remove_coord('grid_latitude')
    CSIRO_tasmin.remove_coord('grid_longitude')
    CSIRO_tasmin.add_dim_coord(lats, 1)
    CSIRO_tasmin.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI_tasmin.remove_coord('latitude')
    ICHECDMI_tasmin.remove_coord('longitude')
    ICHECDMI_tasmin.remove_coord('grid_latitude')
    ICHECDMI_tasmin.remove_coord('grid_longitude')
    ICHECDMI_tasmin.add_dim_coord(lats, 1)
    ICHECDMI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM_tasmin.remove_coord('latitude')
    ICHECCCLM_tasmin.remove_coord('longitude')
    ICHECCCLM_tasmin.remove_coord('grid_latitude')
    ICHECCCLM_tasmin.remove_coord('grid_longitude')
    ICHECCCLM_tasmin.add_dim_coord(lats, 1)
    ICHECCCLM_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI_tasmin.remove_coord('latitude')
    ICHECKNMI_tasmin.remove_coord('longitude')
    ICHECKNMI_tasmin.remove_coord('grid_latitude')
    ICHECKNMI_tasmin.remove_coord('grid_longitude')
    ICHECKNMI_tasmin.add_dim_coord(lats, 1)
    ICHECKNMI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI_tasmin.remove_coord('latitude')
    ICHECMPI_tasmin.remove_coord('longitude')
    ICHECMPI_tasmin.remove_coord('grid_latitude')
    ICHECMPI_tasmin.remove_coord('grid_longitude')
    ICHECMPI_tasmin.add_dim_coord(lats, 1)
    ICHECMPI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI_tasmin.remove_coord('latitude')
    ICHECSMHI_tasmin.remove_coord('longitude')
    ICHECSMHI_tasmin.remove_coord('grid_latitude')
    ICHECSMHI_tasmin.remove_coord('grid_longitude')
    ICHECSMHI_tasmin.add_dim_coord(lats, 1)
    ICHECSMHI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL_tasmin.remove_coord('latitude')
    IPSL_tasmin.remove_coord('longitude')
    IPSL_tasmin.remove_coord('grid_latitude')
    IPSL_tasmin.remove_coord('grid_longitude')
    IPSL_tasmin.add_dim_coord(lats, 1)
    IPSL_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC_tasmin.remove_coord('latitude')
    MIROC_tasmin.remove_coord('longitude')
    MIROC_tasmin.remove_coord('grid_latitude')
    MIROC_tasmin.remove_coord('grid_longitude')
    MIROC_tasmin.add_dim_coord(lats, 1)
    MIROC_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM_tasmin.remove_coord('latitude')
    MOHCCCLM_tasmin.remove_coord('longitude')
    MOHCCCLM_tasmin.remove_coord('grid_latitude')
    MOHCCCLM_tasmin.remove_coord('grid_longitude')
    MOHCCCLM_tasmin.add_dim_coord(lats, 1)
    MOHCCCLM_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI_tasmin.remove_coord('latitude')
    MOHCKNMI_tasmin.remove_coord('longitude')
    MOHCKNMI_tasmin.remove_coord('grid_latitude')
    MOHCKNMI_tasmin.remove_coord('grid_longitude')
    MOHCKNMI_tasmin.add_dim_coord(lats, 1)
    MOHCKNMI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI_tasmin.remove_coord('latitude')
    MOHCSMHI_tasmin.remove_coord('longitude')
    MOHCSMHI_tasmin.remove_coord('grid_latitude')
    MOHCSMHI_tasmin.remove_coord('grid_longitude')
    MOHCSMHI_tasmin.add_dim_coord(lats, 1)
    MOHCSMHI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM_tasmin.remove_coord('latitude')
    MPICCLM_tasmin.remove_coord('longitude')
    MPICCLM_tasmin.remove_coord('grid_latitude')
    MPICCLM_tasmin.remove_coord('grid_longitude')
    MPICCLM_tasmin.add_dim_coord(lats, 1)
    MPICCLM_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO_tasmin.remove_coord('latitude')
    MPIREMO_tasmin.remove_coord('longitude')
    MPIREMO_tasmin.remove_coord('grid_latitude')
    MPIREMO_tasmin.remove_coord('grid_longitude')
    MPIREMO_tasmin.add_dim_coord(lats, 1)
    MPIREMO_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI_tasmin.remove_coord('latitude')
    MPISMHI_tasmin.remove_coord('longitude')
    MPISMHI_tasmin.remove_coord('grid_latitude')
    MPISMHI_tasmin.remove_coord('grid_longitude')
    MPISMHI_tasmin.add_dim_coord(lats, 1)
    MPISMHI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI_tasmin.remove_coord('latitude')
    NCCSMHI_tasmin.remove_coord('longitude')
    NCCSMHI_tasmin.remove_coord('grid_latitude')
    NCCSMHI_tasmin.remove_coord('grid_longitude')
    NCCSMHI_tasmin.add_dim_coord(lats, 1)
    NCCSMHI_tasmin.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA_tasmin.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons= NOAA_tasmin.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA_tasmin.remove_coord('latitude')
    NOAA_tasmin.remove_coord('longitude')
    NOAA_tasmin.remove_coord('grid_latitude')
    NOAA_tasmin.remove_coord('grid_longitude')
    NOAA_tasmin.add_dim_coord(lats, 1)
    NOAA_tasmin.add_dim_coord(lons, 2)
     
    lats = iris.coords.DimCoord(CCCmaCanRCM_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM_tasmax.remove_coord('latitude')
    CCCmaCanRCM_tasmax.remove_coord('longitude')
    CCCmaCanRCM_tasmax.remove_coord('grid_latitude')
    CCCmaCanRCM_tasmax.remove_coord('grid_longitude')
    CCCmaCanRCM_tasmax.add_dim_coord(lats, 1)
    CCCmaCanRCM_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI_tasmax.remove_coord('latitude')
    CCCmaSMHI_tasmax.remove_coord('longitude')
    CCCmaSMHI_tasmax.remove_coord('grid_latitude')
    CCCmaSMHI_tasmax.remove_coord('grid_longitude')
    CCCmaSMHI_tasmax.add_dim_coord(lats, 1)
    CCCmaSMHI_tasmax.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM_tasmax.remove_coord('latitude')
    CNRM_tasmax.remove_coord('longitude')
    CNRM_tasmax.remove_coord('grid_latitude')
    CNRM_tasmax.remove_coord('grid_longitude')
    CNRM_tasmax.add_dim_coord(lats, 1)
    CNRM_tasmax.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI_tasmax.remove_coord('latitude')
    CNRMSMHI_tasmax.remove_coord('longitude')
    CNRMSMHI_tasmax.remove_coord('grid_latitude')
    CNRMSMHI_tasmax.remove_coord('grid_longitude')
    CNRMSMHI_tasmax.add_dim_coord(lats, 1)
    CNRMSMHI_tasmax.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO_tasmax.remove_coord('latitude')
    CSIRO_tasmax.remove_coord('longitude')
    CSIRO_tasmax.remove_coord('grid_latitude')
    CSIRO_tasmax.remove_coord('grid_longitude')
    CSIRO_tasmax.add_dim_coord(lats, 1)
    CSIRO_tasmax.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI_tasmax.remove_coord('latitude')
    ICHECDMI_tasmax.remove_coord('longitude')
    ICHECDMI_tasmax.remove_coord('grid_latitude')
    ICHECDMI_tasmax.remove_coord('grid_longitude')
    ICHECDMI_tasmax.add_dim_coord(lats, 1)
    ICHECDMI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM_tasmax.remove_coord('latitude')
    ICHECCCLM_tasmax.remove_coord('longitude')
    ICHECCCLM_tasmax.remove_coord('grid_latitude')
    ICHECCCLM_tasmax.remove_coord('grid_longitude')
    ICHECCCLM_tasmax.add_dim_coord(lats, 1)
    ICHECCCLM_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI_tasmax.remove_coord('latitude')
    ICHECKNMI_tasmax.remove_coord('longitude')
    ICHECKNMI_tasmax.remove_coord('grid_latitude')
    ICHECKNMI_tasmax.remove_coord('grid_longitude')
    ICHECKNMI_tasmax.add_dim_coord(lats, 1)
    ICHECKNMI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI_tasmax.remove_coord('latitude')
    ICHECMPI_tasmax.remove_coord('longitude')
    ICHECMPI_tasmax.remove_coord('grid_latitude')
    ICHECMPI_tasmax.remove_coord('grid_longitude')
    ICHECMPI_tasmax.add_dim_coord(lats, 1)
    ICHECMPI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI_tasmax.remove_coord('latitude')
    ICHECSMHI_tasmax.remove_coord('longitude')
    ICHECSMHI_tasmax.remove_coord('grid_latitude')
    ICHECSMHI_tasmax.remove_coord('grid_longitude')
    ICHECSMHI_tasmax.add_dim_coord(lats, 1)
    ICHECSMHI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL_tasmax.remove_coord('latitude')
    IPSL_tasmax.remove_coord('longitude')
    IPSL_tasmax.remove_coord('grid_latitude')
    IPSL_tasmax.remove_coord('grid_longitude')
    IPSL_tasmax.add_dim_coord(lats, 1)
    IPSL_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC_tasmax.remove_coord('latitude')
    MIROC_tasmax.remove_coord('longitude')
    MIROC_tasmax.remove_coord('grid_latitude')
    MIROC_tasmax.remove_coord('grid_longitude')
    MIROC_tasmax.add_dim_coord(lats, 1)
    MIROC_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM_tasmax.remove_coord('latitude')
    MOHCCCLM_tasmax.remove_coord('longitude')
    MOHCCCLM_tasmax.remove_coord('grid_latitude')
    MOHCCCLM_tasmax.remove_coord('grid_longitude')
    MOHCCCLM_tasmax.add_dim_coord(lats, 1)
    MOHCCCLM_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI_tasmax.remove_coord('latitude')
    MOHCKNMI_tasmax.remove_coord('longitude')
    MOHCKNMI_tasmax.remove_coord('grid_latitude')
    MOHCKNMI_tasmax.remove_coord('grid_longitude')
    MOHCKNMI_tasmax.add_dim_coord(lats, 1)
    MOHCKNMI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI_tasmax.remove_coord('latitude')
    MOHCSMHI_tasmax.remove_coord('longitude')
    MOHCSMHI_tasmax.remove_coord('grid_latitude')
    MOHCSMHI_tasmax.remove_coord('grid_longitude')
    MOHCSMHI_tasmax.add_dim_coord(lats, 1)
    MOHCSMHI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM_tasmax.remove_coord('latitude')
    MPICCLM_tasmax.remove_coord('longitude')
    MPICCLM_tasmax.remove_coord('grid_latitude')
    MPICCLM_tasmax.remove_coord('grid_longitude')
    MPICCLM_tasmax.add_dim_coord(lats, 1)
    MPICCLM_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO_tasmax.remove_coord('latitude')
    MPIREMO_tasmax.remove_coord('longitude')
    MPIREMO_tasmax.remove_coord('grid_latitude')
    MPIREMO_tasmax.remove_coord('grid_longitude')
    MPIREMO_tasmax.add_dim_coord(lats, 1)
    MPIREMO_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI_tasmax.remove_coord('latitude')
    MPISMHI_tasmax.remove_coord('longitude')
    MPISMHI_tasmax.remove_coord('grid_latitude')
    MPISMHI_tasmax.remove_coord('grid_longitude')
    MPISMHI_tasmax.add_dim_coord(lats, 1)
    MPISMHI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI_tasmax.remove_coord('latitude')
    NCCSMHI_tasmax.remove_coord('longitude')
    NCCSMHI_tasmax.remove_coord('grid_latitude')
    NCCSMHI_tasmax.remove_coord('grid_longitude')
    NCCSMHI_tasmax.add_dim_coord(lats, 1)
    NCCSMHI_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA_tasmax.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons= NOAA_tasmax.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA_tasmax.remove_coord('latitude')
    NOAA_tasmax.remove_coord('longitude')
    NOAA_tasmax.remove_coord('grid_latitude')
    NOAA_tasmax.remove_coord('grid_longitude')
    NOAA_tasmax.add_dim_coord(lats, 1)
    NOAA_tasmax.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaCanRCM_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaCanRCM_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                              
    CCCmaCanRCM_pr.remove_coord('latitude')
    CCCmaCanRCM_pr.remove_coord('longitude')
    CCCmaCanRCM_pr.remove_coord('grid_latitude')
    CCCmaCanRCM_pr.remove_coord('grid_longitude')
    CCCmaCanRCM_pr.add_dim_coord(lats, 1)
    CCCmaCanRCM_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(CCCmaSMHI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CCCmaSMHI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CCCmaSMHI_pr.remove_coord('latitude')
    CCCmaSMHI_pr.remove_coord('longitude')
    CCCmaSMHI_pr.remove_coord('grid_latitude')
    CCCmaSMHI_pr.remove_coord('grid_longitude')
    CCCmaSMHI_pr.add_dim_coord(lats, 1)
    CCCmaSMHI_pr.add_dim_coord(lons, 2)  
    
    lats = iris.coords.DimCoord(CNRM_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRM_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    CNRM_pr.remove_coord('latitude')
    CNRM_pr.remove_coord('longitude')
    CNRM_pr.remove_coord('grid_latitude')
    CNRM_pr.remove_coord('grid_longitude')
    CNRM_pr.add_dim_coord(lats, 1)
    CNRM_pr.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CNRMSMHI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CNRMSMHI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CNRMSMHI_pr.remove_coord('latitude')
    CNRMSMHI_pr.remove_coord('longitude')
    CNRMSMHI_pr.remove_coord('grid_latitude')
    CNRMSMHI_pr.remove_coord('grid_longitude')
    CNRMSMHI_pr.add_dim_coord(lats, 1)
    CNRMSMHI_pr.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(CSIRO_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = CSIRO_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    CSIRO_pr.remove_coord('latitude')
    CSIRO_pr.remove_coord('longitude')
    CSIRO_pr.remove_coord('grid_latitude')
    CSIRO_pr.remove_coord('grid_longitude')
    CSIRO_pr.add_dim_coord(lats, 1)
    CSIRO_pr.add_dim_coord(lons, 2) 
    
    lats = iris.coords.DimCoord(ICHECDMI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECDMI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')    
    
    ICHECDMI_pr.remove_coord('latitude')
    ICHECDMI_pr.remove_coord('longitude')
    ICHECDMI_pr.remove_coord('grid_latitude')
    ICHECDMI_pr.remove_coord('grid_longitude')
    ICHECDMI_pr.add_dim_coord(lats, 1)
    ICHECDMI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECCCLM_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECCCLM_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECCCLM_pr.remove_coord('latitude')
    ICHECCCLM_pr.remove_coord('longitude')
    ICHECCCLM_pr.remove_coord('grid_latitude')
    ICHECCCLM_pr.remove_coord('grid_longitude')
    ICHECCCLM_pr.add_dim_coord(lats, 1)
    ICHECCCLM_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECKNMI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECKNMI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECKNMI_pr.remove_coord('latitude')
    ICHECKNMI_pr.remove_coord('longitude')
    ICHECKNMI_pr.remove_coord('grid_latitude')
    ICHECKNMI_pr.remove_coord('grid_longitude')
    ICHECKNMI_pr.add_dim_coord(lats, 1)
    ICHECKNMI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECMPI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECMPI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees') 
    
    ICHECMPI_pr.remove_coord('latitude')
    ICHECMPI_pr.remove_coord('longitude')
    ICHECMPI_pr.remove_coord('grid_latitude')
    ICHECMPI_pr.remove_coord('grid_longitude')
    ICHECMPI_pr.add_dim_coord(lats, 1)
    ICHECMPI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(ICHECSMHI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = ICHECSMHI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    ICHECSMHI_pr.remove_coord('latitude')
    ICHECSMHI_pr.remove_coord('longitude')
    ICHECSMHI_pr.remove_coord('grid_latitude')
    ICHECSMHI_pr.remove_coord('grid_longitude')
    ICHECSMHI_pr.add_dim_coord(lats, 1)
    ICHECSMHI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(IPSL_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = IPSL_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    IPSL_pr.remove_coord('latitude')
    IPSL_pr.remove_coord('longitude')
    IPSL_pr.remove_coord('grid_latitude')
    IPSL_pr.remove_coord('grid_longitude')
    IPSL_pr.add_dim_coord(lats, 1)
    IPSL_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MIROC_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MIROC_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
                                
    MIROC_pr.remove_coord('latitude')
    MIROC_pr.remove_coord('longitude')
    MIROC_pr.remove_coord('grid_latitude')
    MIROC_pr.remove_coord('grid_longitude')
    MIROC_pr.add_dim_coord(lats, 1)
    MIROC_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCCCLM_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCCCLM_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCCCLM_pr.remove_coord('latitude')
    MOHCCCLM_pr.remove_coord('longitude')
    MOHCCCLM_pr.remove_coord('grid_latitude')
    MOHCCCLM_pr.remove_coord('grid_longitude')
    MOHCCCLM_pr.add_dim_coord(lats, 1)
    MOHCCCLM_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCKNMI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCKNMI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCKNMI_pr.remove_coord('latitude')
    MOHCKNMI_pr.remove_coord('longitude')
    MOHCKNMI_pr.remove_coord('grid_latitude')
    MOHCKNMI_pr.remove_coord('grid_longitude')
    MOHCKNMI_pr.add_dim_coord(lats, 1)
    MOHCKNMI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MOHCSMHI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MOHCSMHI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MOHCSMHI_pr.remove_coord('latitude')
    MOHCSMHI_pr.remove_coord('longitude')
    MOHCSMHI_pr.remove_coord('grid_latitude')
    MOHCSMHI_pr.remove_coord('grid_longitude')
    MOHCSMHI_pr.add_dim_coord(lats, 1)
    MOHCSMHI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPICCLM_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPICCLM_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPICCLM_pr.remove_coord('latitude')
    MPICCLM_pr.remove_coord('longitude')
    MPICCLM_pr.remove_coord('grid_latitude')
    MPICCLM_pr.remove_coord('grid_longitude')
    MPICCLM_pr.add_dim_coord(lats, 1)
    MPICCLM_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPIREMO_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPIREMO_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPIREMO_pr.remove_coord('latitude')
    MPIREMO_pr.remove_coord('longitude')
    MPIREMO_pr.remove_coord('grid_latitude')
    MPIREMO_pr.remove_coord('grid_longitude')
    MPIREMO_pr.add_dim_coord(lats, 1)
    MPIREMO_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(MPISMHI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = MPISMHI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    MPISMHI_pr.remove_coord('latitude')
    MPISMHI_pr.remove_coord('longitude')
    MPISMHI_pr.remove_coord('grid_latitude')
    MPISMHI_pr.remove_coord('grid_longitude')
    MPISMHI_pr.add_dim_coord(lats, 1)
    MPISMHI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NCCSMHI_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons = NCCSMHI_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NCCSMHI_pr.remove_coord('latitude')
    NCCSMHI_pr.remove_coord('longitude')
    NCCSMHI_pr.remove_coord('grid_latitude')
    NCCSMHI_pr.remove_coord('grid_longitude')
    NCCSMHI_pr.add_dim_coord(lats, 1)
    NCCSMHI_pr.add_dim_coord(lons, 2)
    
    lats = iris.coords.DimCoord(NOAA_pr.coord('latitude').points[:,0], standard_name='latitude', units='degrees')
    lons= NOAA_pr.coord('longitude').points[0]
    for i in range(len(lons)):
        if lons[i]>100.:
            lons[i] = lons[i]-360.
    lons = iris.coords.DimCoord(lons, standard_name='longitude', units='degrees')
    
    NOAA_pr.remove_coord('latitude')
    NOAA_pr.remove_coord('longitude')
    NOAA_pr.remove_coord('grid_latitude')
    NOAA_pr.remove_coord('grid_longitude')
    NOAA_pr.add_dim_coord(lats, 1)
    NOAA_pr.add_dim_coord(lons, 2)
    
    #guess bounds    
    CCCmaCanRCM_tas.coord('latitude').guess_bounds()
    CCCmaSMHI_tas.coord('latitude').guess_bounds()
    CNRM_tas.coord('latitude').guess_bounds()
    CNRMSMHI_tas.coord('latitude').guess_bounds()
    CSIRO_tas.coord('latitude').guess_bounds()
    ICHECDMI_tas.coord('latitude').guess_bounds()
    ICHECCCLM_tas.coord('latitude').guess_bounds()
    ICHECKNMI_tas.coord('latitude').guess_bounds()
    ICHECMPI_tas.coord('latitude').guess_bounds()
    ICHECSMHI_tas.coord('latitude').guess_bounds()
    IPSL_tas.coord('latitude').guess_bounds()
    MIROC_tas.coord('latitude').guess_bounds()
    MOHCCCLM_tas.coord('latitude').guess_bounds()
    MOHCKNMI_tas.coord('latitude').guess_bounds() 
    MOHCSMHI_tas.coord('latitude').guess_bounds()
    MPICCLM_tas.coord('latitude').guess_bounds()
    MPIREMO_tas.coord('latitude').guess_bounds()
    MPISMHI_tas.coord('latitude').guess_bounds()
    NCCSMHI_tas.coord('latitude').guess_bounds()
    NOAA_tas.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_tas.coord('longitude').guess_bounds()
    CCCmaSMHI_tas.coord('longitude').guess_bounds()
    CNRM_tas.coord('longitude').guess_bounds()
    CNRMSMHI_tas.coord('longitude').guess_bounds()
    CSIRO_tas.coord('longitude').guess_bounds()
    ICHECDMI_tas.coord('longitude').guess_bounds()
    ICHECCCLM_tas.coord('longitude').guess_bounds()
    ICHECKNMI_tas.coord('longitude').guess_bounds()
    ICHECMPI_tas.coord('longitude').guess_bounds()
    ICHECSMHI_tas.coord('longitude').guess_bounds()
    IPSL_tas.coord('longitude').guess_bounds()
    MIROC_tas.coord('longitude').guess_bounds()
    MOHCCCLM_tas.coord('longitude').guess_bounds()
    MOHCKNMI_tas.coord('longitude').guess_bounds() 
    MOHCSMHI_tas.coord('longitude').guess_bounds()
    MPICCLM_tas.coord('longitude').guess_bounds()
    MPIREMO_tas.coord('longitude').guess_bounds()
    MPISMHI_tas.coord('longitude').guess_bounds()
    NCCSMHI_tas.coord('longitude').guess_bounds()
    NOAA_tas.coord('longitude').guess_bounds()
    
    CCCmaCanRCM_tasmin.coord('latitude').guess_bounds()
    CCCmaSMHI_tasmin.coord('latitude').guess_bounds()
    CNRM_tasmin.coord('latitude').guess_bounds()
    CNRMSMHI_tasmin.coord('latitude').guess_bounds()
    CSIRO_tasmin.coord('latitude').guess_bounds()
    ICHECDMI_tasmin.coord('latitude').guess_bounds()
    ICHECCCLM_tasmin.coord('latitude').guess_bounds()
    ICHECKNMI_tasmin.coord('latitude').guess_bounds()
    ICHECMPI_tasmin.coord('latitude').guess_bounds()
    ICHECSMHI_tasmin.coord('latitude').guess_bounds()
    IPSL_tasmin.coord('latitude').guess_bounds()
    MIROC_tasmin.coord('latitude').guess_bounds()
    MOHCCCLM_tasmin.coord('latitude').guess_bounds()
    MOHCKNMI_tasmin.coord('latitude').guess_bounds() 
    MOHCSMHI_tasmin.coord('latitude').guess_bounds()
    MPICCLM_tasmin.coord('latitude').guess_bounds()
    MPIREMO_tasmin.coord('latitude').guess_bounds()
    MPISMHI_tasmin.coord('latitude').guess_bounds()
    NCCSMHI_tasmin.coord('latitude').guess_bounds()
    NOAA_tasmin.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_tasmin.coord('longitude').guess_bounds()
    CCCmaSMHI_tasmin.coord('longitude').guess_bounds()
    CNRM_tasmin.coord('longitude').guess_bounds()
    CNRMSMHI_tasmin.coord('longitude').guess_bounds()
    CSIRO_tasmin.coord('longitude').guess_bounds()
    ICHECDMI_tasmin.coord('longitude').guess_bounds()
    ICHECCCLM_tasmin.coord('longitude').guess_bounds()
    ICHECKNMI_tasmin.coord('longitude').guess_bounds()
    ICHECMPI_tasmin.coord('longitude').guess_bounds()
    ICHECSMHI_tasmin.coord('longitude').guess_bounds()
    IPSL_tasmin.coord('longitude').guess_bounds()
    MIROC_tasmin.coord('longitude').guess_bounds()
    MOHCCCLM_tasmin.coord('longitude').guess_bounds()
    MOHCKNMI_tasmin.coord('longitude').guess_bounds() 
    MOHCSMHI_tasmin.coord('longitude').guess_bounds()
    MPICCLM_tasmin.coord('longitude').guess_bounds()
    MPIREMO_tasmin.coord('longitude').guess_bounds()
    MPISMHI_tasmin.coord('longitude').guess_bounds()
    NCCSMHI_tasmin.coord('longitude').guess_bounds()
    NOAA_tasmin.coord('longitude').guess_bounds()
    
    CCCmaCanRCM_tasmax.coord('latitude').guess_bounds()
    CCCmaSMHI_tasmax.coord('latitude').guess_bounds()
    CNRM_tasmax.coord('latitude').guess_bounds()
    CNRMSMHI_tasmax.coord('latitude').guess_bounds()
    CSIRO_tasmax.coord('latitude').guess_bounds()
    ICHECDMI_tasmax.coord('latitude').guess_bounds()
    ICHECCCLM_tasmax.coord('latitude').guess_bounds()
    ICHECKNMI_tasmax.coord('latitude').guess_bounds()
    ICHECMPI_tasmax.coord('latitude').guess_bounds()
    ICHECSMHI_tasmax.coord('latitude').guess_bounds()
    IPSL_tasmax.coord('latitude').guess_bounds()
    MIROC_tasmax.coord('latitude').guess_bounds()
    MOHCCCLM_tasmax.coord('latitude').guess_bounds()
    MOHCKNMI_tasmax.coord('latitude').guess_bounds() 
    MOHCSMHI_tasmax.coord('latitude').guess_bounds()
    MPICCLM_tasmax.coord('latitude').guess_bounds()
    MPIREMO_tasmax.coord('latitude').guess_bounds()
    MPISMHI_tasmax.coord('latitude').guess_bounds()
    NCCSMHI_tasmax.coord('latitude').guess_bounds()
    NOAA_tasmax.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_tasmax.coord('longitude').guess_bounds()
    CCCmaSMHI_tasmax.coord('longitude').guess_bounds()
    CNRM_tasmax.coord('longitude').guess_bounds()
    CNRMSMHI_tasmax.coord('longitude').guess_bounds()
    CSIRO_tasmax.coord('longitude').guess_bounds()
    ICHECDMI_tasmax.coord('longitude').guess_bounds()
    ICHECCCLM_tasmax.coord('longitude').guess_bounds()
    ICHECKNMI_tasmax.coord('longitude').guess_bounds()
    ICHECMPI_tasmax.coord('longitude').guess_bounds()
    ICHECSMHI_tasmax.coord('longitude').guess_bounds()
    IPSL_tasmax.coord('longitude').guess_bounds()
    MIROC_tasmax.coord('longitude').guess_bounds()
    MOHCCCLM_tasmax.coord('longitude').guess_bounds()
    MOHCKNMI_tasmax.coord('longitude').guess_bounds() 
    MOHCSMHI_tasmax.coord('longitude').guess_bounds()
    MPICCLM_tasmax.coord('longitude').guess_bounds()
    MPIREMO_tasmax.coord('longitude').guess_bounds()
    MPISMHI_tasmax.coord('longitude').guess_bounds()
    NCCSMHI_tasmax.coord('longitude').guess_bounds()
    NOAA_tasmax.coord('longitude').guess_bounds()
    
    CCCmaCanRCM_pr.coord('latitude').guess_bounds()
    CCCmaSMHI_pr.coord('latitude').guess_bounds()
    CNRM_pr.coord('latitude').guess_bounds()
    CNRMSMHI_pr.coord('latitude').guess_bounds()
    CSIRO_pr.coord('latitude').guess_bounds()
    ICHECDMI_pr.coord('latitude').guess_bounds()
    ICHECCCLM_pr.coord('latitude').guess_bounds()
    ICHECKNMI_pr.coord('latitude').guess_bounds()
    ICHECMPI_pr.coord('latitude').guess_bounds()
    ICHECSMHI_pr.coord('latitude').guess_bounds()
    IPSL_pr.coord('latitude').guess_bounds()
    MIROC_pr.coord('latitude').guess_bounds()
    MOHCCCLM_pr.coord('latitude').guess_bounds()
    MOHCKNMI_pr.coord('latitude').guess_bounds() 
    MOHCSMHI_pr.coord('latitude').guess_bounds()
    MPICCLM_pr.coord('latitude').guess_bounds()
    MPIREMO_pr.coord('latitude').guess_bounds()
    MPISMHI_pr.coord('latitude').guess_bounds()
    NCCSMHI_pr.coord('latitude').guess_bounds()
    NOAA_pr.coord('latitude').guess_bounds()
    
    CCCmaCanRCM_pr.coord('longitude').guess_bounds()
    CCCmaSMHI_pr.coord('longitude').guess_bounds()
    CNRM_pr.coord('longitude').guess_bounds()
    CNRMSMHI_pr.coord('longitude').guess_bounds()
    CSIRO_pr.coord('longitude').guess_bounds()
    ICHECDMI_pr.coord('longitude').guess_bounds()
    ICHECCCLM_pr.coord('longitude').guess_bounds()
    ICHECKNMI_pr.coord('longitude').guess_bounds()
    ICHECMPI_pr.coord('longitude').guess_bounds()
    ICHECSMHI_pr.coord('longitude').guess_bounds()
    IPSL_pr.coord('longitude').guess_bounds()
    MIROC_pr.coord('longitude').guess_bounds()
    MOHCCCLM_pr.coord('longitude').guess_bounds()
    MOHCKNMI_pr.coord('longitude').guess_bounds() 
    MOHCSMHI_pr.coord('longitude').guess_bounds()
    MPICCLM_pr.coord('longitude').guess_bounds()
    MPIREMO_pr.coord('longitude').guess_bounds()
    MPISMHI_pr.coord('longitude').guess_bounds()
    NCCSMHI_pr.coord('longitude').guess_bounds()
    NOAA_pr.coord('longitude').guess_bounds()
    
    
    
    #-------------------------------------------------------------------------
    #PART 2: LOAD OBSERVED DATA
    #bring in all the files we need and give them a name
    CRU_tas = '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.tmp.dat.nc'
    UDel_tas = '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_air.mon.mean.v401.nc'
    CRU_tasmin= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.01.1901.2016.tmn.dat.nc'
    CRU_tasmax= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.01.1901.2016.tmx.dat.nc'    
    CRU_pr= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/cru_ts4.00.1901.2015.pre.dat.nc'
    UDel_pr= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/UDel_precip.mon.total.v401.nc'
    GPCC_pr= '/exports/csce/datastore/geos/users/s0899345/Actual_Data/ESRL_PSD_GPCC_precip.mon.combined.total.v7.nc'
    
    #Load exactly one cube from given file
    CRU_tas = iris.load_cube(CRU_tas, 'near-surface temperature')
    UDel_tas = iris.load_cube(UDel_tas)
    CRU_tasmin = iris.load_cube(CRU_tasmin, 'near-surface temperature minimum')  
    CRU_tasmax = iris.load_cube(CRU_tasmax, 'near-surface temperature maximum')
    CRU_pr = iris.load_cube(CRU_pr, 'precipitation')
    UDel_pr = iris.load_cube(UDel_pr)
    GPCC_pr = iris.load_cube(GPCC_pr)
    
    #guess bounds  
    CRU_tas.coord('latitude').guess_bounds()
    UDel_tas.coord('latitude').guess_bounds()
    CRU_tasmin.coord('latitude').guess_bounds()
    CRU_tasmax.coord('latitude').guess_bounds()
    CRU_pr.coord('latitude').guess_bounds()
    UDel_pr.coord('latitude').guess_bounds()
    GPCC_pr.coord('latitude').guess_bounds()
    
    CRU_tas.coord('longitude').guess_bounds()
    UDel_tas.coord('longitude').guess_bounds()
    CRU_tasmin.coord('longitude').guess_bounds()
    CRU_tasmax.coord('longitude').guess_bounds()
    CRU_pr.coord('longitude').guess_bounds()
    UDel_pr.coord('longitude').guess_bounds()
    GPCC_pr.coord('longitude').guess_bounds()
    
    
    
    #-------------------------------------------------------------------------
    #PART 3: FORMAT DATA GENERAL
    #we are only interested in the latitude and longitude relevant to Central Malawi 
    Central_Malawi = iris.Constraint(longitude=lambda v: 32.5 <= v <= 35.5, latitude=lambda v: -15 <= v <= -12)        
    
    CCCmaCanRCM_tas = CCCmaCanRCM_tas.extract(Central_Malawi)
    CCCmaSMHI_tas = CCCmaSMHI_tas.extract(Central_Malawi)
    CNRM_tas = CNRM_tas.extract(Central_Malawi)
    CNRMSMHI_tas = CNRMSMHI_tas.extract(Central_Malawi)
    CSIRO_tas = CSIRO_tas.extract(Central_Malawi)
    ICHECDMI_tas = ICHECDMI_tas.extract(Central_Malawi)
    ICHECCCLM_tas = ICHECCCLM_tas.extract(Central_Malawi)
    ICHECKNMI_tas = ICHECKNMI_tas.extract(Central_Malawi)
    ICHECMPI_tas = ICHECMPI_tas.extract(Central_Malawi)
    ICHECSMHI_tas = ICHECSMHI_tas.extract(Central_Malawi)
    IPSL_tas = IPSL_tas.extract(Central_Malawi)
    MIROC_tas = MIROC_tas.extract(Central_Malawi)
    MOHCCCLM_tas = MOHCCCLM_tas.extract(Central_Malawi)
    MOHCKNMI_tas = MOHCKNMI_tas.extract(Central_Malawi)
    MOHCSMHI_tas = MOHCSMHI_tas.extract(Central_Malawi)
    MPICCLM_tas = MPICCLM_tas.extract(Central_Malawi)
    MPIREMO_tas = MPIREMO_tas.extract(Central_Malawi)
    MPISMHI_tas = MPISMHI_tas.extract(Central_Malawi)
    NCCSMHI_tas = NCCSMHI_tas.extract(Central_Malawi)
    NOAA_tas = NOAA_tas.extract(Central_Malawi)
    
    CCCmaCanRCM_tasmin = CCCmaCanRCM_tasmin.extract(Central_Malawi)
    CCCmaSMHI_tasmin = CCCmaSMHI_tasmin.extract(Central_Malawi)
    CNRM_tasmin = CNRM_tasmin.extract(Central_Malawi)
    CNRMSMHI_tasmin = CNRMSMHI_tasmin.extract(Central_Malawi)
    CSIRO_tasmin = CSIRO_tasmin.extract(Central_Malawi)
    ICHECDMI_tasmin = ICHECDMI_tasmin.extract(Central_Malawi)
    ICHECCCLM_tasmin = ICHECCCLM_tasmin.extract(Central_Malawi)
    ICHECKNMI_tasmin = ICHECKNMI_tasmin.extract(Central_Malawi)
    ICHECMPI_tasmin = ICHECMPI_tasmin.extract(Central_Malawi)
    ICHECSMHI_tasmin = ICHECSMHI_tasmin.extract(Central_Malawi)
    IPSL_tasmin = IPSL_tasmin.extract(Central_Malawi)
    MIROC_tasmin = MIROC_tasmin.extract(Central_Malawi)
    MOHCCCLM_tasmin = MOHCCCLM_tasmin.extract(Central_Malawi)
    MOHCKNMI_tasmin = MOHCKNMI_tasmin.extract(Central_Malawi)
    MOHCSMHI_tasmin = MOHCSMHI_tasmin.extract(Central_Malawi)
    MPICCLM_tasmin = MPICCLM_tasmin.extract(Central_Malawi)
    MPIREMO_tasmin = MPIREMO_tasmin.extract(Central_Malawi)
    MPISMHI_tasmin = MPISMHI_tasmin.extract(Central_Malawi)
    NCCSMHI_tasmin = NCCSMHI_tasmin.extract(Central_Malawi)
    NOAA_tasmin = NOAA_tasmin.extract(Central_Malawi)
    
    CCCmaCanRCM_tasmax = CCCmaCanRCM_tasmax.extract(Central_Malawi)
    CCCmaSMHI_tasmax = CCCmaSMHI_tasmax.extract(Central_Malawi)
    CNRM_tasmax = CNRM_tasmax.extract(Central_Malawi)
    CNRMSMHI_tasmax = CNRMSMHI_tasmax.extract(Central_Malawi)
    CSIRO_tasmax = CSIRO_tasmax.extract(Central_Malawi)
    ICHECDMI_tasmax = ICHECDMI_tasmax.extract(Central_Malawi)
    ICHECCCLM_tasmax = ICHECCCLM_tasmax.extract(Central_Malawi)
    ICHECKNMI_tasmax = ICHECKNMI_tasmax.extract(Central_Malawi)
    ICHECMPI_tasmax = ICHECMPI_tasmax.extract(Central_Malawi)
    ICHECSMHI_tasmax = ICHECSMHI_tasmax.extract(Central_Malawi)
    IPSL_tasmax = IPSL_tasmax.extract(Central_Malawi)
    MIROC_tasmax = MIROC_tasmax.extract(Central_Malawi)
    MOHCCCLM_tasmax = MOHCCCLM_tasmax.extract(Central_Malawi)
    MOHCKNMI_tasmax = MOHCKNMI_tasmax.extract(Central_Malawi)
    MOHCSMHI_tasmax = MOHCSMHI_tasmax.extract(Central_Malawi)
    MPICCLM_tasmax = MPICCLM_tasmax.extract(Central_Malawi)
    MPIREMO_tasmax = MPIREMO_tasmax.extract(Central_Malawi)
    MPISMHI_tasmax = MPISMHI_tasmax.extract(Central_Malawi)
    NCCSMHI_tasmax = NCCSMHI_tasmax.extract(Central_Malawi)
    NOAA_tasmax = NOAA_tasmax.extract(Central_Malawi)
    
    CCCmaCanRCM_pr = CCCmaCanRCM_pr.extract(Central_Malawi)
    CCCmaSMHI_pr = CCCmaSMHI_pr.extract(Central_Malawi)
    CNRM_pr = CNRM_pr.extract(Central_Malawi)
    CNRMSMHI_pr = CNRMSMHI_pr.extract(Central_Malawi)
    CSIRO_pr = CSIRO_pr.extract(Central_Malawi)
    ICHECDMI_pr = ICHECDMI_pr.extract(Central_Malawi)
    ICHECCCLM_pr = ICHECCCLM_pr.extract(Central_Malawi)
    ICHECKNMI_pr = ICHECKNMI_pr.extract(Central_Malawi)
    ICHECMPI_pr = ICHECMPI_pr.extract(Central_Malawi)
    ICHECSMHI_pr = ICHECSMHI_pr.extract(Central_Malawi)
    IPSL_pr = IPSL_pr.extract(Central_Malawi)
    MIROC_pr = MIROC_pr.extract(Central_Malawi)
    MOHCCCLM_pr = MOHCCCLM_pr.extract(Central_Malawi)
    MOHCKNMI_pr = MOHCKNMI_pr.extract(Central_Malawi)
    MOHCSMHI_pr = MOHCSMHI_pr.extract(Central_Malawi)
    MPICCLM_pr = MPICCLM_pr.extract(Central_Malawi)
    MPIREMO_pr = MPIREMO_pr.extract(Central_Malawi)
    MPISMHI_pr = MPISMHI_pr.extract(Central_Malawi)
    NCCSMHI_pr = NCCSMHI_pr.extract(Central_Malawi)
    NOAA_pr = NOAA_pr.extract(Central_Malawi)
    
    CRU_tas = CRU_tas.extract(Central_Malawi)
    UDel_tas = UDel_tas.extract(Central_Malawi)
    CRU_tasmin = CRU_tasmin.extract(Central_Malawi)
    CRU_tasmax = CRU_tasmax.extract(Central_Malawi)
    CRU_pr = CRU_pr.extract(Central_Malawi)
    UDel_pr = UDel_pr.extract(Central_Malawi)
    GPCC_pr = GPCC_pr.extract(Central_Malawi)
    
    #Convert units to match, CORDEX data is in Kelvin but Observed data in Celsius, we would like to show all data in Celsius
    CCCmaCanRCM_tas.convert_units('Celsius')
    CCCmaSMHI_tas.convert_units('Celsius')
    CNRM_tas.convert_units('Celsius')
    CNRMSMHI_tas.convert_units('Celsius')
    CSIRO_tas.convert_units('Celsius')
    ICHECDMI_tas.convert_units('Celsius')
    ICHECCCLM_tas.convert_units('Celsius') 
    ICHECKNMI_tas.convert_units('Celsius')
    ICHECMPI_tas.convert_units('Celsius')
    ICHECSMHI_tas.convert_units('Celsius')
    IPSL_tas.convert_units('Celsius')
    MIROC_tas.convert_units('Celsius')
    MOHCCCLM_tas.convert_units('Celsius')
    MOHCKNMI_tas.convert_units('Celsius')
    MOHCSMHI_tas.convert_units('Celsius')
    MPICCLM_tas.convert_units('Celsius')
    MPIREMO_tas.convert_units('Celsius')
    MPISMHI_tas.convert_units('Celsius')
    NCCSMHI_tas.convert_units('Celsius')
    NOAA_tas.convert_units('Celsius')
    
    CCCmaCanRCM_tasmin.convert_units('Celsius')
    CCCmaSMHI_tasmin.convert_units('Celsius')
    CNRM_tasmin.convert_units('Celsius')
    CNRMSMHI_tasmin.convert_units('Celsius')
    CSIRO_tasmin.convert_units('Celsius')
    ICHECDMI_tasmin.convert_units('Celsius')
    ICHECCCLM_tasmin.convert_units('Celsius') 
    ICHECKNMI_tasmin.convert_units('Celsius')
    ICHECMPI_tasmin.convert_units('Celsius')
    ICHECSMHI_tasmin.convert_units('Celsius')
    IPSL_tasmin.convert_units('Celsius')
    MIROC_tasmin.convert_units('Celsius')
    MOHCCCLM_tasmin.convert_units('Celsius')
    MOHCKNMI_tasmin.convert_units('Celsius')
    MOHCSMHI_tasmin.convert_units('Celsius')
    MPICCLM_tasmin.convert_units('Celsius')
    MPIREMO_tasmin.convert_units('Celsius')
    MPISMHI_tasmin.convert_units('Celsius')
    NCCSMHI_tasmin.convert_units('Celsius')
    NOAA_tasmin.convert_units('Celsius')
    
    CCCmaCanRCM_tasmax.convert_units('Celsius')
    CCCmaSMHI_tasmax.convert_units('Celsius')
    CNRM_tasmax.convert_units('Celsius')
    CNRMSMHI_tasmax.convert_units('Celsius')
    CSIRO_tasmax.convert_units('Celsius')
    ICHECDMI_tasmax.convert_units('Celsius')
    ICHECCCLM_tasmax.convert_units('Celsius') 
    ICHECKNMI_tasmax.convert_units('Celsius')
    ICHECMPI_tasmax.convert_units('Celsius')
    ICHECSMHI_tasmax.convert_units('Celsius')
    IPSL_tasmax.convert_units('Celsius')
    MIROC_tasmax.convert_units('Celsius')
    MOHCCCLM_tasmax.convert_units('Celsius')
    MOHCKNMI_tasmax.convert_units('Celsius')
    MOHCSMHI_tasmax.convert_units('Celsius')
    MPICCLM_tasmax.convert_units('Celsius')
    MPIREMO_tasmax.convert_units('Celsius')
    MPISMHI_tasmax.convert_units('Celsius')
    NCCSMHI_tasmax.convert_units('Celsius')
    NOAA_tasmax.convert_units('Celsius')
    
    #Convert units to match, CORDEX data in precipitation_flux (kg m-2 s-1) but want all data in precipitation rate per month (mm month-1).
    #Since 1 kg of rain spread over 1 m of surface is 1mm in thickness, and there are 60*60*24*365.25=31557600 seconds in a year and 12 months in the year, the conversion is:
    Convert=31557600/12
       
    CCCmaCanRCM_pr = CCCmaCanRCM_pr*Convert
    CCCmaSMHI_pr = CCCmaSMHI_pr*Convert
    CNRM_pr = CNRM_pr*Convert
    CNRMSMHI_pr = CNRMSMHI_pr*Convert 
    CSIRO_pr = CSIRO_pr*Convert
    ICHECDMI_pr = ICHECDMI_pr*Convert
    ICHECCCLM_pr = ICHECCCLM_pr*Convert
    ICHECKNMI_pr = ICHECKNMI_pr*Convert
    ICHECMPI_pr = ICHECMPI_pr*Convert
    ICHECSMHI_pr = ICHECSMHI_pr*Convert
    IPSL_pr = IPSL_pr*Convert
    MIROC_pr = MIROC_pr*Convert
    MOHCCCLM_pr = MOHCCCLM_pr*Convert
    MOHCKNMI_pr = MOHCKNMI_pr*Convert
    MOHCSMHI_pr = MOHCSMHI_pr*Convert
    MPICCLM_pr = MPICCLM_pr*Convert
    MPIREMO_pr = MPIREMO_pr*Convert
    MPISMHI_pr = MPISMHI_pr*Convert
    NCCSMHI_pr = NCCSMHI_pr*Convert
    NOAA_pr = NOAA_pr*Convert
    
    
    #Convert units to match, UDel data in cm per month but want precipitation rate in mm per month. Since there are 10mm in a cm, the conversion is:
    Convert=10
    UDel_pr = UDel_pr*Convert
    
    #rename units to make names match after conversion
    CRU_tas.units = Unit('degrees Celsius')
    UDel_tas.units = Unit('degrees Celsius')
    CRU_pr.units = Unit('mm per month')
    UDel_pr.units = Unit('mm per month')
    GPCC_pr.units = Unit('mm per month')
    
    #add time constraint for baseline data
    iris.FUTURE.cell_datetime_objects = True
    t_constraint = iris.Constraint(time=lambda cell: 1971 <= cell.point.year <= 2000)
    
    CCCmaCanRCM_tas = CCCmaCanRCM_tas.extract(t_constraint)
    CCCmaSMHI_tas = CCCmaSMHI_tas.extract(t_constraint)
    CNRM_tas = CNRM_tas.extract(t_constraint)
    CNRMSMHI_tas = CNRMSMHI_tas.extract(t_constraint)
    CSIRO_tas = CSIRO_tas.extract(t_constraint)
    ICHECDMI_tas = ICHECDMI_tas.extract(t_constraint)
    ICHECCCLM_tas = ICHECCCLM_tas.extract(t_constraint)
    ICHECKNMI_tas = ICHECKNMI_tas.extract(t_constraint)
    ICHECMPI_tas = ICHECMPI_tas.extract(t_constraint)
    ICHECSMHI_tas = ICHECSMHI_tas.extract(t_constraint)
    IPSL_tas = IPSL_tas.extract(t_constraint)
    MIROC_tas = MIROC_tas.extract(t_constraint)
    MOHCCCLM_tas = MOHCCCLM_tas.extract(t_constraint)
    MOHCKNMI_tas = MOHCKNMI_tas.extract(t_constraint)
    MOHCSMHI_tas = MOHCSMHI_tas.extract(t_constraint)
    MPICCLM_tas = MPICCLM_tas.extract(t_constraint)
    MPIREMO_tas = MPIREMO_tas.extract(t_constraint)
    MPISMHI_tas = MPISMHI_tas.extract(t_constraint)
    NCCSMHI_tas = NCCSMHI_tas.extract(t_constraint)
    NOAA_tas = NOAA_tas.extract(t_constraint)
    
    CCCmaCanRCM_tasmin = CCCmaCanRCM_tasmin.extract(t_constraint)
    CCCmaSMHI_tasmin = CCCmaSMHI_tasmin.extract(t_constraint)
    CNRM_tasmin = CNRM_tasmin.extract(t_constraint)
    CNRMSMHI_tasmin = CNRMSMHI_tasmin.extract(t_constraint)
    CSIRO_tasmin = CSIRO_tasmin.extract(t_constraint)
    ICHECDMI_tasmin = ICHECDMI_tasmin.extract(t_constraint)
    ICHECCCLM_tasmin = ICHECCCLM_tasmin.extract(t_constraint)
    ICHECKNMI_tasmin = ICHECKNMI_tasmin.extract(t_constraint)
    ICHECMPI_tasmin = ICHECMPI_tasmin.extract(t_constraint)
    ICHECSMHI_tasmin = ICHECSMHI_tasmin.extract(t_constraint)
    IPSL_tasmin = IPSL_tasmin.extract(t_constraint)
    MIROC_tasmin = MIROC_tasmin.extract(t_constraint)
    MOHCCCLM_tasmin = MOHCCCLM_tasmin.extract(t_constraint)
    MOHCKNMI_tasmin = MOHCKNMI_tasmin.extract(t_constraint)
    MOHCSMHI_tasmin = MOHCSMHI_tasmin.extract(t_constraint)
    MPICCLM_tasmin = MPICCLM_tasmin.extract(t_constraint)
    MPIREMO_tasmin = MPIREMO_tasmin.extract(t_constraint)
    MPISMHI_tasmin = MPISMHI_tasmin.extract(t_constraint)
    NCCSMHI_tasmin = NCCSMHI_tasmin.extract(t_constraint)
    NOAA_tasmin = NOAA_tasmin.extract(t_constraint)
    
    CCCmaCanRCM_tasmax = CCCmaCanRCM_tasmax.extract(t_constraint)
    CCCmaSMHI_tasmax = CCCmaSMHI_tasmax.extract(t_constraint)
    CNRM_tasmax = CNRM_tasmax.extract(t_constraint)
    CNRMSMHI_tasmax = CNRMSMHI_tasmax.extract(t_constraint)
    CSIRO_tasmax = CSIRO_tasmax.extract(t_constraint)
    ICHECDMI_tasmax = ICHECDMI_tasmax.extract(t_constraint)
    ICHECCCLM_tasmax = ICHECCCLM_tasmax.extract(t_constraint)
    ICHECKNMI_tasmax = ICHECKNMI_tasmax.extract(t_constraint)
    ICHECMPI_tasmax = ICHECMPI_tasmax.extract(t_constraint)
    ICHECSMHI_tasmax = ICHECSMHI_tasmax.extract(t_constraint)
    IPSL_tasmax = IPSL_tasmax.extract(t_constraint)
    MIROC_tasmax = MIROC_tasmax.extract(t_constraint)
    MOHCCCLM_tasmax = MOHCCCLM_tasmax.extract(t_constraint)
    MOHCKNMI_tasmax = MOHCKNMI_tasmax.extract(t_constraint)
    MOHCSMHI_tasmax = MOHCSMHI_tasmax.extract(t_constraint)
    MPICCLM_tasmax = MPICCLM_tasmax.extract(t_constraint)
    MPIREMO_tasmax = MPIREMO_tasmax.extract(t_constraint)
    MPISMHI_tasmax = MPISMHI_tasmax.extract(t_constraint)
    NCCSMHI_tasmax = NCCSMHI_tasmax.extract(t_constraint)
    NOAA_tasmax = NOAA_tasmax.extract(t_constraint)
    
    CCCmaCanRCM_pr = CCCmaCanRCM_pr.extract(t_constraint)
    CCCmaSMHI_pr = CCCmaSMHI_pr.extract(t_constraint)
    CNRM_pr = CNRM_pr.extract(t_constraint)
    CNRMSMHI_pr = CNRMSMHI_pr.extract(t_constraint)
    CSIRO_pr = CSIRO_pr.extract(t_constraint)
    ICHECDMI_pr = ICHECDMI_pr.extract(t_constraint)
    ICHECCCLM_pr = ICHECCCLM_pr.extract(t_constraint)
    ICHECKNMI_pr = ICHECKNMI_pr.extract(t_constraint)
    ICHECMPI_pr = ICHECMPI_pr.extract(t_constraint)
    ICHECSMHI_pr = ICHECSMHI_pr.extract(t_constraint)
    IPSL_pr = IPSL_pr.extract(t_constraint)
    MIROC_pr = MIROC_pr.extract(t_constraint)
    MOHCCCLM_pr = MOHCCCLM_pr.extract(t_constraint)
    MOHCKNMI_pr = MOHCKNMI_pr.extract(t_constraint)
    MOHCSMHI_pr = MOHCSMHI_pr.extract(t_constraint)
    MPICCLM_pr = MPICCLM_pr.extract(t_constraint)
    MPIREMO_pr = MPIREMO_pr.extract(t_constraint)
    MPISMHI_pr = MPISMHI_pr.extract(t_constraint)
    NCCSMHI_pr = NCCSMHI_pr.extract(t_constraint)
    NOAA_pr = NOAA_pr.extract(t_constraint)
    
    CRU_tas = CRU_tas.extract(t_constraint)
    UDel_tas = UDel_tas.extract(t_constraint)
    CRU_tasmin = CRU_tasmin.extract(t_constraint)
    CRU_tasmax = CRU_tasmax.extract(t_constraint)
    CRU_pr = CRU_pr.extract(t_constraint)
    GPCC_pr = GPCC_pr.extract(t_constraint)
    UDel_pr = UDel_pr.extract(t_constraint)
    
    #add day of the year to all files
    iriscc.add_month_number(CCCmaCanRCM_tas, 'time')
    iriscc.add_month_number(CCCmaSMHI_tas, 'time')
    iriscc.add_month_number(CNRM_tas, 'time')
    iriscc.add_month_number(CNRMSMHI_tas, 'time')
    iriscc.add_month_number(CSIRO_tas, 'time')
    iriscc.add_month_number(ICHECDMI_tas, 'time')
    iriscc.add_month_number(ICHECCCLM_tas, 'time')
    iriscc.add_month_number(ICHECKNMI_tas, 'time')
    iriscc.add_month_number(ICHECMPI_tas, 'time')
    iriscc.add_month_number(ICHECSMHI_tas, 'time')
    iriscc.add_month_number(IPSL_tas, 'time')
    iriscc.add_month_number(MIROC_tas, 'time')
    iriscc.add_month_number(MOHCCCLM_tas, 'time')
    iriscc.add_month_number(MOHCKNMI_tas, 'time')
    iriscc.add_month_number(MOHCSMHI_tas, 'time')
    iriscc.add_month_number(MPICCLM_tas, 'time')
    iriscc.add_month_number(MPIREMO_tas, 'time')
    iriscc.add_month_number(MPISMHI_tas, 'time')
    iriscc.add_month_number(NCCSMHI_tas, 'time')
    iriscc.add_month_number(NOAA_tas, 'time')
    
    iriscc.add_month_number(CCCmaCanRCM_tasmin, 'time')
    iriscc.add_month_number(CCCmaSMHI_tasmin, 'time')
    iriscc.add_month_number(CNRM_tasmin, 'time')
    iriscc.add_month_number(CNRMSMHI_tasmin, 'time')
    iriscc.add_month_number(CSIRO_tasmin, 'time')
    iriscc.add_month_number(ICHECDMI_tasmin, 'time')
    iriscc.add_month_number(ICHECCCLM_tasmin, 'time')
    iriscc.add_month_number(ICHECKNMI_tasmin, 'time')
    iriscc.add_month_number(ICHECMPI_tasmin, 'time')
    iriscc.add_month_number(ICHECSMHI_tasmin, 'time')
    iriscc.add_month_number(IPSL_tasmin, 'time')
    iriscc.add_month_number(MIROC_tasmin, 'time')
    iriscc.add_month_number(MOHCCCLM_tasmin, 'time')
    iriscc.add_month_number(MOHCKNMI_tasmin, 'time')
    iriscc.add_month_number(MOHCSMHI_tasmin, 'time')
    iriscc.add_month_number(MPICCLM_tasmin, 'time')
    iriscc.add_month_number(MPIREMO_tasmin, 'time')
    iriscc.add_month_number(MPISMHI_tasmin, 'time')
    iriscc.add_month_number(NCCSMHI_tasmin, 'time')
    iriscc.add_month_number(NOAA_tasmin, 'time')
    
    iriscc.add_month_number(CCCmaCanRCM_tasmax, 'time')
    iriscc.add_month_number(CCCmaSMHI_tasmax, 'time')
    iriscc.add_month_number(CNRM_tasmax, 'time')
    iriscc.add_month_number(CNRMSMHI_tasmax, 'time')
    iriscc.add_month_number(CSIRO_tasmax, 'time')
    iriscc.add_month_number(ICHECDMI_tasmax, 'time')
    iriscc.add_month_number(ICHECCCLM_tasmax, 'time')
    iriscc.add_month_number(ICHECKNMI_tasmax, 'time')
    iriscc.add_month_number(ICHECMPI_tasmax, 'time')
    iriscc.add_month_number(ICHECSMHI_tasmax, 'time')
    iriscc.add_month_number(IPSL_tasmax, 'time')
    iriscc.add_month_number(MIROC_tasmax, 'time')
    iriscc.add_month_number(MOHCCCLM_tasmax, 'time')
    iriscc.add_month_number(MOHCKNMI_tasmax, 'time')
    iriscc.add_month_number(MOHCSMHI_tasmax, 'time')
    iriscc.add_month_number(MPICCLM_tasmax, 'time')
    iriscc.add_month_number(MPIREMO_tasmax, 'time')
    iriscc.add_month_number(MPISMHI_tasmax, 'time')
    iriscc.add_month_number(NCCSMHI_tasmax, 'time')
    iriscc.add_month_number(NOAA_tasmax, 'time')
    
    iriscc.add_month_number(CCCmaCanRCM_pr, 'time')
    iriscc.add_month_number(CCCmaSMHI_pr, 'time')
    iriscc.add_month_number(CNRM_pr, 'time')
    iriscc.add_month_number(CNRMSMHI_pr, 'time')
    iriscc.add_month_number(CSIRO_pr, 'time')
    iriscc.add_month_number(ICHECDMI_pr, 'time')
    iriscc.add_month_number(ICHECCCLM_pr, 'time')
    iriscc.add_month_number(ICHECKNMI_pr, 'time')
    iriscc.add_month_number(ICHECMPI_pr, 'time')
    iriscc.add_month_number(ICHECSMHI_pr, 'time')
    iriscc.add_month_number(IPSL_pr, 'time')
    iriscc.add_month_number(MIROC_pr, 'time')
    iriscc.add_month_number(MOHCCCLM_pr, 'time')
    iriscc.add_month_number(MOHCKNMI_pr, 'time')
    iriscc.add_month_number(MOHCSMHI_pr, 'time')
    iriscc.add_month_number(MPICCLM_pr, 'time')
    iriscc.add_month_number(MPIREMO_pr, 'time')
    iriscc.add_month_number(MPISMHI_pr, 'time')
    iriscc.add_month_number(NCCSMHI_pr, 'time')
    iriscc.add_month_number(NOAA_pr, 'time')
    
    iriscc.add_month_number(CRU_tas, 'time')
    iriscc.add_month_number(UDel_tas, 'time')
    iriscc.add_month_number(CRU_tasmin, 'time')
    iriscc.add_month_number(CRU_tasmax, 'time')
    iriscc.add_month_number(CRU_pr, 'time')
    iriscc.add_month_number(UDel_pr, 'time')
    iriscc.add_month_number(GPCC_pr, 'time')
    
    #add year data to files
    iriscc.add_year(CCCmaCanRCM_tas, 'time')
    iriscc.add_year(CCCmaSMHI_tas, 'time')
    iriscc.add_year(CNRM_tas, 'time')
    iriscc.add_year(CNRMSMHI_tas, 'time')
    iriscc.add_year(CSIRO_tas, 'time')
    iriscc.add_year(ICHECDMI_tas, 'time')
    iriscc.add_year(ICHECCCLM_tas, 'time')
    iriscc.add_year(ICHECKNMI_tas, 'time')
    iriscc.add_year(ICHECMPI_tas, 'time')
    iriscc.add_year(ICHECSMHI_tas, 'time')
    iriscc.add_year(IPSL_tas, 'time')
    iriscc.add_year(MIROC_tas, 'time')
    iriscc.add_year(MOHCCCLM_tas, 'time')
    iriscc.add_year(MOHCKNMI_tas, 'time')
    iriscc.add_year(MOHCSMHI_tas, 'time')
    iriscc.add_year(MPICCLM_tas, 'time')
    iriscc.add_year(MPIREMO_tas, 'time')
    iriscc.add_year(MPISMHI_tas, 'time')
    iriscc.add_year(NCCSMHI_tas, 'time')
    iriscc.add_year(NOAA_tas, 'time')
    
    iriscc.add_year(CCCmaCanRCM_tasmin, 'time')
    iriscc.add_year(CCCmaSMHI_tasmin, 'time')
    iriscc.add_year(CNRM_tasmin, 'time')
    iriscc.add_year(CNRMSMHI_tasmin, 'time')
    iriscc.add_year(CSIRO_tasmin, 'time')
    iriscc.add_year(ICHECDMI_tasmin, 'time')
    iriscc.add_year(ICHECCCLM_tasmin, 'time')
    iriscc.add_year(ICHECKNMI_tasmin, 'time')
    iriscc.add_year(ICHECMPI_tasmin, 'time')
    iriscc.add_year(ICHECSMHI_tasmin, 'time')
    iriscc.add_year(IPSL_tasmin, 'time')
    iriscc.add_year(MIROC_tasmin, 'time')
    iriscc.add_year(MOHCCCLM_tasmin, 'time')
    iriscc.add_year(MOHCKNMI_tasmin, 'time')
    iriscc.add_year(MOHCSMHI_tasmin, 'time')
    iriscc.add_year(MPICCLM_tasmin, 'time')
    iriscc.add_year(MPIREMO_tasmin, 'time')
    iriscc.add_year(MPISMHI_tasmin, 'time')
    iriscc.add_year(NCCSMHI_tasmin, 'time')
    iriscc.add_year(NOAA_tasmin, 'time')
    
    iriscc.add_year(CCCmaCanRCM_tasmax, 'time')
    iriscc.add_year(CCCmaSMHI_tasmax, 'time')
    iriscc.add_year(CNRM_tasmax, 'time')
    iriscc.add_year(CNRMSMHI_tasmax, 'time')
    iriscc.add_year(CSIRO_tasmax, 'time')
    iriscc.add_year(ICHECDMI_tasmax, 'time')
    iriscc.add_year(ICHECCCLM_tasmax, 'time')
    iriscc.add_year(ICHECKNMI_tasmax, 'time')
    iriscc.add_year(ICHECMPI_tasmax, 'time')
    iriscc.add_year(ICHECSMHI_tasmax, 'time')
    iriscc.add_year(IPSL_tasmax, 'time')
    iriscc.add_year(MIROC_tasmax, 'time')
    iriscc.add_year(MOHCCCLM_tasmax, 'time')
    iriscc.add_year(MOHCKNMI_tasmax, 'time')
    iriscc.add_year(MOHCSMHI_tasmax, 'time')
    iriscc.add_year(MPICCLM_tasmax, 'time')
    iriscc.add_year(MPIREMO_tasmax, 'time')
    iriscc.add_year(MPISMHI_tasmax, 'time')
    iriscc.add_year(NCCSMHI_tasmax, 'time')
    iriscc.add_year(NOAA_tasmax, 'time')
    
    iriscc.add_year(CCCmaCanRCM_pr, 'time')
    iriscc.add_year(CCCmaSMHI_pr, 'time')
    iriscc.add_year(CNRM_pr, 'time')
    iriscc.add_year(CNRMSMHI_pr, 'time')
    iriscc.add_year(CSIRO_pr, 'time')
    iriscc.add_year(ICHECDMI_pr, 'time')
    iriscc.add_year(ICHECCCLM_pr, 'time')
    iriscc.add_year(ICHECKNMI_pr, 'time')
    iriscc.add_year(ICHECMPI_pr, 'time')
    iriscc.add_year(ICHECSMHI_pr, 'time')
    iriscc.add_year(IPSL_pr, 'time')
    iriscc.add_year(MIROC_pr, 'time')
    iriscc.add_year(MOHCCCLM_pr, 'time')
    iriscc.add_year(MOHCKNMI_pr, 'time')
    iriscc.add_year(MOHCSMHI_pr, 'time')
    iriscc.add_year(MPICCLM_pr, 'time')
    iriscc.add_year(MPIREMO_pr, 'time')
    iriscc.add_year(MPISMHI_pr, 'time')
    iriscc.add_year(NCCSMHI_pr, 'time')
    iriscc.add_year(NOAA_pr, 'time')
    
    iriscc.add_year(CRU_tas, 'time')
    iriscc.add_year(UDel_tas, 'time')
    iriscc.add_year(CRU_tasmin, 'time')
    iriscc.add_year(CRU_tasmax, 'time')
    iriscc.add_year(CRU_pr, 'time')
    iriscc.add_year(UDel_pr, 'time')
    iriscc.add_year(GPCC_pr, 'time')
    
    #We are interested in plotting the data by month, so we need to take a mean of all the data by month 
    CCCmaCanRCM_tas = CCCmaCanRCM_tas.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_tas = CCCmaSMHI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_tas = CNRM_tas.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_tas = CNRMSMHI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_tas = CSIRO_tas.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_tas = ICHECDMI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_tas = ICHECCCLM_tas.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_tas = ICHECKNMI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_tas = ICHECMPI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_tas = ICHECSMHI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_tas = IPSL_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_tas = MIROC_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_tas = MOHCCCLM_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_tas = MOHCKNMI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_tas = MOHCSMHI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_tas = MPICCLM_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_tas = MPIREMO_tas.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_tas = MPISMHI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_tas = NCCSMHI_tas.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_tas = NOAA_tas.aggregated_by('month_number', iris.analysis.MEAN)
    
    CCCmaCanRCM_tasmin = CCCmaCanRCM_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_tasmin = CCCmaSMHI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_tasmin = CNRM_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_tasmin = CNRMSMHI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_tasmin = CSIRO_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_tasmin = ICHECDMI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_tasmin = ICHECCCLM_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_tasmin = ICHECKNMI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_tasmin = ICHECMPI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_tasmin = ICHECSMHI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_tasmin = IPSL_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_tasmin = MIROC_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_tasmin = MOHCCCLM_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_tasmin = MOHCKNMI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_tasmin = MOHCSMHI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_tasmin = MPICCLM_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_tasmin = MPIREMO_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_tasmin = MPISMHI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_tasmin = NCCSMHI_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_tasmin = NOAA_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    
    CCCmaCanRCM_tasmax = CCCmaCanRCM_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_tasmax = CCCmaSMHI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_tasmax = CNRM_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_tasmax = CNRMSMHI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_tasmax = CSIRO_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_tasmax = ICHECDMI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_tasmax = ICHECCCLM_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_tasmax = ICHECKNMI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_tasmax = ICHECMPI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_tasmax = ICHECSMHI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_tasmax = IPSL_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_tasmax = MIROC_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_tasmax = MOHCCCLM_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_tasmax = MOHCKNMI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_tasmax = MOHCSMHI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_tasmax = MPICCLM_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_tasmax = MPIREMO_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_tasmax = MPISMHI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_tasmax = NCCSMHI_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_tasmax = NOAA_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    
    CCCmaCanRCM_pr = CCCmaCanRCM_pr.aggregated_by('month_number', iris.analysis.MEAN)
    CCCmaSMHI_pr = CCCmaSMHI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    CNRM_pr = CNRM_pr.aggregated_by('month_number', iris.analysis.MEAN)
    CNRMSMHI_pr = CNRMSMHI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    CSIRO_pr = CSIRO_pr.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECDMI_pr = ICHECDMI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECCCLM_pr = ICHECCCLM_pr.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECKNMI_pr = ICHECKNMI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECMPI_pr = ICHECMPI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    ICHECSMHI_pr = ICHECSMHI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    IPSL_pr = IPSL_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MIROC_pr = MIROC_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCCCLM_pr = MOHCCCLM_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCKNMI_pr = MOHCKNMI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MOHCSMHI_pr = MOHCSMHI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MPICCLM_pr = MPICCLM_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MPIREMO_pr = MPIREMO_pr.aggregated_by('month_number', iris.analysis.MEAN)
    MPISMHI_pr = MPISMHI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    NCCSMHI_pr = NCCSMHI_pr.aggregated_by('month_number', iris.analysis.MEAN)
    NOAA_pr = NOAA_pr.aggregated_by('month_number', iris.analysis.MEAN)
    
    CRU_tas = CRU_tas.aggregated_by('month_number', iris.analysis.MEAN)
    UDel_tas = UDel_tas.aggregated_by('month_number', iris.analysis.MEAN)
    CRU_tasmin = CRU_tasmin.aggregated_by('month_number', iris.analysis.MEAN)
    CRU_tasmax = CRU_tasmax.aggregated_by('month_number', iris.analysis.MEAN)
    CRU_pr = CRU_pr.aggregated_by('month_number', iris.analysis.MEAN)
    UDel_pr = UDel_pr.aggregated_by('month_number', iris.analysis.MEAN)
    GPCC_pr = GPCC_pr.aggregated_by('month_number', iris.analysis.MEAN)
    
    #Returns an array of area weights, with the same dimensions as the cube.
    CCCmaCanRCM_tas_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_tas)
    CCCmaSMHI_tas_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_tas)
    CNRM_tas_grid_areas = iris.analysis.cartography.area_weights(CNRM_tas)
    CNRMSMHI_tas_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_tas)
    CSIRO_tas_grid_areas = iris.analysis.cartography.area_weights(CSIRO_tas)
    ICHECDMI_tas_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_tas)
    ICHECCCLM_tas_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_tas)
    ICHECKNMI_tas_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_tas)
    ICHECMPI_tas_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_tas)
    ICHECSMHI_tas_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_tas)
    IPSL_tas_grid_areas = iris.analysis.cartography.area_weights(IPSL_tas)
    MIROC_tas_grid_areas = iris.analysis.cartography.area_weights(MIROC_tas)
    MOHCCCLM_tas_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_tas)
    MOHCKNMI_tas_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_tas)
    MOHCSMHI_tas_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_tas)
    MPICCLM_tas_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_tas)
    MPIREMO_tas_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_tas)
    MPISMHI_tas_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_tas)
    NCCSMHI_tas_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_tas)
    NOAA_tas_grid_areas = iris.analysis.cartography.area_weights(NOAA_tas)
    
    CCCmaCanRCM_tasmin_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_tasmin)
    CCCmaSMHI_tasmin_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_tasmin)
    CNRM_tasmin_grid_areas = iris.analysis.cartography.area_weights(CNRM_tasmin)
    CNRMSMHI_tasmin_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_tasmin)
    CSIRO_tasmin_grid_areas = iris.analysis.cartography.area_weights(CSIRO_tasmin)
    ICHECDMI_tasmin_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_tasmin)
    ICHECCCLM_tasmin_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_tasmin)
    ICHECKNMI_tasmin_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_tasmin)
    ICHECMPI_tasmin_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_tasmin)
    ICHECSMHI_tasmin_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_tasmin)
    IPSL_tasmin_grid_areas = iris.analysis.cartography.area_weights(IPSL_tasmin)
    MIROC_tasmin_grid_areas = iris.analysis.cartography.area_weights(MIROC_tasmin)
    MOHCCCLM_tasmin_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_tasmin)
    MOHCKNMI_tasmin_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_tasmin)
    MOHCSMHI_tasmin_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_tasmin)
    MPICCLM_tasmin_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_tasmin)
    MPIREMO_tasmin_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_tasmin)
    MPISMHI_tasmin_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_tasmin)
    NCCSMHI_tasmin_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_tasmin)
    NOAA_tasmin_grid_areas = iris.analysis.cartography.area_weights(NOAA_tasmin)
    
    CCCmaCanRCM_tasmax_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_tasmax)
    CCCmaSMHI_tasmax_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_tasmax)
    CNRM_tasmax_grid_areas = iris.analysis.cartography.area_weights(CNRM_tasmax)
    CNRMSMHI_tasmax_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_tasmax)
    CSIRO_tasmax_grid_areas = iris.analysis.cartography.area_weights(CSIRO_tasmax)
    ICHECDMI_tasmax_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_tasmax)
    ICHECCCLM_tasmax_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_tasmax)
    ICHECKNMI_tasmax_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_tasmax)
    ICHECMPI_tasmax_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_tasmax)
    ICHECSMHI_tasmax_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_tasmax)
    IPSL_tasmax_grid_areas = iris.analysis.cartography.area_weights(IPSL_tasmax)
    MIROC_tasmax_grid_areas = iris.analysis.cartography.area_weights(MIROC_tasmax)
    MOHCCCLM_tasmax_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_tasmax)
    MOHCKNMI_tasmax_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_tasmax)
    MOHCSMHI_tasmax_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_tasmax)
    MPICCLM_tasmax_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_tasmax)
    MPIREMO_tasmax_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_tasmax)
    MPISMHI_tasmax_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_tasmax)
    NCCSMHI_tasmax_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_tasmax)
    NOAA_tasmax_grid_areas = iris.analysis.cartography.area_weights(NOAA_tasmax)
    
    CCCmaCanRCM_pr_grid_areas = iris.analysis.cartography.area_weights(CCCmaCanRCM_pr)
    CCCmaSMHI_pr_grid_areas = iris.analysis.cartography.area_weights(CCCmaSMHI_pr)
    CNRM_pr_grid_areas = iris.analysis.cartography.area_weights(CNRM_pr)
    CNRMSMHI_pr_grid_areas = iris.analysis.cartography.area_weights(CNRMSMHI_pr)
    CSIRO_pr_grid_areas = iris.analysis.cartography.area_weights(CSIRO_pr)
    ICHECDMI_pr_grid_areas = iris.analysis.cartography.area_weights(ICHECDMI_pr)
    ICHECCCLM_pr_grid_areas = iris.analysis.cartography.area_weights(ICHECCCLM_pr)
    ICHECKNMI_pr_grid_areas = iris.analysis.cartography.area_weights(ICHECKNMI_pr)
    ICHECMPI_pr_grid_areas = iris.analysis.cartography.area_weights(ICHECMPI_pr)
    ICHECSMHI_pr_grid_areas = iris.analysis.cartography.area_weights(ICHECSMHI_pr)
    IPSL_pr_grid_areas = iris.analysis.cartography.area_weights(IPSL_pr)
    MIROC_pr_grid_areas = iris.analysis.cartography.area_weights(MIROC_pr)
    MOHCCCLM_pr_grid_areas = iris.analysis.cartography.area_weights(MOHCCCLM_pr)
    MOHCKNMI_pr_grid_areas = iris.analysis.cartography.area_weights(MOHCKNMI_pr)
    MOHCSMHI_pr_grid_areas = iris.analysis.cartography.area_weights(MOHCSMHI_pr)
    MPICCLM_pr_grid_areas = iris.analysis.cartography.area_weights(MPICCLM_pr)
    MPIREMO_pr_grid_areas = iris.analysis.cartography.area_weights(MPIREMO_pr)
    MPISMHI_pr_grid_areas = iris.analysis.cartography.area_weights(MPISMHI_pr)
    NCCSMHI_pr_grid_areas = iris.analysis.cartography.area_weights(NCCSMHI_pr)
    NOAA_pr_grid_areas = iris.analysis.cartography.area_weights(NOAA_pr)
    
    CRU_tas_grid_areas = iris.analysis.cartography.area_weights(CRU_tas)
    UDel_tas_grid_areas = iris.analysis.cartography.area_weights(UDel_tas)
    CRU_tasmin_grid_areas = iris.analysis.cartography.area_weights(CRU_tasmin)
    CRU_tasmax_grid_areas = iris.analysis.cartography.area_weights(CRU_tasmax)
    CRU_pr_grid_areas = iris.analysis.cartography.area_weights(CRU_pr)
    GPCC_pr_grid_areas = iris.analysis.cartography.area_weights(GPCC_pr)
    UDel_pr_grid_areas = iris.analysis.cartography.area_weights(UDel_pr)
    
    #We want to plot the mean for the whole region so we need a mean of all the lats and lons
    CCCmaCanRCM_tas_mean = CCCmaCanRCM_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_tas_grid_areas)  
    CCCmaSMHI_tas_mean = CCCmaSMHI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_tas_grid_areas)  
    CNRM_tas_mean = CNRM_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_tas_grid_areas)
    CNRMSMHI_tas_mean = CNRMSMHI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_tas_grid_areas)  
    CSIRO_tas_mean = CSIRO_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_tas_grid_areas)  
    ICHECDMI_tas_mean = ICHECDMI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_tas_grid_areas)  
    ICHECCCLM_tas_mean = ICHECCCLM_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_tas_grid_areas)  
    ICHECKNMI_tas_mean = ICHECKNMI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_tas_grid_areas)  
    ICHECMPI_tas_mean = ICHECMPI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_tas_grid_areas)  
    ICHECSMHI_tas_mean = ICHECSMHI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_tas_grid_areas)  
    IPSL_tas_mean = IPSL_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_tas_grid_areas)
    MIROC_tas_mean = MIROC_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_tas_grid_areas)  
    MOHCCCLM_tas_mean = MOHCCCLM_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_tas_grid_areas)  
    MOHCKNMI_tas_mean = MOHCKNMI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_tas_grid_areas)  
    MOHCSMHI_tas_mean = MOHCSMHI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_tas_grid_areas)  
    MPICCLM_tas_mean = MPICCLM_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_tas_grid_areas)  
    MPIREMO_tas_mean = MPIREMO_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_tas_grid_areas)  
    MPISMHI_tas_mean = MPISMHI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_tas_grid_areas)  
    NCCSMHI_tas_mean = NCCSMHI_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_tas_grid_areas)  
    NOAA_tas_mean = NOAA_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_tas_grid_areas) 
    
    CCCmaCanRCM_tasmin_mean = CCCmaCanRCM_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_tasmin_grid_areas)  
    CCCmaSMHI_tasmin_mean = CCCmaSMHI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_tasmin_grid_areas)  
    CNRM_tasmin_mean = CNRM_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_tasmin_grid_areas)
    CNRMSMHI_tasmin_mean = CNRMSMHI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_tasmin_grid_areas)  
    CSIRO_tasmin_mean = CSIRO_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_tasmin_grid_areas)  
    ICHECDMI_tasmin_mean = ICHECDMI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_tasmin_grid_areas)  
    ICHECCCLM_tasmin_mean = ICHECCCLM_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_tasmin_grid_areas)  
    ICHECKNMI_tasmin_mean = ICHECKNMI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_tasmin_grid_areas)  
    ICHECMPI_tasmin_mean = ICHECMPI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_tasmin_grid_areas)  
    ICHECSMHI_tasmin_mean = ICHECSMHI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_tasmin_grid_areas)  
    IPSL_tasmin_mean = IPSL_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_tasmin_grid_areas)
    MIROC_tasmin_mean = MIROC_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_tasmin_grid_areas)  
    MOHCCCLM_tasmin_mean = MOHCCCLM_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_tasmin_grid_areas)  
    MOHCKNMI_tasmin_mean = MOHCKNMI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_tasmin_grid_areas)  
    MOHCSMHI_tasmin_mean = MOHCSMHI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_tasmin_grid_areas)  
    MPICCLM_tasmin_mean = MPICCLM_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_tasmin_grid_areas)  
    MPIREMO_tasmin_mean = MPIREMO_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_tasmin_grid_areas)  
    MPISMHI_tasmin_mean = MPISMHI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_tasmin_grid_areas)  
    NCCSMHI_tasmin_mean = NCCSMHI_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_tasmin_grid_areas)  
    NOAA_tasmin_mean = NOAA_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_tasmin_grid_areas) 
    
    CCCmaCanRCM_tasmax_mean = CCCmaCanRCM_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_tasmax_grid_areas)  
    CCCmaSMHI_tasmax_mean = CCCmaSMHI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_tasmax_grid_areas)  
    CNRM_tasmax_mean = CNRM_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_tasmax_grid_areas)
    CNRMSMHI_tasmax_mean = CNRMSMHI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_tasmax_grid_areas)  
    CSIRO_tasmax_mean = CSIRO_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_tasmax_grid_areas)  
    ICHECDMI_tasmax_mean = ICHECDMI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_tasmax_grid_areas)  
    ICHECCCLM_tasmax_mean = ICHECCCLM_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_tasmax_grid_areas)  
    ICHECKNMI_tasmax_mean = ICHECKNMI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_tasmax_grid_areas)  
    ICHECMPI_tasmax_mean = ICHECMPI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_tasmax_grid_areas)  
    ICHECSMHI_tasmax_mean = ICHECSMHI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_tasmax_grid_areas)  
    IPSL_tasmax_mean = IPSL_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_tasmax_grid_areas)
    MIROC_tasmax_mean = MIROC_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_tasmax_grid_areas)  
    MOHCCCLM_tasmax_mean = MOHCCCLM_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_tasmax_grid_areas)  
    MOHCKNMI_tasmax_mean = MOHCKNMI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_tasmax_grid_areas)  
    MOHCSMHI_tasmax_mean = MOHCSMHI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_tasmax_grid_areas)  
    MPICCLM_tasmax_mean = MPICCLM_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_tasmax_grid_areas)  
    MPIREMO_tasmax_mean = MPIREMO_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_tasmax_grid_areas)  
    MPISMHI_tasmax_mean = MPISMHI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_tasmax_grid_areas)  
    NCCSMHI_tasmax_mean = NCCSMHI_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_tasmax_grid_areas)  
    NOAA_tasmax_mean = NOAA_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_tasmax_grid_areas) 
    
    CCCmaCanRCM_pr_mean = CCCmaCanRCM_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaCanRCM_pr_grid_areas)  
    CCCmaSMHI_pr_mean = CCCmaSMHI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CCCmaSMHI_pr_grid_areas)  
    CNRM_pr_mean = CNRM_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRM_pr_grid_areas)
    CNRMSMHI_pr_mean = CNRMSMHI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CNRMSMHI_pr_grid_areas)  
    CSIRO_pr_mean = CSIRO_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CSIRO_pr_grid_areas)  
    ICHECDMI_pr_mean = ICHECDMI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECDMI_pr_grid_areas)  
    ICHECCCLM_pr_mean = ICHECCCLM_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECCCLM_pr_grid_areas)  
    ICHECKNMI_pr_mean = ICHECKNMI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECKNMI_pr_grid_areas)  
    ICHECMPI_pr_mean = ICHECMPI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECMPI_pr_grid_areas)  
    ICHECSMHI_pr_mean = ICHECSMHI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=ICHECSMHI_pr_grid_areas)  
    IPSL_pr_mean = IPSL_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=IPSL_pr_grid_areas)
    MIROC_pr_mean = MIROC_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MIROC_pr_grid_areas)  
    MOHCCCLM_pr_mean = MOHCCCLM_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCCCLM_pr_grid_areas)  
    MOHCKNMI_pr_mean = MOHCKNMI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCKNMI_pr_grid_areas)  
    MOHCSMHI_pr_mean = MOHCSMHI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MOHCSMHI_pr_grid_areas)  
    MPICCLM_pr_mean = MPICCLM_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPICCLM_pr_grid_areas)  
    MPIREMO_pr_mean = MPIREMO_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPIREMO_pr_grid_areas)  
    MPISMHI_pr_mean = MPISMHI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=MPISMHI_pr_grid_areas)  
    NCCSMHI_pr_mean = NCCSMHI_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NCCSMHI_pr_grid_areas)  
    NOAA_pr_mean = NOAA_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=NOAA_pr_grid_areas) 
    
    CRU_tas_mean = CRU_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_tas_grid_areas)
    UDel_tas_mean = UDel_tas.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_tas_grid_areas)
    CRU_tasmin_mean = CRU_tasmin.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_tasmin_grid_areas)
    CRU_tasmax_mean = CRU_tasmax.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_tasmax_grid_areas)
    CRU_pr_mean = CRU_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=CRU_pr_grid_areas)
    UDel_pr_mean = UDel_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=UDel_pr_grid_areas)
    GPCC_pr_mean = GPCC_pr.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=GPCC_pr_grid_areas)
    
    
    #-------------------------------------------------------------------------
    #PART 4: RE-BASELINE PAST MODELS   
    
    #for the observed data and the baseline past data we don't need to average for each year, but the average for the whole time period, so collapse by year
    CCCmaCanRCM_b_tas_mean = CCCmaCanRCM_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    CCCmaSMHI_b_tas_mean = CCCmaSMHI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    CNRM_b_tas_mean = CNRM_tas_mean.collapsed(['year'], iris.analysis.MEAN)
    CNRMSMHI_b_tas_mean = CNRMSMHI_tas_mean.collapsed(['year'], iris.analysis.MEAN)   
    CSIRO_b_tas_mean = CSIRO_tas_mean.collapsed(['year'], iris.analysis.MEAN)
    ICHECDMI_b_tas_mean = ICHECDMI_tas_mean.collapsed(['year'], iris.analysis.MEAN)  
    ICHECCCLM_b_tas_mean = ICHECCCLM_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECKNMI_b_tas_mean = ICHECKNMI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECMPI_b_tas_mean = ICHECMPI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECSMHI_b_tas_mean = ICHECSMHI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    IPSL_b_tas_mean = IPSL_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    MIROC_b_tas_mean = MIROC_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCCCLM_b_tas_mean = MOHCCCLM_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCKNMI_b_tas_mean = MOHCKNMI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCSMHI_b_tas_mean = MOHCSMHI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    MPICCLM_b_tas_mean = MPICCLM_tas_mean.collapsed(['year'], iris.analysis.MEAN)        
    MPIREMO_b_tas_mean = MPIREMO_tas_mean.collapsed(['year'], iris.analysis.MEAN)           
    MPISMHI_b_tas_mean = MPISMHI_tas_mean.collapsed(['year'], iris.analysis.MEAN) 
    NCCSMHI_b_tas_mean = NCCSMHI_tas_mean.collapsed(['year'], iris.analysis.MEAN)  
    NOAA_b_tas_mean = NOAA_tas_mean.collapsed(['year'], iris.analysis.MEAN)  
    
    CCCmaCanRCM_b_tasmin_mean = CCCmaCanRCM_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    CCCmaSMHI_b_tasmin_mean = CCCmaSMHI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    CNRM_b_tasmin_mean = CNRM_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)               
    CNRMSMHI_b_tasmin_mean = CNRMSMHI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)   
    CSIRO_b_tasmin_mean = CSIRO_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)
    ICHECDMI_b_tasmin_mean = ICHECDMI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)  
    ICHECCCLM_b_tasmin_mean = ICHECCCLM_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECKNMI_b_tasmin_mean = ICHECKNMI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECMPI_b_tasmin_mean = ICHECMPI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECSMHI_b_tasmin_mean = ICHECSMHI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    IPSL_b_tasmin_mean = IPSL_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    MIROC_b_tasmin_mean = MIROC_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCCCLM_b_tasmin_mean = MOHCCCLM_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCKNMI_b_tasmin_mean = MOHCKNMI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCSMHI_b_tasmin_mean = MOHCSMHI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    MPICCLM_b_tasmin_mean = MPICCLM_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)        
    MPIREMO_b_tasmin_mean = MPIREMO_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)         
    MPISMHI_b_tasmin_mean = MPISMHI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN) 
    NCCSMHI_b_tasmin_mean = NCCSMHI_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)  
    NOAA_b_tasmin_mean = NOAA_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)  
    
    CCCmaCanRCM_b_tasmax_mean = CCCmaCanRCM_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    CCCmaSMHI_b_tasmax_mean = CCCmaSMHI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    CNRM_b_tasmax_mean = CNRM_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)            
    CNRMSMHI_b_tasmax_mean = CNRMSMHI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)   
    CSIRO_b_tasmax_mean = CSIRO_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)
    ICHECDMI_b_tasmax_mean = ICHECDMI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)  
    ICHECCCLM_b_tasmax_mean = ICHECCCLM_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECKNMI_b_tasmax_mean = ICHECKNMI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECMPI_b_tasmax_mean = ICHECMPI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECSMHI_b_tasmax_mean = ICHECSMHI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    IPSL_b_tasmax_mean = IPSL_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    MIROC_b_tasmax_mean = MIROC_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCCCLM_b_tasmax_mean = MOHCCCLM_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCKNMI_b_tasmax_mean = MOHCKNMI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCSMHI_b_tasmax_mean = MOHCSMHI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    MPICCLM_b_tasmax_mean = MPICCLM_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)        
    MPIREMO_b_tasmax_mean = MPIREMO_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)      
    MPISMHI_b_tasmax_mean = MPISMHI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN) 
    NCCSMHI_b_tasmax_mean = NCCSMHI_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)  
    NOAA_b_tasmax_mean = NOAA_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)
    
    CCCmaCanRCM_b_pr_mean = CCCmaCanRCM_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    CCCmaSMHI_b_pr_mean = CCCmaSMHI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    CNRM_b_pr_mean = CNRM_pr_mean.collapsed(['year'], iris.analysis.MEAN)                      
    CNRMSMHI_b_pr_mean = CNRMSMHI_pr_mean.collapsed(['year'], iris.analysis.MEAN)   
    CSIRO_b_pr_mean = CSIRO_pr_mean.collapsed(['year'], iris.analysis.MEAN)
    ICHECDMI_b_pr_mean = ICHECDMI_pr_mean.collapsed(['year'], iris.analysis.MEAN)  
    ICHECCCLM_b_pr_mean = ICHECCCLM_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECKNMI_b_pr_mean = ICHECKNMI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECMPI_b_pr_mean = ICHECMPI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    ICHECSMHI_b_pr_mean = ICHECSMHI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    IPSL_b_pr_mean = IPSL_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    MIROC_b_pr_mean = MIROC_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCCCLM_b_pr_mean = MOHCCCLM_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCKNMI_b_pr_mean = MOHCKNMI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    MOHCSMHI_b_pr_mean = MOHCSMHI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    MPICCLM_b_pr_mean = MPICCLM_pr_mean.collapsed(['year'], iris.analysis.MEAN)        
    MPIREMO_b_pr_mean = MPIREMO_pr_mean.collapsed(['year'], iris.analysis.MEAN)           
    MPISMHI_b_pr_mean = MPISMHI_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    NCCSMHI_b_pr_mean = NCCSMHI_pr_mean.collapsed(['year'], iris.analysis.MEAN)  
    NOAA_b_pr_mean = NOAA_pr_mean.collapsed(['year'], iris.analysis.MEAN)  
    
    CRU_tas_mean = CRU_tas_mean.collapsed(['year'], iris.analysis.MEAN)  
    UDel_tas_mean = UDel_tas_mean.collapsed(['year'], iris.analysis.MEAN)  
    CRU_tasmin_mean = CRU_tasmin_mean.collapsed(['year'], iris.analysis.MEAN)     
    CRU_tasmax_mean = CRU_tasmax_mean.collapsed(['year'], iris.analysis.MEAN)     
    CRU_pr_mean = CRU_pr_mean.collapsed(['year'], iris.analysis.MEAN)     
    UDel_pr_mean = UDel_pr_mean.collapsed(['year'], iris.analysis.MEAN)    
    GPCC_pr_mean = GPCC_pr_mean.collapsed(['year'], iris.analysis.MEAN) 
    
    #Create average
    Obs_tas = (CRU_tas_mean + UDel_tas_mean)/2.
    Obs_tasmin = (CRU_tasmin_mean.data)
    Obs_tasmax = (CRU_tasmax_mean.data)    
    Obs_pr = (CRU_pr_mean + UDel_pr_mean + GPCC_pr_mean)/3
    
    #We want to see the change in temperature from the baseline
    CCCmaCanRCM_tas_mean = (CCCmaCanRCM_tas_mean.data - CCCmaCanRCM_b_tas_mean.data + Obs_tas.data)
    CCCmaSMHI_tas_mean = (CCCmaSMHI_tas_mean.data - CCCmaSMHI_b_tas_mean.data + Obs_tas.data)
    CNRM_tas_mean = (CNRM_tas_mean.data - CNRM_b_tas_mean.data + Obs_tas.data)
    CNRMSMHI_tas_mean = (CNRMSMHI_tas_mean.data - CNRMSMHI_b_tas_mean.data + Obs_tas.data)  
    CSIRO_tas_mean = (CSIRO_tas_mean.data - CSIRO_b_tas_mean.data + Obs_tas.data)
    ICHECDMI_tas_mean = (ICHECDMI_tas_mean.data - ICHECDMI_b_tas_mean.data + Obs_tas.data) 
    ICHECCCLM_tas_mean = (ICHECCCLM_tas_mean.data - ICHECCCLM_b_tas_mean.data + Obs_tas.data)
    ICHECKNMI_tas_mean = (ICHECKNMI_tas_mean.data - ICHECKNMI_b_tas_mean.data + Obs_tas.data)
    ICHECMPI_tas_mean = (ICHECMPI_tas_mean.data - ICHECMPI_b_tas_mean.data + Obs_tas.data)
    ICHECSMHI_tas_mean = (ICHECSMHI_tas_mean.data - ICHECSMHI_b_tas_mean.data + Obs_tas.data)
    IPSL_tas_mean = (IPSL_tas_mean.data - IPSL_b_tas_mean.data + Obs_tas.data)
    MIROC_tas_mean = (MIROC_tas_mean.data - MIROC_b_tas_mean.data + Obs_tas.data)
    MOHCCCLM_tas_mean = (MOHCCCLM_tas_mean.data - MOHCCCLM_b_tas_mean.data + Obs_tas.data)
    MOHCKNMI_tas_mean = (MOHCKNMI_tas_mean.data - MOHCKNMI_b_tas_mean.data + Obs_tas.data)
    MOHCSMHI_tas_mean = (MOHCSMHI_tas_mean.data - MOHCSMHI_b_tas_mean.data + Obs_tas.data)
    MPICCLM_tas_mean = (MPICCLM_tas_mean.data - MPICCLM_b_tas_mean.data + Obs_tas.data)      
    MPIREMO_tas_mean = (MPIREMO_tas_mean.data - MPIREMO_b_tas_mean.data + Obs_tas.data)        
    MPISMHI_tas_mean = (MPISMHI_tas_mean.data - MPISMHI_b_tas_mean.data + Obs_tas.data)
    NCCSMHI_tas_mean = (NCCSMHI_tas_mean.data - NCCSMHI_b_tas_mean.data + Obs_tas.data) 
    NOAA_tas_mean = (NOAA_tas_mean.data - NOAA_b_tas_mean.data + Obs_tas.data)
    
    CCCmaCanRCM_tasmin_mean = (CCCmaCanRCM_tasmin_mean.data - CCCmaCanRCM_b_tasmin_mean.data + Obs_tasmin)
    CCCmaSMHI_tasmin_mean = (CCCmaSMHI_tasmin_mean.data - CCCmaSMHI_b_tasmin_mean.data + Obs_tasmin)
    CNRM_tasmin_mean = (CNRM_tasmin_mean.data - CNRM_b_tasmin_mean.data + Obs_tasmin)
    CNRMSMHI_tasmin_mean = (CNRMSMHI_tasmin_mean.data - CNRMSMHI_b_tasmin_mean.data + Obs_tasmin)  
    CSIRO_tasmin_mean = (CSIRO_tasmin_mean.data - CSIRO_b_tasmin_mean.data + Obs_tasmin)
    ICHECDMI_tasmin_mean = (ICHECDMI_tasmin_mean.data - ICHECDMI_b_tasmin_mean.data + Obs_tasmin) 
    ICHECCCLM_tasmin_mean = (ICHECCCLM_tasmin_mean.data - ICHECCCLM_b_tasmin_mean.data + Obs_tasmin)
    ICHECKNMI_tasmin_mean = (ICHECKNMI_tasmin_mean.data - ICHECKNMI_b_tasmin_mean.data + Obs_tasmin)
    ICHECMPI_tasmin_mean = (ICHECMPI_tasmin_mean.data - ICHECMPI_b_tasmin_mean.data + Obs_tasmin)
    ICHECSMHI_tasmin_mean = (ICHECSMHI_tasmin_mean.data - ICHECSMHI_b_tasmin_mean.data + Obs_tasmin)
    IPSL_tasmin_mean = (IPSL_tasmin_mean.data - IPSL_b_tasmin_mean.data + Obs_tasmin)
    MIROC_tasmin_mean = (MIROC_tasmin_mean.data - MIROC_b_tasmin_mean.data + Obs_tasmin)
    MOHCCCLM_tasmin_mean = (MOHCCCLM_tasmin_mean.data - MOHCCCLM_b_tasmin_mean.data + Obs_tasmin)
    MOHCKNMI_tasmin_mean = (MOHCKNMI_tasmin_mean.data - MOHCKNMI_b_tasmin_mean.data + Obs_tasmin)
    MOHCSMHI_tasmin_mean = (MOHCSMHI_tasmin_mean.data - MOHCSMHI_b_tasmin_mean.data + Obs_tasmin)
    MPICCLM_tasmin_mean = (MPICCLM_tasmin_mean.data - MPICCLM_b_tasmin_mean.data + Obs_tasmin)
    MPIREMO_tasmin_mean = (MPIREMO_tasmin_mean.data - MPIREMO_b_tasmin_mean.data + Obs_tasmin) 
    MPISMHI_tasmin_mean = (MPISMHI_tasmin_mean.data - MPISMHI_b_tasmin_mean.data + Obs_tasmin)
    NCCSMHI_tasmin_mean = (NCCSMHI_tasmin_mean.data - NCCSMHI_b_tasmin_mean.data + Obs_tasmin) 
    NOAA_tasmin_mean = (NOAA_tasmin_mean.data - NOAA_b_tasmin_mean.data + Obs_tasmin)
    
    CCCmaCanRCM_tasmax_mean = (CCCmaCanRCM_tasmax_mean.data - CCCmaCanRCM_b_tasmax_mean.data + Obs_tasmax)
    CCCmaSMHI_tasmax_mean = (CCCmaSMHI_tasmax_mean.data - CCCmaSMHI_b_tasmax_mean.data + Obs_tasmax)
    CNRM_tasmax_mean = (CNRM_tasmax_mean.data - CNRM_b_tasmax_mean.data + Obs_tasmax)
    CNRMSMHI_tasmax_mean = (CNRMSMHI_tasmax_mean.data - CNRMSMHI_b_tasmax_mean.data + Obs_tasmax)  
    CSIRO_tasmax_mean = (CSIRO_tasmax_mean.data - CSIRO_b_tasmax_mean.data + Obs_tasmax)
    ICHECDMI_tasmax_mean = (ICHECDMI_tasmax_mean.data - ICHECDMI_b_tasmax_mean.data + Obs_tasmax) 
    ICHECCCLM_tasmax_mean = (ICHECCCLM_tasmax_mean.data - ICHECCCLM_b_tasmax_mean.data + Obs_tasmax)
    ICHECKNMI_tasmax_mean = (ICHECKNMI_tasmax_mean.data - ICHECKNMI_b_tasmax_mean.data + Obs_tasmax)
    ICHECMPI_tasmax_mean = (ICHECMPI_tasmax_mean.data - ICHECMPI_b_tasmax_mean.data + Obs_tasmax)
    ICHECSMHI_tasmax_mean = (ICHECSMHI_tasmax_mean.data - ICHECSMHI_b_tasmax_mean.data + Obs_tasmax)
    IPSL_tasmax_mean = (IPSL_tasmax_mean.data - IPSL_b_tasmax_mean.data + Obs_tasmax)
    MIROC_tasmax_mean = (MIROC_tasmax_mean.data - MIROC_b_tasmax_mean.data + Obs_tasmax)
    MOHCCCLM_tasmax_mean = (MOHCCCLM_tasmax_mean.data - MOHCCCLM_b_tasmax_mean.data + Obs_tasmax)
    MOHCKNMI_tasmax_mean = (MOHCKNMI_tasmax_mean.data - MOHCKNMI_b_tasmax_mean.data + Obs_tasmax)
    MOHCSMHI_tasmax_mean = (MOHCSMHI_tasmax_mean.data - MOHCSMHI_b_tasmax_mean.data + Obs_tasmax)
    MPICCLM_tasmax_mean = (MPICCLM_tasmax_mean.data - MPICCLM_b_tasmax_mean.data + Obs_tasmax)
    MPIREMO_tasmax_mean = (MPIREMO_tasmax_mean.data - MPIREMO_b_tasmax_mean.data + Obs_tasmax) 
    MPISMHI_tasmax_mean = (MPISMHI_tasmax_mean.data - MPISMHI_b_tasmax_mean.data + Obs_tasmax)
    NCCSMHI_tasmax_mean = (NCCSMHI_tasmax_mean.data - NCCSMHI_b_tasmax_mean.data + Obs_tasmax) 
    NOAA_tasmax_mean = (NOAA_tasmax_mean.data - NOAA_b_tasmax_mean.data + Obs_tasmax)
    
    CCCmaCanRCM_pr_mean = (CCCmaCanRCM_pr_mean.data - CCCmaCanRCM_b_pr_mean.data + Obs_pr.data)
    CCCmaSMHI_pr_mean = (CCCmaSMHI_pr_mean.data - CCCmaSMHI_b_pr_mean.data + Obs_pr.data)
    CNRM_pr_mean = (CNRM_pr_mean.data - CNRM_b_pr_mean.data + Obs_pr.data)
    CNRMSMHI_pr_mean = (CNRMSMHI_pr_mean.data - CNRMSMHI_b_pr_mean.data + Obs_pr.data)  
    CSIRO_pr_mean = (CSIRO_pr_mean.data - CSIRO_b_pr_mean.data + Obs_pr.data)
    ICHECDMI_pr_mean = (ICHECDMI_pr_mean.data - ICHECDMI_b_pr_mean.data + Obs_pr.data) 
    ICHECCCLM_pr_mean = (ICHECCCLM_pr_mean.data - ICHECCCLM_b_pr_mean.data + Obs_pr.data)
    ICHECKNMI_pr_mean = (ICHECKNMI_pr_mean.data - ICHECKNMI_b_pr_mean.data + Obs_pr.data)
    ICHECMPI_pr_mean = (ICHECMPI_pr_mean.data - ICHECMPI_b_pr_mean.data + Obs_pr.data)
    ICHECSMHI_pr_mean = (ICHECSMHI_pr_mean.data - ICHECSMHI_b_pr_mean.data + Obs_pr.data)
    IPSL_pr_mean = (IPSL_pr_mean.data - IPSL_b_pr_mean.data + Obs_pr.data)
    MIROC_pr_mean = (MIROC_pr_mean.data - MIROC_b_pr_mean.data + Obs_pr.data)
    MOHCCCLM_pr_mean = (MOHCCCLM_pr_mean.data - MOHCCCLM_b_pr_mean.data + Obs_pr.data)
    MOHCKNMI_pr_mean = (MOHCKNMI_pr_mean.data - MOHCKNMI_b_pr_mean.data + Obs_pr.data)
    MOHCSMHI_pr_mean = (MOHCSMHI_pr_mean.data - MOHCSMHI_b_pr_mean.data + Obs_pr.data)
    MPICCLM_pr_mean = (MPICCLM_pr_mean.data - MPICCLM_b_pr_mean.data + Obs_pr.data)      
    MPIREMO_pr_mean = (MPIREMO_pr_mean.data - MPIREMO_b_pr_mean.data + Obs_pr.data)       
    MPISMHI_pr_mean = (MPISMHI_pr_mean.data - MPISMHI_b_pr_mean.data + Obs_pr.data)
    NCCSMHI_pr_mean = (NCCSMHI_pr_mean.data - NCCSMHI_b_pr_mean.data + Obs_pr.data) 
    NOAA_pr_mean = (NOAA_pr_mean.data - NOAA_b_pr_mean.data + Obs_pr.data)
    
    
    
    #-------------------------------------------------------------------------
    #PART 5: PRINT DATA
    import csv
    with open('output_Historical_dailymonhtly_Tasmin_Tasmax_Pr.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow(['Parameter', 'Means'])
        
        writer.writerow(["CCCmaCanRCM_tas_mean"] + CCCmaCanRCM_tas_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_tas_mean"] + CCCmaSMHI_tas_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_tas_mean"] + CNRM_tas_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_tas_mean"] +CNRMSMHI_tas_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_tas_mean"] +CSIRO_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_tas_mean"] +ICHECDMI_tas_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_tas_mean"] +ICHECCCLM_tas_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_tas_mean"] +ICHECKNMI_tas_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_tas_mean"] +ICHECMPI_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_tas_mean"] +ICHECSMHI_tas_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_tas_mean"] +IPSL_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_tas_mean"] +MIROC_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_tas_mean"] +MOHCCCLM_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_tas_mean"] +MOHCKNMI_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_tas_mean"] +MOHCSMHI_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_tas_mean"] +MPICCLM_tas_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_tas_mean"] +MPIREMO_tas_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_tas_mean"] +MPISMHI_tas_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_tas_mean"] +NCCSMHI_tas_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_tas_mean"] +NOAA_tas_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCM_tasmin_mean"] + CCCmaCanRCM_tasmin_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_tasmin_mean"] + CCCmaSMHI_tasmin_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_tasmin_mean"] + CNRM_tasmin_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_tasmin_mean"] +CNRMSMHI_tasmin_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_tasmin_mean"] +CSIRO_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_tasmin_mean"] +ICHECDMI_tasmin_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_tasmin_mean"] +ICHECCCLM_tasmin_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_tasmin_mean"] +ICHECKNMI_tasmin_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_tasmin_mean"] +ICHECMPI_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_tasmin_mean"] +ICHECSMHI_tasmin_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_tasmin_mean"] +IPSL_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_tasmin_mean"] +MIROC_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_tasmin_mean"] +MOHCCCLM_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_tasmin_mean"] +MOHCKNMI_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_tasmin_mean"] +MOHCSMHI_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_tasmin_mean"] +MPICCLM_tasmin_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_tasmin_mean"] +MPIREMO_tasmin_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_tasmin_mean"] +MPISMHI_tasmin_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_tasmin_mean"] +NCCSMHI_tasmin_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_tasmin_mean"] +NOAA_tasmin_mean.data.flatten().astype(np.str).tolist()) 
        
        writer.writerow(["CCCmaCanRCM_tasmax_mean"] + CCCmaCanRCM_tasmax_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_tasmax_mean"] + CCCmaSMHI_tasmax_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_tasmax_mean"] + CNRM_tasmax_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_tasmax_mean"] +CNRMSMHI_tasmax_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_tasmax_mean"] +CSIRO_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_tasmax_mean"] +ICHECDMI_tasmax_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_tasmax_mean"] +ICHECCCLM_tasmax_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_tasmax_mean"] +ICHECKNMI_tasmax_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_tasmax_mean"] +ICHECMPI_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_tasmax_mean"] +ICHECSMHI_tasmax_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_tasmax_mean"] +IPSL_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_tasmax_mean"] +MIROC_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_tasmax_mean"] +MOHCCCLM_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_tasmax_mean"] +MOHCKNMI_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_tasmax_mean"] +MOHCSMHI_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_tasmax_mean"] +MPICCLM_tasmax_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_tasmax_mean"] +MPIREMO_tasmax_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_tasmax_mean"] +MPISMHI_tasmax_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_tasmax_mean"] +NCCSMHI_tasmax_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_tasmax_mean"] +NOAA_tasmax_mean.data.flatten().astype(np.str).tolist())
        
        writer.writerow(["CCCmaCanRCM_pr_mean"] + CCCmaCanRCM_pr_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CCCmaSMHI_pr_mean"] + CCCmaSMHI_pr_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRM_pr_mean"] + CNRM_pr_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["CNRMSMHI_pr_mean"] +CNRMSMHI_pr_mean.data.flatten().astype(np.str).tolist())   
        writer.writerow(["CSIRO_pr_mean"] +CSIRO_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECDMI_pr_mean"] +ICHECDMI_pr_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["ICHECCCLM_pr_mean"] +ICHECCCLM_pr_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECKNMI_pr_mean"] +ICHECKNMI_pr_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["ICHECMPI_pr_mean"] +ICHECMPI_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["ICHECSMHI_pr_mean"] +ICHECSMHI_pr_mean.data.flatten().astype(np.str).tolist())
        writer.writerow(["IPSL_pr_mean"] +IPSL_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MIROC_pr_mean"] +MIROC_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCCCLM_pr_mean"] +MOHCCCLM_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCKNMI_pr_mean"] +MOHCKNMI_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MOHCSMHI_pr_mean"] +MOHCSMHI_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["MPICCLM_pr_mean"] +MPICCLM_pr_mean.data.flatten().astype(np.str).tolist())    
        writer.writerow(["MPIREMO_pr_mean"] +MPIREMO_pr_mean.data.flatten().astype(np.str).tolist()) 
        writer.writerow(["MPISMHI_pr_mean"] +MPISMHI_pr_mean.data.flatten().astype(np.str).tolist())      
        writer.writerow(["NCCSMHI_pr_mean"] +NCCSMHI_pr_mean.data.flatten().astype(np.str).tolist())       
        writer.writerow(["NOAA_pr_mean"] +NOAA_pr_mean.data.flatten().astype(np.str).tolist())
        
if __name__ == '__main__':
    main()     
    
    