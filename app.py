import json
import html
from datetime import datetime, date
from zoneinfo import ZoneInfo
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

st.markdown('\n<style>\n.catalog-hero{margin:20px 0 24px;padding:30px 34px;border-radius:24px;background:linear-gradient(115deg,#006c84,#008da4 65%,#49b7be);box-shadow:0 16px 32px #006b8429;position:relative;overflow:hidden}\n.catalog-hero:after{content:"";position:absolute;right:-60px;top:-120px;width:300px;height:300px;border:38px solid #ffffff17;border-radius:50%}\n.catalog-hero .eyebrow{font-size:.72rem;letter-spacing:.15em;color:#d1f5f7;font-weight:800}\n.catalog-hero h2{font-size:1.85rem!important;color:white!important;margin:10px 0!important;line-height:1.4!important}\n.catalog-hero p{color:#e5f8fa;font-size:.88rem;max-width:660px}\n.catalog-chip{display:inline-block;margin:8px 8px 0 0;padding:7px 12px;border:1px solid #ffffff45;border-radius:25px;background:#ffffff1e;color:white;font-size:.74rem;font-weight:700}\n.catalog-label{font-size:.75rem;letter-spacing:.07em;color:#567c87;font-weight:800;margin:20px 0 8px}\n.catalog-number{font-size:.7rem;color:#00849b;font-weight:800;letter-spacing:.12em}\n.catalog-name{font-size:1rem;color:#164554;font-weight:800;line-height:1.55;margin:8px 0}\n.catalog-meta{font-size:.73rem;color:#72929a;margin-bottom:10px}\ndiv[data-testid="stVerticalBlockBorderWrapper"]{border-radius:19px!important;border-color:#b9dfe4!important;background:linear-gradient(145deg,#fff,#e9f8fa)!important;box-shadow:0 5px 17px #006c840b;transition:transform .18s,box-shadow .18s}\ndiv[data-testid="stVerticalBlockBorderWrapper"]:hover{transform:translateY(-2px);box-shadow:0 12px 24px #006c8420;border-color:#78c9d2!important}\n[data-testid="stTextInput"] input{border-radius:13px!important;background:#fff!important;min-height:48px!important}\n@media(max-width:700px){.catalog-hero{padding:22px}.catalog-hero h2{font-size:1.45rem!important}}\n</style>\n', unsafe_allow_html=True)

ICONS = {
"X-quang": """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="23" y="8" width="54" height="84" rx="8" stroke="#007E96" stroke-width="3.5"/><path d="M50 20v62" stroke="#007E96" stroke-width="3"/><path d="M46 33c-14-14-20-2-20 15 0 17 9 24 20 24V33ZM54 33c14-14 20-2 20 15 0 17-9 24-20 24V33Z" fill="#92D7DB" fill-opacity=".75" stroke="#007E96" stroke-width="2.5"/><path d="M33 45l13 5m-13 7 13 3m21-15-13 5m13 7-13 3" stroke="white" stroke-width="2.5"/></svg>""",
"CT": """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="14" y="8" width="72" height="76" rx="17" fill="#E0F3F5" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="43" r="25" fill="white" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="43" r="17" stroke="#92D7DB" stroke-width="5"/><path d="M50 62v28m-22 0h44" stroke="#007E96" stroke-width="4" stroke-linecap="round"/><rect x="35" y="61" width="30" height="9" rx="4" fill="#92D7DB" stroke="#007E96" stroke-width="2"/></svg>""",
"MRI": """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="12" y="7" width="76" height="81" rx="19" fill="#E0F3F5" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="44" r="27" fill="white" stroke="#007E96" stroke-width="3.5"/><circle cx="50" cy="44" r="18" fill="#D4EFF2" stroke="#92D7DB" stroke-width="3"/><path d="M50 52v35m-28 0h56" stroke="#007E96" stroke-width="4" stroke-linecap="round"/><path d="M38 65h24l8 15H30l8-15Z" fill="white" stroke="#007E96" stroke-width="2.5"/></svg>"""
}
SUBS = {
    "X-quang": [("Kỹ thuật chụp", "Danh sách kỹ thuật X-quang theo bộ phận"), ("Hình ảnh bệnh lý", "Hình ảnh và dấu hiệu bệnh lý X-quang")],
    "CT": [("Kỹ thuật chụp", "Danh sách kỹ thuật chụp cắt lớp vi tính"), ("Hình ảnh bệnh lý", "Hình ảnh và dấu hiệu bệnh lý trên CT")],
    "MRI": [("Kỹ thuật chụp", "Danh sách kỹ thuật chụp cộng hưởng từ"), ("Hình ảnh bệnh lý", "Hình ảnh và dấu hiệu bệnh lý trên MRI")],
}
EN = {"X-quang":"RADIOGRAPHY", "CT":"COMPUTED TOMOGRAPHY", "MRI":"MAGNETIC RESONANCE"}
if "modality" not in st.session_state: st.session_state.modality=None
if "sub" not in st.session_state: st.session_state.sub=None
if "xray_region" not in st.session_state: st.session_state.xray_region=None
if "xray_part" not in st.session_state: st.session_state.xray_part=None

def go(mod=None, sub=None):
    st.session_state.modality=mod
    st.session_state.sub=sub
    st.session_state.xray_region=None
    st.session_state.xray_part=None
    st.session_state.xray_article=None
    st.session_state.xray_group=None
    st.session_state.scan_article=None
    st.rerun()


# Danh mục tiêu đề kỹ thuật X-quang. Đây chỉ là tên bài, không phải nội dung kỹ thuật.
XRAY_CHEST_GROUP = "Kỹ thuật chụp X-quang phổi"
XRAY_CHEST_VIEWS = [
    "Kỹ thuật chụp X-quang ngực thẳng",
    "Kỹ thuật chụp X-quang ngực nghiêng",
    "Kỹ thuật chụp X-quang ngực chếch",
]
XRAY_TECHNIQUES = [
    XRAY_CHEST_GROUP,
    "Kỹ thuật chụp X-quang cột sống cổ",
    "Kỹ thuật chụp X-quang cột sống ngực",
    "Kỹ thuật chụp X-quang cột sống thắt lưng",
    "Kỹ thuật chụp X-quang cột sống cùng cụt",
    "Kỹ thuật chụp X-quang bụng KUB",
    "Kỹ thuật chụp X-quang bụng ASP",
    "Kỹ thuật chụp X-quang khung chậu",
    "Kỹ thuật chụp X-quang khớp háng",
    "Kỹ thuật chụp X-quang Blondeau",
    "Kỹ thuật chụp X-quang Hirtz",
    "Kỹ thuật chụp X-quang xương mũi nghiêng",
    "Kỹ thuật chụp X-quang sọ thẳng/nghiêng",
    "Kỹ thuật chụp X-quang Schüller",
    "Kỹ thuật chụp X-quang cổ nghiêng tia mềm",
    "Kỹ thuật chụp X-quang xương đòn",
    "Kỹ thuật chụp X-quang khớp vai",
    "Kỹ thuật chụp X-quang xương cánh tay",
    "Kỹ thuật chụp X-quang khớp khuỷu",
    "Kỹ thuật chụp X-quang xương cẳng tay",
    "Kỹ thuật chụp X-quang cổ tay",
    "Kỹ thuật chụp X-quang bàn tay",
    "Kỹ thuật chụp X-quang xương đùi",
    "Kỹ thuật chụp X-quang khớp gối",
    "Kỹ thuật chụp X-quang xương cẳng chân",
    "Kỹ thuật chụp X-quang cổ chân",
    "Kỹ thuật chụp X-quang bàn chân",
    "Kỹ thuật chụp X-quang phổi nhi AP",
    "Kỹ thuật chụp X-quang xương ức",
    "Kỹ thuật chụp X-quang cột sống toàn trục (Whole body)",
    "Kỹ thuật chụp X-quang Lower leg",
    "Kỹ thuật chụp X-quang VA",
]

# Tên kỹ thuật CT/MRI được chuẩn hóa để hiển thị, CHƯA xác minh
# là tên nguyên văn trong danh mục kỹ thuật Bộ Y tế.
CT_TECHNIQUES = [
    "Chụp CLVT sọ não không tiêm thuốc cản quang",
    "Chụp CLVT lồng ngực không tiêm thuốc cản quang",
    "Chụp CLVT lồng ngực có tiêm thuốc cản quang",
    "Chụp CLVT Bụng không tiêm thuốc cản quang",
    "Chụp CLVT Bụng có tiêm thuốc cản quang",
    "Chụp CLVT Xoang",
    "Chụp CLVT hàm mặt",
    "Chụp CLVT nha khoa",
    "Chụp CLVT phần mềm vùng cổ không tiêm thuốc cản quang",
    "Chụp CLVT phần mềm vùng cổ có tiêm thuốc cản quang",
    "Chụp CLVT cột sống cổ",
    "Chụp CLVT cột sống ngực",
    "Chụp CLVT cột sống thắt lưng",
    "Chụp CLVT chi trên",
    "Chụp CLVT chi dưới",
    "Chụp CLVT mạch máu não có tiêm thuốc cản quang (CTA)",
    "Chụp CLVT động mạch phổi có tiêm thuốc cản quang (CTPA)",
    "Chụp CLVT động mạch chủ ngực – bụng có tiêm thuốc cản quang (CTA)",
    "Chụp CLVT động mạch vành có tiêm thuốc cản quang (CCTA)",
    "Chụp CLVT mạch máu chi dưới có tiêm thuốc cản quang (CTA)",
    "Chụp CLVT mạch máu chi trên có tiêm thuốc cản quang (CTA)",
]
MRI_TECHNIQUES = [
    "Chụp CHT sọ não không tiêm thuốc đối quang từ",
    "Chụp CHT sọ não có tiêm thuốc đối quang từ",
    "Chụp CHT tuyến yên động học có tiêm thuốc đối quang từ (Dynamic)",
    "Chụp CHT hốc mắt có tiêm thuốc đối quang từ",
    "Chụp CHT cột sống cổ",
    "Chụp CHT cột sống ngực",
    "Chụp CHT cột sống thắt lưng",
    "Chụp CHT lồng ngực (phổi)",
    "Chụp CHT tầng bụng không tiêm thuốc đối quang từ",
    "Chụp CHT tầng bụng có tiêm thuốc đối quang từ",
    "Chụp CHT vùng chậu không tiêm thuốc đối quang từ",
    "Chụp CHT vùng chậu có tiêm thuốc đối quang từ",
    "Chụp CHT khớp vai",
    "Chụp CHT khớp khuỷu",
    "Chụp CHT cổ tay",
    "Chụp CHT khớp háng",
    "Chụp CHT khớp gối",
    "Chụp CHT cổ chân",
    "Chụp CHT phần mềm chi",
]
if "scan_article" not in st.session_state:
    st.session_state.scan_article = None


st.markdown('\n<style>\n/* v15: premium editorial library instead of repetitive cards */\n.catalog-hero{padding:36px 40px 34px!important;border-radius:26px!important;background:radial-gradient(circle at 92% 12%,#48bec8 0,transparent 29%),linear-gradient(115deg,#005b75,#007f97 60%,#16a3ae)!important;box-shadow:0 22px 42px #005a7528!important}\n.catalog-hero h2{font-size:2.05rem!important;letter-spacing:-.04em}\n.catalog-hero .eyebrow{letter-spacing:.2em!important}\n.catalog-label{padding:12px 3px;border-bottom:1px solid #add5dc;margin:25px 0 18px!important;font-size:.74rem!important}\n.catalog-illustration{height:76px;width:76px;display:flex;align-items:center;justify-content:center;border-radius:18px;background:linear-gradient(140deg,#cceff1,#f4ffff);border:1px solid #b6e0e4;box-shadow:inset 0 1px 0 #fff}\n.catalog-item-category{font-size:.65rem;font-weight:800;color:#007e96;letter-spacing:.12em;margin-bottom:8px}\n.catalog-item-category span{color:#91aab2}\n.catalog-item-name{font-size:1.05rem;font-weight:800;color:#173c4b;line-height:1.55;letter-spacing:-.02em}\n.catalog-item-sub{font-size:.73rem;color:#76949b;margin-top:8px}\ndiv[data-testid="stVerticalBlockBorderWrapper"]{border:1px solid #c2e0e4!important;border-left:4px solid #00869e!important;border-radius:17px!important;background:linear-gradient(110deg,#fff 10%,#f2fbfc 100%)!important;box-shadow:0 5px 17px #006c840a!important;transition:transform .18s,box-shadow .18s}\ndiv[data-testid="stVerticalBlockBorderWrapper"]:hover{transform:translateX(3px);box-shadow:0 12px 26px #006c8421!important;border-left-color:#27b5bd!important}\n@media(max-width:700px){.catalog-hero{padding:25px 22px!important}.catalog-hero h2{font-size:1.5rem!important}.catalog-illustration{height:50px;width:50px}.catalog-illustration svg{width:30px;height:30px}.catalog-item-name{font-size:.85rem}.catalog-item-sub{display:none}.catalog-item-category{font-size:.54rem}}\n</style>\n', unsafe_allow_html=True)

def catalog_header(title, eyebrow, description, count, status):
    st.markdown(
        f'<div class="catalog-hero"><div class="eyebrow">{html.escape(eyebrow)}</div>'
        f'<h2>{html.escape(title)}</h2><p>{html.escape(description)}</p>'
        f'<span class="catalog-chip">{count} mục kỹ thuật</span>'
        f'<span class="catalog-chip">{html.escape(status)}</span></div>',
        unsafe_allow_html=True,
    )

def catalog_tiles(titles, prefix, select):
    """Premium editorial list: one full-width technique per row, no tiled cards."""
    if not titles:
        st.info("Không tìm thấy kỹ thuật phù hợp.")
        return
    st.markdown(
        f'<div class="catalog-label">KHÁM PHÁ THƯ VIỆN <span style="float:right">'
        f'{len(titles):02d} KỸ THUẬT</span></div>',
        unsafe_allow_html=True,
    )
    # Numbering, topic label, and visual motif are presentation-only.
    for index, name in enumerate(titles):
        lower = name.casefold()
        if any(x in lower for x in ("mạch", "cta", "động mạch")):
            kind, symbol = "KHẢO SÁT MẠCH MÁU", "vascular"
        elif any(x in lower for x in ("cột sống", "thắt lưng", "cùng cụt")):
            kind, symbol = "CỘT SỐNG", "spine"
        elif any(x in lower for x in ("sọ", "não", "xoang", "mặt", "mũi", "hốc mắt", "tuyến yên", "schuller", "blondeau", "hirtz", "hirzt")):
            kind, symbol = "ĐẦU · MẶT · CỔ", "head"
        elif any(x in lower for x in ("phổi", "ngực", "bụng", "chậu", "kub", "asp", "ức")):
            kind, symbol = "NGỰC · BỤNG · CHẬU", "torso"
        else:
            kind, symbol = "CƠ XƯƠNG KHỚP", "bone"
        icons = {
            "vascular": '<path d="M24 7v10m0 0L13 29m11-12 11 12M13 29v11m22-11v11M13 40l-6 5m28-5 6 5"/>',
            "spine": '<path d="M24 5c-7 7 7 10 0 17s7 10 0 17 0 6 0 6"/><path d="M17 11h14M17 23h14M17 35h14"/>',
            "head": '<path d="M15 36c-7-5-9-17-3-25C18 3 32 4 37 13c4 8 0 17-8 21v9H17v-7z"/><path d="M16 23h3m10 0h3M20 30q4 4 8 0"/>',
            "torso": '<path d="M24 9v32M20 14c-6-7-13 0-13 13s9 14 13 6V14zm8 0c6-7 13 0 13 13s-9 14-13 6V14z"/>',
            "bone": '<path d="M13 11a6 6 0 1 0-8 8l22 22a6 6 0 1 0 8-8L13 11z"/><path d="M11 15l4-4m16 26 4-4"/>',
        }
        svg = (
            '<svg width="43" height="43" viewBox="0 0 48 48" fill="none" '
            'stroke="#007f96" stroke-width="2.2" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">'
            + icons[symbol] + '</svg>'
        )
        with st.container(border=True):
            left, middle, right = st.columns([0.95, 5.2, 1.55], gap="medium", vertical_alignment="center")
            with left:
                st.markdown(
                    f'<div class="catalog-illustration">{svg}</div>',
                    unsafe_allow_html=True,
                )
            with middle:
                st.markdown(
                    f'<div class="catalog-item-name">{html.escape(name)}</div>',
                    unsafe_allow_html=True,
                )
            with right:
                if st.button("KHÁM PHÁ  ↗", key=f"{prefix}-{index}", use_container_width=True):
                    select(name)
                    st.rerun()

def choose_scan(name):
    st.session_state.scan_article = name

def choose_xray(name):
    if name == XRAY_CHEST_GROUP:
        st.session_state.xray_group = name
    else:
        st.session_state.xray_article = name

def scan_library(mod):
    selected = st.session_state.scan_article
    titles = CT_TECHNIQUES if mod == "CT" else MRI_TECHNIQUES
    short = "CLVT" if mod == "CT" else "CHT"
    if selected is None:
        catalog_header(f"Kỹ thuật chụp {short}", f"THƯ VIỆN {mod} / KỸ THUẬT CHỤP",
                       "Danh mục kỹ thuật theo vùng khảo sát. Nội dung chuyên môn được bổ sung sau khi kiểm duyệt.",
                       len(titles), "Chờ đối chiếu tên Bộ Y tế")
        query = st.text_input("Tìm kỹ thuật", placeholder="Tìm vùng khảo sát, mạch máu, thuốc...", key=f"scan-query-{mod}")
        results = [name for name in titles if query.casefold().strip() in name.casefold()]
        catalog_tiles(results, f"scan-{mod}", choose_scan)
    else:
        if st.button("← DANH SÁCH KỸ THUẬT", key="scan-back"):
            st.session_state.scan_article = None
            st.rerun()
        st.title(selected)
        st.caption("Tên kỹ thuật đang chờ đối chiếu với văn bản Bộ Y tế.")
        articles = [
            a for a in ARTICLES
            if a.get("modality") == mod
            and a.get("reviewed") is True
            and str(a.get("title", "")).strip().casefold() == selected.casefold()
        ]
        if articles:
            for article in articles:
                st.markdown(article.get("content", ""))
                for ref in article.get("references", []):
                    if isinstance(ref, str) and ref.startswith(("https://", "http://")):
                        st.markdown(f"Nguồn: {ref}")
        else:
            st.info("Chưa có bài học được kiểm duyệt cho kỹ thuật này.")
            st.markdown("#### Nội dung sẽ bổ sung khi có tài liệu xác minh")
            for part in ("Chỉ định và phạm vi khảo sát", "Chuẩn bị và an toàn người bệnh",
                         "Tư thế và định vị", "Quy trình/chuỗi xung theo thiết bị",
                         "Thuốc cản quang/đối quang từ (nếu có chỉ định)",
                         "Tiêu chuẩn chất lượng hình ảnh", "Nguồn tài liệu và người kiểm duyệt"):
                st.markdown(f"- {part}")
            st.caption("Không tự động tạo thông số kỹ thuật hoặc hướng dẫn thực hành.")

if "xray_article" not in st.session_state:
    st.session_state.xray_article = None
if "xray_group" not in st.session_state:
    st.session_state.xray_group = None

def xray_library():
    chosen = st.session_state.xray_article
    group = st.session_state.xray_group
    if chosen is None:
        if group == XRAY_CHEST_GROUP:
            if st.button("← DANH SÁCH KỸ THUẬT", key="xray-group-back"):
                st.session_state.xray_group = None
                st.rerun()
            catalog_header("Kỹ thuật chụp X-quang phổi", "X-QUANG / TƯ THẾ CHỤP",
                           "Chọn một tư thế để mở bài học tương ứng.", len(XRAY_CHEST_VIEWS), "Thẳng · Nghiêng · Chếch")
            titles = XRAY_CHEST_VIEWS
        else:
            catalog_header("Kỹ thuật chụp X-quang", "THƯ VIỆN X-QUANG / KỸ THUẬT",
                           "Tra cứu nhanh kỹ thuật chụp theo bộ phận cơ thể.", len(XRAY_TECHNIQUES), "Chờ kiểm duyệt nội dung")
            query = st.text_input("Tìm kỹ thuật chụp", placeholder="Ví dụ: phổi, sọ, khớp gối...")
            titles = [t for t in XRAY_TECHNIQUES if query.casefold().strip() in t.casefold() or (t == XRAY_CHEST_GROUP and "ngực" in query.casefold())]
        catalog_tiles(titles, "xray", choose_xray)
    else:
        if st.button("← QUAY LẠI", key="xray-article-back"):
            st.session_state.xray_article = None
            st.rerun()
        st.title(chosen)
        # Chỉ hiển thị nội dung được đánh dấu đã kiểm duyệt trong articles.json.
        items = [
            a for a in ARTICLES
            if a.get("modality") == "X-quang"
            and a.get("reviewed") is True
            and str(a.get("title", "")).strip().casefold() == chosen.casefold()
        ]
        if not items:
            st.info("Bài này chưa có nội dung được kiểm duyệt. Bạn có thể bổ sung sau vào articles.json.")
            st.markdown("#### Bố cục bài học dự kiến")
            for section in ("Mục đích chụp", "Chuẩn bị người bệnh", "Tư thế chụp", "Tia trung tâm và điểm định tâm", "Giới hạn trường chiếu", "Tiêu chuẩn đánh giá ảnh", "Hình minh họa", "Nguồn tham khảo"):
                st.markdown(f"- {section}")
            st.caption("Chưa có hướng dẫn kỹ thuật hoặc thông số nào được tự động tạo.")
        for article in items:
            st.markdown(article.get("content", ""))
            for ref in article.get("references", []):
                if isinstance(ref, str) and ref.startswith(("https://", "http://")):
                    st.markdown(f"Nguồn: {ref}")

# Menu tiện ích dùng chung cho cả ba chuyên ngành.
# Các công cụ liên quan quyết định lâm sàng chưa được kích hoạt khi chưa xác minh.
EXTRA_TOOLS = [
    ("Hỏi AI", "Trợ lý tra cứu tài liệu"),
    ("Tính độ lọc cầu thận eGFR", "Công cụ tính eGFR"),
    ("Tính lượng thuốc & tốc độ tiêm", "Công cụ tính lượng thuốc và tốc độ tiêm"),
    ("Xử lý sốc phản vệ", "Tài liệu xử trí cấp cứu"),
    ("Tài liệu chuyên ngành", "Kho tài liệu tham khảo"),
    ("Sổ trực nội bộ", "Biểu mẫu giao ban phim và thuốc"),
]
if "utility_page" not in st.session_state:
    st.session_state.utility_page = None

def open_utility(name):
    st.session_state.utility_page = name
    st.rerun()

st.markdown("""
<style>
/* Menu tiện ích, giữ nguyên thiết kế thư viện */
.utility-title{font-size:1.45rem;font-weight:800;color:#174656;margin:22px 0 9px}
.utility-desc{font-size:.9rem;color:#668994;line-height:1.8}
[data-testid="stPopover"] button{border-radius:12px!important;font-weight:800!important}
</style>
""", unsafe_allow_html=True)
# Menu thả xuống bằng nút Streamlit thông thường: tránh lỗi icon của popover.
if "utility_menu_open" not in st.session_state:
    st.session_state.utility_menu_open = False

st.markdown("""
<style>
/* Nút menu teal, nổi bật trên nền sáng */
/* Menu nằm cố định góc trên bên trái, độc lập với banner KTCĐHA. */
.st-key-floating_utility_menu {
  position:fixed!important;
  top:118px!important;
  left:20px!important;
  z-index:999!important;
  width:245px!important;
  max-width:calc(100vw - 40px)!important;
}
.st-key-floating_utility_menu > div {gap:8px!important}
.st-key-floating_utility_menu .st-key-utility_menu_toggle button {
  width:118px!important;
}
@media(max-width:700px){
  .st-key-floating_utility_menu{top:75px!important;left:10px!important;width:220px!important}
  .st-key-floating_utility_menu .st-key-utility_menu_toggle button{width:102px!important}
}
div.st-key-utility_menu_toggle button {
  background:linear-gradient(115deg,#006d85,#0999a9)!important;
  color:#fff!important;
  border:1px solid #0b8197!important;
  border-radius:13px!important;
  min-height:46px!important;
  padding:0 21px!important;
  font-weight:800!important;
  letter-spacing:.06em!important;
  box-shadow:0 8px 19px rgba(0,103,125,.20)!important;
}
div.st-key-utility_menu_toggle button:hover {
  background:linear-gradient(115deg,#00586f,#00879e)!important;
  border-color:#00586f!important;
  transform:translateY(-1px);
}
div.st-key-utility_menu_toggle button p {color:white!important}
div.st-key-utility-menu-panel {
  background:#e6f6f8;border:1px solid #9fd7df;border-radius:16px;
  padding:15px;box-shadow:0 12px 28px #006c841a
}
</style>
""", unsafe_allow_html=True)
with st.container(key="floating_utility_menu"):
    if st.button("☰  MENU", key="utility_menu_toggle"):
        st.session_state.utility_menu_open = not st.session_state.utility_menu_open
        st.rerun()
    if st.session_state.utility_menu_open:
        with st.container(key="utility-menu-panel", border=True):
            st.markdown("**TIỆN ÍCH & TÀI LIỆU**")
            for name, description in EXTRA_TOOLS:
                if st.button(name + "  →", key="utility-open-" + name, use_container_width=True):
                    st.session_state.utility_menu_open = False
                    open_utility(name)
st.markdown('<div class="site-head"><div class="brand"><div class="brandmark">✚</div><div><div class="brandtitle">KTCĐHA</div><div class="brandsub">THƯ VIỆN KỸ THUẬT CHẨN ĐOÁN HÌNH ẢNH</div></div></div><div class="headright">BY HUUHUY</div></div>', unsafe_allow_html=True)
# Cải thiện hiển thị trên điện thoại, kể cả khi trình duyệt dùng chế độ tối.
# Giữ nền sáng và độ tương phản cao cho nhãn, ô nhập, lịch và nút.
st.markdown("""
<style>
@media (max-width: 700px) {
  /* Dành khoảng trống cho nút MENU cố định, không che ngày trực hay nút Khóa sổ. */
  .block-container {
    padding-top: 5.6rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 100% !important;
  }
  .st-key-floating_utility_menu {
    top: 12px !important;
    left: 12px !important;
    width: min(210px, calc(100vw - 24px)) !important;
    z-index: 1001 !important;
  }
  .st-key-floating_utility_menu .st-key-utility_menu_toggle button {
    width: 118px !important;
    min-height: 45px !important;
    font-size: .85rem !important;
    white-space: nowrap !important;
  }
  .shift-heading {
    padding: 18px 19px !important;
    margin-top: 8px !important;
  }
  .shift-heading h2 {font-size: 1.35rem !important}
  .shift-subhead {font-size: 1.02rem !important; margin-top: 20px !important}
  [data-testid="stHorizontalBlock"] {gap: .65rem !important}
  [data-testid="stVerticalBlock"] {gap: .7rem}
}
/* Streamlit trên Safari iPhone có thể tự bật dark mode và làm nhãn gần như trắng. */
[data-testid="stAppViewContainer"] {
  color-scheme: light !important;
  color: #173d4b !important;
}
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
[data-testid="stNumberInput"] label,
[data-testid="stNumberInput"] label p,
[data-testid="stTextInput"] label,
[data-testid="stTextInput"] label p,
[data-testid="stDateInput"] label,
[data-testid="stDateInput"] label p,
[data-testid="stAppViewContainer"] .stCaption p {
  color: #244b58 !important;
  opacity: 1 !important;
  font-weight: 650 !important;
}
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input,
[data-testid="stDateInput"] input {
  background: #ffffff !important;
  color: #183f4c !important;
  -webkit-text-fill-color: #183f4c !important;
  border-radius: 10px !important;
  font-size: 16px !important;
  min-height: 46px !important;
  color-scheme: light !important;
}
[data-testid="stNumberInput"] [data-baseweb="input"],
[data-testid="stTextInput"] [data-baseweb="input"],
[data-testid="stDateInput"] [data-baseweb="input"] {
  background: #ffffff !important;
  border: 1px solid #9fcbd2 !important;
  border-radius: 11px !important;
}
[data-testid="stNumberInput"] button {
  background: #e5f4f6 !important;
  color: #006b82 !important;
  border-color: #b6dfe4 !important;
}
[data-testid="stNumberInput"] button svg {
  fill: #006b82 !important;
  stroke: #006b82 !important;
}
[data-testid="stDateInput"] svg {color: #006b82 !important}
[data-testid="stAppViewContainer"] input::placeholder {
  color: #6d8a94 !important;
  -webkit-text-fill-color: #6d8a94 !important;
}
</style>
""", unsafe_allow_html=True)

def internal_log_page():
    """Local-session shift report; protected by configured secret; never server-persist PHI."""
    st.markdown("""
    <style>
    .shift-heading{background:linear-gradient(115deg,#006c84,#1197a8);color:#fff;
       border-radius:19px;padding:22px 27px;margin:13px 0 19px}
    .shift-heading h2{color:white!important;margin:0 0 8px!important;font-size:1.6rem!important}
    .shift-heading p{color:#dff8fa!important;margin:0;font-size:.82rem}
    .shift-subhead{font-size:1.08rem;font-weight:800;color:#006f87;
       border-bottom:2px solid #b9e1e5;padding:12px 0 8px;margin:18px 0 10px}
    .shift-total{border-radius:14px;background:#e1f5f7;border:1px solid #9fd8df;
       padding:15px 18px;margin:10px 0;color:#00677e;font-weight:800}
    </style>""", unsafe_allow_html=True)
    st.markdown('<div class="shift-heading"><h2>SỔ TRỰC NỘI BỘ</h2>'
                '<p>Ghi nhận bàn giao phim, thuốc và số lượng ca trong ca trực</p></div>',
                unsafe_allow_html=True)

    password = st.secrets.get("INTERNAL_LOG_PASSWORD", None)
    if not password:
        st.error("Chưa cấu hình mật khẩu cho Sổ trực nội bộ. "
                 "Thêm INTERNAL_LOG_PASSWORD vào Streamlit Secrets trước khi sử dụng.")
        st.caption("Không nhập dữ liệu bệnh nhân vào website công khai khi chưa có kiểm soát truy cập và lưu trữ phù hợp.")
        return
    if not st.session_state.get("shift_authenticated", False):
        with st.form("shift-login"):
            entered = st.text_input("Mật khẩu truy cập sổ trực", type="password")
            submitted = st.form_submit_button("MỞ SỔ TRỰC", use_container_width=True)
        if submitted:
            import hmac
            if hmac.compare_digest(entered, str(password)):
                st.session_state.shift_authenticated = True
                st.rerun()
            else:
                st.error("Mật khẩu không đúng.")
        return
    if st.button("Khóa sổ trực", key="shift-lock"):
        st.session_state.shift_authenticated = False
        st.rerun()

    today = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).date()
    work_day = st.date_input("Ngày trực", value=today, format="DD/MM/YYYY", key="shift-day")
    st.markdown('<div class="shift-subhead">1. Bàn giao vật tư</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        change_2530 = st.number_input("Thay hộp phim 25×30 (hộp)",min_value=0,step=1,key="shift-change-2530")
        gado_receive = st.number_input("Nhận Gadovist (hộp)",min_value=0,step=1,key="shift-receive-gado")
        gado_patient = st.text_input("Tên bệnh nhân nhận Gadovist",key="shift-gado-patient")
    with c2:
        change_3543 = st.number_input("Thay hộp phim 35×43 (hộp)",min_value=0,step=1,key="shift-change-3543")
        omni_receive = st.number_input("Nhận Omnipaque (lọ)",min_value=0,step=1,key="shift-receive-omni")
        omni_patient = st.text_input("Tên bệnh nhân nhận Omnipaque",key="shift-omni-patient")

    st.markdown('<div class="shift-subhead">2. Thuốc</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        gado_stock = st.number_input("Gadovist – hộp",min_value=0,step=1,key="shift-gado-stock")
        gado_empty = st.number_input("Gadovist – vỏ",min_value=0,step=1,key="shift-gado-empty")
    with c2:
        omni_stock = st.number_input("Omnipaque – lọ",min_value=0,step=1,key="shift-omni-stock")
        omni_empty = st.number_input("Omnipaque – vỏ",min_value=0,step=1,key="shift-omni-empty")

    st.markdown('<div class="shift-subhead">3. Phim 35×43</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    with a: f35_boxes = st.number_input("Số hộp 35×43",min_value=0,step=1,key="shift-f35-boxes")
    with b: f35_covers = st.number_input("Số vỏ 35×43",min_value=0,step=1,key="shift-f35-covers")
    with c: f35_loose = st.number_input("Phim lẻ 35×43",min_value=0,step=1,key="shift-f35-loose")
    total35 = f35_boxes*125 + f35_loose
    st.markdown(f'<div class="shift-total">Σ Phim 35×43 = {f35_boxes} × 125 + {f35_loose} = {total35:,} phim</div>',unsafe_allow_html=True)
    system35 = st.number_input("Phim 35×43 trên hệ thống", min_value=0, step=1, key="shift-f35-system")
    used35 = system35 - total35
    st.metric("Phim 35×43 đã sử dụng (theo chênh lệch)", f"{used35:,} phim")
    a,b = st.columns(2)
    with a:
        ct_cases = st.number_input("CT – số ca",min_value=0,step=1,key="shift-ct-cases")
    with b:
        mri_cases = st.number_input("MRI – số ca",min_value=0,step=1,key="shift-mri-cases")
        mri_films = st.number_input("MRI – số phim",min_value=0,step=1,key="shift-mri-films")
    ct_films = used35 - mri_films
    st.metric("CT – số phim (tự tính)", f"{ct_films:,} phim")
    st.caption("CT = Phim 35×43 trên hệ thống − Tổng phim 35×43 − Phim MRI.")
    if used35 < 0 or ct_films < 0:
        st.warning("Kết quả chênh lệch âm. Vui lòng kiểm tra số liệu phim trên hệ thống, tổng phim và phim MRI.")

    st.markdown('<div class="shift-subhead">4. Phim 25×30</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    with a: f25_boxes = st.number_input("Số hộp 25×30",min_value=0,step=1,key="shift-f25-boxes")
    with b: f25_covers = st.number_input("Số vỏ 25×30",min_value=0,step=1,key="shift-f25-covers")
    with c: a107 = st.number_input("Phòng A107 – số phim",min_value=0,step=1,key="shift-a107")
    total25 = f25_boxes*125 + a107
    st.markdown(f'<div class="shift-total">Σ Phim 25×30 = {f25_boxes} × 125 + {a107} = {total25:,} phim</div>',unsafe_allow_html=True)
    remaining25 = st.number_input("Phim 25×30 tồn trên hệ thống",min_value=0,step=1,key="shift-f25-remaining")
    used25 = remaining25 - total25
    st.metric("Sử dụng phim 25×30",f"{used25:,} phim")
    st.caption("Sử dụng 25×30 = Phim tồn trên hệ thống − Tổng phim 25×30.")
    if used25 < 0: st.warning("Tổng phim 25×30 tính được lớn hơn số phim trên hệ thống. Vui lòng kiểm tra số liệu.")

    st.markdown('<div class="shift-subhead">5. Phim 20×25</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    with a: f20_boxes = st.number_input("Số hộp 20×25",min_value=0,step=1,key="shift-f20-boxes")
    with b: f20_covers = st.number_input("Số vỏ 20×25",min_value=0,step=1,key="shift-f20-covers")
    with c: f20_room = st.number_input("Phòng A107 – số phim (20×25)",min_value=0,step=1,key="shift-f20-room")
    total20 = f20_boxes*125 + f20_room
    st.markdown(f'<div class="shift-total">Σ Phim 20×25 = {f20_boxes} × 125 + {f20_room} = {total20:,} phim</div>',unsafe_allow_html=True)
    remaining20 = st.number_input("Phim 20×25 tồn trên hệ thống",min_value=0,step=1,key="shift-f20-remaining")
    used20 = total20 - remaining20
    st.metric("Sử dụng phim 20×25",f"{used20:,} phim")
    if used20 < 0: st.warning("Số phim tồn trên hệ thống lớn hơn tổng phim tính được. Vui lòng kiểm tra số liệu.")

    st.markdown('<div class="shift-subhead">6. Tổng hợp giao ban</div>', unsafe_allow_html=True)
    st.write(f"**Ngày:** {work_day.strftime('%d/%m/%Y')}  |  **CT:** {ct_cases} ca  |  **MRI:** {mri_cases} ca")
    st.write(f"**Phim:** 35×43: {total35:,}  |  25×30: {total25:,}  |  20×25: {total20:,}")
    st.markdown('<div class="shift-subhead">7. Báo cáo giao ban</div>', unsafe_allow_html=True)
    st.markdown('<div class="shift-subhead">8. Tờ A4 để nhìn và chép vào sổ</div>', unsafe_allow_html=True)
    def e(value):
        return html.escape(str(value), quote=True)
    def n(value):
        return f"{value:,}"
    date_text = work_day.strftime("%d/%m/%Y")
    # Đúng thứ tự cuốn sổ: bàn giao -> thuốc -> phim -> báo cáo giao ban.
    a4_body = f"""
    <div class="paper">
      <h1>Ngày {e(date_text)}</h1>
      <div class="lines">
        <p>– Thay {n(change_3543)} hộp phim 35×43</p>
        <p>– Thay {n(change_2530)} hộp phim 25×30</p>
        <p>– Nhận {n(gado_receive)} hộp Gado ({e(gado_patient)})</p>
        <p>– Nhận {n(omni_receive)} lọ Omnipaque ({e(omni_patient)})</p>
      </div>
      <section>
        <p><strong>* Thuốc:</strong> Omnipaque: {n(omni_stock)} lọ / {n(omni_empty)} vỏ</p>
        <p class="indent">Gadovist: {n(gado_stock)} hộp / {n(gado_empty)} vỏ</p>
      </section>
      <section>
        <p><strong>* Phim 35×43:</strong> {n(f35_boxes)} hộp / {n(f35_covers)} vỏ / {n(f35_loose)} phim lẻ
          <b class="sum">Σ {n(total35)}</b></p>
        <p>– MRI: {n(mri_cases)} ca / {n(mri_films)} phim</p>
        <p>– CT: {n(ct_cases)} ca / {n(ct_films)} phim</p>
        <p class="hint">Hệ thống: {n(system35)} phim · Đã sử dụng: {n(used35)} phim</p>
      </section>
      <section>
        <p><strong>* Phim 25×30:</strong> {n(f25_boxes)} hộp / {n(f25_covers)} vỏ
          <b class="sum">Σ {n(total25)}</b></p>
        <p>– Phòng A107: {n(a107)} phim <span class="side">Sử dụng: {n(used25)} phim</span></p>
        <p class="hint">Phim trên hệ thống: {n(remaining25)}</p>
      </section>
      <section>
        <p><strong>* Phim 20×25:</strong> {n(f20_boxes)} hộp / {n(f20_covers)} vỏ
          <b class="sum">Σ {n(total20)}</b></p>
        <p>– Phòng A107: {n(f20_room)} phim <span class="side">Sử dụng: {n(used20)} phim</span></p>
        <p class="hint">Phim trên hệ thống: {n(remaining20)}</p>
      </section>
      <h2>Báo cáo giao ban {e(date_text)}</h2>
      <div class="summary">
        <p>– XQ: .......... ca</p>
        <p>– CT: .......... ca</p>
        <p>– MRI: .......... ca</p>
        <p>– Siêu âm: Σ .......... <span class="side">SACC: .......... · SUP: ..........</span></p>
      </div>
    </div>"""
    a4_style = """
    @page { size: A4 portrait; margin: 15mm; }
    *{box-sizing:border-box}
    body{margin:0;background:#e8f3f5;color:#202e38;font-family:Arial,'DejaVu Sans',sans-serif}
    .paper{width:210mm;min-height:297mm;margin:18px auto;background:#fff;padding:20mm 20mm 16mm;
      box-shadow:0 9px 30px #173b4a28;font-size:15px;line-height:1.55}
    h1{text-align:center;font-size:21px;margin:0 0 23px;color:#153b4b}
    h2{text-align:center;font-size:19px;margin:28px 0 18px;color:#153b4b}
    p{margin:5px 0}section{margin-top:22px}.indent{padding-left:75px}
    .sum{float:right;color:#006e86}.side{float:right}.hint{font-size:12px;color:#68808a}
    .summary{max-width:450px;margin:auto}.summary p{margin:9px 0}
    .print-toolbar{text-align:center;padding:14px}
    .print-toolbar button{background:#007e96;color:#fff;border:0;padding:12px 22px;
       font-size:15px;border-radius:10px;cursor:pointer}
    @media print{
      body{background:#fff}.paper{margin:0;width:auto;min-height:0;padding:0;box-shadow:none}
      .print-toolbar{display:none}section{break-inside:avoid}
    }
    @media(max-width:850px){.paper{width:100%;min-height:0;margin:0;padding:20px;font-size:13px}}
    """
    document_html = (
        '<!doctype html><html lang="vi"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Sổ trực '+e(date_text)+'</title><style>'+a4_style+'</style></head>'
        '<body><div class="print-toolbar"><button onclick="window.print()">IN / LƯU PDF KHỔ A4</button></div>'
        +a4_body+'</body></html>'
    )
    st.caption("Xem trước ngay bên dưới. Bấm tải mẫu A4 rồi mở bằng trình duyệt để in hoặc lưu PDF.")
    import streamlit.components.v1 as components
    components.html(document_html, height=880, scrolling=True)
    st.download_button(
        "TẢI TỜ A4 ĐÃ ĐIỀN (.html)",
        data=document_html.encode("utf-8"),
        file_name=f"so_truc_A4_{work_day.isoformat()}.html",
        mime="text/html",
        use_container_width=True,
        key="shift-a4-download",
    )
    st.caption("Mở file HTML đã tải → chọn In (Ctrl/Cmd + P) → khổ A4 → In hoặc Lưu dưới dạng PDF.")
    st.warning("Tờ A4 có thể chứa tên bệnh nhân. Không lưu hoặc in trên thiết bị công cộng.")

    st.caption("Mẫu sổ chỉ lưu tạm trong phiên Streamlit. Không tự lưu dữ liệu lên máy chủ.")
    # Export contains patient identifiers. Only download on an authenticated session.
    report = {
        "ngay":work_day.isoformat(),
        "ban_giao":{"thay_hop_25x30":change_2530,"thay_hop_35x43":change_3543,
                    "nhan_gadovist":gado_receive,"benh_nhan_gadovist":gado_patient,
                    "nhan_omnipaque":omni_receive,"benh_nhan_omnipaque":omni_patient},
        "thuoc":{"gadovist_hop":gado_stock,"gadovist_vo":gado_empty,
                 "omnipaque_lo":omni_stock,"omnipaque_vo":omni_empty},
        "phim_35x43":{"hop":f35_boxes,"vo":f35_covers,"phim_le":f35_loose,"tong":total35,
                       "tren_he_thong":system35,"da_su_dung":used35,
                       "ct_ca":ct_cases,"ct_phim":ct_films,"mri_ca":mri_cases,"mri_phim":mri_films},
        "phim_25x30":{"hop":f25_boxes,"vo":f25_covers,"phong_a107":a107,
                       "tong":total25,"ton_he_thong":remaining25,"su_dung":used25},
        "phim_20x25":{"hop":f20_boxes,"vo":f20_covers,"phim_le_phong":f20_room,
                       "tong":total20,"ton_he_thong":remaining20,"su_dung":used20}
    }
    st.download_button("TẢI BÁO CÁO GIAO BAN (.json)",
        data=json.dumps(report,ensure_ascii=False,indent=2).encode("utf-8"),
        file_name=f"so_truc_{work_day.isoformat()}.json",
        mime="application/json",use_container_width=True)
    st.warning("Dữ liệu có tên bệnh nhân là thông tin nhạy cảm. Chỉ sử dụng trên hệ thống được bệnh viện cho phép; "
               "không chia sẻ file báo cáo công khai.")

if st.session_state.utility_page is not None:
    selected = st.session_state.utility_page
    if st.button("← QUAY LẠI THƯ VIỆN", key="utility-return"):
        st.session_state.utility_page = None
        st.rerun()
    st.markdown(f'<div class="catalog-hero"><div class="eyebrow">KTCĐHA / TIỆN ÍCH</div>'
                f'<h2>{html.escape(selected)}</h2>'
                f'<p>{html.escape(dict(EXTRA_TOOLS).get(selected, ""))}</p></div>',
                unsafe_allow_html=True)
    if selected == "Sổ trực nội bộ":
        internal_log_page()
    elif selected == "Hỏi AI":
        st.info("Chức năng Hỏi AI đang được chuẩn bị. Chưa kết nối kho tài liệu đã kiểm duyệt.")
    elif selected == "Tài liệu chuyên ngành":
        st.info("Kho tài liệu chuyên ngành đang được chuẩn bị. Chưa có tài liệu được công bố.")
    elif selected == "Xử lý sốc phản vệ":
        st.warning("Chưa có quy trình xử trí được đối chiếu và phê duyệt. Trong tình huống cấp cứu thực tế, thực hiện quy trình cấp cứu của cơ sở và gọi hỗ trợ khẩn cấp.")
    else:
        st.info("Công cụ đang được chuẩn bị. Chưa có công thức hoặc thông số được xác minh để sử dụng trong thực hành.")
    st.stop()

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
    cols=st.columns(2,gap="large")
    for col,(title,desc) in zip(cols,SUBS[mod]):
        with col:
            st.markdown(f'<div class="subcard"><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
            if st.button(f"Xem {title.lower()} →",key=title):
                go(mod,title)
else:
    if st.button(f"← QUAY LẠI {mod.upper()}",key="back"): go(mod)
    if mod=="X-quang" and sub=="Kỹ thuật chụp":
        xray_library()
        st.stop()
    if mod in ("CT", "MRI") and sub=="Kỹ thuật chụp":
        scan_library(mod)
        st.stop()
    if sub == "Hình ảnh bệnh lý":
        st.markdown(
            f'<div class="catalog-hero"><div class="eyebrow">THƯ VIỆN {html.escape(mod.upper())}</div>'
            f'<h2>Hình ảnh bệnh lý {html.escape(mod)}</h2>'
            '<p>Chuyên mục đang được chuẩn bị. Nội dung và hình ảnh sẽ được bổ sung sau khi kiểm chứng nguồn.</p>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.info("Chưa có dữ liệu hình ảnh bệnh lý. Nội dung sẽ được cập nhật sau.")
        st.stop()
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
