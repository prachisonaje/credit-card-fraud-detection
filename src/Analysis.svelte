<script>
  // You can define your data here
  let tableData = [
    { column1: 'Logistic Regression', column2: '0.9956636997243729', column3: '0.6760556252819613', column4: '0.3970700350717687' },
    { column1: 'Decision Tree', column2: '0.998964203577886', column3: '0.8517770244055978', column4: '1.0' },
    { column1: 'Random Forest', column2: '0.999350432752234', column3: '0.9430364675282913', column4: ' 0.04' },
    { column1: 'XGBoost', column2: '0.9995435473394076', column3: '0.9745198538413308', column4: '8.65123511175625e-05' },
    { column1: 'AdaBoost ', column2: '0.9991573181650603', column3: '0.972568152527001', column4: '0.46770802029256053' },
    { column1: 'Local Outlier Factor', column2: '0.9965942207085425', column3: '', column4: '' }
   
  ];
</script>

<style>
  /* Styling for the table container */
  .table-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50vh; 
  }

  /* Styling for the table */
  table {
    border-collapse: collapse;
    border: 2px solid white;
    color: white;
  }
  th, td {
    border: 1px solid white;
    padding: 8px;
    text-align: left;
  }
  #header2 {
    font-size: 40px;
    font-weight: 400;
    padding: 1rem;
    text-align: center;
  }

</style>

<!-- Table container to center the table -->
<h1 id="header2">Analysis</h1>

<div class="table-container">
  <!-- Table structure -->
  <table>
    <thead>
      <tr>
        <th>Algorithm</th>
        <th>Accuarcy</th>
        <th>Roc_value</th>
        <th>Threshold</th>
      </tr>
    </thead>
    <tbody>
      {#each tableData as row}
        <tr>
          <td>{row.column1}</td>
          <td>{row.column2}</td>
          <td>{row.column3}</td>
          <td>{row.column4}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
