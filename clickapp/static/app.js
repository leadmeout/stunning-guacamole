// document.getElementById('add-row-btn').onclick = duplicate;
// var i = 0;
// var original = document.getElementById('duplicate-form');
//
// function duplicate() {
//   var clone = original.cloneNode(true); // "deep" clone
//   clone.id = "duplicate-form" + ++i; // there can only be one element with an ID
//   original.parentNode.appendChild(clone);
// }


function addRow() {

  const form_table = document.getElementById('table-id')
  const form_row = document.getElementById('table-row');
  const form_row_copy = form_row.cloneNode(true);
  form_table.appendChild(form_row_copy);

}


function deleteRow() {

  const form_table = document.getElementById('table-id')
  const form_row = document.getElementById('table-row');
  form_row.remove();

}
