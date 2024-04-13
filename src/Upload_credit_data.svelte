<!-- UploadCreditData.svelte -->
<script>
  import { Link } from 'svelte-routing';
  import { onMount } from 'svelte';
  import Reports from './Reports.svelte';

  const routes = {
    UploadCreditData: "/Upload_credit_data",
    reports: "/Reports"
  };

  let fileInput;

  async function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    const file = fileInput.files[0]; // Get the selected file

    if (!file) {
      alert('Please choose a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData
      });
      const uploded_file_ids_array = await response.json();
      console.log('Upload successful:', uploded_file_ids_array);
      alert('File uploaded successfully!');
      redirectToReports(uploded_file_ids_array); // Redirect to reports page
    } 
    catch (error) {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading the file.');
    }
  }

  function redirectToReports(ids) {
    window.location.href = routes.reports+'?uploaded_file_ids='+ids.join('+');
  }
</script>

<main id="main">

  <!-- ======= Hero Section ======= -->
  <section id="homesection" style="padding: 0px 0px;">
      <!--__________________________________ header-box______________________________________________ -->
      <div id="header-container" style="margin-bottom: 20px;">
          <h1 id="header2" style="font-size: 24px;">Upload Credit Data Files</h1>
      </div>
      <!-- ___________________________________main-division____________________________________________ -->
      <div id="upload-container">
          <div id="upload-header-container" style="margin-bottom: 10px;">
              <h3 id="upload-header" style="font-size: 18px;">UPLOAD CREDIT CARD DATASET</h3>
          </div>
          <div class="upload">
              <form class="upload-form" on:submit={handleSubmit} enctype="multipart/form-data">
                  <!-- CSRF token -->
                  <!-- svelte-ignore missing-declaration -->
                  <!-- <input type="hidden" name="csrf_token" value="{{ csrf_token }}"> -->
                  <label for="filename" style="font-weight: bold;">File Name</label><br>
                  <input type="text" name="data_file_name" id="filename" style="margin-bottom: 10px; padding: 5px;" placeholder="File Name"><br>
                  <!-- svelte-ignore a11y-label-has-associated-control -->
                  <label style="font-weight: bold;">Upload Credit Card Dataset File</label><br>
                  <input id="file" type="file" bind:this={fileInput} accept=".csv, .xlsx, .xls" style="margin-bottom: 10px;"><br>
                  <label for="description" style="font-weight: bold;">Description of the File</label><br>
                  <textarea placeholder="Description" name="description" id="description" style="margin-bottom: 10px; padding: 5px;"></textarea><br>
                  <input on:click={redirectToReports} id="btn" type="submit" value="SUBMIT" style="background-color: #007bff; color: #fff; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer;">
              </form>
          </div>
      </div>
  </section><!-- End Hero -->

</main>

<style lang="postcss">
  /* Your CSS styles go here */
  /* You can use inline styles or import CSS files directly */
</style>
