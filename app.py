import json
import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="KTCĐHA | Thư viện Chẩn đoán Hình ảnh", page_icon="🏥", layout="wide", initial_sidebar_state="collapsed")
BASE = Path(__file__).parent

def load_articles():
    path = BASE / "articles.json"
    if not path.exists():
        path = BASE / "data" / "articles.json"
    if not path.exists():
        return []
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, list) else []
    except (OSError, ValueError):
        st.error("Không thể đọc articles.json.")
        return []

ARTICLES = load_articles()
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');
html,body,[data-testid="stApp"],button,input {font-family:'Be Vietnam Pro',sans-serif!important}
[data-testid="stAppViewContainer"]{background:#F7FBFC}
[data-testid="stSidebar"],[data-testid="collapsedControl"]{display:none!important}
.block-container{max-width:1160px;padding-top:1.7rem;padding-bottom:3rem}
h1,h2,h3{color:#075C72;letter-spacing:-.035em}
.header{display:flex;align-items:center;gap:12px;margin-bottom:25px}
.logo{width:47px;height:47px;border-radius:13px;background:#DDF3F4;color:#00849B;display:flex;align-items:center;justify-content:center;font-size:25px;font-weight:800}
.brand{font-size:1.55rem;font-weight:800;color:#007C96;line-height:1.2}
.brand-sub{font-size:.69rem;color:#6997A0;letter-spacing:.08em}
.intro{text-align:center;padding:28px 10px 22px}
.eyebrow{font-size:.78rem;font-weight:800;letter-spacing:.13em;color:#00849B}
.intro h1{font-size:2.2rem;margin:12px 0}
.intro p{color:#688C95}
.mod-card{background:white;border:1px solid #D9EDF0;border-radius:22px;padding:25px 12px 15px;text-align:center;min-height:178px;box-shadow:0 9px 24px rgba(23,93,62,.04)}
.mod-icon{display:inline-flex;align-items:center;justify-content:center;width:92px;height:92px;border-radius:22px;background:#E7F7F8;margin-bottom:15px}.mod-icon img{width:72px;height:72px}
.mod-title{font-size:1.35rem;font-weight:800;color:#086D82}
.mod-en{font-size:.78rem;color:#7598A0;margin-top:5px}
.section-card{background:white;border:1px solid #D9EDF0;border-radius:15px;padding:18px;min-height:105px}
.section-card strong{color:#08778B}
.section-card p{color:#6B9299;font-size:.82rem;margin:7px 0 0}
div.stButton>button{border-radius:13px;border:1px solid #CDE8EC;background:#fff;color:#007C96;font-weight:700;width:100%;min-height:44px}
div.stButton>button:hover{background:#E7F7F8;border-color:#00849B;color:#006B82}
div[data-testid="stExpander"]{background:#fff;border-radius:13px}
.footer{border-top:1px solid #D9EDF0;color:#86A4AA;text-align:center;margin-top:40px;padding-top:18px;font-size:.75rem}
@media(max-width:700px){.intro h1{font-size:1.65rem}.mod-card{min-height:145px;padding:16px 5px}.mod-icon{width:70px;height:70px}.mod-icon img{width:56px;height:56px}.mod-title{font-size:1rem}.mod-en{font-size:.62rem}}
</style>
''',unsafe_allow_html=True)

if "section" not in st.session_state:
    st.session_state.section = None
if "subcategory" not in st.session_state:
    st.session_state.subcategory = None

def navigate(section=None, subcategory=None):
    st.session_state.section = section
    st.session_state.subcategory = subcategory
    st.rerun()

st.markdown('<div class="header"><div class="logo">✚</div><div><div class="brand">KTCĐHA</div><div class="brand-sub">THƯ VIỆN KỸ THUẬT CHẨN ĐOÁN HÌNH ẢNH</div></div></div>',unsafe_allow_html=True)

STRUCTURE = {
    "X-quang": [("Quy trình chụp", "Tư thế và kỹ thuật thực hiện"), ("Kỹ thuật X-quang", "Thông số và chất lượng hình ảnh"), ("Hình ảnh bệnh lý", "Nhận diện dấu hiệu trên X-quang")],
    "CT": [("Quy trình chụp", "Protocol theo vùng giải phẫu"), ("Kỹ thuật CT", "Tái tạo, thông số và tối ưu liều"), ("Hình ảnh bệnh lý", "Đặc điểm hình ảnh cắt lớp vi tính")],
    "MRI": [("Quy trình chụp", "Định vị, chuỗi xung và vùng giải phẫu"), ("Kỹ thuật MRI", "Chuỗi xung và tối ưu chất lượng ảnh"), ("Hình ảnh bệnh lý", "Các dấu hiệu bệnh lý trên MRI")]
}
EN = {"X-quang":"Radiography","CT":"Computed Tomography","MRI":"Magnetic Resonance Imaging"}
SVG_ICONS = {'X-quang': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none"><rect x="18" y="10" width="64" height="80" rx="10" stroke="#00849B" stroke-width="3"/><path d="M50 19v62M50 33c-10-11-24-8-24 5v13c0 13 9 17 24 19M50 33c10-11 24-8 24 5v13c0 13-9 17-24 19" stroke="#00849B" stroke-width="3" stroke-linecap="round"/><path d="M33 35l17 11 17-11M31 45l19 9 19-9M34 55l16 8 16-8" stroke="#71C9D1" stroke-width="2.5" stroke-linecap="round"/><path d="M39 75h22" stroke="#00849B" stroke-width="3" stroke-linecap="round"/></svg>', 'CT': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none"><rect x="13" y="10" width="74" height="70" rx="17" stroke="#00849B" stroke-width="4"/><circle cx="50" cy="45" r="24" stroke="#00849B" stroke-width="4"/><circle cx="50" cy="45" r="17" stroke="#71C9D1" stroke-width="3"/><path d="M50 58v31M27 89h46M32 72h36" stroke="#00849B" stroke-width="4" stroke-linecap="round"/><rect x="39" y="57" width="22" height="10" rx="4" fill="#D6F1F3" stroke="#00849B" stroke-width="2"/><path d="M77 24h4" stroke="#71C9D1" stroke-width="3" stroke-linecap="round"/></svg>', 'MRI': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none"><rect x="14" y="8" width="72" height="77" rx="18" stroke="#00849B" stroke-width="4"/><circle cx="50" cy="43" r="25" stroke="#00849B" stroke-width="4"/><circle cx="50" cy="43" r="18" stroke="#71C9D1" stroke-width="3"/><path d="M50 43v32M22 78h56M30 85h40" stroke="#00849B" stroke-width="3.5" stroke-linecap="round"/><path d="M38 65h24l8 13H30l8-13Z" fill="#D6F1F3" stroke="#00849B" stroke-width="2"/><path d="M40 26c5-4 15-4 20 0" stroke="#71C9D1" stroke-width="3" stroke-linecap="round"/></svg>'}
ICONS = {name: "data:image/svg+xml;base64," + base64.b64encode(source.encode("utf-8")).decode("ascii") for name, source in SVG_ICONS.items()}

def show_article(a):
    st.markdown(a.get("content", "Đang cập nhật nội dung."))
    refs = a.get("references", [])
    if isinstance(refs, list):
        for link in refs:
            if isinstance(link,str) and link.startswith(("https://","http://")):
                st.markdown(f"Nguồn: {link}")
    st.caption("Chỉ dùng cho mục đích đào tạo; cần kiểm tra nguồn và quy trình tại cơ sở.")

def category_match(article, sub):
    category = str(article.get("category","")).casefold()
    if sub == "Quy trình chụp":
        return any(x in category for x in ("quy trình","protocol","planning"))
    if sub in ("Kỹ thuật MRI","Kỹ thuật CT","Kỹ thuật X-quang"):
        return any(x in category for x in ("kỹ thuật","technical","image characteristics","sequence"))
    return any(x in category for x in ("bệnh lý","pathology"))

section = st.session_state.section
sub = st.session_state.subcategory
if section is None:
    st.markdown('<div class="intro"><div class="eyebrow">KTCĐHA • BY HUUHUY</div><h1>Thư viện Kỹ thuật Chẩn đoán Hình ảnh</h1><p>Lựa chọn chuyên ngành để bắt đầu khám phá</p></div>',unsafe_allow_html=True)
    cols=st.columns(3,gap="medium")
    for col,name in zip(cols,["X-quang","CT","MRI"]):
        with col:
            st.markdown(f'<div class="mod-card"><div class="mod-icon"><img src="{ICONS[name]}" alt="Biểu tượng {name}" width="72" height="72"></div><div class="mod-title">{name}</div><div class="mod-en">{EN[name]}</div></div>',unsafe_allow_html=True)
            if st.button(f"Khám phá {name}",key=f"nav-{name}"):
                navigate(name)
elif sub is None:
    if st.button("← Về trang chủ",key="back-home"):
        navigate()
    st.title(section)
    st.caption("Chọn nhóm nội dung muốn tìm hiểu.")
    cols=st.columns(3)
    for col,(name,description) in zip(cols,STRUCTURE[section]):
        with col:
            st.markdown(f'<div class="section-card"><strong>{name}</strong><p>{description}</p></div>',unsafe_allow_html=True)
            if st.button("Xem nội dung",key=f"cat-{section}-{name}"):
                navigate(section,name)
else:
    if st.button(f"← Quay lại {section}",key="back-section"):
        navigate(section)
    st.title(f"{sub} · {section}")
    query=st.text_input("Tìm bài học",placeholder="Nhập từ khóa hoặc tên vùng giải phẫu...")
    items=[a for a in ARTICLES if a.get("modality")==section and category_match(a,sub)]
    if query.strip():
        q=query.strip().casefold()
        items=[a for a in items if q in " ".join(str(a.get(k,"")) for k in ("title","summary","content","category")).casefold()]
    st.caption(f"{len(items)} bài học")
    if not items:
        st.info("Chuyên mục đã sẵn sàng. Nội dung sẽ được bổ sung khi có tài liệu nguồn được kiểm chứng.")
    for a in items:
        with st.expander(a.get("title","Bài học")):
            show_article(a)

st.markdown('<div class="footer">KTCĐHA by HUUHUY · Nền tảng học tập hình ảnh y học · Không thay thế quy trình bệnh viện</div>',unsafe_allow_html=True)
