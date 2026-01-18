# InfluxDB Write Configuration

This project uses InfluxDB as the time-series database to store processed earthquake data.

## InfluxDB Setup
- InfluxDB version: 2.x
- Organization: Big_Data_Project
- Bucket: Bucket_Earthquake
- Measurement: earthquakes

## Data Model
Each earthquake record is written with:
- Timestamp: earthquake event time
- Measurement: earthquakes
- Fields:
  - magnitude (float)
  - depth (float)
  - latitude (float)
  - longitude (float)
- Tags:
  - source (usgs / manual)
  - place
  - event_type

## Write Path
Data is written to InfluxDB using:
- Python InfluxDB client
- Batch writes for efficiency
- Idempotent writes based on event ID

## Purpose
InfluxDB enables:
- Efficient time-based queries
- Aggregations over time windows
- Direct integration with Grafana dashboards
