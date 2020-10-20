let btn_pay = document.querySelector('.btn_action')

actionExpense = (el) => {
    action = el.getAttribute('name')
    id = parseInt(el.value),
    debt_line = parseInt(el.parentNode.parentNode.getAttribute('id'))

    console.log(id)

    if (el.getAttribute('name') == 'updateValue') {
        document.querySelector('#pay_expense').addEventListener(
            'click',
            () => pay_expense(id, debt_line)
        )
        document.querySelector('#pay_parcel_expense').addEventListener(
            'click',
            () => pay_parcel_expense(id, debt_line)
        )
    }
    el.getAttribute('name') == 'updateType' ? change_type(id, debt_line) : null 
}

pay_expense = (id_expense, debt_line) => {
    var xhttp = new XMLHttpRequest()

    xhttp.open("POST", "pending/expense/pay/", true)

    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
    xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))

    xhttp.responseType = 'json'
    xhttp.onreadystatechange = function(data) {
        if (this.readyState == 4 && this.status == 200) {
            let json = xhttp.response
            if (json) {
                update_interface_expende(json)
            }
        }
    }

    let expense = {
        'id': id_expense,
        'amount_paid': document.querySelector('#amount_paid').value,
        'note': document.querySelector('#note').value,
        'debt_line': debt_line,
    }

    xhttp.send("expense=" + JSON.stringify(expense))
}

pay_parcel_expense = (id, debt_line) => {
    var xhttp = new XMLHttpRequest()

    xhttp.open("POST", "/pending/pending/expense/pay_parcel/", true)

    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
    xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))

    xhttp.responseType = 'json'
    xhttp.onreadystatechange = function(data) {
        if (this.readyState == 4 && this.status == 200) {
            let json = xhttp.response
            if (json) {
                document.querySelector('#title_toast').textContent = json.title
                document.querySelector('#content_toast').textContent = json.amount_paid
            }
        }
    }

    let parcel = {
        'id': id,
        'amount_paid': document.querySelector('#amount_paid_parcel').value,
        'note': document.querySelector('#note_parcel').value,
        'debt_line': debt_line,
    }

    xhttp.send("parcel=" + JSON.stringify(parcel))
}

change_type = (id_expense, debt_line) => {
    var xhttp = new XMLHttpRequest()

    xhttp.open("POST", "pending/expense/change_type/", true)

    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
    xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))

    xhttp.responseType = 'json'
    xhttp.onreadystatechange = function(data) {
        if (this.readyState == 4 && this.status == 200) {
            let json = xhttp.response
            if (json) {
                update_interface_expende(json)
            }
        }
    }

    let expense = {
        'id': id_expense,
        'debt_line': debt_line,
    }

    xhttp.send("expense=" + JSON.stringify(expense))
}