def generate_recommendations(
    vehicles,
    optimization_results
):

    recommendations = []

    for result in optimization_results:

        vehicle_id = result["vehicle"]

        vehicle = next(
            (
                v for v in vehicles
                if v["id"] == vehicle_id
            ),
            None
        )

        if not vehicle:
            continue

        if result["priority"] == "Critical":

            message = (
                f"{vehicle_id} has only "
                f"{vehicle['soc']}% battery. "
                f"Charge immediately to "
                f"{result['target_soc']}%."
            )

        elif result["priority"] == "High":

            message = (
                f"{vehicle_id} should be charged "
                f"during the low-cost period "
                f"{result['charging_period']}."
            )

        elif result["priority"] == "Medium":

            message = (
                f"{vehicle_id} has reduced battery "
                f"health ({vehicle['soh']}%). "
                f"Use controlled charging and "
                f"avoid unnecessary high SOC."
            )

        else:

            message = (
                f"{vehicle_id} does not require "
                f"immediate charging."
            )

        recommendations.append({
            "vehicle": vehicle_id,
            "message": message,
            "priority": result["priority"]
        })

    return recommendations