<!-- ViewData.svelte -->
<script>
  import { onMount } from "svelte";
  import Papa from "papaparse";

  let show_data = false;

  let csv = {
    data: [{}],
  };
  let predictions = {
    model1: [],
  };
  let headers = [];
  let models = [];

  onMount(async () => {
    show_data = !(Boolean(new URLSearchParams(window.location.search).get("predictions")));  // data = !predictions

    const id = new URLSearchParams(window.location.search).get("id");

    const file_data = await fetch("/api/data/" + id).then((res) => res.text());
    csv = Papa.parse(file_data, { header: true });
    console.log(csv);
    headers = Object.keys(csv.data[0]);

    predictions = await fetch("/api/predictions/" + id).then((res) =>
      res.json()
    );
    models = Object.keys(predictions);
  });
</script>

<main id="main">
  <!-- ======= Hero Section ======= -->
  <section id="homesection" style="padding: 0px 0px;">
    <!--__________________________________ header-box______________________________________________ -->
    <div id="container">
      <!-- <h1 id="header2">VIEW DATA</h1> -->
    </div>
    {#if show_data}
      <button
        type="button"
        on:click={() => (show_data = !show_data)}
        class="btn btn-primary"
        disabled={!show_data}>Hide Data</button>
    {/if}
    {#if !show_data}
      <button
        type="button"
        on:click={() => (show_data = !show_data)}
        class="btn btn-primary"
        disabled={show_data}>Show Data</button>
    {/if}

    <div class="container table-responsive">
      <table class="table table-striped table-bordered dt-responsive nowrap">
        <thead class="thead-light">
          <tr>
            <th>Sr. No.</th>
            {#if show_data}
              {#each headers as header}
                <th>{header}</th>
              {/each}
            {/if}
            {#each models as model}
              <th>{model}</th>
            {/each}
          </tr>
        </thead>
        <tbody>
          {#each csv.data as item, index}
            <tr>
              <td>{index + 1}</td>
              {#if show_data}
                {#each headers as header}
                  <td>{item[header]}</td>
                {/each}
              {/if}
              {#each models as model}
                <td>{predictions[model][index]}</td>
              {/each}
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </section>
</main>

<style>
  #header2 {
    font-size: 40px;
    font-weight: 400;
    padding: 1rem;
    text-align: center;
  }

  .container {
    padding: 30px;
  }

  .table {
    width: 100%;
    background-color: #313030;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .table-striped tbody tr:nth-of-type(odd) {
    background-color: #7e7d7dbd;
  }

  .table-bordered {
    border: 1px solid #dee2e6;
  }

  .table-bordered th,
  .table-bordered td {
    border: 1px solid #dee2e6;
  }

  .dt-responsive {
    overflow-x: auto;
  }

  .nowrap {
    white-space: nowrap;
  }

  .table-responsive {
    overflow-x: auto;
  }

  .btn-primary{
   color: white;
   border-color: white;
   margin-left: 50px;
   padding: 4px;
  }
  
</style>
