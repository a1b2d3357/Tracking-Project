# Project Documentation

## Overview

This project involves tools and scripts designed for analyzing changes in Meta Pixel source code across time, focusing on RiteAid's implementation. It includes an extension for visualizing differences in Meta Pixel code, archives of pixel source code, and tools for fetching and comparing archived versions from the Wayback Machine.

## File Descriptions

### `pixelRecords.txt`
Contains a list of all CDX records fetched from the Wayback CDX API for the RiteAid Meta Pixel JavaScript file.

### `extension_react`
A Chrome extension that visualizes differences between the **base Meta Pixel source code** and the Meta Pixel source code of any website (if present).

- **Bundling**: Uses Webpack for bundling, as Chrome's Content Security Policy restricts loading external libraries in content or background scripts. The `src` and `static` directories are bundled into the `dist` folder.
  
#### Installation Instructions
1. Download the `extension_react` folder locally.
2. In Google Chrome, open **Manage Extensions** and enable **Developer Mode**.
3. Click **Load unpacked** in the top-left corner.
4. Select `extension_react/dist/manifest.json`.

#### Usage Instructions
1. Navigate to a website using Meta Pixel and open the extension.
2. Choose between "Difference in Words" or "Difference in Characters" for comparison, using the `js-diff` library.
3. Click **Generate Report** to visualize differences.
4. The comparison includes three columns:
   - **Base code**: The original source code.
   - **New code**: The current website's Meta Pixel code.
   - **Combined view**: Differences are highlighted—additions in green, deletions in red.

### `Documentation`
The `Documentation` folder contains a PDF explaining the impacts of changing configuration settings. Each change is stored as a local HTML file and must be present alongside the PDF for complete documentation.

### `diff_calculator.ipynb`
This Jupyter notebook is used to:
1. Compute differences between configurations documented in the PDF.
2. Generate `riteaid_code_comparison.csv`, which tracks changes in the Meta Pixel source code over time.

### `riteaid_archived_versions`
This folder contains all archived versions of the Meta Pixel JavaScript file, retrieved using the CDX records stored in `pixelRecords.txt`.

### `waybackDownloader.py`
A Python script designed to:
1. Fetch and store all version records of a website from the Wayback Machine into a specified file.
2. Download the archived versions into the `archived_versions` folder.

### `riteaid_code_comparison.csv`
This CSV file details changes in the RiteAid Meta Pixel source code over time. The columns are:
1. **Timestamp1**: First version's timestamp.
2. **Timestamp2**: Second version's timestamp.
3. **Code 1**: Meta Pixel code from Timestamp1.
4. **Code 2**: Meta Pixel code from Timestamp2.
5. **Parts Added**: Code added between Timestamp1 and Timestamp2.
6. **Parts Deleted**: Code removed between Timestamp1 and Timestamp2.

### `progress.txt`
This file stores the last successful checkpoint for `waybackDownloader.py`, allowing the script to continue API queries from where it last left off when fetching paginated data.

