//Dimention of the visualization
var margin = {top:10, bottom:10, left:100,right:5}

var width = 1400 - margin.left - margin.right;

var height = 900 - margin.top - margin.bottom;

//Container to hold the graph: Scalable Vector Graphics
//Same size as our screen dimension above
var svg = d3.select('#graphHolder').append('svg')
	.attr('width',width + margin.left + margin.right)
	.attr('height',height + margin.top + margin.bottom)
	.append('g')
	.attr('transform', 'translate('+margin.left+','+margin.top+')');
	//.style("border", "1px solid black");

function draw(data)
{
		//Initialize the links
		var link = svg.selectAll('line')
			.data(data.links)
			.enter()
			.append('line')
				.style('stroke','#aaa')

		//Initialize nodes
		var node = svg.selectAll('circle')
			.data(data.nodes)
			.enter()
			.append('circle')
				.attr('r', 30)
				.style('fill', '#69b3a2')

		//Listing the force that will be applied on the network
		var simulation = de.forceSimulation(data.nodes)
			.force('link', d3.forceLink()
				.id(function(d){return d.id;})
				.links(data.links))
			.force('charge', d3.forceManyBody().strength(-350))
			.force('center', d3.forceCenter(width/2, height/2))

		function ticked()
		{
			link
				.attr('x1', function(d){return d.source.x;})
				.attr('y1', function(d){return d.source.y;})
				.attr('x2', function(d){return d.source.x;})
				.attr('xy', function(d){return d.source.y;})

			node
			.attr('cx', function(d){return d.x + 6;})
			.attr('cy', function(d){return d.y - 6;})

		}
		
});



/*
//Tooltip to hold IXP/ISP name
var tooltip = d3.select('body').append('div').attr('class','tooltip')
	.style({
        'background' : 'orangered',
        'color':'white',
        'width':"90px",
		});

//Get crankin' with the data
d3.json('draw_graph', function(data)
{
//Extract nodes and edges from json file
var nodes = data['nodes'];
var links = data['links'];

var force = d3.layout.force()
	.size([width,height])
	.nodes(d3.values(nodes)) //array of nodes
	.links(links) // array of edges
	.on('tick', tick) //EventListner to start calculating x and y values of nodes on the SVG
	.linkDistance(300) //default edge distance
	.start();

//Creating and drwaing links on the SVG
var link = svg.selectAll('.link')
	.data(links)
	.enter().append('line')
	.attr('class','link');

//Drawing nodes on top of the line edges
var node = d3.select('#flags').selectAll('img')
	.data(force.nodes())
	.enter().append('img')

	//Noe get node names/IDs
	.attr('class',function(d){return 'flag flag-'+d.code;})

	//We will need mouse handles when the mouse interacts with the graph
	.on('mouseover', mouseoverHandler)
    .on("mousemove",mouseMoving)
    .on("mouseout", mouseoutHandler);

function tick(e)
{
	//update node position
	node.style('left', function(d){return d.x + 'px'; })
		.style('top', function(d){return d.y + 'px';})
		.call(force.drag);

	//update link posiion
	link.attr('x1', function(d){ return  d.source.x})
        .attr('y1',function(d){ return  d.source.y})
        .attr('x2', function(d){ return  d.target.x})
        .attr('y2',function(d){ return d.target.y})
}

function mouseoverHandler(d)
{
	//display node name when hovering a node
	tooltip.transition().style('opacity', 0.9)
	tooltip.html('<p>' +d['country']+ '</p>');
}

function mouseoutHandler(d)
{
	//clear tooltip
	tooltip.transition().style('opacity', 0);
}

function mouseMoving(d)
{
	 tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px").style("color","white");
}

});*/
