"""程序入口点。"""
import os
import logging
#from pathlib import Path # 不敢动不感动。
"""部分变量说明"""
# version: 程序版本号
# PCL_exe_path: [get_pcl_path()] Plain Craft Launcher 2.exe 文件所在目录的名字
# PCL_dir_path: [get_pcl_path()] Plain Craft Launcher 2.exe 文件所在目录下 "PCL" 文件夹的名字
# now_time: 计算机本地时间
# setup_ini_data: [backup_pcl_config()] setup.ini 文件内容
# UiLauncherTheme: 获取当前主题类型，14为自定义主题
# UiLauncherTransparent: 获取当前透明度，0为40%不透明，600为100%不透明
# UiLauncherDelta: 获取当前主题色调渐变，0为-90色调渐变，180为+180色调渐变
# UiLauncherSat: 获取当前主题饱和度，0为0%饱和度，100为100%饱和度
# UiLauncherHue: 获取当前主题色调，0为0°色调，360为360°色调
# UiLauncherLight: 获取当前主题亮度，0为-20亮度，40为+20亮度
# save_file_name: 保存的文件名
"""部分函数说明"""
# get_pcl_path(): 获取 Plain Craft Launcher 2.exe 目录位置和 "PCL" 文件夹
# backup_pcl_config(): 备份 PCL 配置文件
# get_theme_color(): 获取 setup.ini 里面的自定义主题的颜色值
"""重要全局变量设置"""
version = "1.0.0"
def get_pcl_path():
    global PCL_exe_path, PCL_dir_path
    PCL_exe_path = os.path.dirname(os.path.abspath("Plain Craft Launcher 2.exe"))
    PCL_dir_path = os.path.join(PCL_exe_path, "PCL")
    if not os.path.exists(PCL_dir_path):
        print("这里好像没有 PCL 文件夹，请确保程序的位置和PCL exe在同一目录下且有 PCL 文件夹。")
        input("按任意键后回车退出。")
        exit()
get_pcl_path()
os.system("cls")
"""配置目录"""
if not os.path.exists(f'{PCL_exe_path}/PCL2 Theme Switcher'):
    os.mkdir(f'{PCL_exe_path}/PCL2 Theme Switcher/')
    os.mkdir(f'{PCL_exe_path}/PCL2 Theme Switcher/Logs')
    logging.info("[System] PCL2 Theme Switcher 目录创建成功。")
if not os.path.exists(f'{PCL_exe_path}/PCL2 Theme Switcher/Logs'):
    os.mkdir(f'{PCL_exe_path}/PCL2 Theme Switcher/Logs')
    logging.info("[System] PCL2 Theme Switcher/Logs 目录创建成功。")
"""配置日志"""
# 检测1~5
def modify_logs():
    def Log4(): # 将 Log4 弄到 Log5
        if os.path.exists(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log4.log"):
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log4.log", "r", encoding="utf-8") as log4:
                log4_data = log4.read() # 存储为
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log5.log", "w", encoding="utf-8") as log5:
                log5.write(log4_data) # 写入为
    def Log3(): # 将 Log3 弄到 Log4
        if os.path.exists(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log3.log"):
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log3.log", "r", encoding="utf-8") as log3:
                log3_data = log3.read() # 存储为
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log4.log", "w", encoding="utf-8") as log4:
                log4.write(log3_data) # 写入为
    def Log2(): # 将 Log2 弄到 Log3
        if os.path.exists(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log2.log"):
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log2.log", "r", encoding="utf-8") as log2:
                log2_data = log2.read() # 存储为
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log3.log", "w", encoding="utf-8") as log3:
                log3.write(log2_data)
    def Log1(): # 将 Log1 弄到 Log2
        if os.path.exists(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log1.log"):
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log1.log", "r", encoding="utf-8") as log1:
                log1_data = log1.read() # 存储为
            with open(PCL_exe_path+"/PCL2 Theme Switcher/Logs/Log2.log", "w", encoding="utf-8") as log2:
                log2.write(log1_data) # 写入为
    Log4() # 将 Log4 弄到 Log5
    Log3() # 将 Log3 弄到 Log4
    Log2() # 将 Log2 弄到 Log3
    Log1() # 将 Log1 弄到 Log2
    """重置 Log1.log"""
    with open("PCL2 Theme Switcher/Logs/Log1.log", "w", encoding="utf-8") as reset_log1:
        reset_log1.write("")
modify_logs()
logging.basicConfig(filename=f'{PCL_exe_path}/PCL2 Theme Switcher/Logs/Log1.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', encoding='utf-8')        
logging.info('[System] 新的进程已开始。') # First Commit
logging.info("[System] 程序版本："+version)
def backup_pcl_config():
    global setup_ini_data
    get_pcl_path() # 获取 "PCL" 目录位置
    if os.path.exists(PCL_dir_path): # 检测是否存在 "PCL" 文件夹
        logging.info("[Backup] PCL 文件夹存在。")
        print("已找到 PCL 文件夹。")
        if os.path.exists(PCL_dir_path+"/setup.ini"): # 检测是否存在 "setup.ini"
            logging.info(rf"[Backup] setup.ini 文件存在。位置为： {PCL_dir_path}\setup.ini") # logging - setup.ini
            print("已找到 PCL 配置文件。") # print - setup.ini
            logging.info(rf"[Backup] 正在备份 setup.ini 配置文件。备份后的文件位置为： {PCL_exe_path}\PCL2 Theme Switcher\setup.ini") # logging - backing up setup.ini
            print("正在备份 PCL 配置文件。") # print - backing up setup.ini
            with open(PCL_dir_path+"/setup.ini", 'r', encoding="utf-8") as setup_ini: # 读 setup.ini 内容
                setup_ini_data = setup_ini.read() # setup_ini_data 是 setup.ini 的内容
                logging.info("[Backup] 读取 setup.ini 完毕")
            with open(f'{PCL_exe_path}/PCL2 Theme Switcher/setup.ini', 'w', encoding="utf-8") as backup_setup_ini_data:
                backup_setup_ini_data.write(setup_ini_data)
                logging.info(rf"[Backup] setup.ini 已备份。备份到： {PCL_exe_path}\PCL2 Theme Switcher\setup.ini")
                print("setup.ini 已备份。")
        else:
            logging.error("[Backup] setup.ini 文件不存在。")
            print("\n")
            print("\033[1m没有找到位于 PCL 文件夹下的 setup.ini 文件。请确认你的 setup.ini 是否存在。\033[0m")
            exit()
    else:
        logging.error("[Backup] PCL 文件夹不存在。")
        print("\n")
        print("\033[1m没有找到 PCL 文件夹。请确认你的 PCL 文件夹是否存在。\033[0m")
        exit()
    # DIR (PCL_dir_path) 是我们优先需要的，它表示 "PCL" 文件夹的目录
    # print("DIR:",PCL_dir_path)
    # print("EXE:",PCL_exe_path)
def get_theme_color():
    global UiLauncherTheme
    global UiLauncherTransparent
    global UiLauncherDelta
    global UiLauncherSat
    global UiLauncherHue
    global UiLauncherLight
    global data
    """这是从 setup.ini 中提取主题颜色值，就是从 backup_pcl_config() 那边扣来的 =。=，这就是一个只能读取的 backup_pcl_config() 阉割版本（划掉）"""
    if os.path.exists(PCL_dir_path): # 检测是否存在 "PCL" 文件夹
        logging.info("[Get Theme Color] PCL 文件夹存在。")
        if os.path.exists(PCL_dir_path+"/setup.ini"): # 检测是否存在 "setup.ini"
            logging.info(rf"[Get Theme Color] setup.ini 文件存在。位置为： {PCL_dir_path}\setup.ini") # logging - setup.ini
            with open(PCL_dir_path+"/setup.ini", 'r', encoding="utf-8") as setup_ini: # 读 setup.ini 内容
                setup_ini_data = setup_ini.read() # setup_ini_data 是 setup.ini 的内容
                logging.info("[Get Theme Color] 读取 setup.ini 完毕")
        else:
            logging.error("[Get Theme Color] setup.ini 文件不存在。")
            print("\n")
            print("\033[1m没有找到位于 PCL 文件夹下的 setup.ini 文件。请确认你的 setup.ini 是否存在。\033[0m")
            exit()
    else:
        logging.error("[Get Theme Color] PCL 文件夹不存在。")
        print("\n")
        print("\033[1m没有找到 PCL 文件夹。请确认你的 PCL 文件夹是否存在。\033[0m")
        exit()
    data = setup_ini_data #好晕。。这个data和下面的我不知道是啥了。。。
    def extract_value(data, key):
        global mid_key
        for line in data.splitlines():
            if line.startswith(key):
                return line.split(":", 1)[1].strip()
            mid_key = key
        logging.warning("[Get Theme Color] "+key+": 没有那个数据。") # Designed by Ubuntu
        key = "error"
        return key # 没有找到数据时返回 "error"，供下面判断使用
    
    """开始获取主题值"""
    UiLauncherTheme = extract_value(data, "UiLauncherTheme") # 获取当前主题类型，14为自定义主题
    UiLauncherTransparent = extract_value(data, "UiLauncherTransparent") # 获取当前透明度，0为40%不透明，600为100%不透明
    UiLauncherDelta = extract_value(data, "UiLauncherDelta") # 获取当前主题色调渐变，0为-90色调渐变，180为+180色调渐变
    UiLauncherSat = extract_value(data, "UiLauncherSat") # 获取当前主题饱和度，0为0%饱和度，100为100%饱和度
    UiLauncherHue = extract_value(data, "UiLauncherHue") # 获取当前主题色调，0为0°色调，360为360°色调
    UiLauncherLight = extract_value(data, "UiLauncherLight") # 获取当前主题亮度，0为-20亮度，40为+20亮度

    """报告当前主题值"""
    logging.info("[Get Theme Color] UiLauncherTheme: "+UiLauncherTheme)
    logging.info("[Get Theme Color] UiLauncherTransparent: "+UiLauncherTransparent)
    logging.info("[Get Theme Color] UiLauncherDelta: "+UiLauncherDelta)
    logging.info("[Get Theme Color] UiLauncherSat: "+UiLauncherSat)
    logging.info("[Get Theme Color] UiLauncherHue: "+UiLauncherHue)
    logging.info("[Get Theme Color] UiLauncherLight: "+UiLauncherLight)
    
    if UiLauncherTheme != "14":
        logging.warning("[Get Theme Color] 当前的 UiLauncherTheme 不是 自定义主题(14)。")
        print("你好像并没有切换到自定义主题颜色下，虽然不会写进去，但是请注意一下！")
    if UiLauncherTransparent == "error":
        logging.warning("[Get Theme Color] UiLauncherTransparent 没有找到数据，已切换为默认的 600。")
        print("你好像并没有设置 PCL 主题的 \033[1m透明度\033[0m。已切换为默认设置。")
        UiLauncherTransparent = "600"
    if UiLauncherDelta == "error":
        logging.warning("[Get Theme Color] UiLauncherDelta 没有找到数据，已切换为默认的 90。")
        print("你好像并没有设置 PCL 主题的 \033[1m色调渐变\033[0m。已切换为默认设置。")
        UiLauncherDelta = "90"
    if UiLauncherSat == "error":
        logging.warning("[Get Theme Color] UiLauncherSat 没有找到数据，已切换为默认的 80。")
        print("你好像并没有设置 PCL 主题的 \033[1m饱和度\033[0m。已切换为默认设置。")
        UiLauncherSat = "80"
    if UiLauncherHue == "error":
        logging.warning("[Get Theme Color] UiLauncherHue 没有找到数据，已切换为默认的 180。")
        print("你好像并没有设置 PCL 主题的 \033[1m色调\033[0m。已切换为默认设置。")
        UiLauncherHue = "180"
    if UiLauncherLight == "error":
        logging.warning("[Get Theme Color] UiLauncherLight 没有找到数据，已切换为默认的 20。")
        print("你好像并没有设置 PCL 主题的 \033[1m亮度\033[0m。已切换为默认设置。")
        UiLauncherLight = "20"
        """default
        UiLauncherTheme:14
        UiLauncherTransparent:600
        UiLauncherHue:180
        UiLauncherDelta:90
        UiLauncherLight:20
        UiLauncherSat:80
        """
        """
        print(UiLauncherTransparent)
        print(UiLauncherDelta)
        print(UiLauncherSat)
        print(UiLauncherHue)
        print(UiLauncherLight)
        """
def tech_otakus_save_the_pcl_theme_color(): # 技术宅保存PCL主题颜色
    global save_file_name
    get_theme_color()
    if not os.path.exists("PCL2 Theme Switcher/saves"):
        os.mkdir("PCL2 Theme Switcher/saves")
        logging.info("[System] PCL2 Theme Switcher/saves 目录创建成功。")
    save_file_name = input("\n\033[1m键入你想保存文件的名字（无需带.ini）：\033[0m ")
    logging.info("[Save Theme Color] 正在保存主题颜色，文件名： "+save_file_name+".ini 。")
    if os.path.exists("PCL2 Theme Switcher/saves/"+save_file_name+".ini"):
        while True:
            logging.info("[Save Theme Color] 文件名已存在，询问是否重新键入或覆盖文件。")
            warning_file = input("\033[1m文件名已存在，请重新键入，或按 Enter 覆盖文件。\033[0m\n保存的文件名：")
            if warning_file == "":
                logging.info("[Save Theme Color] 文件名已存在，已覆盖文件。")
                print("\033[1m已选择覆盖文件。\033[0m")
                break
            if warning_file == save_file_name: # 这是警告后输入的和原本输的还是一样的文件名，那只能说你太闲了！
                continue # 干啥的？不到啊！
            else: # 这是如果你警告后输对其他的文件名，别搞混咯~
                save_file_name = warning_file # 保存文件名
                break # 退出循环
    with open("PCL2 Theme Switcher/saves/"+save_file_name+".ini", "w", encoding="utf-8") as save:
        save.write("UiLauncherTransparent:"+UiLauncherTransparent+"\n")
        logging.info("[Save Theme Color] 已写入 UiLauncherTransparent:"+UiLauncherTransparent)
        print("\n")
        print("已保存 \033[1m透明度:"+UiLauncherTransparent+"\033[0m")
        
        save.write("UiLauncherDelta:"+UiLauncherDelta+"\n")
        logging.info("[Save Theme Color] 已写入 UiLauncherDelta:"+UiLauncherDelta)
        print("已保存 \033[1m色调渐变:"+UiLauncherDelta+"\033[0m")
        
        save.write("UiLauncherSat:"+UiLauncherSat+"\n")
        logging.info("[Save Theme Color] 已写入 UiLauncherSat:"+UiLauncherSat)
        print("已保存 \033[1m饱和度:"+UiLauncherSat+"\033[0m")
        
        save.write("UiLauncherHue:"+UiLauncherHue+"\n")
        logging.info("[Save Theme Color] 已写入 UiLauncherHue:"+UiLauncherHue)
        print("已保存 \033[1m色调:"+UiLauncherHue+"\033[0m")
        
        save.write("UiLauncherLight:"+UiLauncherLight+"")
        logging.info("[Save Theme Color] 已写入 UiLauncherLight:"+UiLauncherLight)
        print("已保存 \033[1m亮度:"+UiLauncherLight+"\033[0m")

"""Part 2 - 写入(替换)文件"""
def write_ini(key: str, val): # designed by youzi-3222(youzi-2333)
    """
    写入 ini 文件。
    """
    file = PCL_dir_path+"/setup.ini"
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].startswith(f"{key}:"):
            lines[i] = f"{key}: {val}\n"
            break
    else:
        lines.append(f"{key}: {val}\n")

    with open(file, "w", encoding="utf-8") as f:
        f.writelines(lines)

def replace_pcl_theme_color(): # 技术宅替换PCL主题颜色
    print("\n") # 美观
    backup_pcl_config() # 好吧，整个程序只有这里调用了这个函数。。。
    files = os.listdir(PCL_exe_path+"/PCL2 Theme Switcher/saves") # 获取当前目录下的所有文件
    formatted_files = "\n".join([f"[*] {file}" for file in files]) # 格式化文件列表
    print("\n当前 Saves 文件夹下存储的文件：\n"+formatted_files)
    logging.info("[Replace] 当前 Saves 文件夹下存储的文件：\n"+formatted_files)
    while True:
        ini_file = input("\033[1m键入你想替换的文件名，目前仅支持打开此目录下 PCL2 Theme Switcher/saves 里面的配置文件，无需输入.ini\033[0m:  ")
        if os.path.exists(PCL_exe_path+"/PCL2 Theme Switcher/saves/"+ini_file+".ini"):
            logging.info("[Replace] 即将从此处替换 setup.ini： "+ini_file+".ini")
            with open("PCL2 Theme Switcher/saves/"+ini_file+".ini", "r", encoding="utf-8") as ready_replace:
                ready_replace_ini_data = ready_replace.read()
                data = ready_replace_ini_data
                def extract_value(data, key):
                    global mid_key
                    for line in data.splitlines():
                        if line.startswith(key):
                            return line.split(":", 1)[1].strip()
                    return key
            UiLauncherTransparent = extract_value(data, "UiLauncherTransparent")
            UiLauncherDelta = extract_value(data, "UiLauncherDelta") 
            UiLauncherSat = extract_value(data, "UiLauncherSat")
            UiLauncherHue = extract_value(data, "UiLauncherHue")
            UiLauncherLight = extract_value(data, "UiLauncherLight")
            write_ini("UiLauncherTransparent", UiLauncherTransparent)
            logging.info(f"[Replace] 已从 {ini_file}.ini 写入 UiLauncherTransparent(透明度):"+UiLauncherTransparent)
            print("\n") # 因为刚刚是 input 选择的，这里选择往下一行
            print(f"已从 {ini_file}.ini 写入 透明度:"+UiLauncherTransparent)
            
            write_ini("UiLauncherDelta", UiLauncherDelta)
            logging.info(f"[Replace] 已从 {ini_file}.ini 写入 UiLauncherDelta(色调渐变):"+UiLauncherDelta)
            print(f"已从 {ini_file}.ini 写入 色调渐变:"+UiLauncherDelta)
            
            write_ini("UiLauncherSat", UiLauncherSat)
            logging.info(f"[Replace] 已从 {ini_file}.ini 写入 UiLauncherSat(饱和度):"+UiLauncherSat)
            print(f"已从 {ini_file}.ini 写入 饱和度:"+UiLauncherSat)
            
            write_ini("UiLauncherHue", UiLauncherHue)
            logging.info(f"[Replace] 已从 {ini_file}.ini 写入 UiLauncherHue(色调):"+UiLauncherHue)
            print(f"已从 {ini_file}.ini 写入 色调:"+UiLauncherHue)
            
            write_ini("UiLauncherLight", UiLauncherLight)
            logging.info(f"[Replace] 已从 {ini_file}.ini 写入 UiLauncherLight(亮度):"+UiLauncherLight)
            print(f"已从 {ini_file}.ini 写入 亮度:"+UiLauncherLight)
            
            """结束语"""
            print("\n")
            print("\033[1m已成功替换 PCL 的主题颜色！\033[0m")
            r"""
            print(UiLauncherDelta)
            dataw = re.sub(r'UiLauncherTransparent:\d+',f"UiLauncherTransparent:{UiLauncherTransparent}", data)
            dataw = re.sub(r'UiLauncherDelta:\d+',f"UiLauncherDelta:{UiLauncherDelta}", data)
            dataw = re.sub(r'UiLauncherSat:\d+',f"UiLauncherSat:{UiLauncherSat}", data)
            dataw = re.sub(r'UiLauncherHue:\d+',f"UiLauncherHue:{UiLauncherHue}", data)
            dataw = re.sub(r'UiLauncherLight:\d+',f"UiLauncherLight:{UiLauncherLight}", data)
            with open(PCL_dir_path+"/setup.ini", "r", encoding="utf-8") as backup_setup:
                middle_backup_setup = backup_setup.read()
            with open(PCL_dir_path+"/setup_backup.ini", "w", encoding="utf-8") as next_backup_setup:
                last_backup_setup = middle_backup_setup
                next_backup_setup.write(last_backup_setup)
            with open(PCL_dir_path+"/setup.ini", "w", encoding="utf-8") as replace:
                replace.write(dataw)
            """
            with open(PCL_dir_path+"/setup.ini", "r", encoding="utf-8") as view_setup_ini:
                    temp_review = view_setup_ini.read()
                    logging.info(r"[Replace] 现在的 PCL\setup.ini 的内容为："+"\n"+temp_review)
            break
        else:
            logging.error(f"请求的文件 {ini_file}.ini 不存在，已请求用户重新选择。")
            print(f"文件 \033[1m{ini_file}.ini\033[0m 不存在，请重新输入\033[1m（无需带.ini）\033[0m 。")
def main():
    r_main = input("请选择你想操作的功能：\n1.\033[1m保存当前PCL的自定义主题颜色的配置\033[0m\n2.\033[1m替换PCL的主题颜色\033[0m\n3.\033[1m退出本程序\033[0m\n请选择：")
    get_pcl_path()
    if r_main == "1":
        logging.info("[Page] 切换到 1: 保存当前PCL的自定义主题颜色的配置")
        tech_otakus_save_the_pcl_theme_color()
    if r_main == "2":
        logging.info("[Page] 切换到 2: 替换PCL的主题颜色")
        replace_pcl_theme_color()
    if r_main == "3":
        """ 调试模式（
        os.startfile('Plain Craft Launcher 2.exe')
        os.system("python main.py") 
        """
        logging.info("[Page] 切换到 3: 退出本程序 | 一路走好~")
        print("Say Goodbye~")
        exit()
if __name__ == "__main__":
    main()