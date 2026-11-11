import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="KTCĐHA | Thư viện kỹ thuật CĐHA", page_icon="🩺", layout="wide", initial_sidebar_state="collapsed")
BASE = Path(__file__).resolve().parent

def load_articles():
    for file in (BASE / "articles.json", BASE / "data" / "articles.json"):
        if file.exists():
            try:
                value = json.loads(file.read_text(encoding="utf-8"))
                return value if isinstance(value, list) else []
            except (ValueError, OSError):
                st.warning("Không đọc được dữ liệu articles.json")
                return []
    return []

ARTICLES = load_articles()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');
:root{--teal:#007e96;--aqua:#92d7db;--ink:#153a45}
html,body,[class*="st-"],button,input{font-family:'Be Vietnam Pro',sans-serif!important}
[data-testid="stAppViewContainer"]{background:linear-gradient(155deg,#e0f3f5 0%,#f0fafb 45%,#d7eff2 100%)}
[data-testid="stSidebar"],[data-testid="collapsedControl"]{display:none!important}
header[data-testid="stHeader"]{background:transparent}
.block-container{max-width:1190px!important;padding-top:1rem!important;padding-bottom:3rem!important}
#MainMenu,footer{visibility:hidden}
.site-head{display:flex;align-items:center;justify-content:space-between;padding:22px 30px;border:1px solid #006f85;border-radius:20px;background:linear-gradient(105deg,#006c83,#0097aa);box-shadow:0 14px 32px rgba(0,104,125,.18)}
.brand{display:flex;align-items:center;gap:12px}
.brandmark{width:44px;height:44px;border-radius:13px;background:#a3e4e7;color:#006b80;font-size:25px;font-weight:800;display:flex;align-items:center;justify-content:center}
.brandtitle{font-size:1.45rem;color:white;font-weight:800;letter-spacing:-.04em;line-height:1.2}
.brandsub{font-size:.69rem;color:#d4f4f5;letter-spacing:.055em;margin-top:3px}
.headright{font-size:.75rem;color:#dcf7f8;font-weight:600}
.intro{padding:49px 0 37px;text-align:center}
.kicker{font-size:.78rem;color:#007e96;font-weight:800;letter-spacing:.15em}
.intro h1{font-size:2.55rem!important;color:#173c49!important;margin:12px 0 10px;line-height:1.35;font-weight:800}
.intro p{font-size:.99rem;color:#6b8a94;margin:0}
.modcard{height:285px;background:linear-gradient(145deg,#ffffff 0%,#dcf3f5 100%);border:1px solid #b7e1e6;border-top:5px solid #00849b;border-radius:24px;padding:32px 22px 18px;box-shadow:0 16px 35px rgba(0,104,125,.14);text-align:center;transition:transform .2s,box-shadow .2s}
.modcard:hover{transform:translateY(-4px);box-shadow:0 17px 32px rgba(20,81,96,.11)}
.modvisual{width:126px;height:116px;margin:0 auto 13px;display:flex;align-items:center;justify-content:center;background:linear-gradient(140deg,#d1eef2,#aee0e6);border-radius:22px}
.modvisual svg{width:100px;height:100px}
.modname{font-size:1.5rem;font-weight:800;color:#075d72}
.moddesc{font-size:.79rem;color:#7995a0;margin-top:4px}
div.stButton>button{background:#007e96!important;color:white!important;border:1px solid #007e96!important;border-radius:12px!important;font-weight:700!important;min-height:48px!important;width:100%!important;box-shadow:0 5px 12px rgba(0,126,150,.13)}
div.stButton>button:hover{background:#00687d!important;border-color:#00687d!important;color:white!important}
[data-testid="stHorizontalBlock"]{gap:22px}
.sectiontitle{margin:26px 0 12px;color:#174656;font-weight:800;font-size:1.4rem}
.subcard{height:122px;border:1px solid #b7e1e6;background:linear-gradient(140deg,#ffffff,#e0f4f6);border-radius:16px;padding:19px 17px}
.subcard h3{font-size:1.05rem;margin:0 0 8px;color:#126c80}
.subcard p{font-size:.82rem;color:#7b969e;line-height:1.6;margin:0}
.note{text-align:center;color:#59858f;font-size:.76rem;margin-top:45px}
@media(max-width:700px){.intro{padding:28px 0}.intro h1{font-size:1.65rem!important}.headright{display:none}.modcard{height:220px}.block-container{padding-left:1rem!important;padding-right:1rem!important}}
</style>
""", unsafe_allow_html=True)

ICONS = {
"X-quang": """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="23" y="8" width="54" height="84" rx="8" stroke="#007E96" stroke-width="3.5"/><path d="M50 20v62" stroke="#007E96" stroke-width="3"/><path d="M46 33c-14-14-20-2-20 15 0 17 9 24 20 24V33ZM54 33c14-14 20-2 20 15 0 17-9 24-20 24V33Z" fill="#92D7DB" fill-opacity=".75" stroke="#007E96" stroke-width="2.5"/><path d="M33 45l13 5m-13 7 13 3m21-15-13 5m13 7-13 3" stroke="white" stroke-width="2.5"/></svg>""",
"CT": """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="14" y="8" width="72" height="76" rx="17" fill="#E0F3F5" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="43" r="25" fill="white" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="43" r="17" stroke="#92D7DB" stroke-width="5"/><path d="M50 62v28m-22 0h44" stroke="#007E96" stroke-width="4" stroke-linecap="round"/><rect x="35" y="61" width="30" height="9" rx="4" fill="#92D7DB" stroke="#007E96" stroke-width="2"/></svg>""",
"MRI": """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="12" y="7" width="76" height="81" rx="19" fill="#E0F3F5" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="44" r="27" fill="white" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="44" r="18" fill="#D4EFF2" stroke="#92D7DB" stroke-width="3"/><path d="M50 52v35m-28 0h56" stroke="#007E96" stroke-width="4" stroke-linecap="round"/><path d="M38 65h24l8 15H30l8-15Z" fill="white" stroke="#007E96" stroke-width="2.5"/></svg>"""
}
SUBS = {
"X-quang": [("Quy trình chụp", "Tư thế chụp và kỹ thuật thực hiện"), ("Kỹ thuật X-quang", "Thông số và chất lượng hình ảnh"), ("Hình ảnh bệnh lý", "Nhận diện các dấu hiệu X-quang")],
"CT": [("Quy trình chụp", "Các quy trình theo vùng giải phẫu"), ("Kỹ thuật CT", "Thông số và tái tạo hình ảnh"), ("Hình ảnh bệnh lý", "Dấu hiệu bệnh lý trên CT")],
"MRI": [("Quy trình chụp", "Định vị lát cắt và chuỗi xung"), ("Kỹ thuật MRI", "Chuỗi xung và tối ưu hình ảnh"), ("Hình ảnh bệnh lý", "Dấu hiệu bệnh lý trên MRI")]
}
EN = {"X-quang":"RADIOGRAPHY", "CT":"COMPUTED TOMOGRAPHY", "MRI":"MAGNETIC RESONANCE"}
if "modality" not in st.session_state: st.session_state.modality=None
if "sub" not in st.session_state: st.session_state.sub=None

def go(mod=None, sub=None):
    st.session_state.modality=mod
    st.session_state.sub=sub
    st.rerun()

st.markdown('<div class="site-head"><div class="brand"><div class="brandmark">✚</div><div><div class="brandtitle">KTCĐHA</div><div class="brandsub">THƯ VIỆN KỸ THUẬT CHẨN ĐOÁN HÌNH ẢNH</div></div></div><div class="headright">BY HUUHUY</div></div>', unsafe_allow_html=True)
mod=st.session_state.modality
sub=st.session_state.sub
if mod is None:
    st.markdown('<div class="intro"><div class="kicker">KHÁM PHÁ CHUYÊN NGÀNH</div><h1>Thư viện Chẩn đoán Hình ảnh</h1><p>Chọn một chuyên ngành để xem các nội dung đào tạo</p></div>', unsafe_allow_html=True)
    cols=st.columns(3, gap="large")
    for col,name in zip(cols,("X-quang","CT","MRI")):
        with col:
            st.markdown(f'<div class="modcard"><div class="modvisual">{ICONS[name]}</div><div class="modname">{name}</div><div class="moddesc">{EN[name]}</div></div>', unsafe_allow_html=True)
            if st.button(f"VÀO THƯ VIỆN {name.upper()}  →", key=f"open-{name}"):
                go(name)
elif sub is None:
    if st.button("← TRANG CHỦ", key="home"): go()
    st.markdown(f'<div class="sectiontitle">THƯ VIỆN {mod.upper()}</div>', unsafe_allow_html=True)
    st.caption("Chọn nhóm kiến thức để xem danh sách bài học")
    cols=st.columns(3,gap="large")
    for col,(title,desc) in zip(cols,SUBS[mod]):
        with col:
            st.markdown(f'<div class="subcard"><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
            if st.button(f"Xem {title.lower()} →",key=title):
                go(mod,title)
else:
    if st.button(f"← QUAY LẠI {mod.upper()}",key="back"): go(mod)
    st.markdown(f'<div class="sectiontitle">{sub} / {mod}</div>',unsafe_allow_html=True)
    q=st.text_input("Tìm bài học",placeholder="Nhập tên bài hoặc từ khóa...")
    def matches(a):
        cat=str(a.get("category","")).casefold()
        if sub=="Quy trình chụp": return any(x in cat for x in ("quy trình","protocol","planning"))
        if sub.startswith("Kỹ thuật"): return any(x in cat for x in ("kỹ thuật","technical","sequence","image characteristics"))
        return any(x in cat for x in ("bệnh lý","pathology"))
    items=[a for a in ARTICLES if a.get("modality")==mod and matches(a)]
    if q.strip():
        items=[a for a in items if q.casefold() in " ".join(str(a.get(k,"")) for k in ("title","category","summary","content")).casefold()]
    st.caption(f"{len(items)} bài học")
    if not items:
        st.info("Chưa có bài học thuộc mục này. Có thể bổ sung nội dung sau.")
    for a in items:
        with st.expander(a.get("title","Bài học")):
            st.markdown(a.get("content",""))
            for ref in a.get("references",[]):
                if isinstance(ref,str) and ref.startswith(("http://","https://")):
                    st.markdown(f"Nguồn: {ref}")
            st.caption("Nội dung học tập; cần kiểm tra trước khi áp dụng thực hành.")
st.markdown('<div class="note">KTCĐHA • BY HUUHUY · THƯ VIỆN HỌC TẬP CHẨN ĐOÁN HÌNH ẢNH</div>',unsafe_allow_html=True)
