# Survey Data Pipeline
# Automated ingestion, processing, and freshness monitoring for engagement surveys

import pandas as pd
from datetime import datetime, timedelta

class SurveyDataPipeline:
    def __init__(self):
        self.max_freshness_days = 3
        self.data_quality_threshold = 0.95
        self.batch_size = 100
    
    def ingest_survey_data(self, source_path):
        '''Ingest raw survey data from source'''
        df = pd.read_excel(source_path)
        df['ingestion_time'] = datetime.now()
        return df
    
    def validate_data_quality(self, data):
        '''Validate data quality and completeness'''
        completeness = 1 - (data.isnull().sum().sum() / (data.shape[0] * data.shape[1]))
        quality_pass = completeness >= self.data_quality_threshold
        return {
            'completeness': completeness,
            'quality_pass': quality_pass,
            'issues': data.columns[data.isnull().sum() > 0].tolist()
        }
    
    def check_data_freshness(self, data):
        '''Check age of survey data and alert if stale'''
        latest_survey = pd.to_datetime(data['Survey Week Start']).max()
        freshness_days = (datetime.now() - latest_survey).days
        is_fresh = freshness_days <= self.max_freshness_days
        
        return {
            'latest_survey': latest_survey,
            'freshness_days': freshness_days,
            'is_fresh': is_fresh,
            'status': 'OK' if is_fresh else 'ALERT'
        }
    
    def aggregate_metrics(self, data):
        '''Aggregate survey data into key metrics'''
        metrics = {
            'total_responses': len(data),
            'avg_enps': data['eNPS'].mean(),
            'avg_response_rate': data['Response Rate'].mean(),
            'unique_teams': data['Team'].nunique(),
            'unique_departments': data['Department'].nunique()
        }
        return metrics
    
    def process_batch(self, data):
        '''Process data in batches for efficiency'''
        batches = [data[i:i+self.batch_size] for i in range(0, len(data), self.batch_size)]
        processed = []
        for batch in batches:
            processed.append(self.validate_data_quality(batch))
        return processed
    
    def export_processed_data(self, data, output_path):
        '''Export processed data to analytics database'''
        data.to_csv(output_path, index=False)
        return output_path

if __name__ == "__main__":
    pipeline = SurveyDataPipeline()
    print("Survey Data Pipeline v1.0 initialized")
    print("Freshness target: <3 days | Quality threshold: 95%")
