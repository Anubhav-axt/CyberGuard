import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.constants import PORT_COMMON


def scan_port(target, port, timeout=1):
    """Scan a single port. Returns dict with port info."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            service = PORT_COMMON.get(port, "Unknown")
            return {"port": port, "status": "open", "service": service}
    except (socket.error, OSError):
        pass
    return {"port": port, "status": "closed", "service": PORT_COMMON.get(port, "Unknown")}


def scan_ports(target, start_port=1, end_port=1024, timeout=1, max_threads=100):
    """Scan a range of ports on target."""
    open_ports = []
    all_results = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {
            executor.submit(scan_port, target, port, timeout): port
            for port in range(start_port, end_port + 1)
        }
        for future in as_completed(futures):
            result = future.result()
            all_results.append(result)
            if result["status"] == "open":
                open_ports.append(result)

    open_ports.sort(key=lambda x: x["port"])
    all_results.sort(key=lambda x: x["port"])

    return {
        "target": target,
        "open_ports": open_ports,
        "total_scanned": end_port - start_port + 1,
        "total_open": len(open_ports),
    }
