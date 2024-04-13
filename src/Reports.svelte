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
              <button on:click={() => handleViewData(file)}>View Data</button>
              <button on:click={() => handleDelete(file)}>Delete</button>
              <button on:click={() => handlePrediction(file)}>Prediction</button>
              <button on:click={() => handleAnalysis(file)}>Analysis</button>
            
          </td>
      </tr>
      {/each}
  </tbody>
</table>

<!-- <style lang="postcss">

  .container {
      background-color: black; /* Set background color to black */
      color: white; /* Set text color to white */
      padding-top: 10px;
      background-size: cover; /* Fit background to cover the container */
  height:1000px;
  }

  .hero-section {
      display: flex;
      justify-content: space-between; /* Aligns items to each side */
      align-items: center; /* Vertically centers items */
      text-align: left; /* Ensure text alignment is left, if preferred */
      padding: 20px;
      margin: 0 auto; /* Center the section horizontally */
      max-width: 1200px; /* Limit the width of the section */
  }
.hero-section {
      display: flex;
      justify-content: space-between; /* Aligns items to each side */
      /* align-items: center;  */
      text-align: center; /* Ensure text alignment is left, if preferred */
      padding: 20px;
      margin-top:50px; /* Center the section horizontally */
      max-width: 1200px; /* Limit the width of the section */
  
  }

  .text-content {
      max-width: 50%; /* Adjust based on your preference */
      padding: 0 20px; /* Adjust padding for spacing */
  }

  .image-container {
      width: 50%; /* Adjust based on your preference */
      padding: 0 20px; /* Adjust padding for spacing */
  
  }
.image-container1 {
      width: 40%; /* Adjust based on your preference */
      padding: 0 20px; /* Adjust padding for spacing */
  
  }


  .home-image {
      width: 110%; /* Increase the size of the image */
  height:400px;
  }


.text1{
  text-align: center;
}



.footer {
  /* padding: 20px; */
  background-color: black;
  text-align: center;
  bottom: 0;
  /* width: 100%; */
color: white; /* Set text color to white */
      padding-top: 70px;
  margin-bottom: 50px;
      background-size: cover; /* Fit background to cover the container */
  /* height:650px; */
}


</style> -->