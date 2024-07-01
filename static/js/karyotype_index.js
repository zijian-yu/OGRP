let jsTree = new JsTree($('#container'));
let data = [
    {
        "id": 9,
        "parentId": 0,
        "text": "Oleaceae"
    },
    {
        "id": 1,
        "parentId": 0,
        "text": "Oleaceae nodes",
        "child": [
            {
                "id": 2,
                "parentId": 1,
                "text": "<div class=\"row\">\n" +
                    "    <div class=\"col-lg-10\">\n" +
                    "        <p style=\"margin-bottom: 5px\">MRCAO\n</p>\n" +
                    "    </div>\n" +
                    "    <div class=\"col-lg-2\" style=\"padding: 0\">\n" +
                    "        <a href=\"karyotype/MRCAO\" target=\"_blank\" class=\"bi bi-caret-right\"></a>\n" +
                    "        <a href=\"../../static/image/MRCAO.png\" target=\"_blank\"  class=\"bi bi-eye\"></a>\n" +
                    "    </div>\n" +
                    "</div>",
            },
            {
                "id": 2,
                "parentId": 1,
                "text": "<div class=\"row\">\n" +
                    "    <div class=\"col-lg-10\">\n" +
                    "        <p style=\"margin-bottom: 5px\">CASOF\n</p>\n" +
                    "    </div>\n" +
                    "    <div class=\"col-lg-2\" style=\"padding: 0\">\n" +
                    "        <a href=\"karyotype/CASOF\" target=\"_blank\" class=\"bi bi-caret-right\"></a>\n" +
                    "        <a href=\"../../static/image/CASOF.png\" target=\"_blank\"  class=\"bi bi-eye\"></a>\n" +
                    "    </div>\n" +
                    "</div>",
            }


        ]
    },
    // ----------------------------------------分界线--------------------------------------------
    {
        "id": 6,
        "parentId": 0,
        "text": "Oleaceae species",
        "child": [
            {
                "id": 2,
                "parentId": 1,
                "text": "<div class=\"row\">\n" +
                    "    <div class=\"col-lg-10\">\n" +
                    "        <p style=\"margin-bottom: 5px; font-style: italic;\">Jasminum sambac\n</p>\n" +
                    "    </div>\n" +
                    "    <div class=\"col-lg-2\" style=\"padding: 0\">\n" +
                    "        <a href=\"karyotype/Jsa\" target=\"_blank\" class=\"bi bi-caret-right\"></a>\n" +
                    "        <a href=\"../../static/image/Vvi_Jsa.trajectory.png\" target=\"_blank\"  class=\"bi bi-eye\"></a>\n" +
                    "    </div>\n" +
                    "</div>",
            },
            {
                "id": 2,
                "parentId": 1,
                "text": "<div class=\"row\">\n" +
                    "    <div class=\"col-lg-10\">\n" +
                    "        <p style=\"margin-bottom: 5px; font-style: italic;\">Syringa oblata\n</p>\n" +
                    "    </div>\n" +
                    "    <div class=\"col-lg-2\" style=\"padding: 0\">\n" +
                    "        <a href=\"karyotype/Sob\" target=\"_blank\" class=\"bi bi-caret-right\"></a>\n" +
                    "        <a href=\"../../static/image/Vvi_Sob.trajectory.png\" target=\"_blank\"  class=\"bi bi-eye\"></a>\n" +
                    "    </div>\n" +
                    "</div>",
            },
            {
                "id": 2,
                "parentId": 1,
                "text": "<div class=\"row\">\n" +
                    "    <div class=\"col-lg-10\">\n" +
                    "        <p style=\"margin-bottom: 5px; font-style: italic;\">Fraxinus pennsylvanica\n</p>\n" +
                    "    </div>\n" +
                    "    <div class=\"col-lg-2\" style=\"padding: 0\">\n" +
                    "        <a href=\"karyotype/Fpe\" target=\"_blank\" class=\"bi bi-caret-right\"></a>\n" +
                    "        <a href=\"../../static/image/Vvi_Fpe.trajectory.png\" target=\"_blank\"  class=\"bi bi-eye\"></a>\n" +
                    "    </div>\n" +
                    "</div>",
            },
            {
                "id": 2,
                "parentId": 1,
                "text": "<div class=\"row\">\n" +
                    "    <div class=\"col-lg-10\">\n" +
                    "        <p style=\"margin-bottom: 5px; font-style: italic;\">Olea europaea\n</p>\n" +
                    "    </div>\n" +
                    "    <div class=\"col-lg-2\" style=\"padding: 0\">\n" +
                    "        <a href=\"karyotype/Oeu\" target=\"_blank\" class=\"bi bi-caret-right\"></a>\n" +
                    "        <a href=\"../../static/image/Vvi_Oeu.trajectory.png\" target=\"_blank\"  class=\"bi bi-eye\"></a>\n" +
                    "    </div>\n" +
                    "</div>",
            }
        ]
    }
]

jsTree.init({ data: data,isOpenAll:true, searchInput:$('#txt_seach'), childrenField: "child", value: "id", text: "text" ,clickCallback:(e)=>{
    console.log(e)
}});
$('#openAll').click(function(){
    jsTree.openAll();
})
$('#closeAll').click(function(){
    jsTree.closeAll();
})