(()=>{"use strict";console.log("hi again"),chrome.runtime.onMessage.addListener((function(e,n,t){if(console.log("check request: ",e),"fetchFile"===e.action)return fetch(e.url).then((function(e){return e.text()})).then((function(e){return t({success:!0,code:e})})).catch((function(e){return t({success:!1,error:"error"})})),!0}))})();