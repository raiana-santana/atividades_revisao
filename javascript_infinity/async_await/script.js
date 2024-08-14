// Uma função assíncrona é uma função que é executada enquanto outro processo do programa ocorre.
// Utilizada quando o código pode demorar para retornar uma respostas. Como um código que faz um consumo de API, por exemplo.

async function buscarDados() { // Função assícrona
    // O await é utilizado para esperar que o fetch faça a busca pelos dados na API, uma vez que este processo é demorado
    const request = await fetch('https://dog.ceo/api/breeds/image/random') // Faz a requisição à API. Importante frizar que o "await" só funciona dentro de uma async function
    const data = await request.json() // Faz a conversão da resposta do fetch para um objeto que o JavaScript entende. O await é utilozado aqui por se tratar de uma operação demorada

    console.log(data.message) // Com os dados convertidos, é possível acessar as informações retornadas pela API
}

buscarDados()