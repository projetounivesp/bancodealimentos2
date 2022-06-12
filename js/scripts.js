const pathURL = "https://univespbackbancoalimentos.herokuapp.com/api/v1";

function carregarDados() {
  carregarEstoque();
  doados24();
  doadosinicio();
  retirados24();
  retiradosinicio();
  url = window.location.href.split("/");
  if (url[3] === "formretirada.html") {
    formRetirada();
  }
  if (url[3] === "formdoacao.html") {
    formDoacao();
  }
}

function carregarEstoque() {
  const conteudoestoque = document.getElementById("conteudoestoque");

  fetch(`${pathURL}/estoque/listarprodutoestoque`)
    .then((response) => response.json())
    .then((produtos) => {
      console.log(produtos);

      produtos.map((itens, ix) => {
        var div = `<div>${itens.nomeproduto}</div>
        <div id=totalestoque>
        <div style=background-color:${cor[ix]};width:${
          10 * parseInt(itens.total.toString())
        }px;height:20px>
          </div>
          <div>${itens.total}</div>
          </div>
          `;
        conteudoestoque.innerHTML += div;
      });
    })
    .catch((error) =>
      console.error(
        `Erro ao tentar carregar a lista de produtos em estoque-> ${error}`
      )
    );
}

function doados24() {
  fetch(`${pathURL}/doacao/totaldoado24`)
    .then((response) => response.json())
    .then((produtos) => {
      console.log(produtos);

      document.getElementById("pdoacao24").innerHTML = produtos[0].total;
    })
    .catch((error) =>
      console.error(
        `Erro ao tentar carregar o total de produtos doados 24h-> ${error}`
      )
    );
}

function doadosinicio() {
  fetch(`${pathURL}/doacao/totaldoadoinicio`)
    .then((response) => response.json())
    .then((produtos) => {
      console.log(`doacao inicio -> ${produtos[0].total} `);

      document.getElementById("pdoacaoinicio").innerHTML = produtos[0].total;
    })
    .catch((error) =>
      console.error(
        `Erro ao tentar carregar o total de produtos doados 24h-> ${error}`
      )
    );
}

function retirados24() {
  fetch(`${pathURL}/retirada/totaldoado24`)
    .then((response) => response.json())
    .then((produtos) => {
      console.log(`doacao inicio -> ${produtos[0].total} `);

      document.getElementById("pretirados24").innerHTML = produtos[0].total;
    })
    .catch((error) =>
      console.error(
        `Erro ao tentar carregar o total de produtos doados 24h-> ${error}`
      )
    );
}

function retiradosinicio() {
  fetch(`${pathURL}/retirada/totaldoadoinicio`)
    .then((response) => response.json())
    .then((produtos) => {
      console.log(`doacao inicio -> ${produtos[0].total} `);

      document.getElementById("pretiradosinicio").innerHTML = produtos[0].total;
    })
    .catch((error) =>
      console.error(
        `Erro ao tentar carregar o total de produtos doados 24h-> ${error}`
      )
    );
}

//----------------- Formulários que serão abertos por cada botao ---------------------------------
const btnRetirada = document.getElementById("retirada");
btnRetirada.onclick = () => {
  window.location.replace("formretirada.html");
};

const btnDoacao = document.getElementById("doacao");
btnDoacao.onclick = () => {
  window.location.replace("formdoacao.html");
};

const btnTelaInicial = document.getElementById("telainicial");
btnTelaInicial.onclick = () => {
  window.location.replace("index.html");
};

const btnSobre = document.getElementById("sobre");
btnSobre.onclick = () => {
  window.location.replace("sobre.html");
};

function formRetirada() {
  const produtosestoque = document.getElementById("select-retirada");

  fetch(`${pathURL}/estoque/listarprodutoestoque`)
    .then((response) => response.json())
    .then((produtos) => {
      produtos.map((itens, ix) => {
        produtosestoque.innerHTML += `<option value=${itens.idproduto}>${itens.nomeproduto}</option>`;
      });
    })
    .catch((erro) =>
      console.error(`Erro ao tentar carregar os produtos->${erro}`)
    );
}

function formDoacao() {
  const sr = document.getElementById("select-retirada");
  fetch(`${pathURL}/produto/listar`)
    .then((response) => response.json())
    .then((produtos) => {
      console.log("informacoes " + produtos);

      produtos.map((itens, ix) => {
        sr.innerHTML += `<option value=${itens.idproduto}>${itens.nomeproduto}</option>`;
      });
    })
    .catch((error) =>
      console.error(`Erro ao tentar carregar a lista de produtos -> ${error}`)
    );
}

//cores para as barras do estoque
let cor = [
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
  "#c62828",
  "#64b5f6",
  "#7b1fa2",
  "#009688",
  "#01579b",
  "#cddc39",
  "#ffa726",
  "#ff6f00",
];
