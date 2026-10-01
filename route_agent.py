def route_analysis(routes):

    results = []

    for route in routes:

        results.append({
            "route": route["id"],
            "distance": route["distance"],
            "required_soc": route["required_soc"],
            "priority": route["priority"]
        })

    return results