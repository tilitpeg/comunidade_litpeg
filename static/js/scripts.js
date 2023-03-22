function renderiza_total_membros_ativos(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('membros_total_ativo').innerHTML = data.total
    })
}


function renderiza_total_membros_inativos(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('membros_total_inativo').innerHTML = data.total
    })
}
var nome = "João";
console.log("Olá, " + nome);
function renderiza_genero(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        

        const ctx = document.getElementById('genero').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Quantidade',
                    backgroundColor: [
                        '#a6a6a6',
                        '#3c3c3c',
                        '#212121',
                      ],
                    data: data.data,
                    borderColor: '#000000',
                    borderWidth: 1,

                }],
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                stepSize: 1
                            }
                        }
                    },
                    responsive: true,                   
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Gráfico da Divisão por Gênero'
                    }                   
                },
            }      
        });
    })
}


function renderiza_divisao_bolsa(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('divisao_bolsa').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Quantidade',
                    backgroundColor: [
                        'rgba(144,238,144)',
                        'rgba(60,179,113)',
                        'rgba(46,139,87)',
                        'rgba(0,100,0)',
                        'rgba(0,128,0)',
                        'rgba(34,139,34)',
                        'rgba(50,205,50)',
                        'rgba(124,252,0)'
                        
                      ],
                    data: data.data,
                    borderColor: '#000000',
                    borderWidth: 1,

                }],
                options: {
                    responsive: true,                   
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    title: {
                        display: true,
                        text: 'Gráfico da Divisão por Gênero'
                    }                   
                },
            }
        });
    })
}


function renderiza_divisao_funcao(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('divisao_funcao').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: [
                        'Discente Graduação',
                    ],
                    backgroundColor: [
                        'rgba(144,238,144)',
                        'rgba(60,179,113)',
                        'rgba(46,139,87)',
                        'rgba(0,100,0)',
                        'rgba(0,128,0)',
                        'rgba(34,139,34)',
                        'rgba(50,205,50)',
                        'rgba(124,252,0)'
                      ],
                    data: data.data,
                    borderColor: '#000000',
                    borderWidth: 1,

                }],
                options: {
                    responsive: true,                   
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    title: {
                        display: true,
                        text: 'Gráfico da Divisão por Gênero'
                    }                   
                },
            }
        });
    })
}


function renderiza_qtd_membros_por_lab(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('qtd_membros_por_lab').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Quantidade',
                    backgroundColor: [
                        'rgba(60,60,60)',
                        
                      ],
                    data: data.data,
                    borderColor: '#000000',
                    borderWidth: 1,

                }],
                options: {
                    responsive: true,                   
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    title: {
                        display: true,
                        text: 'Gráfico da Divisão por Gênero'
                    }                   
                },
            }
        });
    })
}

