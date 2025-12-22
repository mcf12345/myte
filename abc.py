import streamlit as st
# 设置网页配置：页面标题为“相册网站”，页面图标为笑脸表情
st.set_page_config(page_title='相册网站', page_icon='😀')

# 定义图片数据列表，每个元素是字典，包含图片URL和对应的描述文本
image_ua = [
    {
        'url': 'https://cdn.britannica.com/73/9173-050-9D9EA4BA.jpg', # 小鱼图片的网络地址
        'text': '小鱼' # 图片的描述文字（作为图片标题）
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

# 将当前的索引存储到内存中，如果内存中没有ind，我才要0，如果有就不设置ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 课本73 分列容器(2)
c1, c2 = st.columns(2)

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

with c1:
    # 课本122页 按钮
    st.button('上一张', use_container_width=True)

with c2:
    st.button('下一张', use_container_width=True, on_click=nextImg)
