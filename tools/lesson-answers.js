(() => {
  const button = document.querySelector('#download-answers');
  if (!button) return;
  const en = document.documentElement.lang === 'en';
  const label = (ko, english) => en ? english : ko;
  document.body.classList.add('js-ready');
  const fields = [...document.querySelectorAll('textarea[data-answer]')];
  const saved = document.querySelector('#confirm-saved');
  let dirty = false;
  const markDirty = () => { dirty = true; saved.disabled = true; };
  fields.forEach(field => field.addEventListener('input', markDirty));
  const checks = [...document.querySelectorAll('article input[type="checkbox"]')];
  checks.forEach(box => box.addEventListener('change', markDirty));
  window.addEventListener('beforeunload', event => { if (dirty) { event.preventDefault(); event.returnValue = ''; } });
  saved.addEventListener('click', () => {
    dirty = false;
    saved.disabled = true;
    document.querySelector('#download-status').textContent = label('저장 확인을 기록했습니다. 내용을 더 바꾸면 다시 내려받으세요.', 'File check confirmed. Download again if you change your answers.');
  });
  button.addEventListener('click', () => {
    const recordSummary = '작성자의 개인 답안이다. 직접 수행·제공 예제·미수행은 작성자가 구분해 적고, 빈칸은 미작성으로 남긴다.';
    const summary = label(recordSummary, 'Personal answers. The author distinguishes direct work, supplied examples and unfinished tasks. Empty answers remain unanswered.');
    const lines = ['# ' + document.title.replace(/ · (실습으로 배우는 네트워크|Hands-on Computer Networks)$/, '') + label(' — 내 기록', ' — my answers'), '', label('요약: ', 'Summary: ') + summary, '', label('작성일: ', 'Date: ') + new Date().toLocaleDateString(en ? 'en-GB' : 'ko-KR'), ''];
    fields.forEach(field => lines.push('## ' + field.dataset.answer, '', field.value.trim() || label('미작성', 'Unanswered'), ''));
    if (checks.length) { lines.push(label('## 완료 확인', '## Completion checks'), ''); checks.forEach(box => lines.push('- [' + (box.checked ? 'x' : ' ') + '] ' + box.closest('li')?.textContent.trim())); lines.push(''); }
    const blob = new Blob([lines.join('\n')], {type:'text/markdown;charset=utf-8'});
    const link = document.createElement('a'); link.href = URL.createObjectURL(blob);
    link.download = document.body.dataset.page.replace('.html', '') + '-my-answers.md';
    link.click(); setTimeout(() => URL.revokeObjectURL(link.href), 60000);
    saved.disabled = false;
    document.querySelector('#download-status').textContent = label('다운로드를 요청했습니다. 브라우저 다운로드 목록과 저장된 파일을 열어 내용을 확인하세요.', 'Download requested. Check your browser downloads and open the saved file to verify its contents.');
  });
})();
