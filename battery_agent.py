def battery_analysis(vehicles):

    results = []

    for vehicle in vehicles:

        soc = vehicle["soc"]
        soh = vehicle["soh"]

        if soc < 30:
            status = "Critical"

        elif soc < 50:
            status = "Low"

        elif soc < 80:
            status = "Medium"

        else:
            status = "Good"

        if soh < 90:
            health_warning = True
        else:
            health_warning = False

        results.append({
            "vehicle": vehicle["id"],
            "soc": soc,
            "soh": soh,
            "status": status,
            "health_warning": health_warning
        })

    return results