services = [{"name": "checkout-api", "error_rate": 0.08}, {"name": "catalog-api", "error_rate": 0.01}]
for service in services:
    if service["error_rate"] >= 0.05:
        print(f"ALERT: {service['name']}")
    else:
        print(f"OK: {service['name']}")
