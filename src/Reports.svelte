<script>
    let file_ids = new URLSearchParams(window.location.search).get('uploaded_file_ids');
    let ids = file_ids.split('+');
    let files = ids.map(id => ({ id, name: `File ${id}`, description: `Description for File ${id}` }));
  
    function handleViewData(file) {
        console.log(`View data for file: ${file.name}`);
        // Add your logic for viewing data
    }
  
    function handleDelete(file) {
        console.log(`Delete file: ${file.name}`);
        // Add your logic for deleting file
    }
  
    function handlePrediction(file) {
        console.log(`Prediction for file: ${file.name}`);
        // Add your logic for prediction
    }
  
    function handleAnalysis(file) {
        console.log(`Analysis for file: ${file.name}`);
        // Add your logic for analysis
    }
  
  </script>
  
  
  <h1>Uploaded Files List</h1>
  <table border="1">
    <thead>
        <tr>
            <th>File Name</th>
            <th>Description</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        {#each files as file}
        <tr>
            <td>{file.name}</td>
            <td>{file.description}</td>
            <td>
                <button class="view-data" on:click={() => handleViewData(file)}>View Data</button>
                <button class="delete" on:click={() => handleDelete(file)}>Delete</button>
                <button class="prediction" on:click={() => handlePrediction(file)}>Prediction</button>
                <button class="analysis" on:click={() => handleAnalysis(file)}>Analysis</button>
              
            </td>
        </tr>
        {/each}
    </tbody>
  </table>
  
  <style lang="postcss">
    table {
      border-collapse: collapse;
      width: 100%;
    }
  
    th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: left;
    }
  
    th {
      background-color: #f2f2f2;
    }
  
    button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  
    button:hover {
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
    }
  
    .view-data {
      background-color: #007bff;
      color: #fff;
    }
  
    .delete {
      background-color: #6c757d;
      color: #fff;
    }
  
    .prediction {
      background-color: #28a745;
      color: #fff;
    }
  
    .analysis {
      background-color: #17a2b8;
      color: #fff;
    }
  </style>
  