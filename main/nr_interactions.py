import os
from newrelic_telemetry_sdk import GaugeMetric, CountMetric, SummaryMetric, MetricClient
from dotenv import load_dotenv
load_dotenv()

nr_license_key = os.getenv("PROD_NR_LICENSE_KEY")


def update_terminal_server_access(data):
    metric_client = MetricClient(nr_license_key)
    batch = []
    key = 'terminal_server_access'
    for item in data:
        metric = GaugeMetric(key, 100, tags=item)
        batch.append(metric)
    response = metric_client.send_batch(batch)
    response.raise_for_status()
