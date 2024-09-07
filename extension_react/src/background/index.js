console.log("hi again")
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("check request: ",request)
    if (request.action === "fetchFile") {
        fetch(request.url)
            .then(response => response.text())
            .then(data => sendResponse({ success: true, code: data }))
            .catch(error => sendResponse({ success: false, error: "error" }));
        return true; // Indicates that the response is asynchronous
    }
});