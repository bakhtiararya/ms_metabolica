# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import copy

# main sheet in the original file is called "7T_NAC_GSH_MRSI_AtlasROI_metabo"

main_data = pd.read_excel("C:\\Users\\Arya\\Desktop\\dummy.xlsx", "Sheet1")

"""
for row in main_data.iterrows():
    x = 1 
    #print(row)
 """   
    
before_date_dict = { }   
    
# iterate through the Excel file and add subject ID with date to the dictionary
for row in main_data.iterrows():
    name = row[1].bnum
    date = row[1].tnum
    if ((name, date) not in before_date_dict):
        d = { (name, date) : 0 }
        before_date_dict.update(d);

date_dict = {('subj01', '2016_11_04'): 0,
 ('subj01', '2016_12_02'): 4,
 ('subj02', '2016_12_01'): 0,
 ('subj02', '2016_12_20'): 4,
 ('subj04', '09_18_17'): 0,
 ('subj04', '10_10_17'): 4}

        
# dictionary containing the values for each individual ROI
ROI_dict_template = { "SNR" : [],
                      "FWHM" : [],
                      "GPC.PCh_readRCr" : [],
                      "NAA.NAAG_readRCr" : [],
                      "Glu_readRCr" : [],
                      "Gln_readRCr" : [],
                      "Glu.Gln_readRCr" : [],
                      "mI_readRCr" : [],
                      "Gly_readRCr" : [],
                      "mI.Gly_readRCr" : [],
                      "GSH_readRCr" : [],
                      "GABA_readRCr" : [],
                      "tNAA_readRCr_corr" : [],
                      "tNAA_readRCr_corr_cut" : []
                    }   


def get_timepoint(subj_ID, date):
    return date_dict[(subj_ID, date)]

main_subject_dict = { } 

for row in main_data.iterrows():
    subj_ID = row[1].bnum
    date = row[1].tnum
    timepoint = get_timepoint(subj_ID, date) # convert date to 0 or 4
    
    if (subj_ID, timepoint) not in main_subject_dict:
        main_subject_dict[(subj_ID, timepoint)] = {}
    
    roi_value = row[1].ROIvalue
    
    if roi_value not in main_subject_dict[(subj_ID, timepoint)]:
         main_subject_dict[(subj_ID, timepoint)][roi_value] = copy.deepcopy(ROI_dict_template)
         
    main_subject_dict[(subj_ID, timepoint)][roi_value]["SNR"] = row[1]["SNR"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["FWHM"] = row[1]["FWHM"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["GPC.PCh_readRCr"] = row[1]["GPC.PCh_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["NAA.NAAG_readRCr"] = row[1]["NAA.NAAG_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["Glu_readRCr"] = row[1]["Glu_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["Gln_readRCr"] = row[1]["Gln_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["Glu.Gln_readRCr"] = row[1]["Glu.Gln_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["mI_readRCr"] = row[1]["mI_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["Gly_readRCr"] = row[1]["Gly_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["mI.Gly_readRCr"] = row[1]["mI.Gly_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["GSH_readRCr"] = row[1]["GSH_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["GABA_readRCr"] = row[1]["GABA_readRCr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["tNAA_readRCr_corr"] = row[1]["tNAA_readRCr_corr"]
    main_subject_dict[(subj_ID, timepoint)][roi_value]["tNAA_readRCr_corr_cut"] = row[1]["tNAA_readRCr_corr_cut"]
     
         
         
    
        








