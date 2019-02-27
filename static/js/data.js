queue()
    .defer(d3.json, "/get_data")
    .await(makeGraphs);

function makeGraphs(error, recipeData) {
    var ndx = crossfilter(recipeData);

    main_ingredient(ndx);
    vegetarian(ndx);
    time(ndx);
    
    dc.renderAll();

}


function main_ingredient(ndx) {
  var dim = ndx.dimension(dc.pluck('main_ingredient'));
  var group = dim.group();
  
  
  dc.pieChart("#main_ingredient")
      .height(400)
      .width(350)
      .radius(140)
      .transitionDuration(1000)
      .dimension(dim)
      .group(group)
      .legend(dc.legend());
}


function vegetarian(ndx) {
    var dim = ndx.dimension(dc.pluck('vegetarian'));
    var group = dim.group();

    dc.barChart("#vegetarian")
        .width(500)
        .height(350)
        .margins({ top: 10, right: 50, bottom: 50, left: 50 })
        .dimension(dim)
        .group(group)
        .transitionDuration(1000)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .elasticY(true)
        .xAxisLabel("Meat vs Vegetarian")
        .yAxis().ticks(10);
}


function time(ndx) {
    var dim = ndx.dimension(dc.pluck('time'));
    var group = dim.group();

    dc.barChart("#time")
        .width(500)
        .height(350)
        .margins({ top: 10, right: 50, bottom: 50, left: 50 })
        .dimension(dim)
        .group(group)
        .transitionDuration(1000)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .elasticY(true)
        .xAxisLabel("Time")
        .yAxis().ticks(10);
}
