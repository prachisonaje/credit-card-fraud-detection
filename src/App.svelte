<script>
	import Navbar from './Navbar.svelte';
	import Home from './Home.svelte';
	import Dash from './Dash.svelte';
	import Reports from './Reports.svelte';
	import UploadCreditData from './Upload_credit_data.svelte';
	import View_data from './View_data.svelte';
	import Analysis from './Analysis.svelte';
	import '@fontsource/montserrat';
	import '@fontsource/mulish';
	import { Router, Route } from 'svelte-routing';
</script>

<Router>
	<Navbar /> 
	<Route path="/" component={Home} />
	<Route path="/dash" component={Dash} />
	<Route path="/reports" component={Reports} /> 
	<Route path="/upload_credit_data" component={UploadCreditData}/>
	<Route path="/view-data" component={View_data} />
	<Route path="/analysis" component={Analysis}/>
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