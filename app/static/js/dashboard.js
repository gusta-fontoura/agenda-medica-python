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

    if (!tableEl || !emptyState) return;

    var data = (typeof AGENDAMENTOS_DATA !== 'undefined') ? AGENDAMENTOS_DATA : [];

    table = new Tabulator(tableEl, {
        data: data,
        layout: 'fitDataStretch',
        columns: [
            { title: 'Data', field: 'data', minWidth: 100, headerSort: true },
            { title: 'Horario', field: 'horario', minWidth: 80, headerSort: true },
            { title: 'Paciente', field: 'paciente', minWidth: 150, headerSort: true },
            { title: 'CPF', field: 'cpf', minWidth: 130, headerSort: false },
            { title: 'Medico', field: 'medico', minWidth: 150, headerSort: true },
            { title: 'Especialidade', field: 'especialidade', minWidth: 120, headerSort: true },
            { title: 'Convenio', field: 'convenio', minWidth: 120, headerSort: true },
            { title: 'Status', field: 'status', minWidth: 110, headerSort: true, formatter: statusFormatter },
        ],
        pagination: false,
        placeholder: 'Nenhum agendamento encontrado',
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

    if (!data || data.length === 0) {
        tableEl.style.display = 'none';
        emptyState.classList.remove('hidden');
    }

    var searchInput = document.getElementById('search-input');
    if (searchInput) {
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
    }
});
