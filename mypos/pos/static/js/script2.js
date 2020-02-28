var product_ids = [];
var total = 0;

function addItem3(id,name,size) {

  var tableBody = document.getElementById('summary-table-body');
  var tr = document.createElement('tr');

  var td_id = document.createElement('td');
  td_id.innerHTML = id;

  var td_name = document.createElement('td');
  td_name.innerHTML = name;

  var td_size = document.createElement('td');
  td_size.innerHTML = size;



  total =total+ 1;

  tr.appendChild(td_id);
  tr.appendChild(td_name);
  tr.appendChild(td_size);
 
  
 
  clearTotal();

  tableBody.appendChild(tr);
  tableBody.appendChild(getTotal());

  product_ids.push(id)
}

function clearAllItems() {
  var table = document.getElementById('summary-table-body');
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }

  product_ids = [];
  total = 0;

  table.appendChild(getTotal());
}

function clearTotal() {
  var total_tr = document.getElementById("total-tr");
  if (total_tr !== null) {
    total_tr.parentNode.removeChild(total_tr);
  }
}

function getTotal(){
  var tr_total = document.createElement('tr');
  tr_total.setAttribute('id', 'total-tr')

  var td_total_display = document.createElement('td');
  td_total_display.setAttribute('class', 'thick-line text-right');
  td_total_display.innerHTML = "<strong>Total: </strong>";

  var td_total = document.createElement('td');
  td_total.setAttribute('class', 'thick-line text-right');
  td_total.innerHTML = "<strong>" + total + " </strong>";

  tr_total.appendChild(td_total_display);
  tr_total.appendChild(td_total);

  return tr_total;
}

function postExport(url,storage_id,namelist) {
  data = {
    'namelist': namelist,
    'storage_id': storage_id,
    'product_ids' : product_ids,
    'total' : total,
  };

  let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];

  let form = document.createElement('form');
  form.action = url;
  form.method = "POST";

  let inp = document.createElement('input');
  inp.type = 'hidden';
  inp.name = 'data';
  inp.value = JSON.stringify(data);

  form.appendChild(csrftoken);
  form.appendChild(inp);

  document.body.appendChild(form);
  form.submit();
}
