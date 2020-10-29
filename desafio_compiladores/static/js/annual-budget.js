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

/* ==> Hyperlinks ============================================================== */

updateExpense = (id) => {
    window.open('http://127.0.0.1:8000/admin/expense/expense/' + id + '/change/', '_blank')
}

updateParcelExpense = (id) => {
    window.open('http://127.0.0.1:8000/admin/expense/parcel/' + id + '/change/', '_blank')
}

/* ==> Calculator ============================================================== */
function calc(e) {

    var operacao = e.value;

    var n1 = parseFloat(document.getElementById("n1").value.replace(',', '.'));
    var n2 = parseFloat(document.getElementById("n2").value.replace(',', '.'));

    var calculo = eval(n1 + operacao + n2);

    if (!isNaN(calculo)) {
        document.querySelector('#result').value = calculo;
    }
}

function limpar() {
    //alert("1");
    var f = document.getElementById("frm");
    var n1 = f.n1;
    var n2 = f.n2;
    n1.value = "";
    n2.value = "";
}

/* ==> Association of fields ============================================================== */
let id_assoc = ''

function assoc(el) {
    id_assoc = `#${el.name}`

    document.querySelectorAll('.item-assoc').forEach(el => { el.addEventListener('click', click, true) })
}

function click(e) {
    e = e || window.event;
    var target = e.target || e.srcElement
    var text = target.innerText

    text = text.replace('R$ ', '')
    text = text.replace(',', '.')

    document.querySelector(id_assoc).value = text
}

function formatter(el) {
    let value = el.value
    
    if (!value.includes('R$')) {
        let formatter = new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL',
            minimumFractionDigits: 2,
        });
        let formatted = formatter.format(el.value)
    
        el.value = formatted
    }
}

/* ==> Sum of columns in table ============================================================== */

function column_sum(total_column, children) {
    document.querySelectorAll('table').forEach(table => {
        let sum = 0

        table.querySelectorAll('tr').forEach(column => {
            if (!column.classList.contains('ignore-sum') || !table.classList.contains('ignore-sum')) {
                try {
                    let content = parseFloat(column.children[children].textContent.replace(',', '.'))
                    isNaN(content) ? null : sum += content
                } catch (error) {
                    null
                }
            }
        })
        
        try {
            sum ? document.querySelector('#' + total_column + table.getAttribute('id').replace('t', '')).textContent = 'R$ ' + sum.toFixed(2).replace('.', ',') : null   
        } catch (error) {
            sum ? document.querySelector('#' + total_column).textContent = `R$ ${sum.toFixed(2).replace('.', ',')}` : null
        }
    })
}