import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PRICE LIST - デコレーション料金表", page_icon="💎", layout="centered")

# Streamlit本体の背景色を黒にする
st.markdown("""
<style>
    .stApp {
        background-color: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

# 完全に独立したWebページ（HTMLドキュメント）として組み立てる
html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
<style>
    /* iframeの中の背景も黒に合わせる */
    body {
        background-color: #1a1a1a;
        margin: 0;
        padding: 20px 10px;
        display: flex;
        justify-content: center;
        font-family: 'Times New Roman', YuMincho, 'Yu Mincho', serif;
    }
    .price-card {
        background: linear-gradient(145deg, #111111, #1e1e1e);
        border: 2px solid #b8860b;
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        padding: 32px 24px;
        color: white;
        width: 100%;
        max-width: 400px;
        box-sizing: border-box;
    }
    .price-title {
        color: #d4af37;
        font-size: 24px;
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
        padding-bottom: 16px;
        margin-bottom: 20px;
    }
    .menu-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 4px;
    }
    .menu-name {
        color: #e0e0e0;
        font-size: 15px;
        margin: 0;
        letter-spacing: 0.05em;
    }
    .menu-price {
        color: #d4af37;
        font-size: 18px;
    }
    .menu-desc {
        color: #888;
        font-size: 11px;
        margin: 0;
    }
    
    /* Swiper (スライダー) の設定 */
    .swiper-container {
        width: 100%;
        margin-top: 12px;
        overflow: hidden;
    }
    .swiper-wrapper {
        transition-timing-function: linear !important;
    }
    .swiper-slide {
        width: 120px !important;
    }
    .swiper-slide img {
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 6px;
        border: 2px solid #333;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
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
</head>
<body>

<div class="price-card">
<div class="price-title">PRICE LIST</div>
<div class="price-subtitle">BESPOKE RHINESTONE DECORATION</div>

<div class="menu-item">
<div class="menu-header">
<div class="menu-name">アイコスケース デコ</div>
<div class="menu-price">¥14,900<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">ケース代・ストーン代込み / 全面フルデコ</p>
<div class="swiper-container">
    <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Design+A"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Design+B"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Design+C"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Design+D"></div>
    </div>
</div>
</div>

<div class="menu-item">
<div class="menu-header">
<div class="menu-name">たばこケース デコ (大)</div>
<div class="menu-price">¥17,300<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">全面デコレーション / オーダーメイドデザイン</p>
<div class="swiper-container">
    <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Sample+1"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Sample+2"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Sample+3"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Sample+4"></div>
    </div>
</div>
</div>

<div class="menu-item">
<div class="menu-header">
<div class="menu-name">たばこケース デコ (小)</div>
<div class="menu-price">¥15,000<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">ワンポイントデザイン / イニシャル等</p>
<div class="swiper-container">
    <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Mini+1"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Mini+2"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Mini+3"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Mini+4"></div>
    </div>
</div>
</div>

<div class="menu-item">
<div class="menu-header">
<div class="menu-name">アイコス本体 デコ</div>
<div class="menu-price">¥14,200<span style="font-size:10px; color:#888;">〜</span></div>
</div>
<p class="menu-desc">※お客様のお持ち込み本体への施工</p>
<div class="swiper-container">
    <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Body+1"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Body+2"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Body+3"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/200x200/111111/d4af37?text=Body+4"></div>
    </div>
</div>
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

<!-- 外部プログラム（Swiper）を確実に動かす -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const swipers = document.querySelectorAll('.swiper-container');
        swipers.forEach(function(el) {
            new Swiper(el, {
                slidesPerView: 'auto',
                spaceBetween: 10,
                loop: true,
                speed: 3000,
                autoplay: {
                    delay: 0,
                    disableOnInteraction: false,
                },
                freeMode: true,
            });
        });
    });
</script>
</body>
</html>
"""

# components.html を使って、安全な iframe 内で完全なWebページとして表示させる
components.html(html_content, height=1300, scrolling=False)
