### Custom definitions and classes if any ###
import numpy as np
import pandas as pd
import joblib
import csv

def predictRuns(testInput):
    #prediction = 0
    with open('reg_model.joblib','rb') as f:
        reg_model=joblib.load(f)
    with open('venue_encoder.joblib','rb') as f:
        venue_encoder=joblib.load(f)
    with open('team_encoder.joblib','rb') as f:
        team_encoder=joblib.load(f)

    testc=pd.read_csv(testInput)
    
    testc['venue']=venue_encoder.transform(testc['venue'])
    testc['batting_team']=team_encoder.transform(testc['batting_team'])
    testc['bowling_team']=team_encoder.transform(testc['bowling_team'])
    
    testc['batsmen']=testc.batsmen.map(lambda x: [i.strip() for i in x.split(',')])
    testc['wkt']=testc.batsmen.apply(len)-2
   
    testc=testc[['venue','innings','batting_team','bowling_team','wkt']]
    
    return round(reg_model.predict(testc)[0])