def status_line(name, error_rate):
    if error_rate >= 0.05:
        return f"ALERT: {name} needs attention"
    return f"OK: {name}"

print(status_line("checkout-api", 0.08))
