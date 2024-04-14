<script>
  import { onMount } from "svelte";

  let files = [];

  onMount(async () => {
    const response = await fetch("/api/files");
    files = await response.json();
  });

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
<div class="table">
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
        <td>{file.filename}</td>
        <td>{file.description}</td>
        <td>
          <a href="/view-data?id={file.id}"><button class="view-data">View Data</button></a>
          <button class="delete" on:click={() => handleDelete(file)}>Delete</button>
          <a href="/view-data?id={file.id}&predictions=true"><button class="prediction">Prediction</button></a>
          <button class="analysis" on:click={() => handleAnalysis(file)}>Analysis</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>
</div>
<style lang="postcss">

  h1 {
    font-size: x-large;
    padding: 1em;
  }

  div.table {
    display: flex;
    flex-grow: 1;
    padding: 1em;
  }

  table {
    border-collapse: collapse;
    width: 100%;
  }

  th,
  td {
    border: 2px solid rgb(199, 61, 61);
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #939090;
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
