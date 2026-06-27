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
    if (lang === 'th' || lang.indexOf('th') === 0) {
      opts.loadingLabel = 'กำลังตรวจสอบ APK...';
      opts.loadingMeta = 'กำลังดึงเวอร์ชัน Android ล่าสุด';
      opts.readyLabel = 'ดาวน์โหลด APK';
      opts.emptyLabel = 'APK จะพร้อมใช้งานเร็วๆ นี้';
      opts.emptyMeta = 'ไฟล์ APK สำหรับ Android ยังไม่พร้อมดาวน์โหลด โปรดลองใหม่ภายหลัง';
      opts.errorLabel = 'APK ไม่พร้อมใช้งานชั่วคราว';
      opts.errorMeta = 'ไม่สามารถตรวจสอบ APK ล่าสุดได้ โปรดลองใหม่ภายหลัง';
    } else if (lang === 'ar' || lang.indexOf('ar') === 0) {
      opts.loadingLabel = 'جارٍ التحقق من توفر APK...';
      opts.loadingMeta = 'جارٍ جلب أحدث إصدار لأندرويد.';
      opts.readyLabel = 'تنزيل APK';
      opts.emptyLabel = 'APK سيصدر قريبًا';
      opts.emptyMeta = 'ملف APK لأندرويد غير متاح بعد. يرجى المحاولة لاحقًا.';
      opts.errorLabel = 'APK غير متاح مؤقتًا';
      opts.errorMeta = 'تعذر التحقق من أحدث APK. يرجى المحاولة لاحقًا.';
    } else if (lang === 'pt' || lang.indexOf('pt') === 0) {
      opts.loadingLabel = 'Verificando disponibilidade do APK...';
      opts.loadingMeta = 'Buscando a versão mais recente para Android.';
      opts.readyLabel = 'Baixar APK';
      opts.emptyLabel = 'APK disponível em breve';
      opts.emptyMeta = 'O APK para Android ainda não está disponível. Verifique novamente mais tarde.';
      opts.errorLabel = 'APK temporariamente indisponível';
      opts.errorMeta = 'Não foi possível verificar o APK mais recente. Tente novamente mais tarde.';
    } else if (lang === 'es' || lang.indexOf('es') === 0) {
      opts.loadingLabel = 'Comprobando disponibilidad del APK...';
      opts.loadingMeta = 'Buscando la versión más reciente para Android.';
      opts.readyLabel = 'Descargar APK';
      opts.emptyLabel = 'APK disponible próximamente';
      opts.emptyMeta = 'El APK de Android todavía no está disponible. Vuelve a comprobarlo más tarde.';
      opts.errorLabel = 'APK temporalmente no disponible';
      opts.errorMeta = 'No se pudo comprobar el APK más reciente. Inténtalo de nuevo más tarde.';
    } else if (lang === 'ko' || lang.indexOf('ko') === 0) {
      opts.loadingLabel = 'APK 확인 중...';
      opts.loadingMeta = '최신 Android 버전을 확인하고 있습니다.';
      opts.readyLabel = 'APK 다운로드';
      opts.emptyLabel = 'APK 곧 공개';
      opts.emptyMeta = 'Android APK는 아직 다운로드할 수 없습니다. 잠시 후 다시 확인해 주세요.';
      opts.errorLabel = 'APK를 일시적으로 확인할 수 없습니다';
      opts.errorMeta = '최신 APK를 확인하지 못했습니다. 잠시 후 다시 시도해 주세요.';
    } else if (lang === 'ja' || lang.indexOf('ja') === 0) {
      opts.loadingLabel = 'APK の確認中...';
      opts.loadingMeta = '最新の Android 版を取得しています。';
      opts.readyLabel = 'APK をダウンロード';
      opts.emptyLabel = 'APK はまもなく公開';
      opts.emptyMeta = 'Android APK はまだ公開されていません。しばらくしてから再度ご確認ください。';
      opts.errorLabel = 'APK を一時的に確認できません';
      opts.errorMeta = '最新 APK を確認できませんでした。後でもう一度お試しください。';
    } else if (lang === 'tw' || lang.indexOf('zh-tw') === 0) {
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
    } else if (lang === 'id' || lang.indexOf('id') === 0) {
      opts.loadingLabel = 'Memeriksa ketersediaan APK...';
      opts.loadingMeta = 'Mengambil versi Android terbaru.';
      opts.readyLabel = 'Unduh APK';
      opts.emptyLabel = 'APK segera tersedia';
      opts.emptyMeta = 'APK untuk Android belum tersedia. Silakan coba lagi nanti.';
      opts.errorLabel = 'APK sementara tidak tersedia';
      opts.errorMeta = 'Tidak dapat memeriksa APK terbaru. Silakan coba lagi nanti.';
    } else if (lang === 'vi' || lang.indexOf('vi') === 0) {
      opts.loadingLabel = 'Đang kiểm tra APK...';
      opts.loadingMeta = 'Đang lấy phiên bản Android mới nhất.';
      opts.readyLabel = 'Tải APK';
      opts.emptyLabel = 'APK sắp ra mắt';
      opts.emptyMeta = 'APK Android chưa sẵn sàng để tải. Vui lòng quay lại sau.';
      opts.errorLabel = 'APK tạm thời không khả dụng';
      opts.errorMeta = 'Không thể kiểm tra APK mới nhất. Vui lòng thử lại sau.';
    } else if (lang === 'de' || lang.indexOf('de') === 0) {
      opts.loadingLabel = 'APK wird geprüft...';
      opts.loadingMeta = 'Hole die neueste Android-Version';
      opts.readyLabel = 'APK herunterladen';
      opts.emptyLabel = 'APK demnächst verfügbar';
      opts.emptyMeta = 'Die APK-Datei für Android ist noch nicht verfügbar. Bitte versuchen Sie es später erneut.';
      opts.errorLabel = 'APK vorübergehend nicht verfügbar';
      opts.errorMeta = 'Die neueste APK konnte nicht überprüft werden. Bitte versuchen Sie es später erneut.';
    } else if (lang === 'fr' || lang.indexOf('fr') === 0) {
      opts.loadingLabel = 'Vérification de l APK...';
      opts.loadingMeta = 'Récupération de la dernière version Android';
      opts.readyLabel = 'Télécharger l APK';
      opts.emptyLabel = 'APK bientôt disponible';
      opts.emptyMeta = 'Le fichier APK pour Android n est pas encore disponible. Veuillez réessayer plus tard.';
      opts.errorLabel = 'APK temporairement indisponible';
      opts.errorMeta = 'Impossible de vérifier le dernier APK. Veuillez réessayer plus tard.';
    } else if (lang === 'ru' || lang.indexOf('ru') === 0) {
      opts.loadingLabel = 'Проверка APK...';
      opts.loadingMeta = 'Получение последней версии Android';
      opts.readyLabel = 'Скачать APK';
      opts.emptyLabel = 'APK скоро будет доступен';
      opts.emptyMeta = 'Файл APK для Android пока недоступен. Пожалуйста, попробуйте позже.';
      opts.errorLabel = 'APK временно недоступен';
      opts.errorMeta = 'Не удалось проверить последний APK. Пожалуйста, попробуйте позже.';
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
        var pageLang = (document.documentElement && document.documentElement.lang || '').toLowerCase();
        var readyPrefix = 'Ready to download ';
        if (pageLang.indexOf('ar') === 0) readyPrefix = 'جاهز للتنزيل ';
        else if (pageLang.indexOf('vi') === 0) readyPrefix = 'Sẵn sàng tải xuống ';
        else if (pageLang.indexOf('id') === 0) readyPrefix = 'Siap diunduh ';
        else if (pageLang.indexOf('pt') === 0) readyPrefix = 'Pronto para baixar ';
        else if (pageLang.indexOf('es') === 0) readyPrefix = 'Listo para descargar ';
        var meta = readyPrefix + version + (size ? ' · ' + size : '') + '.';
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
