var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
var option;
var days = ['Arabidopsis thaliana', 'Spirodela polyrrhiza', 'Vvitis vinifera', 'Tetracentron sinense', 'Papaver somniferum',
 'Aquilegia coerulea', 'Coptis chinensis'];
var hours = ['CYP51', 'CYP701', 'CYP703',
        'CYP706', 'CYP71', 'CYP719', 'CYP71-like', 'CYP736', 'CYP75', 'CYP76', 'CYP77', 'CYP78'
        , 'CYP79', 'CYP80', 'CYP81', 'CYP82', 'CYP84', 'CYP89', 'CYP93', 'CYP93-like', 'CYP98'
        , 'CYP705', 'CYP712', 'CYP73', 'CYP83', 'CYP92', 'CYP99', 'CYP710', 'CYP711', 'CYP714'
        , 'CYP72', 'CYP734', 'CYP749', 'CYP709', 'CYP715', 'CYP721', 'CYP723', 'CYP735', 'CYP727'
        , 'CYP74', 'CYP702', 'CYP707', 'CYP716', 'CYP720', 'CYP85', 'CYP87', 'CYP88', 'CYP90'
        , 'CYP708', 'CYP718', 'CYP722', 'CYP724', 'CYP728', 'CYP729', 'CYP733', 'CYP704', 'CYP86'
        , 'CYP94', 'CYP96', 'CYP97', 'CYP91'];

var data = [
[0,0,2],[0,1,1],[0,2,1],[0,3,7],[0,4,51],[0,5,0],[0,6,0],[0,7,0],[0,8,1],[0,9,8],[0,10,5],[0,11,6],[0,12,8],[0,13,0],[0,14,16],[0,15,5],[0,16,1],[0,17,7],[0,18,1],[0,19,0],[0,20,3],[0,21,30],[0,22,2],[0,23,1],[0,24,2],[0,25,0],[0,26,0],[0,27,4],[0,28,1],[0,29,2],[0,30,10],[0,31,1],[0,32,0],[0,33,3],[0,34,1],[0,35,1],[0,36,0],[0,37,2],[0,38,0],[0,39,2],[0,40,6],[0,41,4],[0,42,2],[0,43,1],[0,44,1],[0,45,1],[0,46,2],[0,47,4],[0,48,3],[0,49,1],[0,50,1],[0,51,1],[0,52,0],[0,53,0],[0,54,0],[0,55,3],[0,56,10],[0,57,6],[0,58,14],[0,59,3],[0,60,2],
[1,0,0],[1,1,0],[1,2,0],[1,3,0],[1,4,12],[1,5,5],[1,6,0],[1,7,0],[1,8,0],[1,9,20],[1,10,0],[1,11,2],[1,12,0],[1,13,0],[1,14,1],[1,15,0],[1,16,0],[1,17,4],[1,18,1],[1,19,0],[1,20,0],[1,21,5],[1,22,0],[1,23,3],[1,24,0],[1,25,1],[1,26,0],[1,27,1],[1,28,1],[1,29,0],[1,30,4],[1,31,0],[1,32,1],[1,33,3],[1,34,0],[1,35,1],[1,36,0],[1,37,1],[1,38,0],[1,39,6],[1,40,2],[1,41,0],[1,42,0],[1,43,0],[1,44,4],[1,45,0],[1,46,1],[1,47,0],[1,48,0],[1,49,0],[1,50,0],[1,51,0],[1,52,1],[1,53,0],[1,54,0],[1,55,3],[1,56,1],[1,57,2],[1,58,15],[1,59,0],[1,60,0],
[2,0,2],[2,1,0],[2,2,1],[2,3,0],[2,4,33],[2,5,3],[2,6,0],[2,7,0],[2,8,0],[2,9,21],[2,10,2],[2,11,2],[2,12,3],[2,13,0],[2,14,12],[2,15,3],[2,16,2],[2,17,3],[2,18,0],[2,19,0],[2,20,0],[2,21,11],[2,22,0],[2,23,0],[2,24,1],[2,25,0],[2,26,0],[2,27,0],[2,28,0],[2,29,1],[2,30,12],[2,31,2],[2,32,0],[2,33,15],[2,34,1],[2,35,3],[2,36,0],[2,37,3],[2,38,0],[2,39,5],[2,40,0],[2,41,2],[2,42,7],[2,43,0],[2,44,14],[2,45,8],[2,46,1],[2,47,1],[2,48,2],[2,49,0],[2,50,3],[2,51,3],[2,52,0],[2,53,0],[2,54,1],[2,55,6],[2,56,2],[2,57,1],[2,58,9],[2,59,0],[2,60,0],
[3,0,2],[3,1,0],[3,2,1],[3,3,4],[3,4,31],[3,5,7],[3,6,0],[3,7,0],[3,8,1],[3,9,13],[3,10,4],[3,11,6],[3,12,1],[3,13,0],[3,14,12],[3,15,3],[3,16,1],[3,17,4],[3,18,0],[3,19,0],[3,20,0],[3,21,8],[3,22,0],[3,23,4],[3,24,0],[3,25,1],[3,26,0],[3,27,1],[3,28,0],[3,29,4],[3,30,20],[3,31,0],[3,32,2],[3,33,0],[3,34,0],[3,35,2],[3,36,0],[3,37,3],[3,38,0],[3,39,4],[3,40,1],[3,41,0],[3,42,12],[3,43,0],[3,44,26],[3,45,6],[3,46,2],[3,47,1],[3,48,0],[3,49,1],[3,50,0],[3,51,5],[3,52,0],[3,53,0],[3,54,0],[3,55,3],[3,56,3],[3,57,5],[3,58,23],[3,59,0],[3,60,0],
[4,0,2],[4,1,2],[4,2,3],[4,3,2],[4,4,61],[4,5,12],[4,6,0],[4,7,0],[4,8,3],[4,9,30],[4,10,7],[4,11,4],[4,12,0],[4,13,3],[4,14,5],[4,15,12],[4,16,0],[4,17,4],[4,18,0],[4,19,0],[4,20,2],[4,21,18],[4,22,0],[4,23,2],[4,24,3],[4,25,0],[4,26,0],[4,27,1],[4,28,0],[4,29,1],[4,30,6],[4,31,0],[4,32,3],[4,33,7],[4,34,2],[4,35,2],[4,36,0],[4,37,2],[4,38,0],[4,39,14],[4,40,4],[4,41,8],[4,42,11],[4,43,0],[4,44,11],[4,45,7],[4,46,0],[4,47,7],[4,48,3],[4,49,0],[4,50,0],[4,51,1],[4,52,0],[4,53,0],[4,54,1],[4,55,11],[4,56,3],[4,57,8],[4,58,23],[4,59,4],[4,60,0],
[5,0,2],[5,1,0],[5,2,2],[5,3,2],[5,4,103],[5,5,16],[5,6,0],[5,7,0],[5,8,3],[5,9,70],[5,10,4],[5,11,3],[5,12,2],[5,13,9],[5,14,12],[5,15,10],[5,16,1],[5,17,3],[5,18,0],[5,19,0],[5,20,1],[5,21,11],[5,22,1],[5,23,0],[5,24,0],[5,25,0],[5,26,0],[5,27,3],[5,28,0],[5,29,0],[5,30,36],[5,31,0],[5,32,2],[5,33,19],[5,34,0],[5,35,4],[5,36,0],[5,37,3],[5,38,0],[5,39,5],[5,40,3],[5,41,8],[5,42,18],[5,43,0],[5,44,12],[5,45,7],[5,46,0],[5,47,3],[5,48,5],[5,49,2],[5,50,2],[5,51,7],[5,52,3],[5,53,0],[5,54,4],[5,55,6],[5,56,2],[5,57,3],[5,58,23],[5,59,0],[5,60,1],
[6,0,1],[6,1,0],[6,2,1],[6,3,0],[6,4,44],[6,5,12],[6,6,0],[6,7,0],[6,8,3],[6,9,27],[6,10,3],[6,11,3],[6,12,1],[6,13,0],[6,14,12],[6,15,10],[6,16,0],[6,17,0],[6,18,0],[6,19,0],[6,20,0],[6,21,14],[6,22,1],[6,23,1],[6,24,0],[6,25,1],[6,26,0],[6,27,0],[6,28,0],[6,29,0],[6,30,9],[6,31,0],[6,32,1],[6,33,11],[6,34,0],[6,35,3],[6,36,0],[6,37,0],[6,38,0],[6,39,1],[6,40,2],[6,41,3],[6,42,9],[6,43,0],[6,44,9],[6,45,5],[6,46,3],[6,47,4],[6,48,0],[6,49,1],[6,50,0],[6,51,3],[6,52,0],[6,53,0],[6,54,1],[6,55,7],[6,56,2],[6,57,2],[6,58,7],[6,59,2],[6,60,1],
]
data = data.map(function (item) {
    return [item[1], item[0], item[2] || '-'];
});

option = {
    tooltip: {
        position: 'top'
    },
    grid: {
        height: '80%',
        top: '1%'
    },
    
    xAxis: {
        type: 'category',
        data: hours,
        splitArea: {
            show: true
        },

    },
    yAxis: {
        type: 'category',
        data: days,
        splitArea: {
            show: true
        },
        axisLabel: {
            fontStyle: 'italic',
            rotate: 30
        }

    },
    visualMap: {
        min: 0,
        max: 20,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: '10%'
    },
    series: [{
        name: 'gene families',
        type: 'heatmap',
        data: data,
        label: {
            show: true
        },
        emphasis: {
            itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    }]
};



option && myChart.setOption(option);
myChart.on('click', function (params) {
        var name = params.name;
        // document.write(name);
        // window.location.href="../../static/data/dotplot/tree_and_mcscan.png";
        // window.location.href="../../static/data/hhh.fasta";
        if (name === "CYP51") {
            window.location.href="../../static/data/heatmap_tree/51png.png";
        }
        if (name === "CYP701") {
            window.location.href="../../static/data/heatmap_tree/51png.png";
        }
        if (name === "CYP703") {
            window.location.href="../../static/data/heatmap_tree/703png.png";
        }
        if (name === "CYP706") {
            window.location.href="../../static/data/heatmap_tree/706png.png";
        }
        if (name === "CYP71") {
            window.location.href="../../static/data/heatmap_tree/71.png";
        }
        if (name === "CYP719") {
            window.location.href="../../static/data/heatmap_tree/719.color-co-bs.png";
        }
        if (name === "CYP71-like") {
            window.location.href="../../static/data/heatmap_tree/71_likepng.png";
        }
        if (name === "CYP736") {
            window.location.href="../../static/data/heatmap_tree/736png.png";
        }
        if (name === "CYP75") {
            window.location.href="../../static/data/heatmap_tree/75png.png";
        }
        if (name === "CYP76") {
            window.location.href="../../static/data/heatmap_tree/76png.png";
        }
        if (name === "CYP77") {
            window.location.href="../../static/data/heatmap_tree/77png.png";
        }
        if (name === "CYP78") {
            window.location.href="../../static/data/heatmap_tree/78png.png";
        }
        if (name === "CYP79") {
            window.location.href="../../static/data/heatmap_tree/79png.png";
        }
        if (name === "CYP80") {
            window.location.href="../../static/data/heatmap_tree/80.x.png";
        }
        if (name === "CYP81") {
            window.location.href="../../static/data/heatmap_tree/81png.png";
        }
        if (name === "CYP82") {
            window.location.href="../../static/data/heatmap_tree/82.co.png";
        }
        if (name === "CYP84") {
            window.location.href="../../static/data/heatmap_tree/84png.png";
        }
        if (name === "CYP89") {
            window.location.href="../../static/data/heatmap_tree/89png.png";
        }if (name === "CYP93") {
            window.location.href="../../static/data/heatmap_tree/93png.png";
        }
        if (name === "CYP93-like") {
            window.location.href="../../static/data/heatmap_tree/CYP93-like.png";
        }
        if (name === "CYP98") {
            window.location.href="../../static/data/heatmap_tree/CYP98png.png";
        }
        if (name === "CYP705") {
            window.location.href="../../static/data/heatmap_tree/705png.png";
        }
        if (name === "CYP712") {
            window.location.href="../../static/data/heatmap_tree/CYP712.png";
        }
        if (name === "CYP73") {
            window.location.href="../../static/data/heatmap_tree/73png.png";
        }
        if (name === "CYP83") {
            window.location.href="../../static/data/heatmap_tree/83png.png";
        }
        if (name === "CYP92") {
            window.location.href="../../static/data/heatmap_tree/92png.png";
        }
        if (name === "CYP99") {
            window.location.href="../../static/data/heatmap_tree/99png.png";
        }
        if (name === "CYP710") {
            window.location.href="../../static/data/heatmap_tree/710png.png";
        }
        if (name === "CYP711") {
            window.location.href="../../static/data/heatmap_tree/711png.png";
        }
        if (name === "CYP714") {
            window.location.href="../../static/data/heatmap_tree/714png.png";
        }
        if (name === "CYP72") {
            window.location.href="../../static/data/heatmap_tree/72png.png";
        }
        if (name === "CYP734") {
            window.location.href="../../static/data/heatmap_tree/734png.png";
        }
        if (name === "CYP749") {
            window.location.href="../../static/data/heatmap_tree/749png.png";
        }
        if (name === "CYP715") {
           window.location.href="../../static/data/heatmap_tree/715png.png";
        }
        if (name === "CYP721") {
            window.location.href="../../static/data/heatmap_tree/721png.png";
        }
        if (name === "CYP723") {
            window.location.href="../../static/data/heatmap_tree/723png.png";
        }
        if (name === "CYP735") {
            window.location.href="../../static/data/heatmap_tree/735png.png";
        }
        if (name === "CYP727") {
            window.location.href="../../static/data/heatmap_tree/727png.png";
        }
        if (name === "CYP74") {
            window.location.href="../../static/data/heatmap_tree/74png.png";
        }
        if (name === "CYP702") {
            window.location.href="../../static/data/heatmap_tree/702png.png";
        }
        if (name === "CYP707") {
            window.location.href="../../static/data/heatmap_tree/707png.png";
        }
        if (name === "CYP716") {
            window.location.href="../../static/data/heatmap_tree/716png.png";
        }
        if (name === "CYP720") {
            window.location.href="../../static/data/heatmap_tree/720png.png";
        }
        if (name === "CYP85") {
            window.location.href="../../static/data/heatmap_tree/85png.png";
        }
        if (name === "CYP87") {
            window.location.href="../../static/data/heatmap_tree/87png.png";
        }
        if (name === "CYP88") {
            window.location.href="../../static/data/heatmap_tree/88png.png";
        }
        if (name === "CYP90") {
            window.location.href="../../static/data/heatmap_tree/90png.png";
        }
        if (name === "CYP708") {
            window.location.href="../../static/data/heatmap_tree/708png.png";
        }
        if (name === "CYP709") {
            window.location.href="../../static/data/heatmap_tree/709png.png";
        }
        if (name === "CYP718") {
            window.location.href="../../static/data/heatmap_tree/718png.png";
        }
        if (name === "CYP722") {
            window.location.href="../../static/data/heatmap_tree/722png.png";
        }
        if (name === "CYP724") {
            window.location.href="../../static/data/heatmap_tree/724png.png";
        }
        if (name === "CYP728") {
            window.location.href="../../static/data/heatmap_tree/728png.png";
        }
        if (name === "CYP729") {
            window.location.href="../../static/data/heatmap_tree/729png.png";
        }
        if (name === "CYP733") {
            window.location.href="../../static/data/heatmap_tree/733png.png";
        }
        if (name === "CYP704") {
            window.location.href="../../static/data/heatmap_tree/704png.png";
        }
        if (name === "CYP86") {
            window.location.href="../../static/data/heatmap_tree/86png.png";
        }
        if (name === "CYP94") {
            window.location.href="../../static/data/heatmap_tree/94png.png";
        }
        if (name === "CYP96") {
            window.location.href="../../static/data/heatmap_tree/96png.png";
        }
        if (name === "CYP97") {
            window.location.href="../../static/data/heatmap_tree/97png.png";
        }
        if (name === "CYP91") {
            window.location.href="../../static/data/heatmap_tree/91png.png";
        }
    });