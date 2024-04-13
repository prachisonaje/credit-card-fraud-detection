<!-- Home.svelte -->
<script>
  import { Link } from 'svelte-routing';

  const routes = {
      UploadCreditData: "/Upload_credit_data",
      reports: "/Reports"
      // account_details: "/account_details",
  };
</script>

<main id="main">
  <!-- ======= Hero Section ======= -->
  <section id="homesection">
      <!--__________________________________ header-box______________________________________________ -->
      <div id="header-container">
          <h1 id="header2">USER DASHBOARD</h1>
      </div>
      <!-- ___________________________________main-division____________________________________________ -->
      <div id="main-container">
          <div class="inner-box">
              <Link to={routes.UploadCreditData}>
                  <svg viewBox="0 0 80 80" width="200px" height="200px">
                      <circle class="circle" cx="40" cy="40" r="38"/>
                      <text x="40" y="35" font-size="10px" fill="#FFFFFF" text-anchor="middle">Upload</text>
                      <text x="40" y="47" font-size="10px" fill="#FFFFFF" text-anchor="middle">Files</text>
                  </svg>
              </Link>
          </div>

          <div class="inner-box">
              <Link to={routes.reports}>
                  <svg viewBox="0 0 80 80" width="200px" height="200px">
                      <circle class="circle" cx="40" cy="40" r="38"/>
                      <text x="40" y="35" font-size="10px" fill="#FFFFFF" text-anchor="middle">Files</text>
                      <text x="40" y="47" font-size="10px" fill="#FFFFFF" text-anchor="middle">Report</text>
                  </svg>
              </Link>
          </div>
      </div>
  </section><!-- End Hero -->
</main>

<style lang="postcss">
  #homesection {
      padding: 0px;
  }

  #main-container {
      display: flex;
      justify-content: space-around;
  }
</style>
