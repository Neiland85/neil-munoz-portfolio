const CONSENT_KEY = "nm_cookie_consent";
const ANALYTICS_ID = "plausible-analytics-script";

function getConsent() {
  return localStorage.getItem(CONSENT_KEY);
}

function setConsent(value) {
  localStorage.setItem(CONSENT_KEY, value);
}

function hasAnalyticsConsent() {
  return getConsent() === "accepted_all";
}

function analyticsAlreadyLoaded() {
  return document.getElementById(ANALYTICS_ID) !== null;
}

function loadAnalytics() {
  if (!hasAnalyticsConsent() || analyticsAlreadyLoaded()) {
    return;
  }

  const script = document.createElement("script");
  script.id = ANALYTICS_ID;
  script.defer = true;
  script.dataset.domain = window.location.hostname;
  script.src = "https://plausible.io/js/script.js";
  document.head.appendChild(script);
}

function hideBanner() {
  const banner = document.getElementById("cookie-banner");
  if (banner) {
    banner.classList.add("hidden");
  }
}

function showBanner() {
  const banner = document.getElementById("cookie-banner");
  if (banner) {
    banner.classList.remove("hidden");
  }
}

function bindBannerActions() {
  const acceptBtn = document.getElementById("accept-all");
  const rejectBtn = document.getElementById("reject-all");
  const manageBtn = document.getElementById("manage-cookies");

  if (acceptBtn) {
    acceptBtn.addEventListener("click", () => {
      setConsent("accepted_all");
      hideBanner();
      loadAnalytics();
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener("click", () => {
      setConsent("rejected");
      hideBanner();
    });
  }

  if (manageBtn) {
    manageBtn.addEventListener("click", () => {
      localStorage.removeItem(CONSENT_KEY);
      showBanner();
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  bindBannerActions();

  const consent = getConsent();

  if (!consent) {
    showBanner();
    return;
  }

  hideBanner();
  loadAnalytics();
});
