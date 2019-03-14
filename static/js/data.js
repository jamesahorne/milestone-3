queue()
    .defer(d3.json, "/get_data")
    .await(makeGraphs);


function makeGraphs(error, recipeData) {
    var ndx = crossfilter(recipeData);

    main_ingredient(ndx);
    vegetarian(ndx);
    time(ndx);
    allergens(ndx);

    dc.renderAll();

}


function main_ingredient(ndx) {
    var dim = ndx.dimension(dc.pluck('main_ingredient'));
    var group = dim.group();

    dc.pieChart("#main_ingredient")
        .width(300)
        .height(350)
        .radius(125)
        .transitionDuration(1000)
        .dimension(dim)
        .group(group)
        .legend(dc.legend());
}


function vegetarian(ndx) {
    var dim = ndx.dimension(dc.pluck('vegetarian'));
    var group = dim.group();

    dc.barChart("#vegetarian")
        .width(300)
        .height(350)
        .margins({ top: 10, right: 50, bottom: 50, left: 30 })
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
    let scale = d3.scale.ordinal()
        .domain([
            "0-5 mins",
            "5-10 mins",
            "10-30 mins",
            "30+ mins"
        ])
        .range([0, 1, 2, 3]);
        
    dc.rowChart("#time")
        .width(300)
        .height(350)
        .margins({ top: 10, right: 20, bottom: 50, left: 30 })
        .dimension(dim)
        .group(group)
        .transitionDuration(1000)
        .elasticX(true)
        .ordering(function(k) {
            return scale(k.key);
        });
}


function allergens(ndx) {
    var dim = ndx.dimension(dc.pluck('allergens'));
    var group = dim.group();

    dc.pieChart("#allergens")
        .width(300)
        .height(350)
        .radius(125)
        .transitionDuration(1000)
        .dimension(dim)
        .group(group)
        .legend(dc.legend());
}
