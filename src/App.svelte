<script>
	import Navbar from './Navbar.svelte';
	import Home from './Home.svelte';
	import Dash from './Dash.svelte';
	import Reports from './Reports.svelte';
	import UploadCreditData from './Upload_credit_data.svelte';
	import '@fontsource/montserrat';
	import '@fontsource/mulish';
	import { Router, Route } from 'svelte-routing';
</script>

<Router>
	<Navbar /> 
	<Route path="/" component={Home} />
	<Route path="/dash" component={Dash} />
	<Route path="/reports" component={Reports} /> 
	<Route path="/Upload_credit_data" component={UploadCreditData}/> 
</Router>


<style lang="postcss">
	/* main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
		
	}

	

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	} */
</style>