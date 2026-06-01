<script>
  import '@fontsource/montserrat'
  import '@fontsource/mulish'
  import {Link} from 'svelte-routing'
  </script>

<nav class="navbar"> 
	<img src="/images/logo.png" alt="logo" class="logo">
	<div class="nav-links">
		<Link class='a' to="/">Home</Link>
		<Link class='a' to="/dash">Dashboad</Link>
	</div>
</nav>
<style lang="postcss">
	.navbar {
    display: flex;
    align-items: center; /* Corrected from 'centre' to 'center' */
    background-color: black;
    color: white;
    padding: 25px 15px;
  }

  .logo {
    width: 150px;
    height: 50px;
    margin-right: 70px;
    margin-left: 40px;
  }

  .nav-links {
    /* display: flex; */
    align-items: center;
    font-size: 20px;
	/* color: white; */
    margin-right: 50px; /* Adjust this value as needed for spacing */
	text-transform:uppercase;
	word-spacing: 15px;
	
	
  
  }

</style>


