chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    // Return true to indicate that the response will be sent asynchronously
    console.log("received",msg);

    if (msg === "base") {
        fetch(chrome.runtime.getURL('base_code.txt'))
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(baseCode => {
                sendResponse({success: true, code: baseCode});
                console.log("Base code fetched:", baseCode);
            })
            .catch(error => {
                console.error("Failed to fetch base code:", error);
                sendResponse({ success:false,error: error.message });
            });

        // Return true to keep the message channel open for the asynchronous response
        return true;
    }

    if (msg === "new") {
        console.log("new msg");
        let scriptTags = document.getElementsByTagName('script');
        let url = "";
        console.log(scriptTags);

        // Loop through all script tags to find the one with the specific src
        for (let script of scriptTags) {
            if (script.src.includes('connect.facebook.net/signals/config/')) {
                url = script.src;
                break;  // Exit loop after finding the correct script
            }
        }

        console.log(url);

        if (url) {
            chrome.runtime.sendMessage({ action: "fetchFile", url: url }, (response) => {
                if (response.success) {
                    const newCode = response.code;
                    // console.log("Check: ",newCode)
                    let configuration = "fbq.registerPlugin" + newCode.split('fbq.registerPlugin')[1].split('/*')[0];
                    console.log("Configuration extracted");
                    sendResponse({success: true, code: configuration})
                } else {
                    console.error("Failed to fetch file:", response.error);
                    sendResponse({success:false,error:"issue"});
                }
            });
            
            // Return true to keep the message channel open for the asynchronous response
            return true;
        } else {
            // If URL is not found, send an error response
            sendResponse({ success: false, error: 'URL not found' });
            return true;
        }
    }
    return false
});