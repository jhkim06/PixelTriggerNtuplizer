from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SingleElectron200PU_PhaseIIFall17D'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'rerun_EBTP_HGCalTP_L1_L1TTracklet_onMC_L1_FEVTHLTDEBUG.py'

config.Data.inputDataset = '/SingleE_FlatPt-2to100/PhaseIIFall17D-L1TPU200_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'
#config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 1
#config.Data.outputPrimaryDataset = 'SingleElectron_PU200'
config.Data.splitting = 'FileBased'
config.Data.outLFNDirBase = '/store/user/jhkim/'
config.Data.publication = False
config.Data.outputDatasetTag = 'SingleElectron_200PU_PhaseIIFall17D'

config.Site.storageSite = 'T2_KR_KNU'
