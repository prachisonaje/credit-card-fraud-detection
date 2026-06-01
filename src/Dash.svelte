<!-- Home.svelte -->
<script>
  import { Link } from 'svelte-routing';

  const routes = {
      UploadCreditData: "/upload_credit_data",
      reports: "/reports"
      // account_details: "/account_details",
  };
</script>

<main id="main" style="height: 100vh;">
    <!-- ======= Hero Section ======= -->
    <section id="homesection">
        <!--__________________________________ header-box______________________________________________ -->
        <div id="header-container">
            <h1>USER DASHBOARD</h1>
        </div>
        <!-- ___________________________________main-division____________________________________________ -->
        <div id="main-container">
            <div class="inner-box">
                <Link to={routes.UploadCreditData}>
                    <svg viewBox="0 0 80 80" width="200px" height="200px">
                        <rect class="square" x="2" y="12" width="76" height="76" fill="rgb(0, 100, 200)"/>
                        <text x="40" y="45" font-size="12px" fill="#FFFFFF" text-anchor="middle">Upload</text>
                        <text x="40" y="62" font-size="12px" fill="#FFFFFF" text-anchor="middle">Files</text>
                    </svg>
                </Link>
            </div>
        
            <div class="inner-box">
                <Link to={routes.reports}>
                    <svg viewBox="0 0 80 80" width="200px" height="200px">
                        <rect class="square" x="2" y="12" width="76" height="76" fill="rgb(0, 100, 200)"/>
                        <text x="40" y="45" font-size="12px" fill="#FFFFFF" text-anchor="middle">Report</text>
                        <text x="40" y="62" font-size="12px" fill="#FFFFFF" text-anchor="middle">Files</text>
                    </svg>
                </Link>
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
    #main{
     background-color: black;
    overflow: hidden;

    }
  #homesection {
      padding: 0px;
      
  }

  #main-container {
      display: flex;
      justify-content: space-around;

     
  }
  #header-container h1{
    font-size: 40px;
    text-align: center;
    color: white;
  }
  .footer .container2{
    /* padding: 20px; */
    text-align: center;
    bottom: 0;
    margin-top: 250px;
	color: white; 
    padding-top: 70px;
	/* margin-bottom: -50px; */
    background-size: cover; /* Fit background to cover the container */
		
  }
</style>
