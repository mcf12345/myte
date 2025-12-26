import streamlit as st
import pandas as pd
from PIL import Image
import io
import os

# 设置页面基本配置
st.set_page_config(
    page_title="综合网站",
    page_icon="🌐",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
<style>
    .stApp {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
        padding-top: 20px;
    }
    .stSidebar [data-testid="stRadio"] label {
        font-size: 16px;
        padding: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------- 核心：侧边栏导航 ----------------------
st.sidebar.title("📚 网站导航")
st.sidebar.markdown("---")  # 分隔线
page = st.sidebar.radio(
    "选择功能模块",
    ["首页", "视频中心", "音乐播放器", "相册网站", "KTV数据分析", "个人简历生成器"],
    index=0,
    key="sidebar_nav"
)
st.sidebar.markdown("---")


# ---------------------- 首页 ----------------------
if page == "首页":
    st.header("欢迎来到综合多媒体网站")
 
    # 扩展器：网站说明
    with st.expander("📖 关于本网站", expanded=True):
        st.write("""
        本网站整合了以下实训内容：
        - 视频中心：实训1（视频播放功能）
        - 音乐播放器：实训3（音频播放功能）
        - 相册网站：实训4（图片展示功能）
        - KTV数据分析：实训5（数据可视化功能）
        - 个人简历生成器：实训6（表单与预览功能）
        """)
    
    # 列容器：功能预览
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📹 视频中心")
        st.video("https://www.w3school.com.cn/example/html5/mov_bbb.mp4")
    with col2:
        st.subheader("🎵 音乐播放器")
        st.audio("https://music.163.com/song/media/outer/url?id=3312734747.mp3")
    with col3:
        st.subheader("🖼️ 相册网站")
        st.image("https://img-baofun.zhhainiao.com/fs/75b3cf7355b91ef08df8d735f4724c13.jpg", caption="小狗")

# ---------------------- 视频中心（实训1） ----------------------
elif page == "视频中心":
    st.header("🎬 视频中心")
    st.markdown("---")
    
    # 视频列表
    video_arr = [
        {'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4', 'title': '不良人-第1集'},
        {'url': 'https://www.w3schools.com/html/movie.mp4', 'title': '不良人-第2集'},
        {'url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4', 'title': '不良人-第3集'},
    ]
    
    # 会话状态：保存当前播放索引
    if 'video_ind' not in st.session_state:
        st.session_state.video_ind = 0
    
    # 显示当前视频
    st.subheader(video_arr[st.session_state.video_ind]['title'])
    st.video(video_arr[st.session_state.video_ind]['url'])
    
    # 列容器：剧集切换按钮
    cols = st.columns(len(video_arr))
    for i, col in enumerate(cols):
        with col:
            st.button(
                f"第{i+1}集",
                key=f"video_btn_{i}",
                on_click=lambda idx=i: st.session_state.update(video_ind=idx),
                use_container_width=True
            )

# ---------------------- 音乐播放器（实训3） ----------------------
elif page == "音乐播放器":
    st.header("🎵 音乐播放器")
    st.markdown("---")
    
    music_list = [
        {'url': 'https://music.163.com/song/media/outer/url?id=3312734747.mp3', 'img': 'http://p2.music.126.net/Qlau9o7vEllouRV9x7qEKg==/109951172215963831.jpg?param=130y130', 'title': 'Pretty-王鹤棣'},
        {'url': 'https://music.163.com/song/media/outer/url?id=3312735541.mp3', 'img': 'http://p1.music.126.net/vJPca_ni17kyiBs82J2LCA==/109951172215963424.jpg?param=130y130', 'title': '优雅-王鹤棣'},
    ]
    
    # 会话状态
    if 'music_ind' not in st.session_state:
        st.session_state.music_ind = 0
    
    # 列容器：封面 + 播放区域
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(music_list[st.session_state.music_ind]['img'], use_container_width=True)
    with col2:
        st.subheader(music_list[st.session_state.music_ind]['title'])
        st.audio(music_list[st.session_state.music_ind]['url'], format="audio/mp3")
    
    # 列容器：上一首/下一首
    col_prev, col_next = st.columns(2)
    with col_prev:
        st.button(
            "⬅️ 上一首",
            on_click=lambda: st.session_state.update(music_ind=(st.session_state.music_ind-1)%len(music_list)),
            use_container_width=True
        )
    with col_next:
        st.button(
            "下一首 ➡️",
            on_click=lambda: st.session_state.update(music_ind=(st.session_state.music_ind+1)%len(music_list)),
            use_container_width=True
        )

# ---------------------- 相册网站（实训4） ----------------------
elif page == "相册网站":
    st.header("🖼️ 相册网站")
    st.markdown("---")
    
    image_list = [
        {'url': 'https://img-baofun.zhhainiao.com/fs/75b3cf7355b91ef08df8d735f4724c13.jpg', 'title': '小狗'},
        {'url': 'https://wallpaperm.cmcm.com/0a600ff25939e144e04d2ea417bafa36.jpg', 'title': '小鸟'},
        {'url': 'https://ts1.tc.mm.bing.net/th/id/R-C.66d7b796377883a92aad65b283ef1f84?rik=sQ%2fKoYAcr%2bOwsw', 'title': '小猫'},
    ]
    
    # 会话状态
    if 'image_ind' not in st.session_state:
        st.session_state.image_ind = 0
    
    # 主图展示
    st.image(
        image_list[st.session_state.image_ind]['url'],
        caption=image_list[st.session_state.image_ind]['title'],
        use_container_width=True
    )
    
    # 列容器：切换按钮
    col_prev, col_next = st.columns(2)
    with col_prev:
        st.button(
            "⬅️ 上一张",
            on_click=lambda: st.session_state.update(image_ind=(st.session_state.image_ind-1)%len(image_list)),
            use_container_width=True
        )
    with col_next:
        st.button(
            "下一张 ➡️",
            on_click=lambda: st.session_state.update(image_ind=(st.session_state.image_ind+1)%len(image_list)),
            use_container_width=True
        )
    
    # 扩展器：缩略图预览
    with st.expander("🖨️ 全部图片预览", expanded=False):
        tabs = st.tabs([img['title'] for img in image_list])
        for i, tab in enumerate(tabs):
            with tab:
                st.image(image_list[i]['url'], use_container_width=True)

# ---------------------- KTV数据分析（实训5） ----------------------
elif page == "KTV数据分析":
    st.header("📊 南宁市KTV经营数据分析")
    st.markdown("---")
    
    # 模拟数据
    ktv_data = {
        "月份": ["01月", "02月", "03月", "04月", "05月", "06月"],
        "星光KTV": [280, 320, 350, 380, 420, 450],
        "乐迪KTV": [220, 250, 230, 260, 280, 300],
        "盛世KTV": [300, 310, 340, 360, 390, 410],
    }
    df = pd.DataFrame(ktv_data)
    
    # 选项卡：数据展示
    tab1, tab2 = st.tabs(["📋 数据表格", "📈 趋势图表"])
    with tab1:
        st.dataframe(df, use_container_width=True)
        with st.expander("💡 数据说明", expanded=False):
            st.write("表格展示南宁市3家KTV月度营收（单位：千元）")
    with tab2:
        st.line_chart(df, x="月份", y=["星光KTV", "乐迪KTV", "盛世KTV"], use_container_width=True)

# ---------------------- 个人简历生成器（实训6） ----------------------
elif page == "个人简历生成器":
    st.header("📝 个人简历生成器")
    st.markdown("---")
    
    # 列容器：表单 + 预览
    col_form, col_preview = st.columns([1, 2])
    with col_form:
        st.subheader("填写个人信息")
        # 基础信息
        name = st.text_input("姓名", "罗雨湾")
        position = st.text_input("应聘职位", "软件测试")
        phone = st.text_input("联系电话", "17677169536")
        email = st.text_input("邮箱", "237917611@qq.com")
        education = st.selectbox("学历", ["本科", "硕士", "博士"], index=0)
        
        # 扩展器：更多信息
        with st.expander("🔍 更多信息", expanded=False):
            gender = st.radio("性别", ["女", "男"], index=0)
            skills = st.multiselect("专业技能", ["Python", "Java", "SQL", "测试"], default=["Python", "测试"])
            bio = st.text_area("个人简介", "具备5年软件测试经验，熟悉自动化测试流程。")
    
    with col_preview:
        st.subheader("简历预览")
        st.markdown(f"# {name}")
        st.markdown(f"## 应聘职位：{position}")
        st.markdown("---")
        # 联系方式
        col_contact1, col_contact2 = st.columns(2)
        with col_contact1:
            st.write(f"📞 电话：{phone}")
            st.write(f"🎓 学历：{education}")
        with col_contact2:
            st.write(f"📧 邮箱：{email}")
            st.write(f"⚧️ 性别：{gender}")
        
        # 技能展示
        st.markdown("### 🛠️ 专业技能")
        skill_cols = st.columns(len(skills))
        for i, skill in enumerate(skills):
            skill_cols[i].markdown(f"✅ {skill}")
        
        # 个人简介
        st.markdown("### 📖 个人简介")
        st.write(bio)

