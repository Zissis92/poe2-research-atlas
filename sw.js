const CACHE='poe2-atlas-v0.5';
const FILES=['./','./index.html','./manifest.webmanifest'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES))));
self.addEventListener('activate',e=>e.waitUntil(
  caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k))))
));
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(u.hostname==='raw.githubusercontent.com') return;
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));
});
