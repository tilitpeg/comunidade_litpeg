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
                        '#04fc73', '#fc042d', '#04fafc'
                      ],
                    data: data.data,
                    borderColor: '#000000',
                    borderWidth: 1,

                }],
                options: {
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
                        'rgba(255, 99, 132)',
                        'rgba(255, 159, 64)',
                        'rgba(255, 205, 86)',
                        'rgba(75, 192, 192)',
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
                    label: 'Quantidade',
                    backgroundColor: [
                        'rgba(255, 99, 132)',
                        'rgba(255, 159, 64)',
                        'rgba(255, 205, 86)',
                        'rgba(75, 192, 192)',
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
                        'rgba(255, 99, 132)',
                        'rgba(255, 159, 64)',
                        'rgba(255, 205, 86)',
                        'rgba(75, 192, 192)',
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

