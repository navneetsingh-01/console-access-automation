import os
from newrelic_telemetry_sdk import GaugeMetric, CountMetric, SummaryMetric, MetricClient
from dotenv import load_dotenv
load_dotenv()

nr_license_key = os.getenv("PROD_NR_LICENSE_KEY")

data = {'server': 'dub-ts', 'line': '0/2/1', 'port': 5002,
        'device': 'dub-dst-a', 'last_tested': '2023-12-20 06:52:34.718842'}


def update_terminal_server_access():
    metric_client = MetricClient(nr_license_key)
    batch = []
    key = 'terminal_server_access_test'
    metric = GaugeMetric(key, 20)
    batch.append(metric)
    response = metric_client.send_batch(batch)
    response.raise_for_status()

update_terminal_server_access()