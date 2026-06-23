(function(){
  var DEFAULTS = {
    versionUrl: 'https://public-files.foneclaw.ai/FoneClaw/Version/version.json',
    downloadBaseUrl: 'https://public-files.foneclaw.ai/',
    loadingLabel: 'Checking APK availability...',
    loadingMeta: 'Fetching the latest Android version.',
    readyLabel: 'Download APK',
    emptyLabel: 'APK coming soon',
    emptyMeta: 'The Android APK is not available yet. Please check back later.',
    errorLabel: 'APK temporarily unavailable',
    errorMeta: 'Could not check the latest APK. Please try again later.',
    title: '',
    copy: '',
    fallbackHtml: ''
  };

  function track(name, params){
    try {
      if (typeof window.trackEvent === 'function') window.trackEvent(name, params || {});
      else if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
    } catch(e) {}
  }

  function formatApkSize(bytes){
    var size = Number(bytes || 0);
    if (!Number.isFinite(size) || size <= 0) return '';
    if (size >= 1024 * 1024 * 1024) return (size / 1024 / 1024 / 1024).toFixed(2) + ' GB';
    if (size >= 1024 * 1024) return (size / 1024 / 1024).toFixed(1) + ' MB';
    if (size >= 1024) return (size / 1024).toFixed(1) + ' KB';
    return size + ' B';
  }

  function normalizeApkPath(apkPath){
    if (typeof apkPath !== 'string') return '';
    var clean = apkPath.trim();
    if (!clean) return '';
    return clean.replace(/^\/+/, '');
  }

  function readOptions(root){
    var opts = {};
    Object.keys(DEFAULTS).forEach(function(key){ opts[key] = DEFAULTS[key]; });
    var lang = (document.documentElement && document.documentElement.lang || '').toLowerCase();
    if (lang === 'tw' || lang.indexOf('zh-tw') === 0) {
      opts.loadingLabel = '正在檢查 APK 可用性...';
      opts.loadingMeta = '正在取得最新 Android 版本。';
      opts.readyLabel = '下載 APK';
      opts.emptyLabel = 'APK 即將開放';
      opts.emptyMeta = 'Android APK 暫時尚未開放下載，請稍後再試。';
      opts.errorLabel = 'APK 暫時無法下載';
      opts.errorMeta = '暫時無法檢查最新 APK，請稍後再試。';
    } else if (lang.indexOf('zh') === 0) {
      opts.loadingLabel = '正在检查 APK 可用性...';
      opts.loadingMeta = '正在获取最新 Android 版本。';
      opts.readyLabel = '下载 APK';
      opts.emptyLabel = 'APK 即将上线';
      opts.emptyMeta = 'Android APK 暂未开放下载，请稍后再试。';
      opts.errorLabel = 'APK 暂时不可用';
      opts.errorMeta = '暂时无法检查最新 APK，请稍后重试。';
    }
    if (!root || !root.dataset) return opts;
    if (root.dataset.versionUrl) opts.versionUrl = root.dataset.versionUrl;
    if (root.dataset.downloadBaseUrl) opts.downloadBaseUrl = root.dataset.downloadBaseUrl;
    if (root.dataset.loadingLabel) opts.loadingLabel = root.dataset.loadingLabel;
    if (root.dataset.loadingMeta) opts.loadingMeta = root.dataset.loadingMeta;
    if (root.dataset.readyLabel) opts.readyLabel = root.dataset.readyLabel;
    if (root.dataset.emptyLabel) opts.emptyLabel = root.dataset.emptyLabel;
    if (root.dataset.emptyMeta) opts.emptyMeta = root.dataset.emptyMeta;
    if (root.dataset.errorLabel) opts.errorLabel = root.dataset.errorLabel;
    if (root.dataset.errorMeta) opts.errorMeta = root.dataset.errorMeta;
    if (root.dataset.title) opts.title = root.dataset.title;
    if (root.dataset.copy) opts.copy = root.dataset.copy;
    if (root.dataset.fallbackHtml) opts.fallbackHtml = root.dataset.fallbackHtml;
    return opts;
  }

  function ensureMarkup(root, opts){
    root.classList.add('foneclaw-apk-cta');
    root.setAttribute('aria-live', 'polite');
    if (root.querySelector('.foneclaw-apk-cta__button')) return;

    if (opts.title) {
      var title = document.createElement('h3');
      title.className = 'foneclaw-apk-cta__title';
      title.textContent = opts.title;
      root.appendChild(title);
    }
    if (opts.copy) {
      var copy = document.createElement('p');
      copy.className = 'foneclaw-apk-cta__copy';
      copy.textContent = opts.copy;
      root.appendChild(copy);
    }
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'foneclaw-apk-cta__button is-loading';
    btn.disabled = true;
    btn.setAttribute('aria-disabled', 'true');
    btn.textContent = opts.loadingLabel;
    root.appendChild(btn);

    var meta = document.createElement('div');
    meta.className = 'foneclaw-apk-cta__meta';
    meta.textContent = opts.loadingMeta;
    root.appendChild(meta);

    if (opts.fallbackHtml) {
      var fallback = document.createElement('div');
      fallback.className = 'foneclaw-apk-cta__fallback';
      fallback.innerHTML = opts.fallbackHtml;
      root.appendChild(fallback);
    }
  }

  function setButtonState(root, state, label, metaText){
    var btn = root.querySelector('.foneclaw-apk-cta__button');
    var meta = root.querySelector('.foneclaw-apk-cta__meta');
    if (!btn || !meta) return;
    btn.classList.remove('is-loading','is-ready','is-disabled');
    btn.classList.add(state === 'ready' ? 'is-ready' : state === 'loading' ? 'is-loading' : 'is-disabled');
    btn.textContent = label;
    meta.textContent = metaText || '';
    var disabled = state !== 'ready';
    btn.disabled = disabled;
    btn.setAttribute('aria-disabled', disabled ? 'true' : 'false');
  }

  function initOne(root){
    if (!root || root.dataset.foneclawApkCtaReady === 'true') return;
    root.dataset.foneclawApkCtaReady = 'true';
    var opts = readOptions(root);
    var downloadUrl = '';
    ensureMarkup(root, opts);
    setButtonState(root, 'loading', opts.loadingLabel, opts.loadingMeta);

    var btn = root.querySelector('.foneclaw-apk-cta__button');
    if (btn) {
      btn.addEventListener('click', function(){
        if (!downloadUrl) return;
        track('apk_download_click', { link_url: downloadUrl });
        window.location.href = downloadUrl;
      });
    }

    fetch(opts.versionUrl, { cache: 'no-store' })
      .then(function(response){
        if (!response.ok) throw new Error('HTTP ' + response.status);
        return response.json();
      })
      .then(function(data){
        var apkPath = normalizeApkPath(data && data.apkPath);
        if (!apkPath) {
          downloadUrl = '';
          setButtonState(root, 'disabled', opts.emptyLabel, opts.emptyMeta);
          return;
        }
        downloadUrl = opts.downloadBaseUrl.replace(/\/+$/, '') + '/' + apkPath;
        var version = data && data.version ? 'v' + data.version : 'latest version';
        var size = formatApkSize(data && data.apkSize);
        var meta = 'Ready to download ' + version + (size ? ' · ' + size : '') + '.';
        setButtonState(root, 'ready', opts.readyLabel, meta);
      })
      .catch(function(error){
        downloadUrl = '';
        setButtonState(root, 'disabled', opts.errorLabel, opts.errorMeta);
        track('apk_version_check_failed', { message: String(error && error.message || error) });
        if (window.console && console.warn) console.warn('FoneClaw APK version check failed:', error);
      });
  }

  function initAll(){
    document.querySelectorAll('[data-foneclaw-apk-cta]').forEach(initOne);
  }

  window.FoneClawApkCTA = { init: initAll, initOne: initOne };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll);
  else initAll();
})();
