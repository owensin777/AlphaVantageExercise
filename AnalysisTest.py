import Analysis 


analysis_obj = Analysis.Analysis.Analysis(analysis_config="./config")
analysis_obj.load_data()
analysis_output = analysis_obj.compute_analysis()
analysis_obj.notify_done(analysis_output)
print(analysis_output)