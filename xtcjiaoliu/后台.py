import os,sys,time,shutil
def addppt():
    pass
def addvideo():
    pass
def editboard():
    pass
def addapk():
    pass
def addpicbak():
    page='''<div class="col-md-4 col-sm-4 filtr-item" data-category="3" data-sort="Industrial site">
						<div class="agileits-img">
							<a href="*#{file_url}#*" class="swipebox" title="Praesent non purus fermentum, eleifend velit non Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus tortor diam, ac lobortis justo rutrum quis.">
								<img src="*#{file_url}#*" alt="" class="img-responsive " />
							</a>	
						</div>
					</div>'''
    page2="""<div class="clearfix"> </div>
				</div>
			</div>
		</div>"""
    print("=====加图片=====")
    print("图片命名为picture.jpg然后放到根目录")
    input("好了就敲回车")
    print("准备移动文件...",end='')
    import os,shutil
    #创建目录文件夹
    #os.makedirs('./image/', exist_ok=True)
    # 参数 旧路径：新路径
    filename='./images/pic/'+str(time.time())+".jpg"
    shutil.move('picture.jpg',filename)
    print("成功!")
    print("读取HTML...",end='')
    file_content=""
    with open("picture/index.html",'r+',encoding="utf-8") as f:
        file_content=f.read()
        print(file_content)
        print("成功！")
        print("编辑HTML...",end='')
        file_content.replace(page2,"")
        file_content+=(page.replace("*#{file_url}#*",filename))
        file_content+=page2
        print(file_content)
        
        print("成功！")
    print("写入HTML...",end='')
    with open("picture/index.html",'w',encoding="utf-8") as f:
        f.write(file_content)
    print("成功！")
        
def addpic():
    pass
    
print("一只小流浪后台    1.0    ")
print("输1：加ppt，输2：加视频，输3，编辑小黑板，输4：上传apk,输5：加图片")
userinput=int(input(":"))
if userinput==1:
    addppt()
elif userinput==2:
    addvideo()
elif userinput==3:
    editboard()
elif userinput==4:
    addapk()
elif userinput==5:
    addpic()
else:
    print("输入错误")

    
    
    
