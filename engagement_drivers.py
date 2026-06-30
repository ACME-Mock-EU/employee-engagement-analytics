# Engagement Driver Analysis
# Analyze key factors impacting employee engagement and eNPS

import pandas as pd
import numpy as np

class EngagementDriverAnalysis:
    def __init__(self):
        self.drivers = [
            'workload',
            'tooling',
            'manager support',
            'recognition',
            'career path'
        ]
        self.driver_weight = {'critical': 1.0, 'high': 0.8, 'medium': 0.5}
    
    def analyze_driver_impact(self, data):
        '''Analyze correlation between drivers and eNPS scores'''
        driver_impact = {}
        for driver in data['Driver Theme'].unique():
            driver_data = data[data['Driver Theme'] == driver]
            impact = {
                'avg_score': driver_data['Driver Score'].mean(),
                'avg_enps': driver_data['eNPS'].mean(),
                'correlation': driver_data[['Driver Score', 'eNPS']].corr().iloc[0, 1]
            }
            driver_impact[driver] = impact
        return driver_impact
    
    def identify_critical_drivers(self, data, threshold=3.5):
        '''Identify drivers with highest impact on engagement'''
        driver_analysis = self.analyze_driver_impact(data)
        critical = {k: v for k, v in driver_analysis.items() if v['avg_score'] >= threshold}
        return critical
    
    def department_driver_analysis(self, data):
        '''Analyze driver themes by department'''
        dept_drivers = data.groupby('Department')['Driver Theme'].value_counts().unstack(fill_value=0)
        return dept_drivers
    
    def recommend_interventions(self, data):
        '''Generate intervention recommendations based on driver analysis'''
        recommendations = {}
        critical_drivers = self.identify_critical_drivers(data)
        
        for driver in critical_drivers:
            if driver == 'workload':
                recommendations['workload'] = "Implement workload redistribution and capacity planning"
            elif driver == 'manager support':
                recommendations['manager_support'] = "Enhance manager training and 1-on-1 cadence"
            elif driver == 'career path':
                recommendations['career_path'] = "Develop clear career progression framework"
            elif driver == 'recognition':
                recommendations['recognition'] = "Formalize peer and manager recognition program"
            elif driver == 'tooling':
                recommendations['tooling'] = "Assess and upgrade tool stack and infrastructure"
        
        return recommendations

if __name__ == "__main__":
    analysis = EngagementDriverAnalysis()
    print("Engagement Driver Analysis v1.0 initialized")
    print("Key drivers: workload, tooling, manager support, recognition, career path")
