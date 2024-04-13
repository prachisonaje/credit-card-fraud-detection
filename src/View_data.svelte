<!-- ViewData.svelte -->
<script>
    import { onMount } from 'svelte';
    import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css';
    import 'datatables.net-buttons-bs4/css/buttons.bootstrap4.min.css';
    import 'datatables.net-bs4';
    import 'datatables.net-buttons-bs4';
  
    let columns = [
      { title: "Sr No." },
      // Add other hardcoded columns if any.
      //...
    ];
  
    onMount(() => {
      const table = $('#example').DataTable({
        serverSide: true,
        ajax: {
          url: "{% url 'retrieve_data_by_id' id %}", // Adjust this if necessary
          type: 'GET'
        },
        columns: columns,
        dom: 'Bfrtip',
        buttons: [
          {
            extend: 'copy',
            text: 'Copy'
          },
          {
            extend: 'excel',
            text: 'Download excel'
          },
        ],
        initComplete: function () {
          const btns = document.querySelectorAll('.dt-button');
          btns.forEach(btn => {
            btn.classList.add('btn', 'btn-primary', 'btn-sm');
            btn.classList.remove('dt-button');
          });
        },
        pageLength: 100,
        lengthMenu: [[100, 250, 500, 1000], [100, 250, 500, 1000]]
      });
    });
  </script>
  
  <main id="main">
    <!-- ======= Hero Section ======= -->
    <section id="homesection" style="padding: 0px 0px;">
      <!--__________________________________ header-box______________________________________________ -->
      <div id="header-container">
        <h1 id="header2">VIEW DATA</h1>
      </div>
      <div class="container" style="width: 90%; margin-top: 13px;">
        <table id="example"
               class="table table-striped table-bordered dt-responsive nowrap table-wrapper-scroll-y my-custom-scrollbar"
               style="width:100%;">
        </table>
      </div>
    </section><!-- End Hero -->
  </main>
  