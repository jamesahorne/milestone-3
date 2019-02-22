queue()
    .defer(d3.json, "/get_data")
    .await(makeGraphs);

function makeGraphs(error, recipeData) {
    var ndx = crossfilter(recipeData);

    main_ingredient(ndx);
    
    dc.renderAll();

}

function main_ingredients(ndx) {
    var dim = ndx.dimension(dc.pluck('main_ingredient'));
    var group = dim.group();

    dc.barChart("#main_ingredient")
        .width(400)
        .height(300)
        .margins({ top: 10, right: 50, bottom: 50, left: 50 })
        .dimension(dim)
        .group(group)
        .transitionDuration(500)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .elasticY(true)
        .xAxisLabel("Main ingredients")
        .yAxis().ticks(10);
}
