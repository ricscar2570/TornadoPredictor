
from prometheus_client import start_http_server, Counter

requests_total = Counter("requests_total", "Numero totale di richieste")
errors_total = Counter("errors_total", "Numero totale di errori")

def increment_requests():
    requests_total.inc()

def increment_errors():
    errors_total.inc()

if __name__ == "__main__":
    start_http_server(8000)
    print("Monitoraggio Prometheus avviato sulla porta 8000.")
