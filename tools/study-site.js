/* Site navigation and page-title search. Lesson models and answers are independent. */
(() => {
  const en = document.documentElement.lang === 'en';
  const menu = document.querySelector('.study-menu');
  const sidebar = document.querySelector('.study-sidebar');
  const compact = window.matchMedia('(max-width: 980px)');
  function setMenu(open) {
    if (!open && sidebar.contains(document.activeElement)) menu.focus();
    menu.setAttribute('aria-expanded', String(open));
    const label = en
      ? (open ? 'Collapse learning menu' : 'Expand learning menu')
      : (open ? '학습 메뉴 접기' : '학습 메뉴 펼치기');
    menu.setAttribute('aria-label', label);
    menu.querySelector('.study-menu-tooltip').textContent = label;
    sidebar.hidden = !open;
    document.body.classList.toggle('study-sidebar-collapsed', !open);
  }
  function closeMenu() {
    setMenu(false);
  }
  setMenu(!compact.matches);
  menu.hidden = false;
  compact.addEventListener('change', () => setMenu(!compact.matches));
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') === 'true';
    setMenu(!open);
  });
  menu.addEventListener('pointerleave', () => delete menu.dataset.tooltipDismissed);
  menu.addEventListener('blur', () => delete menu.dataset.tooltipDismissed);
  document.addEventListener('keydown', event => {
    const editing = event.target.closest('input, textarea, select, [contenteditable="true"]');
    if (event.key !== 'Escape' || event.defaultPrevented || editing || dialog.open) return;
    const open = menu.getAttribute('aria-expanded') === 'true';
    if (open) {
      closeMenu();
      menu.focus();
    }
    if (open || menu.matches(':hover, :focus-within')) menu.dataset.tooltipDismissed = 'true';
  });
  document.addEventListener('click', event => {
    if (compact.matches && !sidebar.contains(event.target) && !menu.contains(event.target)) closeMenu();
  });
  const dialog = document.querySelector('.study-search-dialog');
  const input = dialog.querySelector('input');
  const results = dialog.querySelector('.search-results');
  const status = dialog.querySelector('[role="status"]');
  const pages = JSON.parse(document.querySelector('#study-search-data').textContent);
  function renderSearch() {
    const query = input.value.toLocaleLowerCase().trim();
    const words = query.split(/\s+/).filter(Boolean);
    const matches = pages.filter(page => words.every(word => (page.title + ' ' + page.group + ' ' + page.keywords).toLocaleLowerCase().includes(word)));
    results.replaceChildren();
    for (const page of matches) {
      const link = document.createElement('a');
      link.href = page.href;
      const group = document.createElement('small');
      group.textContent = page.group;
      const title = document.createElement('span');
      title.textContent = page.title;
      link.append(group, title);
      results.append(link);
    }
    status.textContent = en
      ? (matches.length ? `${matches.length} learning materials` : 'No materials found. Try another week or concept.')
      : (matches.length ? `${matches.length}개의 자료` : '찾는 자료가 없습니다. 주차나 개념 이름을 바꿔 보세요.');
  }
  function openSearch() {
    if (compact.matches) closeMenu();
    renderSearch();
    dialog.showModal();
    input.focus();
  }
  document.querySelector('.study-search-trigger').addEventListener('click', openSearch);
  dialog.querySelector('.search-close').addEventListener('click', () => dialog.close());
  input.addEventListener('input', renderSearch);
  input.addEventListener('keydown', event => {
    if (event.key === 'ArrowDown') {
      const first = results.querySelector('a');
      if (first) { event.preventDefault(); first.focus(); }
    }
  });
  document.addEventListener('keydown', event => {
    const editing = event.target.closest('input, textarea, select, [contenteditable="true"]');
    if (event.key === '/' && !editing && !dialog.open) {
      event.preventDefault();
      openSearch();
    }
  });
  const tocLinks = document.querySelectorAll('.toc a[href^="#"], .contents a[href^="#"], .book-layout nav a[href^="#"]');
  const headings = new Map();
  for (const link of tocLinks) {
    const id = decodeURIComponent(link.hash.slice(1));
    const heading = document.getElementById(id);
    if (heading) headings.set(heading, link);
  }
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        for (const link of tocLinks) link.removeAttribute('aria-current');
        headings.get(entry.target).setAttribute('aria-current', 'location');
      }
    }, {rootMargin: '-12% 0px -64% 0px'});
    for (const heading of headings.keys()) observer.observe(heading);
  }
})();
