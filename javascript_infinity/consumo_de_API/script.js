const botao = document.querySelector('#buscarDog'); //pegando o elemento botão com o querySelector

botao.addEventListener('click', buscadorDeCachorro); //addEventListener que recebe o evento de click e executa uma função

//função que executa a busca pela API
function buscadorDeCachorro(){
    const api = 'https://dog.ceo/api/breeds/image/random'; //URL da API que devolve uma imagem aleatória de algum cachorro

    fetch(api)
    .then(response => response.json()) //converte a resposta da API, que está em formato JSON (string), em um objeto javascript
    .then(data => {
        const image = document.createElement('img') //cria um element 'img' dinamicamente, com javascript
        image.setAttribute('src', data.message); //define o 'src' com a URL da imagem retornada pela API
        document.body.appendChild(image) //adiciona a imagem ao body
    })
    
}