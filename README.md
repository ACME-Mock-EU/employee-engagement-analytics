# Employee Engagement Analytics Platform

## Overview
Real-time eNPS (Employee Net Promoter Score) tracking, team performance dashboards, and survey data analysis for workforce insights and engagement optimization.

## Problem Statement
Acme Horizon Group's employee engagement survey data (June-July 2026) reveals:
- **eNPS Range:** -34 to 55 (wide variance across teams)
- **Low Response Rates:** 20-91% participation inconsistency
- **Engagement Gaps:** 6% to 75% positive feedback rate variance
- **Data Freshness:** 1-21 days lag in survey data
- **Departmental Differences:** Product Support, Engineering, Operations, Customer Success, Sales, Data Analysis

**Key Drivers Impacting Engagement:**
- Workload management
- Tooling & infrastructure
- Manager support and feedback
- Recognition programs
- Career path clarity

## Solution Architecture
- Real-time eNPS tracking dashboard
- Weekly survey data aggregation pipeline
- Team performance comparison analytics
- Engagement trend analysis and forecasting
- Manager coaching dashboards
- Automated engagement alerts

## Supported Metrics
- **eNPS Score** (Employee Net Promoter Score)
- **Positive Feedback Rate** (engagement sentiment)
- **Response Rate** (survey participation)
- **Driver Themes** (workload, tooling, recognition, career path, manager support)
- **Driver Score** (impact measurement)
- **Data Freshness** (pipeline latency)

## Key Statistics (June-July 2026)
- **Departments Tracked:** 6 (Product Support, Engineering, Operations, Customer Success, Sales, Data Analysis)
- **Teams Analyzed:** 17+ unique teams
- **Locations:** Chicago, EMEA, New York
- **Tenure Bands:** 7 segments (0-6 months to 5+ years)
- **Average eNPS:** 5.7 (room for improvement)
- **Average Response Rate:** 58% (need to increase participation)
- **Average Positive Feedback:** 27.6%

## Technology Stack
- Language: Python/Node.js
- Data Pipeline: Apache Airflow / Prefect
- Analytics: SQL, Pandas, Scikit-learn
- Visualization: Tableau / Looker / Grafana
- Database: PostgreSQL / Snowflake
- Monitoring: Datadog / New Relic

## Getting Started
```bash
git clone https://github.com/ACME-Mock-EU/employee-engagement-analytics.git
cd employee-engagement-analytics
pip install -r requirements.txt
python main.py
```

## API Endpoints
- `GET /metrics/eNPS` - Retrieve current eNPS scores by team
- `GET /metrics/engagement` - Team engagement metrics
- `GET /trends/eNPS` - Historical eNPS trends
- `GET /drivers` - Key engagement drivers
- `POST /survey/ingest` - Ingest survey data

## Data Sources
- Weekly employee engagement surveys (all departments)
- Team performance reviews
- Manager feedback sessions
- HR system integration

## Key Timeline
- **June 1:** Data collection starts
- **June 22:** Initial trends identified
- **July 6:** Driver analysis completed
- **July 20:** v1.0.0 release with dashboards
- **July 27:** Full engagement platform live

## Contributing
See CONTRIBUTING.md for guidelines.

## License
Internal use only - Acme Horizon Group

## Support
Contact: data-analytics@acmemock02.de
