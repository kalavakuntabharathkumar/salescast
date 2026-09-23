# Retail Sales Forecasting Pipeline with Automated Monitoring

End-to-end forecasting pipeline for the Walmart Recruiting Store Sales Forecasting dataset.

## Pipeline
CSV -> Pandas cleaning -> feature engineering -> Gradient Boosting -> validation -> artifact -> monitoring.

The project includes Terraform templates for Azure Blob Storage, Docker packaging, scheduled GitHub Actions retraining, and Prometheus/Grafana monitoring.

### Expected dataset
Place the Kaggle training CSV at `data/train.csv` with columns such as `Store`, `Dept`, `Date`, `Weekly_Sales`, `IsHoliday`, `Type`, `Size`, `Temperature`, `Fuel_Price`, `MarkDown1`-`5`, `CPI`, and `Unemployment`.

### Run
```bash
pip install -r requirements.txt
python src/pipeline.py --input data/train.csv
```
