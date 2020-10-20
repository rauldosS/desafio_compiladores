// -> assíncrono -------------------------------------------
(async () => {
    const resp = await fetch('/expense/list_expense/')
    const jsonData = await resp.json()
    console.log(`JsonData: ${JSON.stringify(jsonData)}`)
}) ()

fetch('/expense/list_expense/')
    .then( function(response ) {
        return response.json()
    })
    .then( function(myJson) {
        console.log(JSON.stringify(myJson))
    })


// -> Exemplo completo assíncrono --------------------------------

const list_expenses = async () => {
    const resp = await fetch('/expense/list_expense/')
    const jsonData = await resp.json()
    
    const table = document.querySelector('#expenses')

    table.innerHTML = ''

    for (let [parcel, datas] of Object.entries(jsonData)) {
        table.innerHTML += "<tr>\
                                <td><i class='fas fa-" + datas.type_expense + " text-success'></i></td>\
                                <td>" + datas.date_expense + "</td>\
                                <td>" + datas.creditor + "</td>\
                                <td>" + datas.category + "</td>\
                                <td>" + datas.description + "</td>\
                                <td>" + datas.original_value + "</td>\
                                <td>" + datas.amount_paid + "</td>\
                            </tr>"
    }
    
    table.innerHTML += "<tr><td>Total</td> <td></td> <td></td> <td></td> <td></td> <td id='original'></td> <td id='paid'></td></tr>"
}

// -> Exemplo completo xhttp request --------------------------------

function teste() {
    // e.preventDefault()
    var xhttp = new XMLHttpRequest()

    xhttp.open("GET", "/expense/list_expense/", true)

    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
    xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))

    xhttp.responseType = 'json'
    xhttp.onreadystatechange = function(data) {
        if (this.readyState == 4 && this.status == 200) {
            let json = xhttp.response
            if (json) {
                const table = document.querySelector('#expenses')

                table.innerHTML = ''

                for (let [parcel, datas] of Object.entries(json)) {
                    table.innerHTML += "<tr>\
                                            <td><i class='fas fa-" + datas.type_expense + " text-success'></i></td>\
                                            <td>" + datas.date_expense + "</td>\
                                            <td>" + datas.creditor + "</td>\
                                            <td>" + datas.category + "</td>\
                                            <td>" + datas.description + "</td>\
                                            <td>" + datas.original_value + "</td>\
                                            <td>" + datas.amount_paid + "</td>\
                                        </tr>"
                }
                
                table.innerHTML += "<tr><td>Total</td> <td></td> <td></td> <td></td> <td></td> <td id='original'></td> <td id='paid'></td></tr>"
            }
        }
    }

    xhttp.send()
}

function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = function() {
    updateTables()
}