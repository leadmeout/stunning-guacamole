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

  const formTable = document.getElementById('table-id');
  const formRow = document.getElementById('table-row');
  const formRowCopy = formRow.cloneNode(true);
  formTable.appendChild(formRowCopy);

}


function deleteRow() {

  const formTable = document.getElementById('table-id');
  var rowCount = formTable.rows.length;

  if (rowCount >= 3) {
    formTable.deleteRow(rowCount - 1)
  } else {
    alert('Die letzte Zeile darf nicht gelöscht werden!' + '\n' + "The last row cannot be deleted!")
  };
}
