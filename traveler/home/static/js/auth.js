  // Получаем элементы
  const modal = document.getElementById("myModal");
  const btn = document.getElementById("openModalBtn");
  const span = document.getElementsByClassName("close")[0];

  // Открытие модального окна
  btn.onclick = function() {
    modal.style.display = "block";
  }

  // Закрытие модального окна
  span.onclick = function() {
    modal.style.display = "none";
  }

  // Закрытие при клике вне окна
  window.onclick = function(event) {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  }

