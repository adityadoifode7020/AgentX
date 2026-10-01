def charging_analysis(stations):

    results = []

    for station in stations:

        utilization = (
            (station["chargers"] -
             station["available_chargers"])
            / station["chargers"]
        ) * 100

        results.append({
            "station": station["id"],
            "location": station["location"],
            "available_chargers":
                station["available_chargers"],
            "power_kw": station["power_kw"],
            "utilization": round(utilization, 2)
        })

    return results