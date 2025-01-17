var zTree;
var demoIframe;

//灞曞紑鎵€鏈夎妭鐐�
function showIconForTree(treeId, treeNode) {
    for (i = 0; i < 5; i++) {
        return !treeNode.isParent;
    }
};
var setting = {
    view: {
        dblClickExpand: false,
        showLine: true,
        selectedMulti: false,
        showIcon: showIconForTree,
        fontCss: getFont,
        nameIsHTML: true
    },
    data: {
        simpleData: {
            enable: true,
            idKey: "id",
            pIdKey: "pId",
            rootPId: ""
        }
    },
    callback: {
        beforeClick: function (treeId, treeNode) {
            if (treeNode.isParent === false) {
                //console.info(treeNode);
                //鐐瑰嚮寮瑰嚭鎮诞妗�
                jQuery.ajax({
                    async: false,
                    url: "/getbrowsejson",
                    // url: "/getspecies_datajson",
                    type: "GET",
                    data: "wzid=" + treeNode.cateid,
                    contentType: "application/x-www-form-urlencoded",//formdata鐢╢alse
                    processData: true, //璇锋眰鏁版嵁鏄惁涓烘煡璇㈠瓧绗︿覆,formmdata鐢╢alse
                    cache: true,//formdata鐢╢alse
                    dataType: "text",//xml,html,script,json,jsonp,text
                    global: true,
                    ifModified: false,
                    success: function (result, status, xhr) {
                        var d = eval("(" + xhr.responseText + ")");
                        setTimeout(function () {
                            $('.curSelectedNode').parent('li').css('position', 'relative');
                            var str = '<div class="info clear">' +
                                '<div class="info_img"><img src="' + d.wz.wzpic + '"></div>' +
                                '<div class="info_right">' +
                                '<h3 style="font-style:italic;">' + d.wz.wzname + '</h3>' +
                                '<ul class="clear">' +
                                '<li title="' + d.wz.wzlinktext + '" style="overflow: hidden;white-space: nowrap;text-overflow: ellipsis;"><a href="' + d.wz.wzlink + '" target="_blank">Genome info.:&nbsp;' + d.wz.wzlinktext + '</a></li>' +
                                '<li><a href="/browsehref3?wzid=' + treeNode.cateid + '" target="_blank">Syntenic blocks:&nbsp;' + d.SyntenicblockID + '</a></li>' +
                                '<li><a href="/browsehref1?wzid=' + treeNode.cateid + '" target="_blank"><xieti style="font-style:italic">MIR</xieti> families:&nbsp;' + d.MIRfamily + '</a></li>' +
                                '<li><a href="/browsehref4?wzid=' + treeNode.cateid + '&type=sRNA-Seq" target="_blank">sRNA-Seq datasets:&nbsp;' + d['sRNA-seq'] + '</a></li>' +
                                '<li><a href="/browsehref1?wzid=' + treeNode.cateid + '" target="_blank"><xieti style="font-style:italic">MIR</xieti> loci:&nbsp;' + d.miRNA_gene_ID + '</a></li>' +
                                // '<li><a href="/browsehref4?wzid=' + treeNode.cateid + '&type=RNA-Seq" target="_blank">RNA-Seq datasets:&nbsp;' + d['RNA-seq'] + '</a></li>' +
                                '<li><a href="/browsehref4?wzid=' + treeNode.cateid + '&type=Degradome" target="_blank">PARE-Seq datasets:&nbsp;' + d['Degradome'] + '</a></li>' +
                                '<li><a href="/browsehref2?wzid=' + treeNode.cateid + '" target="_blank">Clusters:&nbsp;' + d.ClusterID + '</a></li>' +
                                '</ul>' +
                                '</div>' +
                                '</div>'
                            $('.curSelectedNode').parent('li').append(str);
                        }, 30)
                    },
                    beforeSend: function (xhr) {
                    },
                    complete: function (xhr, status) {
                    },
                    error: function () {
                    }
                });
            }
        }
    }
};

function getFont(treeId, node) {
    return node.font ? node.font : {};
}

$(document).ready(function () {

});

function loadReady() {
    var bodyH = demoIframe.contents().find("body").get(0).scrollHeight,
        htmlH = demoIframe.contents().find("html").get(0).scrollHeight,
        maxH = Math.max(bodyH, htmlH), minH = Math.min(bodyH, htmlH),
        h = demoIframe.height() >= maxH ? minH : maxH;
    if (h < 530) h = 530;
    demoIframe.height(h);
}

/*
$(document).click(function(){
    $('.ztree li .info').remove();
})*/
function stopPropagation(e) {
    var ev = e || window.event;
    if (ev.stopPropagation) {
        ev.stopPropagation();
    } else if (window.event) {
        window.event.cancelBubble = true;//鍏煎IE
    }
}

$(document).bind('click', function () {
    $(".ztree li .info").remove();
});
$(".ztree li .info").click(function (e) {
    stopPropagation(e);
});
