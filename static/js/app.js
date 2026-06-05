document.addEventListener("DOMContentLoaded", function () {
    console.log("Login cargado correctamente");
});

function toggleSidebar() {

    const sidebar = document.querySelector('.sidebar');
    const main = document.querySelector('.main');

    sidebar.classList.toggle('collapsed');
    main.classList.toggle('expanded');
}