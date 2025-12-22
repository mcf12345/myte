import streamlit as st
# 设置网页配置：页面标题为“相册网站”，页面图标为笑脸表情
st.set_page_config(page_title='相册网站', page_icon='😀')

# 定义图片数据列表，每个元素是字典，包含图片URL和对应的描述文本
image_ua = [
    {
        'url': 'https://img-baofun.zhhainiao.com/fs/75b3cf7355b91ef08df8d735f4724c13.jpg', # 小狗图片的网络地址
        'text': '小狗' # 图片的描述文字（作为图片标题）
    },
    {
        'url': 'https://wallpaperm.cmcm.com/0a600ff25939e144e04d2ea417bafa36.jpg',# 小鸟图片的网络地址
        'text': '小鸟'# 图片的描述文字
    },
    {
        'url': 'https://ts1.tc.mm.bing.net/th/id/R-C.66d7b796377883a92aad65b283ef1f84?rik=sQ%2fKoYAcr%2bOwsw&riu=http%3a%2f%2fwww.quazero.com%2fuploads%2fallimg%2f140305%2f1-140305131415.jpg&ehk=Hxl%2fQ9pbEiuuybrGWTEPJOhvrFK9C3vyCcWicooXfNE%3d&risl=&pid=ImgRaw&r=0', # 小猫图片的网络地址
        'text': '小猫' # 图片的描述文字
    },
]

# 初始化会话状态：保存当前显示图片的索引，首次运行时设为0（显示第一张）
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前索引对应的图片和标题
st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 分割页面为两列容器，用于并排放置“上一张”和“下一张”按钮
c1, c2 = st.columns(2)

# 定义“下一张”按钮的逻辑：索引+1，取模实现循环（最后一张→第一张）
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

# 定义“上一张”按钮的逻辑：索引-1，取模实现循环（第一张→最后一张）
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)

with c1:
    # 给“上一张”按钮绑定prevImg函数，点击时执行逻辑
    st.button('上一张', use_container_width=True, on_click=prevImg)

with c2:
    # “下一张”按钮绑定nextImg函数（原有逻辑保留）
    st.button('下一张', use_container_width=True, on_click=nextImg)
