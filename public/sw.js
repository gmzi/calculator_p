const staticCacheName = 'calpy-cache';

// Function to install resources in cache
async function cacheResources(resources) {
    const cache = await caches.open(staticCacheName);
    await cache.addAll(resources);
}

// Install event listener: Cache resources
self.addEventListener('install', async (event) => {
    console.log('fdsfdsfsdfjsdfjisdjfisdjfoisdjfiosdjfiojdsfiojdsiofjdsfioj')
    event.waitUntil(cacheResources([
        '/',
        // './public/pyodide/pyodide-lock.json',
        // './public/pyodide/pyodide.asm.js',
        // './public/pyodide/pyodide.asm.wasm',
        // './public/pyodide/pyodide.d.ts',
        // './public/pyodide/pyodide.js',
        // './public/pyodide/pyodide.js.map',
        // './public/pyodide/pyodide.mjs',
        // './public/pyodide/pyodide.mjs.map',
        // './public/pyodide/python_stdlib.zip',
        // './public/pyscript/codemirror-btSUM_0g.js',
        // './public/pyscript/codemirror-btSUM_0g.js.map',
        // './public/pyscript/codemirror_commands-MgxtVkrD.js',
        // './public/pyscript/codemirror_commands-MgxtVkrD.js.map',
        // './public/pyscript/codemirror_lang-python-luVWQrEE.js',
        // './public/pyscript/codemirror_lang-python-luVWQrEE.js.map',
        // './public/pyscript/codemirror_language-_XiX6II0.js',
        // './public/pyscript/codemirror_language-_XiX6II0.js.map',
        // './public/pyscript/codemirror_state-BKbyfKsm.js',
        // './public/pyscript/codemirror_state-BKbyfKsm.js.map',
        // './public/pyscript/codemirror_view-C0PMO2z_.js',
        // './public/pyscript/codemirror_view-C0PMO2z_.js.map',
        // './public/pyscript/core-CRnTod_F.js',
        // './public/pyscript/core-CRnTod_F.js.map',
        // './public/pyscript/core.css',
        // './public/pyscript/core.js',
        // './public/pyscript/core.js.map',
        // './public/pyscript/deprecations-manager-Cu0y_cMh.js',
        // './public/pyscript/deprecations-manager-Cu0y_cMh.js.map',
        // './public/pyscript/error-CS6gq7CV.js',
        // './public/pyscript/error-CS6gq7CV.js.map',
        // './public/pyscript/index-CTWZX_TW.js',
        // './public/pyscript/index-CTWZX_TW.js.map',
        // './public/pyscript/py-editor-CyMAlOCD.js',
        // './public/pyscript/py-editor-CyMAlOCD.js.map',
        // './public/pyscript/py-terminal-lQnGv6an.js',
        // './public/pyscript/py-terminal-lQnGv6an.js.map',
        // './public/pyscript/toml-CvAfdf9_.js',
        // './public/pyscript/toml-CvAfdf9_.js.map',
        // './public/pyscript/toml-DiUM0_qs.js',
        // './public/pyscript/toml-DiUM0_qs.js.map',
        // './public/pyscript/xterm-DqawCVsv.js',
        // './public/pyscript/xterm-DqawCVsv.js.map',
        // './public/pyscript/xterm-readline-D247p8vq.js',
        // './public/pyscript/xterm-readline-D247p8vq.js.map',
        // './public/pyscript/xterm.css',
        // './public/pyscript/xterm_addon-fit--gyF3PcZ.js',
        // './public/pyscript/xterm_addon-fit--gyF3PcZ.js.map',
        // './public/pyscript/xterm_addon-web-links-Cnej-nJ6.js',
        // './public/pyscript/xterm_addon-web-links-Cnej-nJ6.js.map',
        // './public/pyscript/zip-BVYJ4_a2.js',
        // './public/pyscript/zip-BVYJ4_a2.js.map',

        // './public/methods/compound_interest.py',
        // './public/methods/helpers.py',
        // './public/methods/html_parser.py',
        // './public/methods/treasury_bills.py',
        // './public/pages/comp-interest.html',
        // './public/pages/maturity.html',
        // './public/pages/percentage.html',
        // './public/pages/playground.html',
        // './public/scripts/dropdown.js',
        // './public/scripts/fetchResults.js',
        // './public/scripts/formatCurrencyInput.js',
        // './public/scripts/navigation.js',

        // './public/config.json',
        // './public/favicon.ico',
        // './public/index.html',
        // './public/styles.css',
        // './public/test.html',
        // './package-lock.json',
        // './package.json',
        './index.html',
        './test.html',
        './styles.css',
        './app.js',
        './manifest.json',
        './assets/icons/icon-120.png',
        './config.json',
        './pages/comp-interest.html',
        './pages/maturity.html',
        './pages/percentage.html',
        './pages/playground.html',
        './methods/compound_interest.py',
        './methods/helpers.py',
        './methods/html_parser.py',
        './methods/treasury_bills.py',
        './scripts/dropdown.js',
        './scripts/fetchResults.js',
        './scripts/formatCurrencyInput.js',
        './scripts/navigation.js',
        './pyscript/codemirror-btSUM_0g.js',
        './pyscript/codemirror-btSUM_0g.js.map',
        './pyscript/codemirror_commands-MgxtVkrD.js',
        './pyscript/codemirror_commands-MgxtVkrD.js.map',
        './pyscript/codemirror_lang-python-luVWQrEE.js',
        './pyscript/codemirror_lang-python-luVWQrEE.js.map',
        './pyscript/codemirror_language-_XiX6II0.js',
        './pyscript/codemirror_language-_XiX6II0.js.map',
        './pyscript/codemirror_state-BKbyfKsm.js',
        './pyscript/codemirror_state-BKbyfKsm.js.map',
        './pyscript/codemirror_view-C0PMO2z_.js',
        './pyscript/codemirror_view-C0PMO2z_.js.map',
        './pyscript/core-CRnTod_F.js',
        './pyscript/core-CRnTod_F.js.map',
        './pyscript/core.css',
        './pyscript/core.js',
        './pyscript/core.js.map',
        './pyscript/deprecations-manager-Cu0y_cMh.js',
        './pyscript/deprecations-manager-Cu0y_cMh.js.map',
        './pyscript/error-CS6gq7CV.js',
        './pyscript/error-CS6gq7CV.js.map',
        './pyscript/index-CTWZX_TW.js',
        './pyscript/index-CTWZX_TW.js.map',
        './pyscript/py-editor-CyMAlOCD.js',
        './pyscript/py-editor-CyMAlOCD.js.map',
        './pyscript/py-terminal-lQnGv6an.js',
        './pyscript/py-terminal-lQnGv6an.js.map',
        './pyscript/toml-CvAfdf9_.js',
        './pyscript/toml-CvAfdf9_.js.map',
        './pyscript/toml-DiUM0_qs.js',
        './pyscript/toml-DiUM0_qs.js.map',
        './pyscript/xterm-DqawCVsv.js',
        './pyscript/xterm-DqawCVsv.js.map',
        './pyscript/xterm-readline-D247p8vq.js',
        './pyscript/xterm-readline-D247p8vq.js.map',
        './pyscript/xterm.css',
        './pyscript/xterm_addon-fit--gyF3PcZ.js',
        './pyscript/xterm_addon-fit--gyF3PcZ.js.map',
        './pyscript/xterm_addon-web-links-Cnej-nJ6.js',
        './pyscript/xterm_addon-web-links-Cnej-nJ6.js.map',
        './pyscript/zip-BVYJ4_a2.js',
        './pyscript/zip-BVYJ4_a2.js.map',
    ]));
});

// Activate event listener: Clean up old caches
self.addEventListener('activate', async (event) => {
    const currentCacheNames = [staticCacheName];

    event.waitUntil(
        caches.keys().then(async (cacheNames) => {
            const cachesToDelete = cacheNames.filter((cacheName) => !currentCacheNames.includes(cacheName));
            for (const cacheToDelete of cachesToDelete) {
                await caches.delete(cacheToDelete);
            }
        })
    );
});

// Fetch event listener: Serve from cache if offline
// self.addEventListener('fetch', (event) => {
//     event.respondWith(async function () {
//         const cachedResponse = await caches.match(event.request);

//         if (cachedResponse) {
//             return cachedResponse;
//         }

//         // Fallback to network if not in cache and online
//         if (navigator.onLine) {
//             return fetch(event.request);
//         }

//         // Fallback to offline page if offline and not in cache
//         return new Response('<h1>Content not available offline</h1>', {
//             headers: {
//                 'Content-Type': 'text/html'
//             }
//         });
//     }());
// });
