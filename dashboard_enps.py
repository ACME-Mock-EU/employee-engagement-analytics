# Employee Engagement eNPS Dashboard
# Real-time visualization of eNPS scores and trends

import pandas as pd
from datetime import datetime

class eNPSDashboard:
    def __init__(self):
        self.target_enps = 40
        self.alert_threshold = -10
    
    def load_survey_data(self, filepath):
        '''Load weekly survey data from CSV/Excel'''
        df = pd.read_csv(filepath)
        return df
    
    def calculate_enps_by_team(self, data):
        '''Calculate eNPS score for each team'''
        team_enps = data.groupby('Team')['eNPS'].agg(['mean', 'std', 'min', 'max'])
        return team_enps.round(2)
    
    def calculate_enps_by_department(self, data):
        '''Calculate eNPS by department with trend analysis'''
        dept_enps = data.groupby(['Department', 'Survey Week Start'])['eNPS'].mean()
        return dept_enps
    
    def identify_alerts(self, data):
        '''Identify teams with eNPS below alert threshold'''
        alerts = data[data['eNPS'] < self.alert_threshold][['Team', 'eNPS', 'Driver Theme']]
        return alerts.sort_values('eNPS')
    
    def generate_report(self, data):
        '''Generate executive summary report'''
        report = {
            'total_surveys': len(data),
            'avg_enps': data['eNPS'].mean(),
            'response_rate': data['Response Rate'].mean(),
            'engagement_gap': self.target_enps - data['eNPS'].mean(),
            'departments': data['Department'].nunique(),
            'locations': data['Location'].nunique()
        }
        return report

if __name__ == "__main__":
    dashboard = eNPSDashboard()
    print("eNPS Dashboard v1.0 initialized")
    print("Monitoring: Real-time employee engagement metrics")
