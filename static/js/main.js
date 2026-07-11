document.addEventListener('DOMContentLoaded', () => {
  initCopyButtons();
  initPasswordToggles();
  initSliders();
  initForms();
});

function initCopyButtons() {
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.closest('.result-card-value, .hash-output');
      if (!target) return;
      const text = target.dataset.copyText || target.textContent.trim();
      navigator.clipboard.writeText(text).then(() => {
        const original = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        showToast('Copied to clipboard', 'success');
        setTimeout(() => {
          btn.textContent = original;
          btn.classList.remove('copied');
        }, 2000);
      }).catch(() => {
        showToast('Failed to copy', 'error');
      });
    });
  });
}

function initPasswordToggles() {
  document.querySelectorAll('.password-toggle').forEach(toggle => {
    toggle.addEventListener('click', () => {
      const input = toggle.parentElement.querySelector('input');
      if (!input) return;
      const isPassword = input.type === 'password';
      input.type = isPassword ? 'text' : 'password';
      toggle.textContent = isPassword ? '🙈' : '👁';
      toggle.setAttribute('aria-label', isPassword ? 'Hide password' : 'Show password');
    });
  });
}

function initSliders() {
  document.querySelectorAll('input[type="range"]').forEach(slider => {
    const display = slider.parentElement.querySelector('.slider-value') ||
                    document.getElementById(slider.dataset.display);
    if (!display) return;
    display.textContent = slider.value;
    slider.addEventListener('input', () => {
      display.textContent = slider.value;
    });
  });
}

function initForms() {
  document.querySelectorAll('form[data-ajax]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('[type="submit"]');
      const loadingOverlay = form.closest('.card, .module-card')?.querySelector('.loading-overlay');
      const resultsContainer = form.querySelector('.results-section') ||
                                form.closest('.module-card')?.querySelector('.results-section');

      const originalBtnText = btn?.innerHTML;
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner"></span> Processing...';
      }
      if (loadingOverlay) loadingOverlay.classList.add('active');

      try {
        const formData = new FormData(form);
        const response = await fetch(form.action || window.location.href, {
          method: 'POST',
          body: formData,
          headers: { 'X-Requested-With': 'XMLHttpRequest' }
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const data = await response.json();

        if (resultsContainer && data.html) {
          resultsContainer.innerHTML = data.html;
          resultsContainer.style.display = 'block';
          animateResults(resultsContainer);
          initCopyButtons();
        }

        if (data.message) {
          showToast(data.message, data.type || 'success');
        }
      } catch (err) {
        console.error('Form submission error:', err);
        showToast('An error occurred. Please try again.', 'error');
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = originalBtnText;
        }
        if (loadingOverlay) loadingOverlay.classList.remove('active');
      }
    });
  });
}

function animateResults(container) {
  container.style.opacity = '0';
  container.style.transform = 'translateY(12px)';
  requestAnimationFrame(() => {
    container.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    container.style.opacity = '1';
    container.style.transform = 'translateY(0)';
  });

  container.querySelectorAll('.result-card, .hash-output, .risk-indicator, .port-scan-table tbody tr').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(8px)';
    setTimeout(() => {
      el.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 80 * i);
  });
}

function showToast(message, type = 'info') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;

  const icons = { success: '✓', error: '✕', info: 'ℹ' };
  toast.innerHTML = `<span>${icons[type] || 'ℹ'}</span><span>${message}</span>`;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add('toast-exit');
    toast.addEventListener('animationend', () => toast.remove());
  }, 3500);
}
