from prometheus_client import Counter, Gauge, start_http_server
import time

runs = Counter("forecast_pipeline_runs_total", "Forecast pipeline runs")
last_r2 = Gauge("forecast_last_r2", "R2 from latest validation")
drift_alerts = Counter("forecast_drift_alerts_total", "Detected data drift alerts")

def record_run(r2: float, drift: bool = False):
    runs.inc()
    last_r2.set(r2)
    if drift:
        drift_alerts.inc()

if __name__ == "__main__":
    start_http_server(8000)
    print("Metrics available on :8000")
    while True:
        time.sleep(30)
