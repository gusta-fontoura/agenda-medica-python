var table;

function statusFormatter(cell) {
    var value = cell.getValue();
    var colorClass = '';
    if (value === 'Confirmado') colorClass = 'status-confirmado';
    else if (value === 'Pendente') colorClass = 'status-pendente';
    else if (value === 'Cancelado') colorClass = 'status-cancelado';
    return '<span class="' + colorClass + '">' + value + '</span>';
}

document.addEventListener('DOMContentLoaded', function () {
    var emptyState = document.getElementById('empty-state');
    var tableEl = document.getElementById('agendamentos-table');

    table = new Tabulator(tableEl, {
        ajaxURL: '/api/agendamentos',
        ajaxResponseType: 'json',
        columns: [
            { title: 'Data', field: 'data', width: 120, headerSort: true },
            { title: 'Horario', field: 'horario', width: 100, headerSort: true },
            { title: 'Paciente', field: 'paciente', width: 180, headerSort: true },
            { title: 'CPF', field: 'cpf', width: 150, headerSort: false },
            { title: 'Medico', field: 'medico', width: 180, headerSort: true },
            { title: 'Especialidade', field: 'especialidade', width: 140, headerSort: true },
            { title: 'Convenio', field: 'convenio', width: 140, headerSort: true },
            { title: 'Status', field: 'status', width: 120, headerSort: true, formatter: statusFormatter },
        ],
        layout: 'fitDataStretch',
        pagination: false,
        placeholder: 'Nenhum agendamento encontrado',
        locale: 'pt-br',
        langs: {
            'pt-br': {
                data: {
                    loading: 'Carregando...',
                    error: 'Erro ao carregar dados',
                    empty: 'Nenhum agendamento encontrado',
                }
            }
        },
        ajaxError: function () {
            tableEl.style.display = 'none';
            emptyState.classList.remove('hidden');
            emptyState.querySelector('p').textContent = 'Erro ao carregar agendamentos. Tente novamente mais tarde.';
        },
        dataLoaded: function (data) {
            if (!data || data.length === 0) {
                tableEl.style.display = 'none';
                emptyState.classList.remove('hidden');
            } else {
                tableEl.style.display = '';
                emptyState.classList.add('hidden');
            }
        }
    });

    var searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', function () {
        var value = this.value.toLowerCase();
        if (value === '') {
            table.clearFilter();
        } else {
            table.setFilter(function (data) {
                return (
                    (data.paciente && data.paciente.toLowerCase().indexOf(value) !== -1) ||
                    (data.cpf && data.cpf.toLowerCase().indexOf(value) !== -1) ||
                    (data.medico && data.medico.toLowerCase().indexOf(value) !== -1)
                );
            });
        }
    });
});
