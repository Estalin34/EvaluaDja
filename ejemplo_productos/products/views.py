from django.shortcuts import render, get_object_or_404
from products.services import get_drivers, get_driver_by_id

def driver_list(request):
    """Lista de conductores con paginación"""
    page = int(request.GET.get("page", 1))
    drivers, total = get_drivers(page)

    # Calcula las páginas totales
    total_pages = total // 10
    if total % 10 != 0:
        total_pages += 1
    
    # Calcula las páginas anterior y siguiente
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page * 10 < total else None
    
    return render(request, "drivers_list.html", {
        "drivers": drivers, 
        "page": page, 
        "total": total, 
        "total_pages": total_pages,
        "prev_page": prev_page,
        "next_page": next_page
    })


def driver_detail(request, driver_id):
    """Detalle de un conductor"""
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, "driver_detail.html", {"driver": driver})
