import streamlit as st

st.set_page_config(page_title="PRICE LIST - デコレーション料金表", page_icon="💎", layout="centered")

# カスタムCSSの読み込み
st.markdown("""
<style>
    .stApp {
        background-color: #1a1a1a;
    }
    .price-card {
        background: linear-gradient(145deg, #111111, #1e1e1e);
        border: 2px solid #b8860b;
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        padding: 32px 24px;
        color: white;
        font-family: 'Times New Roman', YuMincho, 'Yu Mincho', serif;
        max-width: 400px; /* 少しスリムに */
        margin: 0 auto;
    }
    .price-title {
        color: #d4af37;
        font-size: 24px; /* 28pxから少し小さく */
        text-align: center;
        letter-spacing: 0.15em;
        border-bottom: 1px solid #d4af37;
        padding-bottom: 8px;
        margin-bottom: 8px;
    }
    .price-subtitle {
        color: #a9a9a9;
        font-size: 11px;
        text-align: center;
        letter-spacing: 0.2em;
        margin-bottom: 28px;
    }
    .menu-item {
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
        margin-bottom: 16px;
    }
    .menu-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 4px;
    }
    .menu-name {
        color: #e0e0e0;
        font-size: 14px; /* 16pxから少し小さくして上品に */
        margin: 0;
        letter-spacing: 0.05em;
    }
    .menu-price {
        color: #d4af37;
        font-size: 18px; /* 20pxから少し小さく */
    }
    .menu-desc {
        color: #888;
        font-size: 11px;
        margin: 0;
    }
    .vip-box {
        margin-top: 28px;
        background-color: rgba(212, 175, 55, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 16px;
        text-align: center;
        border-radius: 4px;
    }
    .vip-title {
        color: #d4af37;
        font-size: 13px;
        margin-bottom: 8px;
        letter-spacing: 0.1em;
    }
    .vip-text {
        color: #aaa;
        font-size: 11px;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# インデント（行頭の空白）を取り除いたHTMLコンテンツ
html_content = """
<div class="price-card">
<div class="price-title">PRICE LIST</div>
<div class="price-subtitle">BESPOKE RHINESTONE DECORATION</div>
<div class="menu-item">
<div class="menu-header">
<h2 class="menu-name">アイコスケース デコ</h2>
<div class="menu-price">¥14,900<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">ケース代・ストーン代込み / 全面フルデコ</p>
</div>
<div class="menu-item">
<div class="menu-header">
<h2 class="menu-name">たばこケース デコ (大)</h2>
<div class="menu-price">¥17,300<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">全面デコレーション / オーダーメイドデザイン</p>
</div>
<div class="menu-item">
<div class="menu-header">
<h2 class="menu-name">たばこケース デコ (小)</h2>
<div class="menu-price">¥15,000<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">ワンポイントデザイン / イニシャル等</p>
</div>
<div class="menu-item">
<div class="menu-header">
<h2 class="menu-name">アイコス本体 デコ</h2>
<div class="menu-price">¥14,200<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">※お客様のお持ち込み本体への施工</p>
</div>
<div class="vip-box">
<div class="vip-title">VIP SERVICE</div>
<div class="vip-text">
高級ジュエリーボックスにてお渡しいたします。<br>
万が一ストーンが取れてしまった場合の<br>
「1回無料お直し保証」をお付けしております。
</div>
</div>
<p style="color: #666; font-size: 9px; text-align: center; margin-top: 24px;">
※デザインの細かさにより価格が変動する場合がございます。
</p>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)
