ecodeSDK.load({
    id:'b1e06d9bafe848dba94dd8b25cf11bb4',
    noCss:true, //是否禁止单独加载css，通常为了减少css数量，css默认前置加载
    cb:function () {
      runScript();
    }
  });

function initButton(rowIndex) {
            let rownum = rowIndex;
            let bjbs_id = WfForm.convertFieldNameToId("bjbs", ${detail});
            WfForm.changeFieldValue(bjbs_id+"_"+rownum, {value:"1"});
}
const runScript = () => { //代码块钩子，类似放在代码块中或者jquery.ready
	const detail = "detail_7";
	//可操作WfForm，以及部分表单dom hiden、ReactDOM.render
	const czId1 = WfForm.convertFieldNameToId("cz2", detail);
	const options = {
		title: '文件详情',
		moduleName: 'ecmlist',
		style: {
			width: 1200,
			height: 400
		},
		callback: function() {},
		onCancel: function() {},
	};
	const uri = "https://ecm.byd.com/views/bmsapp/OA/jointPage";
	const {
		requestid
	} = WfForm.getBaseInfo();
	let rowArr1 = WfForm.getDetailAllRowIndexStr(detail).split(",");
	if (rowArr1.length > 0) {
		for (let i = 0; i < rowArr1.length; i++) {
			let rowIndex = rowArr1[i];
			if (rowIndex != "") {
				let fieldMark = czId1 + "_" + rowIndex; //遍历明细行字段
				let colid = WfForm.getDetailRowKey(fieldMark);
				WfForm.proxyFieldComp(fieldMark,
					`<Button class="ant-btn ant-btn-primary" id="btn_${rowIndex}" 
            onclick="initButton(${rowIndex})"
          >查看</Button>`);
				let changeActionTypeInterval = setInterval(function() {
					let btnDom = $("#btn_" + rowIndex);
					if (btnDom.length > 0) {
						clearInterval(changeActionTypeInterval); // 取到就停止
						//先解绑，防止重复
						btnDom.unbind();
						//绑定点击事件
						let wjbh_fieldid = WfForm.convertFieldNameToId("wjbh",detail);//文件编号
						let wjbbh_fieldid = WfForm.convertFieldNameToId("wjbbh",detail);//文件版本号
						let wjbh_fieldvalue = WfForm.getFieldValue(wjbh_fieldid+"_"+rowIndex);
						let wjbbh_fieldvalue = WfForm.getFieldValue(wjbbh_fieldid+"_"+rowIndex);
						btnDom.click(function() {
							window.weaJs.showDialog(uri + "?docNumber=" + wjbh_fieldvalue +
								"&docRevision=" + wjbbh_fieldvalue + "&processId=" +  requestid +
								"&type=ALL&state=" + urlECMSTATE, options);
						})
					}
				}, 1000);
			}
		}
	}
}
