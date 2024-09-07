<h2>File Descriptions</h2>

<div style="font-family: Arial, sans-serif; line-height: 1.6;">
  <h3>pixelRecords.txt</h3>
  <p>Contains a list of all CDX records fetched from the Wayback CDX API for the pixel JS of RiteAid.</p>

  <h3>extension_react</h3>
    <p>An extension that can be used to visualize the difference between the _ base source code_ of meta pixel source and any website's meta pixel source code (if it contains one) </p>
    <p>Webpack bundler was used since the Content Security Policy does not allow loading any external libraries in content or background scripts of extensions. The code from the static and src folders is bundled into dist.</p>
    <p>Instructions to Install 
     <ol>
      <li>Download the extension_react folder locally</li>
      <li>In Google Chrome, open 'Manage Extensions' and turn on the Developer Mode from top-right</li>
      <li>Click load-unpacked on top left</li>
      <li>Select extension_react/dist/manifest.json</li>
    </ol>
    </p>
    <p>Instructions to Use
     <ol>
      <li>Download the extension_react folder locally</li>
      <li>Navigate to any website using meta-pixel, and open the extension</li>
      <li>Choose Difference in Words for a word-by-word difference, or Difference in Characters for a character-by-character difference as documented in the js-diff library</li>
      <li>Click generate report to visualize the differences</li>
      <li>The first column contains the base code, the second column contains the new code, and the third a combination of the two in. Any differences are highlighted in green (part added) or red(part deleted)</li>
    </ol>
     </p>

  <h3>Documentation</h3>
  <p>Load the pdf inside the folder to read the impacts of changing any configurations. All changes are stored as local HTML files in the folder; hence should be present in the folder of the pdf.</p>
  
 <h3>diff_calculator.ipynb</h3>
  <p>Contains the code used to generate
  <ol>
      <li>Differences between configurations in the documentation.</li>
      <li>Generate riteaid_code_comparison.csv, which presents the changes across pixel source code across time.</li>
    </ol>
   </p>
    
  <h3>riteaid_archived_versions</h3>
  <p>Contains all archives of pixel JS of all versions retrieved from <code>pixelRecords.txt</code>.</p>
  
  <h3>waybackDownloader.py</h3>
  <p>A script to:
    <ol>
      <li>Store all records of all versions of a website on Wayback into a provided file name.</li>
      <li>Download all those versions into the <code>archived_versions</code> folder.</li>
    </ol>
  </p>
  
 <h3>riteaid_code_comparison.csv</h3>
  <p>The CSV contains the changes in Riteaid pixel source code over time. It contains the following columns
    <ol>
      <li>Timestamp1</li>
      <li>Timestamp2</li>
      <li>Code 1</li>
      <li>Code 2</li>
      <li>Parts Added (from timestamp 1 to timestamp 2)</li>
      <li>Parts Deleted (from timestamp 1 to timestamp 2)</li>
    </ol>
  </p>

  <h3>progress.txt</h3>
  <p>Contains the checkpoint used in waybackDownloader.py for querying the API through paging.
  </p>

  
</div>

