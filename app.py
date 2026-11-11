import json
import html
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
