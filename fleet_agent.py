def fleet_analysis(vehicles):

    total = len(vehicles)

    available = sum(
        1 for v in vehicles
        if v["available"]
    )

    charging = sum(
        1 for v in vehicles
        if v["soc"] < 40
    )

    unavailable = total - available

    return {
        "total_vehicles": total,
        "available_vehicles": available,
        "low_battery_vehicles": charging,
        "unavailable_vehicles": unavailable
    }