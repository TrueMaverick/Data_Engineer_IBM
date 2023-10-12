# Data_Engineer_IBM
This repo holds all projects done during the IBM Data Engineering Professional Certificate Course

## Project1 - Toll Plaza ETL 

Project Description

Role/Scenario: A data engineer at a data analytics consulting company has been assigned to a project that aims to de-congest the national 
highways by analyzing the road traffic data from different toll plazas. 
Each highway is operated by a different toll operator with different IT setup that use different file formats.

### A) To create an ETL pipeline using Apache Airflow
The first part of the job is to collect data available in different formats and, consolidate it into a single file . 

### B) To create a streaming data pipeline using Apache Kafka
As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id 
and timestamp are streamed to Kafka. 
In the second part, the job is to create a data pipe line that collects the streaming data and loads it into a database.

#### Files

- ETL_Airflow.py - To define airflow DAGs
  
- streaming_data_reader.py - To create a streaming data pipeline using kafka
  
- toll_traffic_generator.py - To create a streaming data generator simulating data being sent from toll plazas

## Project1 - Weather Reporting ETL 

Project Description

Role/Scenario: I've been tasked by my team to create an automated Extract, Transform, Load (ETL) process to extract daily weather forecast and observed weather data and load it into a live report to be used for further analysis by the analytics team. As part of a larger prediction modelling project, the team wants to use the report to monitor and measure the historical accuracy of temperature forecasts by source and station.

As a proof-of-concept (POC), I am only required to do this for a single station and one source to begin with. For each day at noon (local time), I will gather both the actual temperature and the temperature forecasted for noon on the following day for Casablanca, Morocco.

At a later stage, the team anticipates extending the report to include lists of locations, different forecasting sources, different update frequencies, and other weather metrics such as wind speed and direction, precipitation, and visibility.
