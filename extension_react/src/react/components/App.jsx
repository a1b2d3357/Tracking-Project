import React, { useState } from 'react';
import * as Diff from 'diff';

const normalizeWhitespace = (code) => {
    return code.replace(/\s+/g, ' ').trim(); // Replace multiple spaces with a single space and trim
};

const App = () => {
    const [diffType, setDiffType] = useState('diffChars');

    const handleDiffTypeChange = (event) => {
        setDiffType(event.target.value);
    };


    const compareCode = async () => {
        const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
        const activeTab = tabs[0];

        const baseCode = await chrome.tabs.sendMessage(activeTab.id, "base");
        const newCode = await chrome.tabs.sendMessage(activeTab.id, "new");

        if (baseCode.success && newCode.success) {
            // Normalize whitespace
            const normalizedBaseCode = normalizeWhitespace(baseCode.code);
            const normalizedNewCode = normalizeWhitespace(newCode.code);

            let differences;
            switch (diffType) {
                case 'diffWords':
                    differences = Diff.diffWords(normalizedBaseCode, normalizedNewCode);
                    break;
                case 'diffSentences':
                    differences = Diff.diffSentences(normalizedBaseCode, normalizedNewCode);
                    break;
                case 'diffLines':
                    differences = Diff.diffLines(normalizedBaseCode, normalizedNewCode);
                    break;
                default:
                    differences = Diff.diffChars(normalizedBaseCode, normalizedNewCode);
                    break;
            }

            let baseDisplay = '';
            let newDisplay = '';
            let diffDisplay = '';

            differences.forEach(part => {
                const value = part.value.replace(/\n$/, '').replace(/;/g, ';<br><br>'); // Insert line break after every ';'
                const diffSpan = `<span class="${part.added ? 'added' : part.removed ? 'removed' : 'unchanged'}">${value}</span>`;

                if (part.added) {
                    newDisplay += diffSpan;
                    diffDisplay += `<span class="added">${value}</span>`;
                } else if (part.removed) {
                    baseDisplay += diffSpan;
                    diffDisplay += `<span class="removed">${value}</span>`;
                } else {
                    baseDisplay += diffSpan;
                    newDisplay += diffSpan;
                    diffDisplay += diffSpan;
                }
            });

            // Generate the HTML with an external CSS link
            const generatedHtmlContent = `
                <html>
                <head>
                    <title>Code Comparison</title>
                    <link rel="stylesheet" type="text/css" href="comparison.css"> <!-- Linking external CSS -->
                </head>
                <body>
                    <div class="container">
                        <h1>Code Comparison Report</h1>
                        <div class="diff-container">
                            <div class="code-column" id="base-column">
                                <h2>Base Code</h2>
                                <pre>${baseDisplay}</pre>
                            </div>
                            <div class="code-column" id="new-column">
                                <h2>Current Website Code</h2>
                                <pre>${newDisplay}</pre>
                            </div>
                            <div class="code-column" id="diff-column">
                                <h2>Differences Combined</h2>
                                <pre>${diffDisplay}</pre>
                            </div>
                        </div>
                    </div>
                </body>
                </html>
            `;

            // Open new window to display report
            const newWindow = window.open("", "_blank");
            newWindow.document.write(generatedHtmlContent);
            newWindow.document.close();
        }
    };

    return (
        <main class="app-main">
            <h1>Compare Pixel Code</h1>
            <div class="controls">
                <label htmlFor="diffType">Select Diff Type: </label>
                <select id="diffType" value={diffType} onChange={handleDiffTypeChange}>
                    <option value="diffChars">Character Differences</option>
                    <option value="diffWords">Word Differences</option>
                </select>
            </div>
            <button class="compare-button" onClick={compareCode}>Generate Report</button>
         
            <link rel="stylesheet" href="style.css" />
        </main>
    );
};

export default App;
