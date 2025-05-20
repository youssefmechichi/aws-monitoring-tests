import requests
import pytest
import socket

# Tester si les services HTTP répondent (Grafana, Prometheus, API Web, etc.)
@pytest.mark.parametrize("url", [
    "http://13.53.171.116:9090",     # Prometheus
    "http://13.53.171.116:3000",     # Grafana
])
def test_http_services(url):
    response = requests.get(url, timeout=5)
    assert response.status_code == 200, f"{url} ne répond pas (status {response.status_code})"

# Vérifier port ouvert (e.g. MySQL sur RDS ou autre service)
def test_rds_port():
    host = "test-db.clckk0q8w2jn.eu-north-1.rds.amazonaws.com"
    port = 3306
    try:
        socket.create_connection((host, port), timeout=5)
    except Exception as e:
        pytest.fail(f"Connexion à {host}:{port} impossible: {e}")import requests
import pytest
import socket

# Tester si les services HTTP répondent (Grafana, Prometheus, API Web, etc.)
@pytest.mark.parametrize("url", [
    "http://13.53.171.116:9090",     # Prometheus
    "http://13.53.171.116:3000",     # Grafana
])

