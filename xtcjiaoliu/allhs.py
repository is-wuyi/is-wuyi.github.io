#如果mainserver接收到了在func里定义的请求，就优先发送到这里来处理
#比如访问了host/2333run
#则发送到2333run函数
#返回值为string,一般为html
import allhs,time,os,sys,requests,json
def pptserver(rep_str):
    #req_str没啥用
    data=""
    with open("pptserver_data.json","r",encoding="utf-8") as f:
        data=f.read()
        data=json.loads(data)
    for i in data:
        print(i,end="：")
        print(data[i])
    #做html
    html_1="""<!-- banner-text -->
		<div class="banner-text"> 
			<div class="container"> 
				<div class="banner-w3lstext">
					<h2>PPT资源</h2>
				</div> 	 
			</div>
		</div>
		<!-- //banner-text -->    
	</div>
	<!-- //banner --> 
	<!-- tours -->
	<div class="welcome portfolio">
		<div class="container">  <div class="row fontawesome-icon-list">
				
	"""
    html_2="""</div>
		</div>
	</div>"""
    html_zhong="""<div class="icon-box col-md-3 col-sm-4"><a href="*#*#{pptview_url}#*#*"></a><div id=""><a href="*#*#{pptview_url}#*#*"> <img src="*#*#{pptlogo}#*#*" width="100%" height="150" style="text-align: center;display:block;"><br><span class="text-muted" style="text-align: center;display:block;">*#*#{ppt_name}#*#*</span></a></div></div>"""
	#合成核心html
    total=""" """
    total+=html_1
    for i in data:
        html_tmp=html_zhong
        html_tmp=html_tmp.replace("*#*#{ppt_name}#*#*",i)
        html_tmp=html_tmp.replace("*#*#{pptview_url}#*#*",data[i][1])
        html_tmp=html_tmp.replace("*#*#{pptlogo}#*#*",data[i][0])
        total+=html_tmp
    total+=html_2
    #with open("ke/tmp.html","w",encoding="utf-8") as f:
    #    f.write(total)
    #在次套壳
    
    with open("ke/1.html","r",encoding="utf-8") as f:
        total=f.read()+total
    with open("ke/2.html","r",encoding="utf-8") as f:
        total=total+f.read()
    return total

def picture(rep_str):
    #req_str没啥用
    data=""
    with open("picture_data.json","r",encoding="utf-8") as f:
        data=f.read()
        data=json.loads(data)
    for i in data:
        print(i,end="：")
        print(data[i])
    #做html
    html_1="""<!--banner-text--><div class="banner-text"><div class="container"><div class="banner-w3lstext"><h2>美图合集</h2></div></div></div><!--</div><!--<!--tours--><div class="welcome portfolio"><div class="container"><div class="gallery_gds"><div class="filtr-container">"""
    html_2="""<div class="clearfix"></div></div></div></div></div><div class="col-md-4 col-sm-4 filtr-item"data-category="3"data-sort="Industrial site"><div class="agileits-img"><a href="./images/pic/1653813972.409322.jpg"class="swipebox"title="Praesent non purus fermentum, eleifend velit non Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus tortor diam, ac lobortis justo rutrum quis."><img src="./images/pic/1653813972.409322.jpg"alt=""class="img-responsive "/></a></div></div><div class="clearfix"></div></div></div></div>"""
    html_zhong="""<div class="col-md-4 col-sm-4 filtr-item"data-category="1"data-sort="City wonders"><div class="agileits-img"><a href="*#*#btnurl#*#*"class="swipebox"title="*#*#title#*#*"><img src="*#*#imgurl#*#*"alt=""class="img-responsive  "/></a></div></div>"""
    #合成核心html
    total=""" """
    total+=html_1
    for i in data:
        html_tmp=html_zhong
        html_tmp=html_tmp.replace("*#*#title#*#*",i)
        html_tmp=html_tmp.replace("*#*#btnurl#*#*",data[i][1])
        html_tmp=html_tmp.replace("*#*#imgurl#*#*",data[i][0])
        total+=html_tmp
    total+=html_2
    #with open("ke/tmp.html","w",encoding="utf-8") as f:
    #    f.write(total)
    #在次套壳
    
    with open("ke/1.html","r",encoding="utf-8") as f:
        total=f.read()+total
    with open("ke/2.html","r",encoding="utf-8") as f:
        total=total+f.read()
    return total


def about(req_str):
    fp=''
    with open("aboutbak/index.html",encoding="UTF-8") as f:
        fp=f.read()
    with open("about_num.txt") as f:
        num=f.readlines()
        print(num)
        fp=fp.replace("*#*#{value0}#*#*",num[0])
        fp=fp.replace("*#*#{value1}#*#*",num[1])
        fp=fp.replace("*#*#{value2}#*#*",num[2])
    with open("ke/1.html","r",encoding="utf-8") as f:
        fp=f.read()+fp
    with open("ke/2.html","r",encoding="utf-8") as f:
        fp=fp+f.read()
    
    return fp
def DayGuShi():
    #https://v1.jinrishici.com/all
    res=requests.get("https://v1.jinrishici.com/all")
    jsondata=res.json()
    content=jsondata['content']
    title=jsondata['origin']
    author=jsondata['author']
    return "“"+content+"”"+"——"+author+"《"+title+"》"
    #return "test"


def easteregg(req_str):
    pagee="""
    <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>jQuery响应式Banner图片轮播代码</title>

<link rel="stylesheet" href="css/style.css" />

</head>
<body>

<div class="c-banner">
	<div class="banner">
		<ul>
			<li><img src="img/lunbo1.jpg"></li>
			<li><img src="img/lunbo2.jpg"></li>
			<li><img src="img/lunbo3.jpg"></li>
		</ul>
	</div>
	<div class="nexImg">
		<img src="img/nexImg.png" />
	</div>
	<div class="preImg">
		<img src="img/preImg.png" />
	</div>
	<div class="jumpBtn">
		<ul>
			<li jumpImg="0"></li>
			<li jumpImg="1"></li>
			<li jumpImg="2"></li>
		</ul>
	</div>
</div>

<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript">
//定时器返回值
var time=null;
//记录当前位子
var nexImg = 0;
//用于获取轮播图图片个数
var imgLength = $(".c-banner .banner ul li").length;
//当时动态数据的时候使用,上面那个删除
// var imgLength =0;
//设置底部第一个按钮样式
$(".c-banner .jumpBtn ul li[jumpImg="+nexImg+"]").css("background-color","black");

//页面加载
$(document).ready(function(){
	// dynamicData();
	//启动定时器,设置时间为3秒一次
	time =setInterval(intervalImg,3000);
});

//点击上一张
$(".preImg").click(function(){
	//清楚定时器
	clearInterval(time);
	var nowImg = nexImg;
	nexImg = nexImg-1;
	console.log(nexImg);
	if(nexImg<0){
		nexImg=imgLength-1;
	}
	//底部按钮样式设置
	$(".c-banner .jumpBtn ul li").css("background-color","white");
	$(".c-banner .jumpBtn ul li[jumpImg="+nexImg+"]").css("background-color","black");
	
	//将当前图片试用绝对定位,下一张图片试用相对定位
	$(".c-banner .banner ul img").eq(nowImg).css("position","absolute");
	$(".c-banner .banner ul img").eq(nexImg).css("position","relative");
	
	//轮播淡入淡出
	$(".c-banner .banner ul li").eq(nexImg).css("display","block");
	$(".c-banner .banner ul li").eq(nexImg).stop().animate({"opacity":1},1000);
	$(".c-banner .banner ul li").eq(nowImg).stop().animate({"opacity":0},1000,function(){
		$(".c-banner ul li").eq(nowImg).css("display","none");
	});
	
	//启动定时器,设置时间为3秒一次
	time =setInterval(intervalImg,3000);
})

//点击下一张
$(".nexImg").click(function(){
	clearInterval(time);
	intervalImg();
	time =setInterval(intervalImg,3000);
})

//轮播图
function intervalImg(){
	if(nexImg<imgLength-1){
		nexImg++;
	}else{
		nexImg=0;
	}
	
	//将当前图片试用绝对定位,下一张图片试用相对定位
	$(".c-banner .banner ul img").eq(nexImg-1).css("position","absolute");
	$(".c-banner .banner ul img").eq(nexImg).css("position","relative");
	
	$(".c-banner .banner ul li").eq(nexImg).css("display","block");
	$(".c-banner .banner ul li").eq(nexImg).stop().animate({"opacity":1},1000);
	$(".c-banner .banner ul li").eq(nexImg-1).stop().animate({"opacity":0},1000,function(){
		$(".c-banner .banner ul li").eq(nexImg-1).css("display","none");
	});
	$(".c-banner .jumpBtn ul li").css("background-color","white");
	$(".c-banner .jumpBtn ul li[jumpImg="+nexImg+"]").css("background-color","black");
}

//轮播图底下按钮
//动态数据加载的试用应放在请求成功后执行该代码,否则按钮无法使用
$(".c-banner .jumpBtn ul li").each(function(){
	//为每个按钮定义点击事件
	$(this).click(function(){
		clearInterval(time);
		$(".c-banner .jumpBtn ul li").css("background-color","white");
		jumpImg = $(this).attr("jumpImg");
		if(jumpImg!=nexImg){
			var after =$(".c-banner .banner ul li").eq(jumpImg);
			var befor =$(".c-banner .banner ul li").eq(nexImg);
			
			//将当前图片试用绝对定位,下一张图片试用相对定位
			$(".c-banner .banner ul img").eq(nexImg).css("position","absolute");
			$(".c-banner .banner ul img").eq(jumpImg).css("position","relative");
			
			after.css("display","block");
			after.stop().animate({"opacity":1},1000);
			befor.stop().animate({"opacity":0},1000,function(){
				befor.css("display","none");
			});
			nexImg=jumpImg;
		}
		$(this).css("background-color","black");
		time =setInterval(intervalImg,3000);
	});
});

	//动态数据轮播图
	//动态数据加载的时候不要直接点击demo.html运行否则可能请求不到本地json数据
// function dynamicData(){
// 	$.ajax({
// 		url:"js/test.json",
// 		type:"get",
// 		dataType:"json",
// 		success:function(data){
// 			if(data.code==1){
// 				var data = data.data;
// 				$.each(data,function(i){
// 					$(".c-banner .banner ul").append('<li><img src="'+this.img+'"></li>');
// 					$(".c-banner .jumpBtn ul").append('<li jumpImg="'+i+'"></li>')
// 				})
// 			}
// 			//获取图片总数量
// 			imgLength = $(".c-banner .banner ul li").length;
// 			//为底部按钮定义单击事件
// 			$(".c-banner .jumpBtn ul li").each(function(){
// 				//为每个按钮定义点击事件
// 				$(this).click(function(){
// 					clearInterval(time);
// 					$(".c-banner .jumpBtn ul li").css("background-color","white");
// 					jumpImg = $(this).attr("jumpImg");
// 					if(jumpImg!=nexImg){
// 						var after =$(".c-banner .banner ul li").eq(jumpImg);
// 						var befor =$(".c-banner .banner ul li").eq(nexImg);
// 						
// 						//将当前图片试用绝对定位,下一张图片试用相对定位
// 						$(".c-banner .banner ul img").eq(nexImg).css("position","absolute");
// 						$(".c-banner .banner ul img").eq(jumpImg).css("position","relative");
// 						
// 						after.css("display","block");
// 						after.stop().animate({"opacity":1},1000);
// 						befor.stop().animate({"opacity":0},1000,function(){
// 							befor.css("display","none");
// 						});
// 						nexImg=jumpImg;
// 					}
// 					$(this).css("background-color","black");
// 					time =setInterval(intervalImg,3000);
// 				});
// 			});
// 		}
// 	})
// }
</script>
</body>
</html>    """
    return pagee

def error_test(req_str):
   
   
    return int("你让我出错，我就给你string转int！")
if time.time()<1659492399:
    
    func={
        "/easteregg2333_bak":allhs.easteregg,
        "/error_test":allhs.error_test,
        "/daygs":allhs.DayGuShi,
        "/picture":allhs.picture,
        "/pptserver":allhs.pptserver,
        "/about":allhs.about,
        }

