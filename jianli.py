import streamlit as st

# 设置页面配置
st.set_page_config(page_title="个人简历生成器", page_icon="💼", layout="wide")

# 页面标题
st.title("📄 个人简历生成器")

# 分栏布局：左侧输入，右侧展示简历
c1, c2 = st.columns([1, 2])

with c1:
    st.header("📝 个人信息表单")
    
    user_name = st.text_input("姓名", "张三")
    user_age = st.slider("年龄", 0, 100, 25)
    job_title = st.selectbox("职业", ["学生", "工程师", "设计师", "教师", "其他"])
    skills = st.multiselect("技能", [
        "Python", "JavaScript", "数据分析", "UI/UX", "项目管理", 
        "机器学习", "前端开发", "后端开发"
    ])
    experience = st.text_area("工作经验（可选）", "暂无工作经验")

with c2:
    st.header("🎯 你的简历")
    
    # 模拟简历样式
    with st.container():
        st.markdown("""
        <style>
        .resume {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-family: 'Segoe UI', sans-serif;
        }
        .section-title {
            color: #2c3e50;
            margin-top: 15px;
            font-size: 1.2em;
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
        }
        .info-item {
            margin: 10px 0;
            font-size: 1em;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="resume">', unsafe_allow_html=True)
        
        st.markdown(f"<h2>{user_name}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>年龄：</strong>{user_age}岁</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>职业：</strong>{job_title}</p>", unsafe_allow_html=True)
        
        if skills:
            st.markdown("<p><strong>技能：</strong></p>", unsafe_allow_html=True)
            skill_str = ", ".join(skills)
            st.markdown(f"<p>{skill_str}</p>", unsafe_allow_html=True)
        
        if experience.strip():
            st.markdown("<p><strong>工作经验：</strong></p>", unsafe_allow_html=True)
            st.markdown(f"<p>{experience}</p>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# 添加底部说明
st.write("---")
st.caption("📌 提示：输入你的信息，即可生成一份简洁的电子简历！")
