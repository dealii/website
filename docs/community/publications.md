Publications using deal.II
==========================

!!! note
    This page is an attempt at keeping track of all publications
    that use deal.II. Keeping it up to date is good
    for our users (who can see what others have already done),
    but is also important for keeping our funding agencies
    apprised how widely used deal.II actually is.

    If you have published anything,
    including Diploma, Masters or PhD theses, please
    [cite the relevant deal.II papers](citing.md) and
    <a href="https://github.com/dealii/publication-list/blob/master/README.md">let
    us know about your publication</a>!

<div>
      <div class="well" align="center">
	  <div id="plot" style="width:650px; height:400px"></div>
	  <div id="n_publications"></div>
	</div>
</div>

{!output.html!}

  <!-- Some JQuery needs to come after the body -->
  <script src="js/jquery.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/accordion.js"></script>

  <script type="text/javascript" src="https://www.google.com/jsapi"></script>

  <script type="text/javascript">
    var first_year = 1998;
    var last_year  = 2027;

    // set up the table's structure
    var table = [
    ['Year', 'Publications', { role: 'style' }],
    ['1998',  0, 'blue'],
    ['1999',  0, 'blue'],
    ['2000',  0, 'blue'],
    ['2001',  0, 'blue'],
    ['2002',  0, 'blue'],
    ['2003',  0, 'blue'],
    ['2004',  0, 'blue'],
    ['2005',  0, 'blue'],
    ['2006',  0, 'blue'],
    ['2007',  0, 'blue'],
    ['2008',  0, 'blue'],
    ['2009',  0, 'blue'],
    ['2010',  0, 'blue'],
    ['2011',  0, 'blue'],
    ['2012',  0, 'blue'],
    ['2013',  0, 'blue'],
    ['2014',  0, 'blue'],
    ['2015',  0, 'blue'],
    ['2016',  0, 'blue'],
    ['2017',  0, 'blue'],
    ['2018',  0, 'blue'],
    ['2019',  0, 'blue'],
    ['2020',  0, 'blue'],
    ['2021',  0, 'blue'],
    ['2022',  0, 'blue'],
    ['2023',  0, 'blue'],
    ['2024',  0, 'blue'],
    ['2025',  0, 'silver'],
    ['2026',  0, 'silver'],
    ['2027',  0, 'silver']
    ];

    // now get the number of publications per year from the
    // lists we have in the HTML above

    var tbl = document.getElementById("qs_table");
    var allrows = tbl.getElementsByTagName("tr");
    var curyear=NaN;
    for(i = 0;i < allrows.length; i++)
    {
	if (allrows[i].className=="show")
	{
	  curyear=parseInt(allrows[i].innerText,10);
	  //console.log("parsed '" + allrows[i].innerText + "' as " + curyear);
	}
	else if (allrows[i].className=="entry")
	{
	  if (isNaN(curyear))
	  {
	    console.log("broken entry " + allrows[i].innerText);
	  }
	  else
	  {
	    var index = curyear-first_year+1;
	    if (index < 0 || index > table.length-1)
	    {
	      console.log("invalid year " + curyear + " for  entry " + allrows[i]);
	    }
	    else
	    {
	      table[curyear-first_year+1][1] += 1;
	    }
	  }
	}
	else if (allrows[i].className.indexOf("bibtex")!=-1)
	{
	  // skip bibtex
	}
	else if (allrows[i].className.indexOf("abstract")!=-1)
	{
	  // skip abstract
	}
	else
	    console.log("unknown: " + allrows[i].className);
    }

    var max_per_year = 0;
    for (i=1; i<table.length; ++i)
      if (table[i][1] > max_per_year)
        max_per_year = table[i][1];

    google.load("visualization", "1", {packages:["corechart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
    var data = google.visualization.arrayToDataTable(table);

    var options = {
      width: 650,
      height: 400,
      hAxis: {title: 'Year',
              showTextEvery: '2',
              textStyle: {fontSize:'9'}},
      vAxis: {minValue: 0,
              viewWindow: { max : max_per_year}   },
      legend: {position: 'none'}
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('plot'));

    chart.draw(data, options);
    }

    var n_publications=0;
    for (var i=first_year; i<=last_year; ++i)
      n_publications += table[i-first_year+1][1];
    document.getElementById("n_publications").innerHTML =
        "Known publications using deal.II. Total: <b>" + n_publications +
        "</b>. (Gray bars: Incomplete data.)";
</script>
  
