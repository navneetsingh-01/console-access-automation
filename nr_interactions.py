import os
from newrelic_telemetry_sdk import GaugeMetric, CountMetric, SummaryMetric, MetricClient

nr_license_key = os.getenv("PROD_NR_LICENSE_KEY")


def update_terminal_server_access():
    metric_client = MetricClient(nr_license_key)
    batch = []
    key = "terminal_server_access_test"
    metric = GaugeMetric(key, 20)
    batch.append(metric)
    response = metric_client.send_batch(batch)
    response.raise_for_status()
