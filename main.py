# coding:utf-8
import json, logging, sys

def run():
    mp = Mission_Planning()
    while True:
        try:
            input_ = raw_input()
            if input_ == 'end' or input_ == 'exit':
                break
            input_ = json.loads(input_)
            assert type(input_) is dict
            assert 'func' in input_
            opts = {
                'create_mission': lambda :mp.create_mission(input_['args']),
                'add_data': lambda :mp.add_data(input_['args']),
                'get_main_ui_display': lambda :mp.get_main_ui_display(),
                'get_mission_planning_res': lambda :mp.get_mission_planning_res(),
            }
            print opts[input_['func']]()
        except Exception as e:
            print e



# 第三课题任务规划软件的交互模块
# 可以用jythonc在java中调用 https://wiki.python.org/jython/LearningJython
class Mission_Planning(object):
    def __init__(self):
        pass

    '''
    由应用方/操作人员调用
    输入
    name: 任务名,字符类型
    mission_type: in ['large_scale', 'midium_scale', 'small_scale']
    mission_level: in ['science_experiment', 'normal_mission', 'urgent_mission']
    mission_area: 任务地理区域, [(x1,y1),(x2,y2)...] 一个由list表示的多边形
    weather_condition: in ['rainy', 'sunny', ......]
    wind: in [0,1,2,3,4...]#数字代表风力级别
    sensor: in ['optical', 'nir', ...]
    platform: in ['multi-rotors', 'fixed-wing', ...]
    flying_height: [min_height, max_height]
    flying_speed: [min_speed, max_speed]
    shooting_space_seconds: [min_space, max_space]
    begin_time: like '2018-11-13-14-00'
    end_time: like '2018-11-13-14-00'
    返回
    任务创建的结果:成功or失败
    '''

    def create_mission(self, input_):
        try:
            input_ = str(input_)
            input_ = json.loads(input_)
            assert 'name' in input_

            return input_
        except Exception as e:
            logging.exception(e)
            return 0

    '''
    由应用方/界面调用
    作为create_mission的补充输入,可以添加资源/地图数据,实时数据等
    输入
    json格式的list
    [data1, data2,...]
    其中每个data为一个dict,包括字段
    type: 资源类型
    resources_data: 具体资源
    # TODO 细化具体需要哪些data,如地理底图数据等
    返回
    添加数据的结果:成功or失败
    '''
    def add_data(self, input_):
        try:
            input_ = str(input_)
            input_ = json.loads(input_)

            return input_
        except Exception as e:
            logging.exception(e)
            return 0

    '''
    由后端程序
    获取显示状态
    返回 一个json格式字符串,解析后类型为dict,有以下字段:
    'title': 主程序标题
    'mission_type': 界面上的任务类型 等
    # TODO 明确主界面需要显示的内容
    '''
    def get_main_ui_display(self):
        res = {
            'title': 'main_window_1',
            'mission_type': 'large_scale'
        }
        return json.dumps(res)

    '''
    获取任务规划结果 - 可以发给控制中心执行飞行的结果
    返回值 json格式dict 内容包括:
    'name':'test_mission', //任务名
    'mission_type': MissionType, //任务类型(洪涝 or 反恐 or 生态),枚举型
    'mission_area':[(x1,y1),(x2,y2)...], //要求任务区域:list类型表示的多边形,代表任务区域
    'platform': Platform, //要求平台:枚举类型
    'camera': Camera, //要求相机(载荷):枚举类型
    'begin_time': Unix_time, //任务开始时间, 0即立即开始

    'flying_height': [min_height, max_height], //飞行高度
    'flying_speed': [min_speed, max_speed], //飞行速度
    'shooting_space_seconds': [min_space, max_space], //拍摄间隔
    'track': [(x1,y1),(x2,y2)...], //航迹
    '''
    def get_mission_planning_res(self):
        res = {
            'name': 'mission1',
            'mission_type': 'large_scale',
            'mission_area': [(116.6523885,36.9449586),(116.6523645,36.9443586),(116.6677850,36.9536846),(116.6677474,36.9536833),(116.6677848,36.9536836)]
        }
        return json.dumps(res)

if __name__ == '__main__':
    run()
