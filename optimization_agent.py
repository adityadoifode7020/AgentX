def optimize_fleet(
    vehicles,
    routes,
    stations,
    prices
):

    recommendations = []

    cheapest_period = min(
        prices,
        key=prices.get
    )

    for vehicle in vehicles:

        if not vehicle["available"]:
            continue

        soc = vehicle["soc"]
        soh = vehicle["soh"]

        # Critical battery
        if soc < 30:

            recommendations.append({
                "vehicle": vehicle["id"],
                "action": "Charge Immediately",
                "priority": "Critical",
                "charging_period": "Now",
                "target_soc": 85
            })

        # Low battery
        elif soc < 50:

            recommendations.append({
                "vehicle": vehicle["id"],
                "action": "Schedule Charging",
                "priority": "High",
                "charging_period": cheapest_period,
                "target_soc": 80
            })

        # Battery health protection
        elif soh < 90:

            recommendations.append({
                "vehicle": vehicle["id"],
                "action": "Controlled Charging",
                "priority": "Medium",
                "charging_period": cheapest_period,
                "target_soc": 80
            })

        else:

            recommendations.append({
                "vehicle": vehicle["id"],
                "action": "No Immediate Charging",
                "priority": "Low",
                "charging_period": "Not Required",
                "target_soc": soc
            })

    return recommendations