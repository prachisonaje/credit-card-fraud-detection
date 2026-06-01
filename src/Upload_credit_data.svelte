<!-- UploadCreditData.svelte -->
<script>
  import { Link } from 'svelte-routing';
  import { onMount } from 'svelte';
  import Reports from './Reports.svelte';

  const routes = {
    UploadCreditData: "/upload_credit_data",
    reports: "/reports"
  };

  let fileInput;

  async function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    const file = fileInput.files[0]; // Get the selected file

    if (!file) {
      alert('Please choose a file to upload.');
      return;
    }

    const formData = new FormData(event.target);
    formData.append('file', file);

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData
      });
      const upload_details = await response.json();
      console.log('Upload successful:', upload_details);
      alert('File uploaded successfully!');
      redirectToReports(upload_details.id); // Redirect to reports page
    }
    catch (error) {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading the file.');
    }
  }

  function redirectToReports(id) {
    window.location.href = routes.reports+'?uploaded_file_id='+id;
  }
</script>

<main id="main" style="height: 100vh;">

  <!-- ======= Hero Section ======= -->
  <section id="homesection" style="height: 100%;">
      <!--__________________________________ header-box______________________________________________ -->
      <div id="header-container">
          <h1 id="header2">Upload Credit Data Files</h1>
      </div>
      <!-- ___________________________________main-division____________________________________________ -->
      <div id="upload-container">
        
          <div class="upload">
              <form class="upload-form" on:submit={handleSubmit} enctype="multipart/form-data">
                  <!-- CSRF token -->
                  <!-- svelte-ignore missing-declaration -->
                  <!-- <input type="hidden" name="csrf_token" value="{{ csrf_token }}"> -->
                  <label for="filename">File Name:</label><br>
                  <input type="text" name="filename" id="filename"><br>
                  <!-- svelte-ignore a11y-label-has-associated-control -->
                  <label>Upload Credit Card Dataset File</label><br>
                  <input id="file" type="file" bind:this={fileInput} accept=".csv, .xlsx, .xls"><br>
                  <label for="description">Description of the File:</label><br>
                  <textarea placeholder="Description" name="description" id="description"></textarea><br>
                  <button id="btn" type="submit">SUBMIT</button>
              </form>
          </div>
      </div>
  </section><!-- End Hero -->

  <footer class="footer">
    <div class="container2">
      <p>© 2024 FraudNix. All rights reserved.</p>
      <p>
        Follow us on
        <a href="https://twitter.com/yourprofile">Twitter</a>,
        <a href="https://facebook.com/yourprofile">Facebook</a>, and
        <a href="https://instagram.com/yourprofile">Instagram</a>.
      </p>
    </div>
  </footer>
</main>

<style lang="postcss">
  #homesection {
      padding: 0px;
      background-color: black;
  }

  #header-container {
      margin-bottom: 20px;
  }

  #header2 {
      font-size: 40px;
      text-align: center;
      color: #fff;

  }

  #upload-container {
      margin-bottom: 10px;
      color:rgb(0, 100, 200);
      text-align: center;
  }

  /* #upload-header {
      font-size: 18px;
  } */
  .upload-form{
    text-align: center;
  }
  .upload {
      padding: 0px;
      text-align: left;
  }

  .upload-form label {
      font-weight: bold;
  }

  .upload-form input[type="text"],
  .upload-form textarea {
      margin-bottom: 8px;
      padding: 10px;
      color: black;
  }

  #btn {
      background-color: #007bff;
      color: #fff;
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
  }
  .footer {
  text-align: center;
	color: white; 
	margin-bottom: 10px;
  background-color: black;		
  }
</style>
