// Service Worker - Auto-unregister and bypass cache
self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(keys.map((k) => caches.delete(k)));
    }).then(() => self.registration.unregister())
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  // Always fetch directly from network, no caching
  e.respondWith(fetch(e.request));
});
