document.addEventListener('DOMContentLoaded', () => {
    const modalFiles = [
      { path: 'listar_tarefas.html', id: 'taskModal' },
      { path: 'cadastrar_tarefa.html', id: 'exampleModal' }
    ];
    const container = document.getElementById('modals-container');
  
    // 1) carrega e injeta todos os modais
    Promise.all(
      modalFiles.map(m =>
        fetch(m.path)
          .then(res => res.ok ? res.text() : Promise.reject(res.status))
          .then(html => container.insertAdjacentHTML('beforeend', html))
      )
    )
    .then(() => {
      // 2) agora que os modais existem no DOM, podemos configurar os botões
      document.getElementById('btnListar')
        .addEventListener('click', e => {
          e.preventDefault();
          openModal('taskModal');
        });
  
      document.getElementById('btnCadastrar')
        .addEventListener('click', e => {
          e.preventDefault();
          openModal('exampleModal');
        });
    })
    .catch(console.error);
  
    // função pura pra abrir o modal
    function openModal(modalId) {
      const modal = document.getElementById(modalId);
      // backdrop
      const backdrop = document.createElement('div');
      backdrop.className = 'modal-backdrop fade show';
      document.body.appendChild(backdrop);
      // mostrar modal
      modal.classList.add('show');
      modal.style.display = 'block';
      document.body.classList.add('modal-open');
  
      // fecha ao clicar em qualquer botão .close
      modal.querySelectorAll('.close').forEach(btn =>
        btn.addEventListener('click', () => closeModal(modal, backdrop), { once: true })
      );
    }
  
    // função pura pra fechar o modal
    function closeModal(modal, backdrop) {
      modal.classList.remove('show');
      modal.style.display = 'none';
      document.body.classList.remove('modal-open');
      backdrop.remove();
    }
  });
  