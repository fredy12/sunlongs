
$(function(){
/*** Layout by JS ***/
	var	slideImgWrap = $('#slideImg > ul > li').find('a'),	 	   
	 	 pageSidebar = $('#pageSidebar'),
	 	 pageContent = $('#pageContent'),
	 	sidebarTitle = pageSidebar.find('div.page-sidebar-title'),
	 	 sidebarList = $('#sidebarList'),
	   sidebarListDt = sidebarList.find('dt'),
	 	   footInner = $('#footInner'),
		    footLeft = footInner.find('div.foot-left'),
		   footRight = footInner.find('div.foot-right'),
    footLeftAlignFix = footInner.find('div.left-align-fix'),
		 footLeftDiv = footInner.find('div.foot-left-inner'),
		       isIE6 = !-[1,]&&!window.XMLHttpRequest;

	// 首页区块	
	if ($('#slideImg').length == 0) {
		$('#slideNews').parent('div.main-block-right').css({float: 'none', width: 'auto'});
	} else {
		$('#slideNews').length == 1 ? $('#blockTextPara').height(slideImgWrap.height() - 34 - 15) : $('#blockTextPara').height(slideImgWrap.height()); // 简介模块动态高度，34(slideNews height) , 15(margin-bottom)	
	}	
	
	// 底部导航
	if (footLeft.length == 0) { // 如果底部左侧不显示
		footRight.css({float: 'none', width: 'auto'});
	} else {
		footLeft.height() > footRight.height() ? footRight.height(footLeft.height()) : footLeft.height(footRight.height());
		footLeftAlignFix.css('margin-bottom', Math.floor(footLeftDiv.height() / 2) * -1 + 'px');
	}

	// 内页侧栏
	if (sidebarList.length != 0) {
		// 开启当前二级栏目并去掉上一个二级栏目的水平线
		sidebarList.find('dt.on').parent('dl').addClass('sidebar-dl-current').prev('dl').find('a:eq(0)').addClass('bgnone');
		// 初始化最后一项
		sidebarList.find('dl:last').find('a:eq(0)').addClass('bgnone');
		sidebarList.find('dt.on').find('a').removeClass('bgnone');
		sidebarList.find('dt.on').children('i.subList-mark').removeClass('mark-fold');
		if (isIE6) {
			sidebarList.find('dt.on').next('dd').show();
		}

		sidebarList.find('dl').each(function(el, index) {
			if ($(this).children('dd').length > 0) {
				var markType;
				if ($(this).children('dd').is(':hidden')) {
					markType = 'mark-fold';
				} else {
					markType = '';
				}
				$(this).find('dt').append('<i class="subList-mark ' + markType + '"></i>');	// 如果有三级菜单则为该一级菜单加个标记
			} else {
				$(this).find('dt.on').children('a').addClass('bgnone'); // 如果没有三级菜单去掉水平线
			}				
			if ($(this).find('dt').hasClass('on')) {
				if (isIE6) {
					$(this).find('dd').show();
				}				
			} else {
				$(this).hover(function() { // 二级栏目hover背景
					if ($(this).next('dl').length == 0) { // 判断是否为最后一项
						$(this).toggleClass('sidebar-dl-current').find('a:eq(0)').addClass('bgnone');
					} else {
						$(this).toggleClass('sidebar-dl-current').find('a:eq(0)').toggleClass('bgnone');
					}					
					if ($(this).prev('dl').hasClass('sidebar-dl-current')) {
						$(this).find('a:eq(0)').toggleClass('sidebar-dl-hover');
					} else {
						$(this).prev('dl').find('a:eq(0)').toggleClass('bgnone');
					}
				});				
			}
		});
		// 展开/闭合三级菜单点击事件
		sidebarListDt.find('i.subList-mark').click(function() {
			var _this_ = $(this);
			$(this).parent('dt').next('dd').slideToggle(260, function() {
				_this_.parent('dt').find('a').toggleClass('bgnone');
				_this_.toggleClass('mark-fold');	
			});
					
		});		
	} else if (sidebarList.next('div.page-sidebar-info').length == 0) {
		$('#pageContent').css({float: 'none', width: 'auto'});
	}	

/*** 产品图片展示模块 ***/		
	/* 初始化 */		
	$('#photoNavBox').append($('a.photo-show-nav')).find('a.photo-show-nav').not(':last').after('<span class="photo-nav-line">/</span>').first().addClass('photo-nav-current');	// 构建二级分类导航样式
	var photoWrap = $('#photosWrap'),
		photoContDiv = photoWrap.find('ul.photo-show-content'),
		photoContDiv_1 = photoContDiv.eq(0),
		photoNav = $('#photoNavBox').find('a.photo-show-nav');
		photoContDiv.hide();
		photoContDiv_1.find('img').each(function(){
			var imgurl_1 = $(this).data('imgurl');
			$(this).attr('src',imgurl_1); // 防止页面载入时一次性请求过多图片
		});
		photoContDiv_1.show();

	$('#photoPrev, #photoNext').css('margin-top',(photoContDiv_1.find('img').height() - 128) / 2 + 'px'); // 切换按钮相对于图片垂直居中x

	/* 二级分类导航点击事件 */
	photoNav.click(function() {
		if ($(this).hasClass('photo-nav-current')) return false;
		photoNav.removeClass('photo-nav-current');
		$(this).addClass('photo-nav-current');
		photoContDiv.hide();
		var hrefStr = $(this).attr('href').substr(1);
		photoContDiv.hide().each(function(index, el) {
			// console.log(hrefStr);
			if ($(this).attr('id') === hrefStr) {
				var photo = $(this).find('img');
				photo.each(function(){
					if ($(this).attr('src') !== $(this).data('imgurl')) { 
						$(this).attr('src',$(this).data('imgurl')); // 向服务器请求当前分类下的图片
					}	
				});
				$(this).show();
				
			}
		});
		return false; // 防止触发a标签默认事件		
	});

	var photoNum;
	photoNum = Math.floor(890 / $('ul.photo-show-content').find('img:eq(0)').width());
	$('ul.photo-show-content').marquee({
	    auto: false,
	    speed: 300,
	    showNum: photoNum,
	    stepLen: 1,
	    prevElement: $('#photoNext'),
	    nextElement: $('#photoPrev')
	});	

/*** 全屏banner ***/
	if ($('#flashBanner').length != 0) { 
		var mainImage = $('#flashBanner').find('div.main-banner');
		var isBtnHide;
		if ($('#flashBanner').find('li').length == 1) { // 如果是单张图片，则不显示切换按钮
			$('#btn_prev, #btn_next').remove();
			isBtnHide = true;
		}		
		$('#flashBanner').hover(function(){		
	        $('#btn_prev,#btn_next').fadeIn();
	    },function(){
	    	$('#btn_prev,#btn_next').fadeOut();
	    });
	    $dragBln = false;
		mainImage.touchSlider({
	        flexible : true,
	    	speed : 500,
	    	btn_prev : $('#btn_prev'),
	    	btn_next : $('#btn_next')
		});
		mainImage.bind('mousedown', function() {
			$dragBln = false;
		});
	    mainImage.bind('dragstart', function() {
			$dragBln = true;
		});
		mainImage.find('a').click(function() {
			if($dragBln) {
	    		return false;
			}
		});
		if(!isBtnHide){
			_banner_timer = setInterval(function() { $('#btn_next').click();}, 5000);
		}
		$('#flashBanner').hover(function() {
			clearInterval(_banner_timer);
		}, function() {
			_banner_timer = setInterval(function() { $('#btn_next').click();}, 5000);
		});
		if(!isBtnHide){
			mainImage.bind('touchstart', function() {
				clearInterval(_banner_timer);
			}).bind('touchend', function() {
				_banner_timer = setInterval(function() { $('#btn_next').click();}, 5000);
		    });
		}
	}

/*** 导航条设置 ***/
	/* 当前导航高亮 */
	var nowId = $('#navDownId').val();
	$('#headNav').find('a.head-nav-list1').each(function() {
		if ($(this).attr('id').replace('nav_','') === nowId) {
			$(this).addClass('nav-current');
		}
	});
	/* 鼠标交互事件（title与二级菜单的显示隐藏）*/
	$('#headNav').find('li').hover(function() {
		var li_Wt = $(this).width(),
			dl_Wt = $(this).find('dl').width();
		if (dl_Wt <= li_Wt) { // 如果二级菜单宽度小于一级
			$(this).find('dl').width(li_Wt - 2);
		}
		$(this).find('a').removeAttr('title');
		$(this).find('a.head-nav-list1').not('a.nav-current').addClass('nav-list1-hover');
		$(this).find('dl:has(dd)').show();
	}, function() {
		var nav_a = $(this).find('a');
		nav_a.attr('title',nav_a.text()).removeClass('nav-list1-hover');
		$(this).find('dl').hide();		
	});

/*** 滑动切换效果 ***/
	$("#slideNews").Scroll({speed:500,timer:3000,up:"newsSlideNext",down:"newsSlidePrev"}); // 单排文字
	$('#slideImg').slideMarquee(); // 小图轮播	

/*** 首页搜索框 ***/
	function mySearch(t) {
		var text = t.data("text");
		if (text) {
			var l = "<label>"+text+"</label>",
			    d = t.find(".navsearch_input"),
			    e = d.find("input");
			    e.before(l);
			searchHint(e, d.find("label"), "#999", "#ddd"); // #999：无输入状态搜索框内文字颜色；#ddd输入状态下搜索框内文字颜色；		
		}
		function searchHint(dom,label,color1,color2) {
			label.css("color",color1);		
			if(dom.val() == '')label.show();		
			label.click(function() {
				dom.focus();
			});
			dom.focus(function() {
				label.css("color",color2);
			});
			dom.keyup(function() {
				if($(this).val() == '') {
					label.show();
				} else {
					label.hide();
				}
			});
			dom.focusout(function() {
				if($(this).val()=='') {
					label.show();
					label.css("color",color1);
				}
			});
		}
	}
	mySearch($("#headSearch"));    //传递元素 

});

/*** 
 * 走马灯jQ插件 @20150114封装
 * 格式：$(seletor).slideMarquee() 
 */
;(function($) {
	$.fn.extend({
		"slideMarquee": function() {
			var label_li = $(this).find('li'),
				label_a = label_li.children('a'),
				slide_btn_l = $(this).find('i.slide-btn-l'),
				slide_btn_r = $(this).find('i.slide-btn-r'),
				box_Wt = $(this).width(), // 获取容器宽度用以实现“溢出”
				counter = 0; // 计数器

			label_li.hide().first().show(); // 初始化：显示第一条	

			// 当信息条数小于2条，翻页按钮不可用
			if (label_li.length == 1) {
				slide_btn_r.addClass('slide-btn-disabled');
			}
			
			// 下一条
			slide_btn_r.bind('click',function() {
				if ($(this).hasClass('slide-btn-disabled')) return;
				if (!(label_a.is(':animated'))) { // 防止多次点击使动画堆积
					counter++;
					slide_btn_l.removeClass('slide-btn-disabled');
					if (counter == label_li.length - 1) { // 当到达最后一条时
						$(this).addClass('slide-btn-disabled');
					}		
					label_a.eq([counter - 1]).animate({marginLeft: box_Wt * -1 +'px'}, 300, function() { // 负值，向左移动
						label_li.eq([counter - 1]).hide();
						label_li.eq([counter]).show().children('a').css('marginLeft',box_Wt +'px').animate({marginLeft:0}, 300);
					});		
				}			
			});

			// 上一条
			slide_btn_l.bind('click',function() {
				if ($(this).hasClass('slide-btn-disabled')) return;
				if (!(label_a.is(':animated'))) { // 防止多次点击使动画堆积
					counter--;					
					slide_btn_r.removeClass('slide-btn-disabled');
					if (counter == 0) { // 当到达第一条时
						$(this).addClass('slide-btn-disabled');
					}	
					label_a.eq([counter + 1]).animate({marginLeft: box_Wt +'px'}, 300, function() { // 正值，向右移动
						label_li.eq([counter + 1]).hide();
						label_li.eq([counter]).show().children('a').css('marginLeft',box_Wt * -1 +'px').animate({marginLeft:0}, 300);
					});		
				}			
			});

			return $(this); // 返回本身以便链式操作
		}
	});
})(jQuery);

/*** 单行文字滚动插件 ***/
;(function($){
	$.fn.extend({
		Scroll:function(opt,callback){
				//参数初始化
				if(!opt) var opt={};
				var _btnUp = $("#"+ opt.up);//Shawphy:向上按钮
				var _btnDown = $("#"+ opt.down);//Shawphy:向下按钮
				var timerID;
				var _this=this.eq(0).find("ul:first");
				var     lineH=_this.find("li:first").height(), //获取行高
						line=opt.line?parseInt(opt.line,10):parseInt(this.height()/lineH,10), //每次滚动的行数，默认为一屏，即父容器高度
						speed=opt.speed?parseInt(opt.speed,10):500; //卷动速度，数值越大，速度越慢（毫秒）
						timer=opt.timer; //?parseInt(opt.timer,10):3000; //滚动的时间间隔（毫秒）
				if(line==0) line=1;
				var upHeight=0-line*lineH;
				//滚动函数
				var scrollUp=function(){
						_btnUp.unbind("click",scrollUp); //Shawphy:取消向上按钮的函数绑定
						_this.animate({
								marginTop:upHeight
						},speed,function(){
								for(i=1;i<=line;i++){
										_this.find("li:first").appendTo(_this);
								}
								_this.css({marginTop:0});
								_btnUp.bind("click",scrollUp); //Shawphy:绑定向上按钮的点击事件
						});

				}
				//Shawphy:向下翻页函数
				var scrollDown=function(){
						_btnDown.unbind("click",scrollDown);
						for(i=1;i<=line;i++){
								_this.find("li:last").show().prependTo(_this);
						}
						_this.css({marginTop:upHeight});
						_this.animate({
								marginTop:0
						},speed,function(){
								_btnDown.bind("click",scrollDown);
						});
				}
			   //Shawphy:自动播放
				var autoPlay = function(){
						if(timer)timerID = window.setInterval(scrollUp,timer);
				};
				var autoStop = function(){
						if(timer)window.clearInterval(timerID);
				};
				 //鼠标事件绑定
				_this.hover(autoStop,autoPlay).mouseout();
				// _btnUp.css("cursor","pointer").click( scrollUp ).hover(autoStop,autoPlay);//Shawphy:向上向下鼠标事件绑定
				// _btnDown.css("cursor","pointer").click( scrollDown ).hover(autoStop,autoPlay);
				/** by WingMeng at 20150118 **/
				_btnUp.click( scrollUp ).hover(autoStop,autoPlay);//Shawphy:向上向下鼠标事件绑定
				_btnDown.click( scrollDown ).hover(autoStop,autoPlay);

		}      
	})
})(jQuery);