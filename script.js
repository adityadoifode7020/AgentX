const API = "http://127.0.0.1:8000";


async function loadDashboard() {

    const fleet =
        await fetch(`${API}/fleet`)
        .then(res => res.json());


    const battery =
        await fetch(`${API}/battery`)
        .then(res => res.json());


    const cost =
        await fetch(`${API}/cost`)
        .then(res => res.json());


    const optimization =
        await fetch(`${API}/optimize`)
        .then(res => res.json());


    document.getElementById("total")
        .innerText =
        fleet.total_vehicles;


    document.getElementById("available")
        .innerText =
        fleet.available_vehicles;


    document.getElementById("lowBattery")
        .innerText =
        fleet.low_battery_vehicles;


    document.getElementById("price")
        .innerText =
        "₹" + cost.cheapest_price;


    loadFleetTable(battery);

    loadRecommendations(
        optimization.recommendations
    );
}


function loadFleetTable(data) {

    const table =
        document.getElementById(
            "fleetTable"
        );

    table.innerHTML = "";


    data.forEach(vehicle => {

        const row =
            document.createElement("tr");


        row.innerHTML = `

            <td>${vehicle.vehicle}</td>

            <td>${vehicle.soc}%</td>

            <td>${vehicle.soh}%</td>

            <td>${vehicle.status}</td>

        `;


        table.appendChild(row);

    });

}


function loadRecommendations(data) {

    const container =
        document.getElementById(
            "recommendations"
        );


    container.innerHTML = "";


    data.forEach(item => {

        const div =
            document.createElement("div");


        div.className =
            "recommendation";


        div.innerHTML = `

            <strong>
                ${item.vehicle}
            </strong>

            <br>

            ${item.message}

            <br>

            <small>
                Priority:
                ${item.priority}
            </small>

        `;


        container.appendChild(div);

    });

}


async function getAIAnalysis() {

    const result =
        document.getElementById(
            "aiResult"
        );


    result.innerHTML =
        "🤖 Analyzing fleet data...";


    const response =
        await fetch(
            `${API}/ai-analysis`
        );


    const data =
        await response.json();


    result.innerText =
        data.analysis;

}


loadDashboard();