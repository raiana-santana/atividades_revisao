//criação de uma lista de notas, onde iremos armazenar as notas do aluno
let lista_notas = []

//lista de estudantes, onde estão armazenamos as informações dos alunos, em objetos
let lista_de_estudantes = [
    {id:1, nome:"Nathalia", notas:[7.9,8.7,9.8,6.7]},
    {id:2, nome:"Raiana", notas:[8.9,9.6,9.8,7.7]},
    {id:3, nome:"Lucas", notas:[7.9,8.7,9.8,6.7]}
]

//solicitação do nome do novo aluno 
let aluno_novo = prompt("Digite o nome do novo aluno: ")

//criação de um loop for para rodar 4 vezes, pedindo as 4 notas
for(let i = 1; i <= 4; i++){
    //pedindo as notas
    let nota = parseFloat(prompt(`Digite a ${i} nota`))
    //adicionando cada nota dentro da lista_notas
    lista_notas.push(nota)
}

//criação de uma função que gera um ID automaticamente
function gerarID(){
    //pego o tamanho da lista de estudantes
    let tamanho_lista_estudantes = lista_de_estudantes.length
    //acesso o último valor da lista através de sua posição no array.
    //em javascript, o último valor da lista (array) será sempre o tamanho da lista - 1 
    //também estou acessando a chave id, que faz parte de cada objeto que compõe a lista
    let ultimo_valor = lista_de_estudantes[tamanho_lista_estudantes-1].id

    return ultimo_valor + 1
}

//criando um novo objeto que será adicionado na lista de estudantes
let novo = {id: gerarID(), nome: aluno_novo, notas: lista_notas}

//adicionando o novo aluno na lista de estudantes
lista_de_estudantes.push(novo)

console.log(lista_de_estudantes)