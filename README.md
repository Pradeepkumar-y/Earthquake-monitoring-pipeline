
#Earthquake Monitoring Pipeline
## Overview
This project implements an *end-to-end big data pipeline* for real-time earthquake monitoring.
The system ingests earthquake data from an external API, streams it using Kafka, stores raw data in HDFS, processes it using Apache Spark, persists processed data in a time-series database (InfluxDB), and visualizes trends using Grafana.
We used the official U.S. Geological Survey (USGS) real-time Earthquake API:

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson

This API provides all earthquakes that occurred in the last 1 hour in GeoJSON format.
Data set:https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson

The pipeline demonstrates *data ingestion, storage, processing, fault tolerance, and visualization*, following modern big data architecture principles.

## Architecture Diagram (Logical Flow)

API / Stream 
-Kafka (Producer & Topics)
-HDFS (Raw Storage)
-Spark (Batch / Streaming Processing) 
-InfluxDB (Time-Series Database)
-Grafana (Visualization Dashboard)

## Technology Stack

| Layer | Technology |
|-----|-----------|
| Data Source | USGS Earthquake API |
| Streaming | Apache Kafka |
| Storage (Raw) | HDFS |
| Processing | Apache Spark (PySpark) |
| Time-Series DB | InfluxDB |
| Visualization | Grafana |

## Project Structure
earthquake-monitoring-pipeline/
├── kafka/
│ └── earthquake_producer.py
├── hdfs/
│ └── raw_data_example.csv
├── spark/
│ └── earthquake_raw_to_clean.py
├── influx/
│ └── write_config.md
├── grafana/
│ └── dashboard_screenshots/
└── README.md

## Step-by-Step Pipeline Execution

### Kafka - Data Ingestion

Earthquake data is fetched from the **USGS Earthquake API** and published to Kafka topics.

*Start Kafka*
```bash
/opt/kafka/kafka_2.13-3.6.0/bin/kafka-server-start.sh -daemon \
/opt/kafka/kafka_2.13-3.6.0/config/server.properties
Run Kafka Producer

source ~/kafka_env/bin/activate
python3 kafka/earthquake_producer.py


Kafka acts as a buffer and decoupling layer, enabling scalability and fault tolerance.

##HDFS-Raw Data Storage

Raw earthquake JSON messages are persisted to HDFS for durability and reprocessing.

Example HDFS path:

/raw/earthquake/


Verify raw data:

hdfs dfs -ls /raw/earthquake

##Spark - Data Processing

Apache Spark reads raw JSON files from HDFS, parses nested JSON, and writes clean structured data back to HDFS.

Spark Job

spark-submit spark/earthquake_raw_to_clean.py


Output Path

/clean/earthquake


Verify cleaned data:

hdfs dfs -ls /clean/earthquake


Spark provides:

Distributed processing

Schema enforcement

Batch fault tolerance

##InfluxDB - Time-Series Storage

Clean earthquake data (magnitude, depth, location, timestamp) is written to InfluxDB for time-series analysis.

-Bucket: Bucket_Earthquake

-Measurement: earthquakes

-Fields: magnitude, depth

-Tags: place, source, event_type

InfluxDB enables efficient time-based queries and aggregation.

##Grafana - Visualization

Grafana connects to InfluxDB and visualizes earthquake trends.

Dashboards include:

-Earthquake Magnitude Over Time
-Earthquake Depth Over Time

Grafana provides:

-Interactive dashboards

T-ime range filtering

-Real-time analytics

Screenshots are available under:

grafana/dashboard_screenshots/

##Fault Tolerance & Scalability

-Kafka ensures message durability and replay
-HDFS provides replicated storage
-Spark supports recomputation and scalable execution
-Time-series DB enables efficient aggregation

##Lessons Learned
-Kafka simplifies real-time ingestion
-HDFS allows safe reprocessing of historical data
-Spark schema enforcement avoids data quality issues
-InfluxDB is optimized for temporal queries
-Grafana enables fast operational insights

**## Video Presentation Link**
https://drive.google.com/file/d/12yOeE_5oMQja1bRVseKy8RXZaWFn8TJ8/view?usp=sharing
