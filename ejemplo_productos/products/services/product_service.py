import requests

API_URL = "https://f1api.dev/api/drivers"

def get_drivers(page=1, limit=10):
    """Obtiene los conductores con paginación."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        drivers = data["drivers"]
        start = (page - 1) * limit
        end = start + limit
        return drivers[start:end], len(drivers)
    return [], 0

def get_driver_by_id(driver_id):
    """Obtiene la información de un conductor específico."""
    response = requests.get(f"{API_URL}/{driver_id}")
    if response.status_code == 200:
        return response.json()
    return None
