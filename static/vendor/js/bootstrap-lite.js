(function () {
  function closest(element, selector) {
    while (element && element.nodeType === 1) {
      if (element.matches(selector)) {
        return element;
      }
      element = element.parentElement;
    }
    return null;
  }

  document.addEventListener('click', function (event) {
    var toggle = closest(event.target, '[data-toggle="dropdown"]');

    document.querySelectorAll('.dropdown-menu.show').forEach(function (menu) {
      if (!toggle || !menu.parentElement.contains(toggle)) {
        menu.classList.remove('show');
      }
    });

    if (!toggle) {
      return;
    }

    event.preventDefault();
    var dropdown = closest(toggle, '.dropdown');
    if (!dropdown) {
      return;
    }

    var menu = dropdown.querySelector('.dropdown-menu');
    if (menu) {
      menu.classList.toggle('show');
    }
  });
})();
