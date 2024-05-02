const registerServiceWorker = async () => {
    // feature detection: check if browser supports workers:
    if ('serviceWorker' in navigator) {
      try {
        const registration = await navigator.serviceWorker.register(
          'sw.js',
          {
            // specify the subset of your content that you 
            // want the service worker to control, a value of '/' will mean
            // al content under the app's origin.
            scope: '/',
          }
        );
        if (registration.installing) {
          console.log('Service worker installing');
        } else if (registration.waiting) {
          console.log('Service worker installed');
        } else if (registration.active) {
          console.log('Service worker active');
        }
      } catch (error) {
        console.error(`Registration failed with ${error}`);
      }
    }
  };
  
  registerServiceWorker();
  