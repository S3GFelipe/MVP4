/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/equipamentos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.equipamentos.forEach(item => insertList(item.name, 
                                                item.temp, 
                                                item.proc,
                                                item.vel,
                                                item.tor,
                                                item.des,
                                                item.outcome
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputEquip, inputTemp, inputProc,
                        inputVel, inputTor, inputDes) => {
    
  const formData = new FormData();
  formData.append('name', inputEquip);
  formData.append('temp', inputTemp);
  formData.append('proc', inputProc);
  formData.append('vel', inputVel);
  formData.append('tor', inputTor);
  formData.append('des', inputDes);
 
  let url = 'http://127.0.0.1:5000/equipamento';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then(() => {
      window.location.reload(); // Isso recarregará a página após a adição do item
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/equipamento?name='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputEquip = document.getElementById("newInput").value;
  let inputTemp = document.getElementById("newTemp").value;
  let inputProc = document.getElementById("newProc").value;
  let inputVel = document.getElementById("newVel").value;
  let inputTor = document.getElementById("newTor").value;
  let inputDes = document.getElementById("newDes").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/equipamentos?nome=${inputEquip}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.equipamentos && data.equipamentos.some(item => item.name === inputEquip)) {
        alert("O equipamento já está cadastrado.\nCadastre o equipamento com um nome diferente ou atualize o existente.");
      } else if (inputEquip === '') {
        alert("O nome do equipamento não pode ser vazio!");
      } else if (inputTemp === '' || inputProc === '' || inputVel === '' || inputTor === '' || inputDes === '') {
        alert("Por favor, preencha todos os campos obrigatórios!");
      } else if (isNaN(inputTemp) || isNaN(inputProc) || isNaN(inputVel) || isNaN(inputTor) || isNaN(inputDes)) {
        alert("Os campos de temperatura, processador, velocidade, torque e desgaste precisam ser números!");
      } else {
        insertList(inputEquip, inputTemp, inputProc, inputVel, inputTor, inputDes);
        postItem(inputEquip, inputTemp, inputProc, inputVel, inputTor, inputDes);
        alert("Item adicionado!")
                
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (nameEquip, temp, proc,vel, tor, des, outcome) => {
  var item = [nameEquip, temp, proc,vel, tor, des, outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newTemp").value = "";
  document.getElementById("newProc").value = "";
  document.getElementById("newVel").value = "";
  document.getElementById("newTor").value = "";
  document.getElementById("newDes").value = "";
  
  removeElement();
}
