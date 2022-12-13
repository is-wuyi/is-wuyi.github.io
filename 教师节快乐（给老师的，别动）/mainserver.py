
import traceback
import sys, os
from http.server import BaseHTTPRequestHandler,HTTPServer
import allhs#自定义的
# 一个服务器异常，当发生异常抛出这个。
teshuzhixiang={#指向另一资源（懒得写版本号）
    "/fonts/fontawesome-webfont.woff2?v=4.6.3":"/fonts/fontawesome-webfont.woff2",
    "/fonts/fontawesome-webfont.ttf?v=4.6.3":"/fonts/fontawesome-webfont.ttf"
    }
class ServerException(Exception):
    '''服务器内部错误'''
    pass

class RequestHandler(BaseHTTPRequestHandler):

    Error_Page = """\
    <html>
    <body>
    
    </body>
    
<html><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <body>
<h1>出错了喵</h1>

    <h3>{msg}</h3>

    </body>
    </html>
    </html>
    """

    def do_GET(self):
        full_path2="啊肯定没有"
        try:
            full_path2=(os.getcwd()+teshuzhixiang[self.path])
            print("cnm")
        except:
            pass
        try:
            #print(self.path)
            # 文件完整路径
            # print(os.getcwd() + self.path)
            #如C:\Users\Administrator\Desktop\我的学习资料\python\web_server /plain.html
            full_path = os.getcwd() + self.path
            #print(os.getcwd())
            #优先考虑allhs
            try:
                
                page=allhs.func[self.path](self.path)
               
                
                self.send_response(200)
                
                self.send_header("Content-type", "text/html")
                
                #self.send_header("Content-Length", str(len(page)+23333))
                self.end_headers()
                
                self.wfile.write(page.encode("utf-8"))
                print("done.")
                print(page)
            except:
                #print(sys.print_exc())
            # 如果该路径不存在...
            
                if os.path.exists(full_path+"/index.html"):
                    #套壳
                    
                    with open("ke/1.html","rb") as f:
                        shang=f.read()
                    with open(full_path+"/index.html","rb") as f:
                        zhong=f.read()
                    with open("ke/2.html","rb") as f:
                        xia=f.read()
                    self.send_response(200)
                    #self.send_header("Content-type", "text/html")
                    self.send_header("Content-Length", str(len(shang)+len(zhong)+len(xia)))
                    self.end_headers()
                    self.wfile.write(shang)
                    self.wfile.write(zhong)
                    self.wfile.write(xia)
                elif (not os.path.exists(full_path)) and (not os.path.exists(full_path2)):
                    #抛出异常：文件未找到
                    
                    self.handle_error("本喵竟然找不到文件（{0}）".format(self.path),404)
                # 如果该路径是一个文件
                elif os.path.isfile(full_path):
                    
                    #调用 handle_file 处理该文件
                    self.handle_file(full_path)
                elif os.path.isfile(full_path2):
                    
                    #调用 handle_file 处理该文件
                    self.handle_file(full_path2)
                # 如果该路径不是一个文件
                
                else:
                    #抛出异常：该路径为不知名对象
                    self.handle_error("本喵也不知道发生了什么（{0}）".format(self.path),502)
        # 处理异常
        except Exception as msg:
            print(msg)
            

    def handle_error(self, msg,code):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"),code)


    def create_page(self):
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
        }
        page = self.Page.format(**values)
        return page
	
    def send_content(self,content,status=200,typef="text/html"):
        self.send_response(status)
        #self.send_header("Content-type",typef)
        #self.send_header("Content-Length",str(len(content)))
        self.end_headers()
        self.wfile.write(content)
	# 文件操纵：发送内容
    def handle_file(self,full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content,typef="text")#二进制
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

if __name__ == '__main__':
    serverAddress = ('', 9090)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
